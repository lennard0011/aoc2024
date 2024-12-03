import os

def valid_series(numbers):
    if len(numbers) < 2:
        return True
    if numbers[0] == numbers[1]:
        return False
    
    is_increasing = numbers[0] < numbers[1]
    prev = numbers[0]

    for number in numbers[1:]:
        if is_increasing and number <= prev:
            return False
        elif (not is_increasing) and number >= prev:
            return False

        diff = abs(number - prev)

        if diff < 1 or diff > 3:
            return False
        prev = number
        
    return True


def valid_without_one(numbers):
    for index in range(len(numbers)):
        new_list = numbers.copy()
        new_list.pop(index)
        if valid_series(new_list):
            print(new_list)
            return True
    return False


def run(part):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    input = open(file_path, 'r').read().split('\n')

    result = 0

    for line in input:
        numbers = [int(number) for number in line.split(' ')]
        if valid_series(numbers):
            print(numbers)
            result += 1
        elif part == 2 and valid_without_one(numbers):
            result += 1

    print('result is ' + str(result))


run(2)