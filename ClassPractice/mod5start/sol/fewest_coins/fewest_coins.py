def fewest_coins(amt: int, coins: list[int]):
    """Returns the fewest number of coins required to make amt"""
    # Base case
    if amt in coins:
        return 1
    
    # Recursive case:
    # min_coins = 1 + fewest_coins(amt-coin)
    
    # Find valid next steps
    possible_coins = [coin for coin in coins if coin <= amt]

    possible_coins = []
    for coin in coins:
        if coin <= amt:
            possible_coins.append(coin)

    min_coins = float('inf')

    # Explore each, looking for optimal solution
    for coin in possible_coins:
        n_coin = fewest_coins(amt-coin, coins) + 1

        # Did we find a new optimum?
        if n_coin < min_coins:
            min_coins = n_coin

    return min_coins

def fewest_coins_memo(amt: int, coins: list[int]):
    solved = {coin:1 for coin in coins}
    return _fewest_coins(amt, coins, solved)

def _fewest_coins(amt, coins, solved):
    if amt in solved: return solved[amt]

    possible_coins = [coin for coin in coins if coin <= amt]
    min_coins = float('inf')

    for coin in possible_coins:
        n_coin = _fewest_coins(amt-coin, coins, solved) + 1

        if n_coin < min_coins:
            min_coins = n_coin

    solved[amt] = min_coins

    return solved[amt]

print(fewest_coins_memo(50, [1, 2, 5, 10, 25]))
# if __name__ == '__main__':
#     assert fewest_coins_memo(50, [1, 5, 10, 25]) == 2
#     assert fewest_coins_memo(50, [1, 5, 10, 20, 25]) == 2
#     assert fewest_coins_memo(40, [1, 5, 10, 25]) == 3
#     assert fewest_coins_memo(40, [1, 5, 10, 20, 25]) == 2

#     print("all good!")