from collections import deque


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(x < 0 or x >= input_base for x in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    new_base_digits = deque([])
    base_10 = 0
    for digit in digits:
        base_10 = base_10 * input_base + digit
    while base_10 >= 0:
        new_base_digits.appendleft((base_10 % output_base))
        base_10 //= output_base
        if base_10 == 0:
            break

    return list(new_base_digits)
