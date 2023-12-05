import re

from rich import print

input_file = open("day4/input.txt", "r")
input_lines = input_file.readlines()

score = 0

for line in input_lines:
    winning_numbers = re.findall(r"\d+", line.split("|")[0].split(":")[1])
    card_numbers = re.findall(r"\d+", line.split("|")[1])
    print(winning_numbers)
    print(card_numbers)
    number_of_matches = 0
    for num in card_numbers:
        if num in winning_numbers:
            number_of_matches += 1
    if number_of_matches > 0:
        score += pow(2, number_of_matches - 1)

print(score)
