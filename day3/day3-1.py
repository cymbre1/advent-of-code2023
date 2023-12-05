import re
from rich import print


def is_special_char(c: str):
    return not c.isalnum() and not c == "." and not c == "\n"


def surrounding_positions(schematic: list, row: int, span: tuple[int, int]) -> list[int]:
    return [(y, x) for x in range(span[0] - 1, span[1] + 1) for y in range(row - 1, row + 2) if y >= 0 and y < len(schematic) and x >= 0 and x < len(schematic[row])]


def has_adjacent_symbols(schematic: list[list[str]], x: int, y: int, number_length: tuple[int, int]) -> bool:
    return any(is_special_char(schematic[i[0]][i[1]]) for i in surrounding_positions(schematic, x, number_length))


input_file = open("day3/input.txt", "r")
input_lines = input_file.readlines()

all_part_numbers = 0

for x, y in enumerate(input_lines):
    numeric_inputs = re.finditer(r"\d+", y)
    for num in numeric_inputs:
        if has_adjacent_symbols(input_lines, x, input_lines[x].index(y), num.span()):
            all_part_numbers += int(num.group())

print(all_part_numbers)
