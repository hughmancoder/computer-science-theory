def simulate():
    lockers = [False] * 100  # False for closed, True for open
    for increment in range(1, 101):  # Starting from 1 to 100
        for i in range(increment - 1, 100, increment):  # Adjusting for zero-indexing
            lockers[i] = not lockers[i]

    print(f"{lockers.count(True)} lockers are open")
    
simulate()

# Mathematical solution
"""
Locker Toggling: A locker is toggled (opened/closed) on each divisor of its number. For example:
Locker 12 is toggled on passes 1, 2, 3, 4, 6, and 12.
Locker 15 is toggled on passes 1, 3, 5, and 15.

Even and Odd Number of Divisors:

Most numbers have an even number of divisors (e.g., 12 has pairs: (1, 12), (2, 6), (3, 4)).
Numbers that are perfect squares have an odd number of divisors (e.g., 16 has pairs: (1, 16), (2, 8) and the single divisor 4 (4x4)).

Reasoning behind why pefect squares yield an odd number of divisors and toggle indexes and odd number of times:

Perfect Squares and Odd Number of Divisors
Perfect Squares Unique Property: Numbers that are perfect squares, like 4 (2x2), 9 (3x3), 16 (4x4), etc., have an odd number of divisors. This is because one of the divisors is repeated (2 in the case of 4, 3 in the case of 9, and so on).

For example, the divisors of 16 are 1, 2, 4, 8, and 16. Notice the pairings are (1, 16), (2, 8), and 4 stands alone without a pair.
Impact on Toggling: Since each divisor pair leads to two toggles (cancelling each other out), the unpaired divisor in perfect squares results in an extra toggle that leaves the locker in the opposite state from its start. For perfect squares, this means an odd number of toggles – from closed to open.

Open Lockers:
A locker ends up open only if it is toggled an odd number of times.
Only lockers numbered with perfect squares are toggled an odd number of times (since they have an odd number of divisors).

Counting Perfect Squares:
The perfect squares up to 100 are 1², 2², 3², ..., 10² (i.e., 1, 4, 9, 16, 25, 36, 49, 64, 81, 100).
Therefore, there are 10 lockers (corresponding to these perfect squares) that remain open.

Conclusion: After the 100th pass, 10 lockers remain open.


"""