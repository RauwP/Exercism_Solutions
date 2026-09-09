def is_paired(input_string):
    mag = []
    pairs = {"}": "{", "]": "[", ")": "("}
    for char in input_string:
        if char in "[{(":
            mag.append(char)
        elif char in pairs:
            if not mag or mag.pop() != pairs[char]:
                return False
    return not mag
