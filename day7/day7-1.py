from rich import print

possible_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def is_five_of_a_kind(card: str):
    return any(p for p in possible_cards if card.count(p) == 5)


def is_four_of_a_kind(card: str) -> bool:
    return any(p for p in possible_cards if card.count(p) == 4)


def is_full_house(card: str) -> bool:
    len(list(p for p in possible_cards if card.count(p) == 3)) == 1 and len(list(p for p in possible_cards if card.count(p) == 1)) == 2


def is_three_of_a_kind(card: str):
    return any(p for p in possible_cards if card.count(p) == 3) and any(p for p in possible_cards if card.count(p) == 2)


def is_two_pair(card: str):
    return len(list(p for p in possible_cards if card.count(p) == 2)) == 2


def is_one_pair(card: str):
    return len(list(p for p in possible_cards if card.count(p) == 2)) == 1 and len(list(p for p in possible_cards if card.count(p) == 1)) == 3


def is_high_card(card: str):
    return len(list(p for p in possible_cards if card.count(p) == 1)) == 5


input_file = open("day7/input.txt", "r")
input_lines = input_file.readlines()

high_cards = list(line for line in input_lines if is_high_card(line.split(" ")[0]))

for card in high_cards:
    print(card)
    for letter in card.split(" ")[0]:
        # print(letter)
        print(possible_cards.index(letter))
# print(high_cards.sort(key=lambda x: possible_cards.index(x[0])))

# one_pairs = list(line for line in input_lines if is_one_pair(line.split(" ")[0]))
# print(one_pairs.sort(key=lambda element: possible_cards.index(element)))

# two_pairs = list(line for line in input_lines if is_two_pair(line.split(" ")[0]))
# print(two_pairs.sort(key=lambda element: possible_cards.index(element)))

# three_of_a_kind = list(line for line in input_lines if is_three_of_a_kind(line.split(" ")[0]))
# print(three_of_a_kind.sort(key=lambda element: possible_cards.index(element)))

# full_houses = list(line for line in input_lines if is_full_house(line.split(" ")[0]))
# print(full_houses.sort(key=lambda element: possible_cards.index(element)))

# four_of_a_kind = list(line for line in input_lines if is_four_of_a_kind(line.split(" ")[0]))
# print(four_of_a_kind.sort(key=lambda element: possible_cards.index(element)))

# five_of_a_kind = list(line for line in input_lines if is_five_of_a_kind(line.split(" ")[0]))
# print(five_of_a_kind.sort(key=lambda element: possible_cards.index(element)))
