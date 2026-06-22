def min_added_coins(coins, target):
    coins.sort()
    current_max_reachable = 0
    added_coins = 0
    index = 0
    while current_max_reachable < target:
        if index < len(coins) and coins[index] <= current_max_reachable + 1:
            current_max_reachable += coins[index]
            index += 1
        else:
            added_coin = current_max_reachable + 1
            current_max_reachable += added_coin
            added_coins += 1   
    return added_coins
print(f"Added Coins Ex 1: {min_added_coins([1,4,10], 19)}")             
print(f"Added Coins Ex 2: {min_added_coins([1, 4, 10, 5, 7, 19], 19)}") 