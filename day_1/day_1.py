import os


def decode_calibration_values():
    with open('day_1/input_1.txt') as input:
        sum = 0
        for line in input.readlines():
            first = ''
            last = ''
            for char in line:
                if char.isdigit():
                    if first == '':
                        first = char
                        last = char
                    else:
                        last = char
            sum += int(first+last)
        print(sum)


if __name__ == "__main__":
    decode_calibration_values() # 54951