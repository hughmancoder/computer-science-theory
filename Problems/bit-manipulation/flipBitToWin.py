# Solution 1: employs string conversion
""" def flipBitToWin(num):
    binary_str = bin(num)[2:]  # Convert to binary string, excluding the '0b' prefix.
    max_length = 0
    current_length = 0
    previous_length = 0

    for bit in binary_str:
        if bit == '1':
            current_length += 1
        else:
            
            max_length = max(max_length, previous_length + current_length + 1)
            # Update previous_length: If next bit is 1, it becomes current_length; otherwise, it's 0.
            previous_length = current_length if bit == '0' else 0
            current_length = 0

    # Final update to max_length for the last sequence in the string
    max_length = max(max_length, previous_length + current_length + 1)

    return max_length """

# Solution 2: employs bit manipulation (optimal solution)
def flipBitToWin(num):
    
    if ~num == 0:
        return len(bin(num)) - 2  

    current_length = 0
    previous_length = 0
    max_length = 1

    while num != 0:
        if (num & 1) == 1:
            current_length += 1
        else:
            
            previous_length = 0 if (num & 2) == 0 else current_length
            current_length = 0 

        max_length = max(max_length, current_length + previous_length + 1)
        num >>= 1  

    return max_length

# Test the function
print(flipBitToWin(1775))  # Output: 8
print(flipBitToWin(3))  # Output: 2
