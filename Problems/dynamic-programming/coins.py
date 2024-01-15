class CoinChange:
    def __init__(self):
        self.coins = [25, 10, 5, 1]
        self.memo = {}

    def coin_combinations_iterative(self,amount):
        ways = [0] * (amount + 1)
        ways[0] = 1  # There's only one way to make change for 0 cents

        for coin in self.coins:
            for higher_amount in range(coin, amount + 1):
                higher_amount_remainder = higher_amount - coin
                ways[higher_amount] += ways[higher_amount_remainder]

        return ways[amount]
    
    def change_possibilities_recursive(self, amount):
        self.memo = {}
        return self.recursive_helper(amount, 0)

    # recursive solution
    def recursive_helper(self, n, index):
        if n == 0:
            return 1
        if n < 0 or index == len(self.coins):
            return 0
        
        if (n, index) in self.memo:
            return self.memo[(n, index)]
        
        # we could either use the coin at index or not use it and go to the next coin
        res = self.recursive_helper(n - self.coins[index], index) + self.recursive_helper(n, index + 1)

        # add to lookup table
        self.memo[(n, index)] = res
        return res
        

def test_coin_change():
    coin_change = CoinChange()

    possibilities = coin_change.change_possibilities_recursive(100)
    print("computed possibilities: ",possibilities)
    assert possibilities == 242

    possibilities = coin_change.coin_combinations_iterative(100)
    print("computed possibilities: ",possibilities)
    assert possibilities == 242

    print("All tests passed!")

if __name__ == "__main__":
    test_coin_change()