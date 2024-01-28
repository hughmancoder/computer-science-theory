"""
Find number pair sums divisible by k where a[i] + j[i] % k == 0 and i < j
"""

def solution(a, k):
    count = 0
    remainder_counts = {}

    for num in a:
        remainder = num % k
        if remainder in remainder_counts:
            count += remainder_counts[remainder]
        complement_remainder = (k - remainder) % k
        remainder_counts[complement_remainder] = remainder_counts.get(complement_remainder, 0) + 1

    return count

# Example usage
a = [1, 2, 3, 4, 5]
k = 3
result = solution(a, k)
print(result)  # Output should be 4 as there are 4 pairs: (1, 2), (1, 5), (2, 4), (4,5) are divisible by k