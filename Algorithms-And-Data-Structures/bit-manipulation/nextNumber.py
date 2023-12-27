""" def nextNumber(num):
    ones = sum([1 for bit in bin(num)[2:] if bit == '1'])
    next_smallest = None
    next_largest = None
    temp = num
    # get next smallest
    while True:
        num  -= 1
        one_count = sum([1 for bit in bin(num)[2:] if bit == '1'])
        if one_count == ones:
            next_smallest = num
            break
    
    num = temp
    # get next largest
    while True:
        num += 1
        one_count = sum([1 for bit in bin(num)[2:] if bit == '1'])
        if one_count == ones:
            next_largest = num
            break

    print(next_smallest, next_largest)
    print(bin(next_smallest), bin(next_largest)) """

# TODO revise
class NextNumber:
    def getNextLargest(n):
        c = n
        c0 = 0
        c1 = 0

        # Count trailing zeros and the size of the rightmost block of ones
        while ((c & 1) == 0) and (c != 0):
            c0 += 1
            c >>= 1

        while (c & 1) == 1:
            c1 += 1
            c >>= 1

        # Error: if n == 111...000, then there is no larger number with the same number of 1s.
        if c0 + c1 == 31 or c0 + c1 == 0:
            return -1

        p = c0 + c1  # Position of rightmost non-trailing zero

        n |= (1 << p)  # Flip rightmost non-trailing zero
        n &= ~((1 << p) - 1)  # Clear all bits to the right of p
        n |= (1 << (c1 - 1)) - 1  # Insert (c1-1) ones on the right

        return n

    def getNextSmallest(n):
            temp = n
            c0 = 0
            c1 = 0

            while temp & 1 == 1:
                c1 += 1
                temp >>= 1

            if temp == 0:
                return -1

            while (temp & 1 == 0) and (temp != 0):
                c0 += 1
                temp >>= 1

            p = c0 + c1  # Position of rightmost non-trailing one
            n &= ((~0) << (p + 1))  # Clears from bit p onwards

            mask = (1 << (c1 + 1)) - 1  # Sequence of (c1+1) ones
            n |= mask << (c0 - 1)

            return n

print(NextNumber.getNextLargest(1775))
print(NextNumber.getNextSmallest(1775))