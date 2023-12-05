import re
from rich import print


def is_gear(c: str):
    return c == "*"


def surrounding_positions(schematic: list, row: int, span: tuple[int, int]) -> list[int]:
    return [(y, x) for x in range(span[0] - 1, span[1] + 1) for y in range(row - 1, row + 2) if y >= 0 and y < len(schematic) and x >= 0 and x < len(schematic[row])]


def has_adjacent_gears(schematic: list[list[str]], x: int, y: int, number_length: tuple[int, int]) -> bool:
    return (i for i in surrounding_positions(schematic, x, number_length) if is_gear(schematic[i[0]][i[1]]))


input_file = open("day3/input.txt", "r")
input_lines = input_file.readlines()

possible_gears = {}

for x, y in enumerate(input_lines):
    numeric_inputs = re.finditer(r"\d+", y)
    for num in numeric_inputs:
        for gear in (gears := has_adjacent_gears(input_lines, x, input_lines[x].index(y), num.span())):
            if gear in possible_gears:
                possible_gears[gear].append(int(num.group()))
            else:
                possible_gears[gear] = [int(num.group())]

all_gear_ratios = 0

for gear in possible_gears:
    if len(possible_gears[gear]) == 2:
        gear_ratio = possible_gears[gear][0] * possible_gears[gear][1]
        all_gear_ratios += int(gear_ratio)

print(all_gear_ratios)
