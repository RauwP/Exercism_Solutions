def is_armstrong_number(number):
    n = number
    num_str = str(number)
    num_len = len(num_str)
    total = 0
    while n > 0:
        total += (n % 10) ** num_len
        n //= 10
    return total == number
