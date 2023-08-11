class Solution(object):
    def change(self, amount, coins):
        comb = [0] * (amount + 1)
        comb[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                comb[i] += comb[i - coin]

        return comb[amount]
