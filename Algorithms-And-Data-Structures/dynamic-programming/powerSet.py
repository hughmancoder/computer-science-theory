class Solution:
    def get_all_subsets(self, given_set):
        self.ret = []
        self.get_all_subsets_helper(given_set, 0, [])
        return self.ret

    def get_all_subsets_helper(self, given_set, index, currentSet):
        if index == len(given_set):
            self.ret.append(currentSet.copy())  
            return

        # Case 1: Exclude the current element
        self.get_all_subsets_helper(given_set, index + 1, currentSet)

        # Case 2: Include the current element
        currentSet.append(given_set[index])
        self.get_all_subsets_helper(given_set, index + 1, currentSet)
        currentSet.pop()

solution = Solution()

example_set = [1, 2, 3, 4, 5, 6, 7]
subsets = solution.get_all_subsets(example_set)
print("Subsets of", example_set, ":", subsets)

def test_get_all_subsets():
    test_set = [1, 2]
    expected_output = [[], [1], [2], [1, 2]]
    assert sorted(solution.get_all_subsets(test_set)) == sorted(expected_output), "Test failed!"
    print("Test passed!")

test_get_all_subsets()