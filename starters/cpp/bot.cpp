// La ligne #pragma doit rester tout en haut, avant les #include :
// sur CodinGame, le C++ est compilé sans optimisation.
#pragma GCC optimize("O3,omit-frame-pointer,inline")

// Squelette générique de bot CodinGame (C++17).
// Remplis les zones « À ADAPTER », dans cet ordre :
//   1. les constantes (recopiées de l'énoncé) ;
//   2. readInit et readTurn (le format d'entrée) ;
//   3. legalMoves (toujours au moins un coup légal) ;
//   4. evaluate (la note d'un coup : plus haut = mieux).
// Le reste (chrono, debug, choix du coup) marche déjà.
#include <chrono>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using Clock = std::chrono::steady_clock;

// ---- À ADAPTER : recopie ces valeurs de l'énoncé ----
const char* VERSION = "v1";        // change-la à chaque soumission ; affichée sur stderr au tour 1
constexpr int TURN_LIMIT_MS = 50;           // temps permis par tour
constexpr int FIRST_TURN_LIMIT_MS = 1000;   // temps permis au 1er tour (souvent plus long)
constexpr double BUDGET_RATIO = 0.5;        // on n'utilise que la moitié : le serveur est plus lent
constexpr bool DEBUG = true;                // affiche l'entrée lue et le temps du tour sur stderr

// Tout ce que le bot sait du jeu. Ajoute tes champs ici.
struct State {
    int turn = 0;
    std::vector<std::string> initLines;  // entrée du début de partie, brute
    std::vector<std::string> lines;      // entrée du tour courant, brute
};

// À ADAPTER : lit l'entrée donnée une seule fois, avant le 1er tour.
bool readInit(State& s) {
    std::string line;
    if (!std::getline(std::cin, line)) return false;
    s.initLines = {line};
    return true;
}

// À ADAPTER : lit TOUTES les lignes d'un tour, même celles dont tu n'as pas besoin.
bool readTurn(State& s) {
    std::string line;
    if (!std::getline(std::cin, line)) return false;
    s.lines = {line};
    return true;
}

// À ADAPTER : la liste des coups autorisés. Jamais vide : garde un coup de secours.
std::vector<std::string> legalMoves(const State& s) {
    (void)s;
    return {"WAIT"};
}

// À ADAPTER : la note d'un coup. Commence simple, améliore une idée à la fois.
double evaluate(const State& s, const std::string& move) {
    (void)s;
    (void)move;
    return 0.0;
}

// Note chaque coup légal tant qu'il reste du temps ; garde le meilleur.
std::string pick(const State& s, Clock::time_point deadline) {
    const std::vector<std::string> moves = legalMoves(s);
    std::string best = moves.at(0);
    double bestScore = -std::numeric_limits<double>::infinity();
    for (const std::string& move : moves) {
        if (Clock::now() >= deadline) {
            if (DEBUG) std::cerr << "chrono : arrêt avant la fin de la liste" << std::endl;
            break;
        }
        const double score = evaluate(s, move);
        if (score > bestScore) {
            best = move;
            bestScore = score;
        }
    }
    return best;
}

int main() {
    State s;
    if (!readInit(s)) return 0;
    if (DEBUG) std::cerr << "VERSION " << VERSION << std::endl;
    while (readTurn(s)) {
        const auto start = Clock::now();  // le chrono part quand l'entrée du tour est lue
        ++s.turn;
        const int limitMs = s.turn == 1 ? FIRST_TURN_LIMIT_MS : TURN_LIMIT_MS;
        const auto deadline = start + std::chrono::microseconds(static_cast<long long>(limitMs * BUDGET_RATIO * 1000));
        if (DEBUG) {
            std::cerr << "T" << s.turn << " entree=";
            for (const std::string& l : s.lines) std::cerr << "[" << l << "]";
            std::cerr << std::endl;
        }
        // std::endl vide le tampon : sans lui, l'arbitre ne voit rien et compte un temps dépassé.
        std::cout << pick(s, deadline) << std::endl;
        if (DEBUG) {
            const double ms = std::chrono::duration<double, std::milli>(Clock::now() - start).count();
            std::cerr << "T" << s.turn << " t=" << ms << "ms" << std::endl;
        }
    }
}
