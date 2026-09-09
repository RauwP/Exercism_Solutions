"""Module for calculating the Collatz Conjecture."""


def steps(number):
    """Calculate the number of steps to reach 1 using the Collatz rules."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        step += 1
    return step
