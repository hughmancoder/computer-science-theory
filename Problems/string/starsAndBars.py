def starsAndBarsOptimised(s, startIndex, endIndex):
    n = len(s)
    prefix = [0] * (n + 1)
    # number of *'s to the left of i (including i)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (s[i] == '*')

    res = []
    for l, r in zip(startIndex, endIndex):
        l -= 1
        r = min(r, n)
        while l < r and s[l] != '|':
            l += 1
        while l < r and s[r - 1] != '|':
            r -= 1

        # subtract the number of starts to the left of r inclusive and the number of stars to the left of l exclusive to give us the nubmer of starts between l and r
        res.append(prefix[r] - prefix[l])

    return res

def starsAndBars(s, startIndex, endIndex):
    n = len(startIndex)
    res = []

    for i in range(n):
        l = startIndex[i] - 1
        r = min(endIndex[i] - 1, len(s) - 1)
        cnt = 0
        
        while r > l and s[r] != '|':
            r -= 1

        while l < r and s[l] != '|':
            l += 1
        
        while l < r:
            if s[l] == '*':
                cnt += 1
            l += 1

        res.append(cnt)

    print(res)
    return res

def test_starsAndBars():
    print(starsAndBars('|**|*|**', [1, 1], [5, 6]) == [2, 3])
    print(starsAndBars('|***|*|*|*|', [1, 2, 3], [5, 7, 9]) == [3, 1, 2])
    print(starsAndBars('|***|*|*|*|', [3], [9]) == [2])

test_starsAndBars()