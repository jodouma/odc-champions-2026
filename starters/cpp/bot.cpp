// La ligne #pragma doit rester tout en haut, avant les #include :
// sur CodinGame, le C++ est compilé sans optimisation.
#pragma GCC optimize("O3,omit-frame-pointer,inline")

// Squelette générique de bot CodinGame (C++).
// Adapte readTurn et decide à l'énoncé du jeu.
#include <chrono>
#include <iostream>
#include <string>

using Clock = std::chrono::steady_clock;

// Garde une marge sous la limite de l'énoncé (ex. 50 ms).
constexpr auto TURN_BUDGET = std::chrono::milliseconds(40);

// Lit les entrées d'un tour. À adapter à l'énoncé.
bool readTurn(std::string& state) {
    return static_cast<bool>(std::getline(std::cin, state));
}

// Renvoie l'action du tour. Commence simple : une action toujours légale.
std::string decide(const std::string& state, Clock::time_point deadline) {
    std::string best = "WAIT";
    while (Clock::now() < deadline) {
        // Ici : essayer des actions candidates et garder la meilleure.
        break;
    }
    (void)state;
    return best;
}

int main() {
    std::string state;
    while (readTurn(state)) {
        const auto deadline = Clock::now() + TURN_BUDGET;
        // std::cerr pour le debug : std::cout est réservé aux actions.
        std::cout << decide(state, deadline) << std::endl;
    }
}
