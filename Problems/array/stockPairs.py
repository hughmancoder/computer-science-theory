"""
A financial analyst Is responsible for a portfollo of profitable stocks represented in an array. Each Item in the array represents the yeariy profit of a corresponding stock. The analyst gathers all distinct pairs of stocks that reached the target profit. Distinct pairs are pairs that differ in at least one element. Given the array of profits, find the number of distinct pairs of stocks where the sum of each pair's profits Is exactly equal to the target profit.
Example
stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
target = 12 profit's target
Language Python 3
• © Environment
1 > #|/bin/python3-
10
11 #
12 # Complete the 'stockPairs' function below.
13 #
14 The function is expected to return an INTEGER.
15 # The function accepts following parameters:
16 # 1. INTEGER_ARRAY stocksProfit
17
# 2. LONG_INTEGER target|
18
19
20 def stockPairs (stocksProfit, target):|
#Write your code here
21
23 > if
name == ' main…':-
© Autocomp
• There are 4 pairs of stocks that have the sum of their profits equals to the target 12. Note that because there are two instances of 3 in stocksProfit there are two pairs matching (9, 3): stocksProfits indices 2 and 7, and indices 2 and 8, but only one can be included.
• There are 3 distinct pairs of stocks: (5, 7), (3, 9), and (6, 6) and the return value is 3.
Function Description
Complete the function stockPairs in the editor below.
stockPairs has the following parameter(s):
int stocksProfit[n]: an array of integers representing the stocks profits target: an Integer representing the yearly target profit
Returns:
int: the total number of pairs
"""

def stockPairs(stocksProfit, target):
    profit_count = {}
    for profit in stocksProfit:
        if profit in profit_count:
            profit_count[profit] += 1
        else:
            profit_count[profit] = 1

    pair_count = 0
    for profit in profit_count:
        complement = target - profit
        if complement in profit_count:
            if profit == complement:
                pair_count += profit_count[profit] // 2
                profit_count[profit] %= 2
            else:
                min_count = min(profit_count[profit], profit_count[complement])
                pair_count += min_count
                profit_count[profit] -= min_count
                profit_count[complement] -= min_count

    return pair_count