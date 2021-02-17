from typing import List
from collections import deque


class AhoCorasick:
    def __init__(self):
        self.__count_characters: int = 26
        self.__nodes: List[List[int]] = [[-1 for _ in range(self.__count_characters)]]
        self.__fail: List[int] = [-1]
        self.__acc: List[int] = [0]

    def run(self, first: int, last: int, d: str, genes: List[str], health: List[int]) -> int:
        self.__build_machine(genes, first, last)

        summary: int = 0
        current_state: int = 0

        for i in range(len(d)):
            current_state = self.__find_next_state(current_state, d[i])

            if self.__acc[current_state] != 0:
                for j in range(len(genes)):
                    if (self.__acc[current_state] & (1 << j)) != 0:
                        summary += health[j]
        return summary

    def __insert(self, gene: str, ord_gene: int) -> None:
        curr_state: int = 0

        for g in gene:
            char = ord(g) - ord("a")
            if self.__nodes[curr_state][char] == -1:
                self.__nodes.append([-1 for _ in range(self.__count_characters)])
                self.__fail.append(-1)
                self.__acc.append(0)
                self.__nodes[curr_state][char] = len(self.__acc) - 1    # number of state

            curr_state = self.__nodes[curr_state][char]

        self.__acc[curr_state] |= (1 << ord_gene)

    def __find_next_state(self, current_state: int, character: str) -> int:
        answer: int = current_state
        char: int = ord(character) - ord('a')

        while self.__nodes[answer][char] == -1:
            answer = self.__fail[answer]

        return self.__nodes[answer][char]

    def __create_fail_edges(self) -> None:
        q: deque = deque()

        for i in range(self.__count_characters):
            if self.__nodes[0][i] == -1:
                self.__nodes[0][i] = 0

            if self.__nodes[0][i] != 0:
                self.__fail[self.__nodes[0][i]] = 0
                q.append(self.__nodes[0][i])

        while len(q) != 0:
            state: int = q.popleft()

            for char in range(self.__count_characters):
                if self.__nodes[state][char] != -1:
                    fail: int = self.__fail[state]

                    while self.__nodes[fail][char] == -1:
                        fail = self.__fail[fail]

                    self.__fail[self.__nodes[state][char]] = self.__nodes[fail][char]
                    self.__acc[self.__nodes[state][char]] |= self.__acc[self.__nodes[fail][char]]

                    q.append(self.__nodes[state][char])

    def __build_machine(self, genes: List[str], first: int, last: int) -> None:
        for i in range(first, last + 1):
            self.__insert(genes[i], i)

        self.__create_fail_edges()


if __name__ == '__main__':
    print(AhoCorasick().run(1, 5, "caaab", ["a", "b", "c", "aa", "d", "b"], [1, 2, 3, 4, 5, 6]))
    print(AhoCorasick().run(0, 4, "xyz", ["a", "b", "c", "aa", "d", "b"], [1, 2, 3, 4, 5, 6]))
    print(AhoCorasick().run(2, 4, "bcdybc", ["a", "b", "c", "aa", "d", "b"], [1, 2, 3, 4, 5, 6]))
