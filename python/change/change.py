def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    dp = [None] * (target + 1)
    dp[0] = []

    for current_amount in range(1, target + 1):
        possible_combos = []

        for coin in coins:
            if coin <= current_amount and dp[current_amount - coin] is not None:
                combo = dp[current_amount - coin] + [coin]
                possible_combos.append(combo)
        if possible_combos:
            possible_combos.sort(key=len)
            dp[current_amount] = possible_combos[0]
    if dp[target] is None:
        raise ValueError("can't make target with given coins")
    return sorted(dp[target])
