import string

"""
Theory: In binary, each place after the decimal point represents a fractional part of 1/2, 1/4, 1/8, 1/16, and so on

The Algorithm


"""

def binaryToString(number: int) -> string:
    if number >= 1 or number <= 0:
        return "ERROR"
    binary = "."
    frac = 0.5
    while number > 0:
        if len(binary) > 32:
            return "ERROR"
        
        if number >= frac:
            binary += "1"
            number -= frac
        else:
            binary += "0"
    
        # move onto the next index
        frac /= 2
    
    return binary
       
    
print(binaryToString(0.72)) # ERROR
print(binaryToString(0.25)) # 0.01
print(binaryToString(0.75))  # 0.11
print(binaryToString(0.125)) # 0.001