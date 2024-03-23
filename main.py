import random
import timeit

from algorithms import find_coins_greedy, find_min_coins


if __name__ == "__main__":
    for amounts in (100, 1000, 10000):
        for attempts in (1000, 10000, 100000):
            print(
                "------------------------------------------------------------------------"
            )
            print(
                f"Results for amount range of {amounts} with attempts equal to {attempts}"
            )

            result = timeit.timeit(
                stmt="find_coins_greedy(random.randint(1, amounts))",
                globals=globals(),
                number=attempts,
            )
            print("Greedy algorithm: %s seconds" % result)

            result = timeit.timeit(
                stmt="find_min_coins(random.randint(1, amounts))",
                globals=globals(),
                number=attempts,
            )
            print("Max coin cache dynamic algorithm: %s seconds" % result)
            print(
                "------------------------------------------------------------------------"
            )
            print()
