#include <iostream>
#include <vector>
#include <cassert>

class Kmp {
    std::vector<size_t> lps_(const std::string& str) {
        std::vector<size_t> vec(str.size(), 0);

        size_t first_match = 0;
        size_t i = 1;
        while (i < str.size()) {
            if (str[first_match] == str[i]) {
                vec[i] = first_match + 1;
                first_match++;
                i++;
            } else {
                if (first_match > 0) {
                    first_match = vec[first_match - 1];
                } else {
                    vec[i] = 0;
                    first_match = 0;
                    i++;
                }
            }
        }

        return vec;
    }
public:
    std::vector<size_t> search(const std::string& text, const std::string& pattern) {
        const auto lps = lps_(pattern);

        size_t i_text = 0;
        size_t i_pattern = 0;
        std::vector<size_t> result{};

        while (i_text < text.size()) {
            if (text[i_text] == pattern[i_pattern]) {
                i_text++;
                i_pattern++;
            } else {
                if (i_pattern > 0) {
                    i_pattern = lps[i_pattern - 1];
                } else {
                    i_text++;
                }
            }

            if (i_pattern == pattern.size()) {
                result.push_back(i_text - i_pattern);
                i_pattern = lps[i_pattern - 1];
            }
        }

        return result;
    }
};

int main() {
    assert(Kmp().search("aabaaac", "aa") == (std::vector<size_t >{0, 3, 4}));
    assert(Kmp().search("abcdacabcabc", "abc") == (std::vector<size_t >{0, 6, 9}));
}