from rich import print


def get_full_number(schematic: list, x: int, y: int):
    number = ""

    for index in schematic[x][y - 2 : y + 2]:
        if index.isnumeric():
            number = number + index
    # print(number)
    return number


def check_for_ajacent_numbers(schematic: list, x: int, y: int):
    indexes_with_numbers = []
    transformations = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

    for t in transformations:
        if schematic[x + t[0]][y + t[1]].isnumeric():
            indexes_with_numbers.append((x + t[0], y + t[1]))

    return list(set(indexes_with_numbers))


input_file = open("day3/input.txt", "r")
input_lines = input_file.readlines()

all_adjacent_num_indexes = []

for x in input_lines:
    for y in x:
        if not y.isalnum() and not y == "." and not y == "\n":
            all_adjacent_num_indexes = list(set(all_adjacent_num_indexes + check_for_ajacent_numbers(input_lines, input_lines.index(x), x.index(y))))

all_values = 0
for index in all_adjacent_num_indexes:
    all_values += int(get_full_number(input_lines, index[0], index[1]))

print(all_values)
