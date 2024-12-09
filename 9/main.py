import os
import copy


def decompress_string(file_string):
    length = sum([int(i) for i in file_string])
    file = [-1 for i in range(length)]

    is_file = True
    file_id = 0
    index = 0
    for element in file_string:
        int_element = int(element)
        if is_file:
            file[index:index + int_element] = [file_id for i in range(int_element)]
            file_id += 1
        else:
            file[index:index + int_element] = ["." for i in range(int_element)]
        
        index = index + int_element
        is_file = not is_file
    return file



def reduce_string(file_string):
    pointer_left = 0
    pointer_right = len(file_string) - 1

    cleaned_file = copy.deepcopy(file_string)

    while(True):
        if pointer_left == pointer_right:
            break
        if cleaned_file[pointer_left] != ".":
            pointer_left += 1
            continue
        if cleaned_file[pointer_right] == ".":
            pointer_right -= 1
            continue
        
        cleaned_file[pointer_left] = file_string[pointer_right]
        cleaned_file[pointer_right] = "."
        pointer_left += 1
        pointer_right -= 1
    
    return cleaned_file[:pointer_left + 1]


def calculate_check_sum(cleaned_string):
    sum = 0
    for i in range(len(cleaned_string)):
        if cleaned_string[i] == ".":
            continue
        sum += i * cleaned_string[i]
    return sum


def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle =  open(file_path, 'r').read().split('\n')
    matrix = [list(puzzle_line) for puzzle_line in puzzle]

    line = matrix[0]

    file = decompress_string(line)
    cleaned_string = reduce_string(file)
    check_sum = calculate_check_sum(cleaned_string)

    print(check_sum)


main(1, "input")