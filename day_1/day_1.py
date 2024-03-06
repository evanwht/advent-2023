import os


def decode_calibration_values():
    with open('day_1/input_1.txt') as input:
        sum = 0
        for line in input.readlines():
            # line = replace_string_digits(line)

            first, last = '', ''
            res = ''
            for i in range(len(line)):
                if line[i].isdigit():
                    char = line[i]
                    res += char
                    if first == '':
                        first, last = char, char
                    else:
                        last = char
                else:
                    char = digit_string(line, i)
                    if char != '':
                        res += char
                        if first == '':
                            first, last = char, char
                        else:
                            last = char
            sum += int(first+last)
        print(sum)


digits_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def digit_string(line: str, i: int) -> str:
    if len(line) > i+3 and line[i:i+3] in digits_map.keys():
        return digits_map[line[i:i+3]]
    if len(line) >= i+4 and line[i:i+4] in digits_map.keys():
        return digits_map[line[i:i+4]]
    if len(line) >= i+5 and line[i:i+5] in digits_map.keys():
        return digits_map[line[i:i+5]]
    return ''


if __name__ == "__main__":
    decode_calibration_values()  # 54951
