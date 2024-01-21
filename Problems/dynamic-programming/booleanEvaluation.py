# TODO revise
def count_eval(s, result, memo={}):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 if bool(int(s)) == result else 0
    if str(result) + s in memo:
        return memo[str(result) + s]

    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[0:i]
        right = s[i+1:len(s)]
        left_true = count_eval(left, True, memo)
        left_false = count_eval(left, False, memo)
        right_true = count_eval(right, True, memo)
        right_false = count_eval(right, False, memo)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if c == '^':
            total_true = left_true * right_false + left_false * right_true
        elif c == '&':
            total_true = left_true * right_true
        elif c == '|':
            total_true = left_true * right_true + left_false * right_true + left_true * right_false

        sub_ways = total_true if result else total - total_true
        ways += sub_ways

    memo[str(result) + s] = ways
    return ways

# Test the function
print(count_eval("1^0|0|1", False))  
print(count_eval("0&0&0&1^1|0", True))