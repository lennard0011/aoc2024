import os
import copy


cache = {}


def blink_at_stone_times(stone, times_left):
    cache_key = str(stone) + "_" + str(times_left)
    if cache_key in cache.keys():
        return cache[cache_key]
    
    if times_left == 0:
        result = 1
    elif stone == "0":
        result = blink_at_stone_times("1", times_left - 1)
    elif len(stone) % 2 == 0:
        left_part = str(int(stone[:int(len(stone) / 2)]))
        right_part = str(int(stone[int(len(stone) / 2):]))
        result = blink_at_stone_times(left_part, times_left - 1) + blink_at_stone_times(right_part, times_left - 1)
    else:
        result = blink_at_stone_times(str(int(stone) * 2024), times_left - 1)
    cache[cache_key] = result
    return result


def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle =  open(file_path, 'r').read().split('\n')
    matrix = [puzzle_line.split(" ") for puzzle_line in puzzle]
    stones = matrix[0]

    score = 0
    number_of_blinks = 25 if part == 1 else 75
    for stone in stones:
        score += blink_at_stone_times(stone, number_of_blinks)
        
    print(score)


main(2, "input")