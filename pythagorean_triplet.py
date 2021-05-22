from typing import List


def triplets_with_sum(number: int) -> List[int]:
    """Return a list of Pythagorean triplets for a given natural number."""
    trips = []

    def next_mn(mn_pair):
        m, n = mn_pair
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        trip_sum = a + b + c
        if trip_sum == number:
            trips.append(sorted([a, b, c]))
        elif trip_sum < number:

            # check for non-primitive Pythagorean triplets
            # which are multiples of primitive Pythagorean triplets
            if number % trip_sum == 0:
                f = number // trip_sum
                trips.append(sorted([a * f, b * f, c * f]))

            for mn in coprime_pairs_generator(mn_pair):
                next_mn(mn)

    next_mn([2, 1])
    return trips


def coprime_pairs_generator(mn_pair):
    def multiplier(matrix):
        return [row[0] * mn_pair[0] + row[1] * mn_pair[1] for row in matrix]

    A = ((2, -1),
         (1, 0))
    B = ((2, 1),
         (1, 0))
    C = ((1, 2),
         (0, 1))
    yield multiplier(A)
    yield multiplier(B)
    yield multiplier(C)
