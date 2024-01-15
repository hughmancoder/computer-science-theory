"""
The Algorithm:

Initial Calculations:

start_offset and end_offset are calculated to determine how many bits into their respective bytes x1 and x2 are.
first_full_byte and last_full_byte are the indices of the first and last bytes in the screen array that will be completely filled by the line.

Setting Full Bytes:

The loop sets all the bytes from first_full_byte to last_full_byte to 0xFF (all bits set to 1), effectively turning on all the pixels in these bytes.
Creating Masks for Start and End:

start_mask is used to turn on bits in the byte containing x1, and end_mask for x2. These masks ensure only the part of the byte where the line should be is affected.
Setting Start and End of Line:

If x1 and x2 are in the same byte, a combined mask (byte_mask) is created and applied to this byte.
If they are in different bytes, start_mask and end_mask are applied to their respective bytes.
Edge Cases:

The function handles the case where x1 and x2 do not align perfectly with byte boundaries.
"""

def drawLine(screen, width, x1, x2, y):
    # Calculate the start and end points
    start_offset = x1 % 8
    first_full_byte = x1 // 8
    if start_offset != 0:
        first_full_byte += 1

    end_offset = x2 % 8
    last_full_byte = x2 // 8
    if end_offset != 7:
        last_full_byte -= 1

    # Set the full bytes
    for b in range(first_full_byte, last_full_byte + 1):
        screen[(width // 8) * y + b] = 0xFF  # 0xFF is all 1s in binary (11111111)

    # Create masks for start and end of line
    start_mask = 0xFF >> start_offset
    end_mask = ~(0xFF >> (end_offset + 1))

    # Set start and end of line
    if (x1 // 8) == (x2 // 8):  # x1 and x2 are in the same byte
        byte_mask = start_mask & end_mask
        screen[(width // 8) * y + (x1 // 8)] |= byte_mask
    else:
        if start_offset != 0:
            byte_number = (width // 8) * y + first_full_byte - 1
            screen[byte_number] |= start_mask
        if end_offset != 7:
            byte_number = (width // 8) * y + last_full_byte + 1
            screen[byte_number] |= end_mask

# Example usage
screen = [0x00] * 24  # Example screen (3 rows, 8 columns each)
width = 24  # Width in bits
drawLine(screen, width, 3, 13, 1)  # Draw line from (3,1) to (13,1)

# Displaying the result
for i in range(0, len(screen), width // 8):
    print(' '.join(f'{byte:08b}' for byte in screen[i:i + width // 8]))


# Initialize a blank screen (3 rows, 8 columns each)
screen = [0x00] * 24  # 24 bytes total, 3 bytes per row
width = 24

# Draw a line from (3, 1) to (13, 1)
drawLine(screen, width, 3, 13, 1)


