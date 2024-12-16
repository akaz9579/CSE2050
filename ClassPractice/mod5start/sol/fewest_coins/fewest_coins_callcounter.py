def fewest_coins(amt: int, coins: list[int]):
    """Returns the fewest number of coins required to make amt"""
    global counter
    counter += 1

    # Base case
    if amt in coins:
        return 1
    
    # Find valid next steps
    possible_coins = [coin for coin in coins if coin <= amt]
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
    global counter
    counter += 1

    if amt in solved: return solved[amt]

    possible_coins = [coin for coin in coins if coin <= amt]
    min_coins = float('inf')

    for coin in possible_coins:
        n_coin = _fewest_coins(amt-coin, coins, solved) + 1

        if n_coin < min_coins:
            min_coins = n_coin

    solved[amt] = min_coins

    return solved[amt]

AMT = 25

# Header
print("="*54)
print(f"{'':14}{'n_calls':-^20}")
print(f"{'amt':<5}{'n_coins':<9}{'w/o memo':10}{'w/ memo':<10}")
print("-"*54)
      
for n_coins in range(1, 6):
    counter = 0
    fewest_coins(AMT, [i for i in range(1, n_coins+1)])
    n_rec = counter

    counter = 0
    fewest_coins_memo(AMT, [i for i in range(1, n_coins+1)])
    n_memo = counter

    print(f"{AMT:<5}{n_coins:<9}{n_rec:<10}{n_memo:<10}")

if __name__ == '__main__':
    assert fewest_coins_memo(50, [1, 5, 10, 25]) == 2
    assert fewest_coins_memo(50, [1, 5, 10, 20, 25]) == 2
    assert fewest_coins_memo(40, [1, 5, 10, 25]) == 3
    assert fewest_coins_memo(40, [1, 5, 10, 20, 25]) == 2

    print("all good!")