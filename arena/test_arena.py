"""Tests de l'arène : python3 -m unittest discover arena"""
import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import arena  # noqa: E402

BOTS = Path(__file__).parent / "bots"


def py_bot(name, code=None):
    """Un bot Python : un fichier de arena/bots, ou du code en ligne."""
    command = [sys.executable, "-u", "-c", code] if code else [sys.executable, "-u", str(BOTS / f"{name}.py")]
    return arena.BotSpec(name, command)


class MatchTest(unittest.TestCase):
    def play(self, *specs, turns=20):
        return {p.bot.name: (rank, p) for rank, p in arena.run_match(list(specs), seed=3, max_turns=turns)}

    def test_three_bots_and_slow_bot_loses(self):
        res = self.play(py_bot("glouton"), py_bot("depart"), py_bot("lent"))
        self.assertEqual(res["glouton"][0], 1)
        self.assertGreater(res["glouton"][1].score, 0)
        self.assertEqual(res["lent"][0], 3)
        self.assertEqual(res["lent"][1].out_turn, 5)
        self.assertIn("temps dépassé", res["lent"][1].reason)

    def test_invalid_action_crash_and_missing_program(self):
        res = self.play(py_bot("glouton"), py_bot("bavard", "print('JUMP')"), py_bot("crash", "raise SystemExit(1)"),
                        arena.BotSpec("absent", ["programme-qui-n-existe-pas"]))
        self.assertIn("action invalide", res["bavard"][1].reason)
        self.assertIn("arrêté", res["crash"][1].reason)
        self.assertIn("impossible de lancer", res["absent"][1].reason)
        self.assertEqual(res["glouton"][0], 1)

    def test_same_seed_same_game(self):
        a = self.play(py_bot("glouton"), py_bot("depart"))
        b = self.play(py_bot("glouton"), py_bot("depart"))
        self.assertEqual(a["glouton"][1].score, b["glouton"][1].score)


class RulesTest(unittest.TestCase):
    def test_moves(self):
        self.assertEqual(arena.next_cell("MOVE 5 0", 2, 3), (3, 3))  # d'abord en x
        self.assertEqual(arena.next_cell("move 2 0", 2, 3), (2, 2))
        self.assertEqual(arena.next_cell("UP", 0, 0), (0, 0))  # bord : on reste
        self.assertEqual(arena.next_cell("WAIT", 4, 4), (4, 4))
        with self.assertRaises(arena.BotError):
            arena.next_cell("MOVE a b", 0, 0)

    def test_spec_names(self):
        self.assertEqual(arena.parse_spec(str(BOTS / "glouton.py")).name, "glouton")
        self.assertEqual(arena.parse_spec("moi=" + str(BOTS / "glouton.py")).name, "moi")
        starter = Path(__file__).parent.parent / "starters" / "python" / "bot.py"
        self.assertEqual(arena.parse_spec(str(starter)).name, "python")
        names = [s.name for s in arena.unique_names([py_bot("a"), py_bot("a")])]
        self.assertEqual(names, ["a", "a#2"])


class TournamentTest(unittest.TestCase):
    def test_round_robin_table(self):
        specs = [py_bot("glouton"), py_bot("depart"), py_bot("aleatoire")]
        with contextlib.redirect_stdout(io.StringIO()):
            table = arena.run_tournament(specs, per_match=2, games=1, seed=1,
                                         timeout_ms=arena.DEFAULT_TIMEOUT_MS, max_turns=15)
        self.assertEqual(table[0][0], "glouton")
        self.assertTrue(all(st["matches"] == 4 for _, st in table))  # 2 adversaires x 2 places


if __name__ == "__main__":
    unittest.main()
