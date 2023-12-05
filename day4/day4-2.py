import re

from rich import print

input_file = open("day4/input.txt", "r")
input_lines = input_file.readlines()
scratchcards = {index: 1 for index in range(len(input_lines))}

for card in input_lines:
    winning_numbers = re.findall(r"\d+", card.split("|")[0].split(":")[1])
    card_numbers = re.findall(r"\d+", card.split("|")[1])

    for num in card_numbers:
        if num in winning_numbers:
            scratchcards[int(num)] += 1

            copy_winning_numbers = re.findall(r"\d+", card.split("|")[0].split(":")[1])
            copy_card_numbers = re.findall(r"\d+", card.split("|")[1])
            for copy_num in copy_card_numbers:
                if copy_num in copy_winning_numbers:
                    scratchcards[int(copy_num)] += 1

print(sum(scratchcards.values()))
