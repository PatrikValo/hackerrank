#include <vector>
#include <assert.h>
#include <iostream>

/**
 * DYNAMIC PROGRAMMING
 * https://www.hackerrank.com/challenges/coin-change/problem
 * @param n - price
 * @param c - available coins
 * @return count of possibilities to get coins
 */
long getWays(int n, const std::vector<long> &c) {
    auto tmp = std::vector<long>(n + 1, 0);
    auto table = std::vector<std::vector<long>>(c.size() + 1, tmp);

    for (long &j : table[0]) {
        j = 0;
    }

    table[0][0] = 1;

    for (long i = 1; i < table.size(); i++) {
        table[i][0] = 1;
        for (long j = 1; j < table[i].size(); j++) {
            long res1 = 0;
            if (j - c[i - 1] >= 0) {
                res1 = table[i][j - c[i - 1]];
            }
            long res2 = table[i - 1][j];
            table[i][j] = res1 + res2;
        }
    }
    return table[c.size()][n];
}

int main() {
    assert(getWays(4, std::vector<long>{1, 2, 3}) == 4);
    assert(getWays(3, std::vector<long>{8, 3, 1, 2}) == 3);
    assert(getWays(10, std::vector<long>{2, 5, 3, 6}) == 5);
    assert(getWays(250,
                   std::vector<long>{41, 34, 46, 9, 37, 32, 42, 21, 7, 13, 1, 24, 3, 43, 2, 23, 8, 45, 19, 30, 29, 18,
                                     35, 11}) == 15685693751);
    return 0;
}
