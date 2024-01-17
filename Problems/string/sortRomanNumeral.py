def romanToDecimal(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(1, len(roman)):
        if i > 0 and values[roman[i]] > values[roman[i - 1]]:
            decimal -= values[roman[i - 1]]
        else: 
            decimal += values[roman[i - 1]]

    decimal += values[roman[-1]]

    print(f"{roman} ->  {decimal}")

    return decimal

def romanToDecimal_(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for i in range(len(roman)):
        if i > 0 and values[roman[i]] > values[roman[i - 1]]:
            decimal += values[roman[i]] - 2 * values[roman[i - 1]]
        else: 
            decimal += values[roman[i]]
    return decimal

def sortRoman(names):
    """
    This function takes a list of strings, each string is comprised of a name and a Roman numeral.
    It sorts the list first by name, then by the decimal value of the Roman numeral.

    Parameters:
    names (list): A list of strings, each string is comprised of a name and a Roman numeral.

    Returns:
    list: A list of strings sorted first by name, then by the decimal value of the Roman numeral.
    """
    names = [name.split() for name in names]
    sorted_names = sorted(names, key=lambda x: (x[0], romanToDecimal(x[1])))
    return [name[0] + ' ' + name[1] for name in sorted_names]


# Test the function with some example inputs
print(sortRoman(['Steven XL', 'Steven XVI', 'David IX', 'Mary XV', 'Mary XIII', 'Mary XX']))  
# Expected output: ['David IX', 'Mary XIII', 'Mary XV', 'Mary XX', 'Steven XVI', 'Steven XL']
