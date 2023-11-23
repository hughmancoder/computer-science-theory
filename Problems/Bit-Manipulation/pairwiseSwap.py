"""Binary to hex conversion is straightforward as 4 adjacent binary bits can be converted to hex representation"""
def pairwiseSwap(n):
    # Mask for odd bits (0xAAAAAAAA for 32-bit integer in hex format 0b10101010101010101010101010101010)
    odd_mask = 0xAAAAAAAA

    # Mask for even bits (0x55555555 for 32-bit integer in hex format 0b01010101010101010101010101010101)
    even_mask = 0x55555555

    # Right shift odd bits and left shift even bits, then combine them
    return ((n & odd_mask) >> 1) | ((n & even_mask) << 1)

# Example usage
number = 23  # For example, binary: 10111
swapped = pairwiseSwap(number)
print("Original:", bin(number))
print("Swapped:", bin(swapped))