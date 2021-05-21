from typing import List
import math


def triplets_with_sum(number: int) -> list[list[int]]:
    """Return a list of Pythagorean triplets for which a + b + c = N"""
    trip = []

    # for n in range(1, number + 1):
    #     print(n)
    #     if n ** 2 + (n + 1) ** 2 == (n + 2) ** 2:
    #         nums = []
    #         a = n ** 2
    #         b = (n + 1) ** 2
    #         c = (n + 2) ** 2
    #         print(math.sqrt(a), math.sqrt(b), math.sqrt(c))
    #         if a + b + c == number:
    #             print("found a triplet")
    #             nums.append(int(math.sqrt(a)))
    #             nums.append(int(math.sqrt(b)))
    #             nums.append(int(math.sqrt(c)))
    #             trip.append(nums)

    nums_list = [n for n in range(1, number + 1)]
    print(nums_list)
    a = nums_list[0]

    return trip


# print(triplets_with_sum(12)) # [[3, 4, 5]]
print(triplets_with_sum(90))  # [[9, 40, 41], [15, 36, 39]]
