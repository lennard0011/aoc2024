import os
import copy


STONE = "#"


def find_start_position(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == "^":
                return x, y
    print('not found')


def go_right(matrix, x, y, seen):
    path_forward = matrix[x][y:]
    if STONE not in path_forward:
        seen.update([(x, y_incrementing) for y_incrementing in range(y, len(matrix[0]))])    
        return None
    new_y = y + path_forward.index(STONE) - 1
    seen.update([(x, y_incrementing) for y_incrementing in range(y, new_y + 1)])
    return (x, new_y)


def go_left(matrix, x, y, seen):
    path_forward = matrix[x][y::-1]
    if STONE not in path_forward:
        seen.update([(x, y_incrementing) for y_incrementing in range(0, y + 1)])    
        return None
    new_y = y - path_forward.index(STONE) + 1
    seen.update([(x, y_incrementing) for y_incrementing in range(new_y, y + 1)])
    return (x, new_y)


def go_up(matrix, x, y, seen):
    path_forward = [matrix[index][y] for index in range(x, -1, -1) ]
    if STONE not in path_forward:
        seen.update([(x_incrementing, y) for x_incrementing in range(0 - 1, x + 1)])
        return None
    new_x = x - path_forward.index(STONE) + 1
    seen.update([(x_incrementing, y) for x_incrementing in range(new_x, x + 1)])
    return (new_x, y)


def go_down(matrix, x, y, seen):
    path_forward = [matrix[index][y] for index in range(x, len(matrix)) ]
    if STONE not in path_forward:
        seen.update([(x_incrementing, y) for x_incrementing in range(x, len(matrix))])
        return None
    new_x = x + path_forward.index(STONE) - 1
    seen.update([(x_incrementing, y) for x_incrementing in range(x, new_x + 1)])
    return (new_x, y)


def solve(matrix):
    x, y = find_start_position(matrix)

    seen = set()
    seen.add((x, y))

    up_position_seen = set()

    while (True):
        if (x, y) in up_position_seen:
            return None
        up_position_seen.add((x,y))

        ans = go_up(matrix, x, y, seen)
        if (ans is None):
            break
        (x, y) = ans
        
        ans = go_right(matrix, x, y, seen)
        if (ans is None):
            break
        (x, y) = ans

        ans = go_down(matrix, x, y, seen)
        if (ans is None):
            break
        (x, y) = ans

        ans = go_left(matrix, x, y, seen)
        if (ans is None):
            break
        (x, y) = ans

    return seen


def permutate_matrix(matrix, seen):
    matrices = []

    x_start, y_start = find_start_position(matrix)

    for (i, j) in seen:
        if i == x_start and j == y_start:
            continue
        if matrix[i][j] == ".":
            new_matrix = copy.deepcopy(matrix)
            new_matrix[i][j] = STONE
            matrices.append(new_matrix)
    
    return matrices



def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle =  open(file_path, 'r').read().split('\n')
    matrix = [list(puzzle_line) for puzzle_line in puzzle]

    score = 0

    if part == 1:
        score += len(solve(matrix))
    elif part == 2:        
        score = 0
        seen = solve(matrix)
        possible_matrices = permutate_matrix(matrix, seen)
        for index in range(len(possible_matrices)):
            print(index)
            if solve(possible_matrices[index]) is None:
                score += 1

    print(score)
   
main(2, "input")