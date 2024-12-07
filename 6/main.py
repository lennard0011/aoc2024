import os

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


def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle =  open(file_path, 'r').read().split('\n')
    matrix = [list(puzzle_line) for puzzle_line in puzzle]

    x, y = find_start_position(matrix)

    seen = set()
    seen.add((x, y))

    while (True):
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

    score = len(seen)
        
    print(score)
   
main(2, "input")