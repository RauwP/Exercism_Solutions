import itertools


def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    # 1. Filter out the excluded numbers
    valid_nums = [x for x in range(1, 10) if x not in exclude]

    # 2. Generate and filter the combinations simultaneously
    return [
        list(combo)
        for combo in itertools.combinations(valid_nums, size)
        if sum(combo) == target
    ]
