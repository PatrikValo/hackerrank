#include <vector>
#include <iostream>
#include <cassert>

class TopologicalSorting {
    std::vector<std::vector<bool>> _graph;
public:
    explicit TopologicalSorting(std::vector<std::vector<bool>> graph) : _graph(std::move(graph)) {}

    void print_graph() {
        std::cout << "digraph G {\n";


        for (size_t state_1 = 0; state_1 < _graph.size(); state_1++) {
            for (size_t state_2 = 0; state_2 < _graph[state_1].size(); state_2++) {
                if (_graph[state_1][state_2]) {
                    std::cout << "\t\"" << state_1 << "\" -> " << "\"" << state_2 << "\"\n";
                }
            }
        }

        std::cout << "}\n";
    }

    std::vector<int> run() {
        auto result = std::vector<int>(_graph.size(), 0);
        auto visited = std::vector<bool>(_graph.size(), false);
        auto index = result.size() - 1;

        for (int i = 0; i < _graph.size(); i++) {
            index = _run(i, visited, result, index);
        }

        return result;
    }

private:
    size_t _run(int curr_state, std::vector<bool> &visited, std::vector<int> &res, size_t index) {
        if (visited[curr_state]) {
            return index;
        }

        visited[curr_state] = true;

        for (int state = 0; state < _graph[curr_state].size(); state++) {
            if (_graph[curr_state][state]) {
                index = _run(state, visited, res, index);
            }
        }

        res[index] = curr_state;
        return --index;
    }
};


int main() {
    auto t = TopologicalSorting({
                                        {false, false, true,  true},
                                        {true,  false, true,  true},
                                        {false, false, false, true},
                                        {false, false, false, false},
                                });
    auto vec = t.run();

    assert(vec == (std::vector<int>{1, 0, 2, 3}));
    t.print_graph();
}
