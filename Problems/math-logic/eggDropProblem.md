# Egg drop problem

## My Binary search solution

Start by dropping an egg at midpoint floor 50

If the egg does not break drop at (top - (midpoint + 1)) / 2

If the egg breaks start at the lower index and test dropping incrementally up the floor unil the egg breaks

Hence with two eggs the best case efficiency would be an order of n/2 for n floors and the average efficiency of this process would be log2\_(10)

## Solution

Drop(Egg 1) + Drop(Egg 2) should be the same

Each drop of egg 1 takes 1 more step, so egg 2 should take one fewer step

X + (X-1) + (X-2) + (X-3) + .. + 1 = 100

X(X+1)/2 = 100

X = 13.65

Hence: X = 14

## To generalise for n floors

X(X+1)/2 = n
