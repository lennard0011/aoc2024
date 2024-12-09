import os


def find_antennas(matrix, channel):
    antenna_locations = []
    for i in range(len(matrix)):
        antenna_locations.extend([(i, j) for j in range(len(matrix[0])) if matrix[i][j] is channel])
    return antenna_locations


def find_difference(antenna_of_interest, other_antenna, row_max, column_max, part):
    (x_current, y_current) = antenna_of_interest
    (x_other, y_other) = other_antenna

    x_delta = x_other - x_current
    y_delta = y_other - y_current

    locations = []

    if part == 1:
        x_current = x_current - x_delta
        y_current = y_current - y_delta
        if 0 <= x_current < row_max and 0 <= y_current < column_max:
            locations.append((x_current, y_current))
    if part == 2:
        locations.append((x_current, y_current))
        while (True):
            x_current = x_current - x_delta
            y_current = y_current - y_delta
            if 0 <= x_current < row_max and 0 <= y_current < column_max:
                locations.append((x_current, y_current))
            else: 
                break

    return locations


def find_anti_node_locations(antenna_locations, row_max, column_max, part):
    locations = []
    for i in range(len(antenna_locations)):
        for j in range(len(antenna_locations)):
            if i == j:
                continue
            antenna_of_interest = antenna_locations[i]
            different_antenna = antenna_locations[j]
            anti_node_locations = find_difference(antenna_of_interest, different_antenna, row_max, column_max, part)
            locations.extend(anti_node_locations)
    return locations


def print_matrix_with_solution(matrix, locations):
    for i in range(len(matrix)):
        row_string = ""
        for j in range(len(matrix[0])):
            if (i,j) in locations and matrix[i][j] == ".":
                row_string += "#"
                continue
            row_string += matrix[i][j]
        print(row_string)
    

def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle =  open(file_path, 'r').read().split('\n')
    matrix = [list(puzzle_line) for puzzle_line in puzzle]

    channels = set()
    anti_node_locations = set()
    for matrix_row in matrix:
        channels.update([channel for channel in matrix_row if channel != "."])

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    for channel in channels:
        # for a channel, calculate the antinodes and put the coordinates in the set.
        antenna_locations = find_antennas(matrix, channel)
        anti_nodes = find_anti_node_locations(antenna_locations, number_of_rows, number_of_columns, part)
        anti_node_locations.update(anti_nodes)

    #print_matrix_with_solution(matrix, anti_node_locations)
    print(len(anti_node_locations))


main(2, "input")