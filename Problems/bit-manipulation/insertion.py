def insertBits(n: int, m: int, i: int, j: int) -> int:
    # clear bits i through j in n
    all_ones = ~0

    # ones before position j and zeros to the left (11110000000)
    left = all_ones << (j + 1)

    # ones after position i and zeros to the left (00000000011)
    right = ((1 << i) - 1)
    
    # fill bits i to j with 0s (11110000011)
    mask = left | right

    # clear bits i through j in n
    n_cleared = n & mask

    # insert bits m into n
    m_shifted = m << i

    # merge m and n to insert m into n
    return m_shifted | n_cleared


N = int('10000000000', 2)  # N is 0b10000000000
M = int('10011', 2)        # M is 0b10011
i = 2
j = 6

result = insertBits(N, M, i, j)
print(f"Output: {bin(result)[2:]}") # Expected: 10001001100