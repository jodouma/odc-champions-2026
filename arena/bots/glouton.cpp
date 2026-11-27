// Bot glouton en C++ : la même idée que glouton.py.
// Compiler : g++ -O2 -o arena/build/glouton arena/bots/glouton.cpp
#include <cstdlib>
#include <iostream>
#include <vector>

int main() {
    int nbPlayers, myId, width, height, nbTurns;
    std::cin >> nbPlayers >> myId >> width >> height >> nbTurns;
    while (true) {
        int x = 0, y = 0;
        for (int i = 0; i < nbPlayers; i++) {
            int px, py, score, active;
            if (!(std::cin >> px >> py >> score >> active)) return 0;
            if (i == myId) { x = px; y = py; }
        }
        int k;
        std::cin >> k;
        double best = -1;
        int bx = x, by = y;
        for (int i = 0; i < k; i++) {
            int ox, oy, v;
            std::cin >> ox >> oy >> v;
            double gain = v / double(std::abs(ox - x) + std::abs(oy - y) + 1);
            if (gain > best) { best = gain; bx = ox; by = oy; }
        }
        std::cout << "MOVE " << bx << " " << by << std::endl;  // std::endl vide le tampon
    }
}
