input_file = open("day1/input.txt", "r")
input_lines = input_file.readlines()

numbers = []

for line in input_lines:
    line_with_no_letters = "".join(filter(str.isdecimal, line))
    numbers.append(int(line_with_no_letters[0] + line_with_no_letters[-1]))

print(sum(numbers))
