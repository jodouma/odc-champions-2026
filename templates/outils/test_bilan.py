"""Tests : python3 -m unittest discover templates/outils"""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import bilan  # noqa: E402


class AbTest(unittest.TestCase):
    def test_clear_win(self):
        out = bilan.ab_report(159, 41)
        self.assertIn("79.5 %", out)
        self.assertIn("A est meilleure", out)
        self.assertNotIn("Attention", out)

    def test_coin_flip_is_not_clear(self):
        self.assertIn("Pas clair", bilan.ab_report(106, 94))

    def test_clear_loss(self):
        self.assertIn("moins bonne", bilan.ab_report(40, 80))

    def test_few_games_warning(self):
        out = bilan.ab_report(15, 5)
        self.assertIn("Attention", out)

    def test_draw_is_half(self):
        self.assertIn("50.0 %", bilan.ab_report(0, 0, 10))

    def test_wilson_bounds(self):
        lo, hi = bilan.wilson(50, 100)
        self.assertAlmostEqual(lo, 0.4038, places=3)
        self.assertAlmostEqual(hi, 0.5962, places=3)
        self.assertEqual(bilan.wilson(0, 0), (0.0, 1.0))


class DefeatsTest(unittest.TestCase):
    def write(self, text):
        f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
        f.write(text)
        f.close()
        self.addCleanup(Path(f.name).unlink)
        return f.name

    def test_table_sorted_by_count(self):
        path = self.write(
            "partie,version,cause,tour,note\n"
            "101,v2,coup illégal,12,\n"
            "102,v2,moins bon,40,\n"
            "103,v2,moins bon,35,\n"
            "\n"
        )
        out = bilan.defeats_table(bilan.read_defeats(path))
        self.assertIn("3 défaites lues.", out)
        lines = out.splitlines()
        self.assertTrue(lines[4].startswith("| moins bon | 2 | 67 % | 102 |"))
        self.assertTrue(lines[5].startswith("| coup illégal | 1 | 33 % | 101 |"))

    def test_missing_cause_is_an_error(self):
        path = self.write("partie,version,cause,tour,note\n104,v2,,10,\n")
        with self.assertRaises(ValueError):
            bilan.read_defeats(path)

    def test_cli(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(bilan.main(["ab", "118", "82"]), 0)
        self.assertIn("Verdict", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
