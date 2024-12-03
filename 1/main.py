import os

def run(part):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'input.txt')
    input = open(file_path, 'r').read().split('\n')

    list_one = []
    list_two = []

    for row in input:
        [element_one, element_two] = row.split('   ')
        list_one.append(element_one)
        list_two.append(element_two)

    result = 0

    list_one.sort()
    list_two.sort()

    if part == 1:
        for index in range(len(list_one)):
            element_one = int(list_one[index])
            element_two = int(list_two[index])

            result += abs(element_one - element_two)
    else:
        for index in range(len(list_one)):
            element_one = list_one[index]
            frequency = len([element_two for element_two in list_two if element_two == element_one])
            result += int(element_one) * frequency
    print('result is ' + str(result))


run(2)