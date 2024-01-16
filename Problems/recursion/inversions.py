"""Optimal DP solution"""
def maxInversions_(prices):
    n = len(prices)
    inversions = 0
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            if prices[j] > prices[i]:
                # count the number of elements greater than i which are left of i
                dp[i] += 1
                
                #  if arr[i] is less than arr[j], it is also less than all the elements that arr[j] is less than, forming inversions.
                inversions += dp[j] 
    return inversions

def maxInversionsBruteForce(prices):
    n = len(prices)
    inversions = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if prices[i] > prices[j] > prices[k]:
                    inversions += 1

    return inversions

def maxInversions(prices):
    """
    This function takes a list of prices and returns the number of inversions in the list.
    An inversion is a strictly decreasing subsequence of length 3.

    Parameters:
    prices (list): A list of integers representing the prices.

    Returns:
    int: The number of inversions in the list.
    """

    memo = {}
    
    def helper(index, prev_price, length):
        if length == 3:
            # print("current_prices:", current_prices)
            return 1
        if index >= len(prices):
            return 0
        
        if (index, prev_price, length) in memo:
            return memo[(index, prev_price, length)]
        res = 0
        
        if not prev_price:
            res += helper(index + 1, prices[index], length + 1)
        elif(prices[index] < prev_price):
            res += helper(index + 1,  prices[index], length + 1)

        # skip current index
        res += helper(index + 1, prev_price, length)
            
        
        memo[(index, prev_price, length)] = res
        return res
                
    return helper(0, None, 0)


print(maxInversions_([5, 3, 4, 2, 1]), "Expected:", 7)
print(maxInversions_([4, 2, 2, 1]), "Expected:", 2)