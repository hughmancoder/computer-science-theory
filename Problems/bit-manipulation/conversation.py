def conversation(a, b):
    count = 0
    while a != b:
        if a & 1 != b & 1:
            count += 1
        a >>= 1
        b >>= 1
    return count

"""
Input: 29 (or 11101), 15 (or 01111)  
Output: 2
"""
print(conversation(29, 15), 2)