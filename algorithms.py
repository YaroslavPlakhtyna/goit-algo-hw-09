from typing import Callable


def find_coins_greedy_init(
    coins: tuple[int] = (1, 2, 5, 10, 50)
) -> Callable[[int], dict[int, int]]:
    coins = sorted(coins, reverse=True)

    def find_coins_greedy(total):
        if not total:
            return {}

        current = 0
        result = {}

        while current != total:
            coin = max(coins, key=lambda c: current + c <= total)
            current += coin
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1

        return result

    return find_coins_greedy


def find_min_coins_init(
    coins: tuple[int] = (1, 2, 5, 10, 50)
) -> Callable[[int], dict[int, int]]:
    max_coin_cache = {}
    coins = sorted(coins, reverse=True)
    max_coin = max(coins)

    def find_min_coins(total: int) -> dict[int, int]:
        if not total:
            return {}

        if total in max_coin_cache:
            return max_coin_cache[total]

        cachable = total
        result = {}
        for coin in coins:
            count = total // coin
            if count > 0:
                result[coin] = count
            total -= coin * count
            if not total:
                if cachable <= max_coin:
                    max_coin_cache[cachable] = result
                return result

    for i in range(1, max_coin + 1):
        max_coin_cache[i] = find_min_coins(i)

    return find_min_coins


find_coins_greedy = find_coins_greedy_init()
find_min_coins = find_min_coins_init()

if __name__ == "__main__":
    gr = find_coins_greedy(113)
    print("Result for greedy algo:", gr)
    mccd = find_min_coins(113)
    print("Result for max coin cache dynamic algo:", mccd)
    assert gr == mccd == {1: 1, 2: 1, 10: 1, 50: 2}
