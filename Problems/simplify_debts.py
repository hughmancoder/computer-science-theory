"""

Optimal Account Balancing

A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
"""
 
# Solution: https://leetcode.ca/2017-03-09-465-Optimal-Account-Balancing/
from collections import defaultdict
import math

"""
Solution 1: O(n!) time, O(n!) space
"""
def minTransactions_(transactions) -> int:
        graph = defaultdict(int)

        for u, v, w in transactions:
            graph[u] -= w
            graph[v] += w
        
        balance = [val for val in graph.values() if val != 0]
        
        def backtrack(index):
            if index == len(balance):
                return 0 
            
            if balance[index] == 0:
                return backtrack(index+1)
            
            result = float('inf')

            for curr in range(index+1,len(balance)):
                
                if balance[index]*balance[curr] < 0:
                    balance[curr]+= balance[index]
                    result = min(result,1+backtrack(index+1))
                    balance[curr]-= balance[index]
            return result 
        
        return backtrack(0)

"""
Solution 1: O(n!) time, O(n!) space
"""
def minTransactions(transactions) -> int:
    balance = [0] * 21

    for u, v, amount in transactions:
      balance[u] -= amount
      balance[v] += amount

    debts = [b for b in balance if b]

    def dfs(s: int) -> int:
      # skip over all the debts that are settled (0)
      while s < len(debts) and not debts[s]:
        s += 1

      if s == len(debts):
        return 0

      ans = math.inf

      for i in range(s + 1, len(debts)):
        if debts[i] * debts[s] < 0:
          debts[i] += debts[s]  # `debts[s]` is settled.
          ans = min(ans, 1 + dfs(s + 1))
          debts[i] -= debts[s]  # Backtrack.

      return ans

    return dfs(0)



"""Dp Bitmask solution """
def minTransfersDP(transactions) -> int:
    g = defaultdict(int)
    for f, t, x in transactions:
        g[f] -= x
        g[t] += x
    nums = [x for x in g.values() if x]
    m = len(nums)
    f = [float('inf')] * (1 << m)
    f[0] = 0
    for i in range(1, 1 << m):
        s = 0
        for j, x in enumerate(nums):
            if i >> j & 1:
                s += x
        if s == 0:
            f[i] = i.bit_count() - 1
            j = (i - 1) & i
            while j > 0:
                f[i] = min(f[i], f[j] + f[i ^ j])
                j = (j - 1) & i
    return f[-1]



# Example usage:
transactions1 = [[0, 1, 10], [2, 0, 5]]
transactions2 = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]

output1 = minTransactions(transactions1)
print("Output 1:", output1) # 2

output2 = minTransactions(transactions2)
print("Output 2:", output2) # 1

