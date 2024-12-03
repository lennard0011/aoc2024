import os
import re

def run(part):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    input = open(file_path, 'r').read().split('\n')

    result = 0
    is_turned_on = True

    for line in input:
        regex = "mul\(\d{1,3},\d{1,3}\)"
        if part == 2:
            regex += "|do\(\)|don't\(\)"
        matches = re.findall(regex, line)
        for match in matches:
            # if part two and enabled, check if there is a don't.
            if match == "don't()":
                is_turned_on = False
                continue

            # if part two and disabled, check if there is a do
            if match == "do()":
                is_turned_on = True
                continue

            if not is_turned_on:
                continue

            [numberOne, numberTwo] = re.findall("\d{1,3},\d{1,3}", match)[0].split(",")
            result += int(numberOne) * int(numberTwo)

    print('result is ' + str(result))


run(2)