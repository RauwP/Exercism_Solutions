def encode(numbers):
    ls = []
    for number in numbers:
        temp_bytes = []
        flag = 0x00
        while True:
            new_num = (number & 0x7F) | flag
            temp_bytes.append(new_num)
            flag = 0x80
            number >>= 7
            if number == 0:
                break
        ls.extend(temp_bytes[::-1])
    return ls


def decode(bytes_):
    decoded_ls = []
    current_val = 0

    for byte in bytes_:
        current_val = (current_val << 7) | (byte & 0x7F)

        if (byte & 0x80) == 0:
            decoded_ls.append(current_val)
            current_val = 0

    if (bytes_[-1] & 0x80) != 0:
        raise ValueError("incomplete sequence")
    return decoded_ls
