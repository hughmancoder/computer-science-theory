"""Relative order is concerned with permutations"""
class Permutations:
    permutations = []

    def permute(self, s: list, curr):
        if len(s) == 0:
            self.permutations.append(curr)
        else:
            s = list(s)  # convert string to list
            for i in range(len(s)):
                # swap
                s[0], s[i] = s[i], s[0]
                
                # generate permutations with the first character fixed
                self.permute(s[1:], curr + s[0])
                
                # backtrack
                s[0], s[i] = s[i], s[0]

    def compute_unique_char_permutations(self, s):
        """
        Compute all permutations of a string of unique characters.

        :param s: input string
        :return: list of permutations
        """
        self.permutations = []
        self.permute(s,"")
        return self.permutations

    def compute_non_unique_char_permutations(self, s):
        """
        Compute all permutations of a string whose characters are not necessarily unique. 
        The list of permutations should not have duplicates.

        :param s: input string
        :return: list of permutations
        """
        s = "".join(set(s))
        self.compute_unique_char_permutations(s)
        return self.permutations

input = "hugh"
permutations = Permutations()

print(permutations.compute_unique_char_permutations(input))
print(permutations.compute_non_unique_char_permutations(input))
