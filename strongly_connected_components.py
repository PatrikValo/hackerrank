from typing import List


class Kosaraju:
    def __init__(self, graph: List[List[int]]):
        self.__graph: List[List[int]] = graph

    def run(self):
        stack = self.__compute_stack()
        self.__graph = self.__transpose()
        return self.__strongly_connected_components(stack)

    def __strongly_connected_components(self, stack: List[int]) -> List[List[int]]:
        visited: List[bool] = [False] * len(self.__graph)
        result: List[List[int]] = []

        while len(stack) != 0:
            v = stack.pop()
            component: List[int] = []
            self.__strongly_connected_components_dfs(v, visited, component)
            if len(component) != 0:
                result.append(component)
        return result

    def __strongly_connected_components_dfs(self, v: int, visited: List[bool], component: List[int]) -> None:
        if visited[v]:
            return

        visited[v] = True
        component.append(v)

        for i in range(len(self.__graph[v])):
            if self.__graph[v][i] == 1:
                self.__strongly_connected_components_dfs(i, visited, component)

    def __compute_stack(self) -> List[int]:
        vertices: int = len(self.__graph)
        visited: List[bool] = [False] * vertices
        stack: List[int] = []

        for v in range(len(self.__graph)):
            self.__compute_stack_dfs(v, visited, stack)

        return stack

    def __compute_stack_dfs(self, v: int, visited: List[bool], stack: List[int]):
        if visited[v]:
            return

        visited[v] = True

        for i in range(len(self.__graph[v])):
            if self.__graph[v][i] == 1:
                self.__compute_stack_dfs(i, visited, stack)
        stack.append(v)

    def __transpose(self) -> List[List[int]]:
        graph = [[0 for _ in range(len(self.__graph[0]))] for _ in range(len(self.__graph))]

        for v1 in range(len(self.__graph)):
            for v2 in range(len(self.__graph[v1])):
                graph[v2][v1] = self.__graph[v1][v2]
        return graph


if __name__ == '__main__':
    kosaraju = Kosaraju([
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])

    print(kosaraju.run())
