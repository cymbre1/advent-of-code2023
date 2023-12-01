from rich import print

numbers_written_out = {
    "twone": "21",
    "eightwo": "82",
    "eighthree": "83",
    "sevenine": "79",
    "threeight": "38",
    "oneight": "18",
    "nineight": "98",
    "fiveight": "58",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

input_file = open("input.txt", "r")
input_lines = input_file.readlines()

new_lines = []
for line in input_lines:
    for written in numbers_written_out:
        line = line.replace(written, numbers_written_out[written])
    new_lines.append(line)

numbers = []
for line in new_lines:
    line_with_no_letters = "".join(filter(str.isdecimal, line))
    numbers.append(int(line_with_no_letters[0] + line_with_no_letters[-1]))

print(sum(numbers))
