"""
Idea: we can surround open and close parent on left + right or both or place a pair on end. Due to symmetry we are not concerned specifically with left and right placements
"""
def parens(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    parens_list = []
    for i in range(n):
        for left in parens(i): # we could have 0 to n on the left 
            for right in parens(n - i - 1): # we could have 0 to n - i on the right. We subtract 1 because we already have a left paren
                parens_list.append('(' + left + ')' + right)
    return parens_list

print(parens(2))
print(parens(3))