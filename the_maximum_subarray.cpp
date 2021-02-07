#include <vector>
#include <cassert>
#include <algorithm>
#include <iostream>

int max_subset_(const std::vector<int>& arr) {
    int minimal_negative = arr[0];
    int max = 0;

    for (int elem: arr) {
        if (elem > 0) {
            max += elem;
        } else {
            if (elem > minimal_negative) {
                minimal_negative = elem;
            }
        }
    }

    return max == 0 ? minimal_negative : max;
}

int max_subarray_(const std::vector<int>& arr) {
    int max_so_far = arr[0];
    int curr_max = arr[0];

    for (size_t i = 1; i < arr.size(); i++) {
        curr_max = std::max(arr[i], curr_max + arr[i]);
        max_so_far = std::max(max_so_far, curr_max);
    }

    return max_so_far;
}

/**
 * https://www.hackerrank.com/challenges/maxsubarray/problem
 * @param arr
 * @return
 */
std::vector<int> max_subarray(const std::vector<int>& arr) {
    return std::vector<int>{max_subarray_(arr), max_subset_(arr)};
}

int main() {
    assert(max_subarray(std::vector<int>{1, 2, 3, 4}) == (std::vector<int>{10, 10}));
    assert(max_subarray(std::vector<int>{2, -1, 2, 3, 4, -5}) == (std::vector<int>{10, 11}));
    assert(max_subarray(std::vector<int>{-2, -3, -1, -4, -6}) == (std::vector<int>{-1, -1}));
    assert(max_subarray(std::vector<int>{-1, 2, 3, -4, 5, 10}) == (std::vector<int>{16, 20}));
    return 0;
}