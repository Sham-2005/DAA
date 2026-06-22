def max_coins(piles):
    piles.sort()
    n = len(piles)
    my_coins = 0
    rounds = n // 3
    for i in range(rounds):
        idx = n - 2 - (2 * i)
        my_coins += piles[idx]
    return my_coins
print(f"Ex 1: {max_coins([2,4,1,2,7,8])}") 
print(f"Ex 2: {max_coins([2,4,5])}")       