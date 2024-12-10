import os
import copy

START = 0
FINISH = 9


def find_start_positions(matrix):
    coordinates = set()
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == START: 
                coordinates.add((i, j))
    return coordinates


def find_ends(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    char = matrix[x][y]

    if char == FINISH:
        return [(x, y)]
    
    found_coordinates = []
    if 0 <= x - 1 < rows and matrix[x - 1][y] == char + 1:
        found_coordinates.extend(find_ends(matrix, x - 1, y))

    if 0 <= x + 1 < rows and matrix[x + 1][y] == char + 1:
        found_coordinates.extend(find_ends(matrix, x + 1, y))

    if 0 <= y - 1 < cols and matrix[x][y - 1] == char + 1:
        found_coordinates.extend(find_ends(matrix, x, y - 1))

    if 0 <= y + 1 < cols and matrix[x][y + 1] == char + 1:
        found_coordinates.extend(find_ends(matrix, x, y + 1))

    return found_coordinates


def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle =  open(file_path, 'r').read().split('\n')
    matrix = [list(map(int, list(puzzle_line))) for puzzle_line in puzzle]

    start_coordinates = find_start_positions(matrix)
    result = 0
    for coordinate in start_coordinates:
        x, y = coordinate
        ends = find_ends(matrix, x, y)
        if part == 1:
            result += len(set(ends))
        if part == 2:
            result += len(ends)
    print(result)


main(2, "input")