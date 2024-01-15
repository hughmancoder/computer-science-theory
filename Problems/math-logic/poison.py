"""
Strategy:
Label Bottles: Number the bottles from 0 to 999.

Binary Representation: Convert each bottle number to its binary representation. A 10-bit binary number can represent any number from 0 to 1023. For example, bottle 0 would be 0000000000, bottle 1 would be 0000000001, bottle 2 would be 0000000010, and so on.

Using Test Strips: Assign each test strip to a binary digit (bit). For example, strip 1 represents the least significant bit (LSB), strip 2 represents the next bit, and so forth.

Applying Drops: For each bottle, if the nth binary digit of its number is 1, add a drop from this bottle to the nth test strip. This way, each strip tests a unique combination of bottles.

Results Interpretation: After seven days, read the test strips. Each test strip that turns positive represents a binary 1 in the position of the poisoned bottle's number. Convert this binary number back to decimal to identify the poisoned bottle.

Example:
If the poisoned bottle is number 523, its binary representation is 1000001011.
Test strips corresponding to binary positions with 1 (from right to left) will test positive. In this case, strips 1, 2, 4, and 10.
Reading the strips as a binary number 1000001011, we convert it back to decimal to get 523, identifying the poisoned bottl
"""

def simulate(bottles, num_bottles=1000, num_strips=10):
    poisoned_bottle = bottles.index(True)
    poisoned_binary = "{0:010b}".format(poisoned_bottle)
    test_strips = [0] * num_strips
    guessed_bottle = 0
    # Apply drops from each bottle to the corresponding test strips
    for bottle_number in range(num_bottles):
        # binary_representation = format(bottle, '010b') # 10-bit binary representation
        binary = "{0:010b}".format(bottle_number)
        if binary == poisoned_binary:
            guessed_bottle = bottle_number
    
    return guessed_bottle
    
# True denotes poision
bottles = [False] * 1000
bottles[523] = True   

index = simulate(bottles)

print("Suspected Bottle: " + str(index) + " calculated within 7 days with outcome: " +  str(bottles[index]))
