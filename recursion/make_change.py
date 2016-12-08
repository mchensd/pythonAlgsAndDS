def dp_make_change(change, min_coins, coins):
    """coins_used = [] * change
    for i in range(change):
        coins_used[i] = [1] * i
    print(coins_used)"""
    for i in range(change + 1):
        coinCount = i

        for j in [c for c in coins if c <= i]:
            if min_coins[i-j] + 1 < coinCount:
                coinCount = min_coins[i-j] + 1

        min_coins[i] = coinCount

    return min_coins[change]

print(dp_make_change(13, [0] * 14, [1,5,10]))