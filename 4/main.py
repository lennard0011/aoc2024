import os

def check_string(string_to_check):
    return string_to_check == "XMAS" or string_to_check == "SAMX"

def check_mas_string(string_to_check):
    return string_to_check == "MAS" or string_to_check == "SAM"
   
#check horizontal right, vertical down, diagonal up-right, diagonal down-right.

def check_horizontal_right(puzzle, x, y):
    number_of_columns = len(puzzle[0])
    if y + 4 > number_of_columns:
        return False
    return check_string(''.join(puzzle[x][y:y+4]))
   

def check_vertical_down(puzzle, x, y):
    number_of_rows = len(puzzle)
    if x + 4 > number_of_rows:
        return False
    return check_string(puzzle[x][y] + puzzle[x+1][y] + puzzle[x+2][y] + puzzle[x+3][y])
   

def check_diagonal_up_right(puzzle, x, y):
    number_of_columns = len(puzzle[0])
    number_of_rows = len(puzzle)
   
    if y + 4 > number_of_columns:
        return False
    if x - 3 < 0:
        return False
   
    return check_string(puzzle[x][y] + puzzle[x-1][y+1] + puzzle[x-2][y+2] + puzzle[x-3][y+3])
   

def check_diagonal_down_right(puzzle, x, y):
    number_of_columns = len(puzzle[0])
    number_of_rows = len(puzzle)
   
    if y + 4 > number_of_columns:
        return False
    if x + 4 > number_of_rows:
        return False
   
    return check_string(puzzle[x][y] + puzzle[x+1][y+1] + puzzle[x+2][y+2] + puzzle[x+3][y+3])


def check_if_x_max(puzzle, x, y):
    # coordinates are of the A
    number_of_columns = len(puzzle[0])
    number_of_rows = len(puzzle)

    if not 0 < x < number_of_rows - 1 :
        return False
    if not 0 < y < number_of_columns - 1:
        return False

    diagonal_left = puzzle[x-1][y-1] + puzzle[x][y] + puzzle[x+1][y+1]
    diagonal_right = puzzle[x-1][y+1] + puzzle[x][y] + puzzle[x+1][y-1]

    return check_mas_string(diagonal_left) and check_mas_string(diagonal_right)


def main(part, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename + ".txt")
    puzzle = [list(line) for line in open(file_path, 'r').read().split('\n')]
           
    number_of_rows = len(puzzle)
    number_of_columns = len(puzzle[0])
   
    score = 0
   
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            char = puzzle[i][j]
            if part == 1:
                if char != 'X' and char != 'S':
                    continue
                if check_horizontal_right(puzzle, i, j):
                    score += 1
                if check_vertical_down(puzzle, i, j):
                    score += 1
                if check_diagonal_up_right(puzzle, i, j):
                    score += 1
                if check_diagonal_down_right(puzzle, i, j):
                    score += 1
            if part == 2:
                if char != 'A':
                    continue
                if check_if_x_max(puzzle, i, j):
                    score += 1
               
    print(score)
   
main(2, "input")