def money_change(n: int):
    coins = [10, 5, 1]
    n_of_coins = 0
    remaining = int(n)
    for coin in coins:
        n_of_coins += remaining//coin
        remaining = remaining % coin

        if remaining == 0:
            break

    assert remaining == 0
    return n_of_coins


if __name__ == "__main__":
    n = int(input())
    print(money_change(n))

