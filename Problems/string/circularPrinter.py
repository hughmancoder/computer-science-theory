import string
from collections import Counter

"""
A printer prints characters from 'A' to 'Z'. z wraps around to A forming a circle. 
The pointer can only print one letter at a time and takes one second to move in either direction.
What is the minimum time needed to print the string?
"""
def circularPrinter(s):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # needle is initially at a
    s = 'A' + s
    n = len(s)
    distance = 0
    for i in range(1, n):
        prev = s[i - 1]
        cur = s[i]

        i = letters.index(prev)
        j = letters.index(cur)

        clockwise = abs(j - i)
        counter_clockwise = 26 - clockwise # i + 26 - j = 26 - (j - i)

        distance += min(clockwise, counter_clockwise)
    
    print(s, distance)
    return distance
    

# test cases

print(circularPrinter("AZGB") == 13)
print(circularPrinter("ZNMD") == 23)
