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

all_hands = []

all_hands += sorted(list(line for line in input_lines if is_high_card(line.split(" ")[0])), reverse=True, key=lambda x: [possible_cards.index(c) for c in x.split(" ")[0]])
all_hands += sorted(list(line for line in input_lines if is_one_pair(line.split(" ")[0])), reverse=True, key=lambda x: [possible_cards.index(c) for c in x.split(" ")[0]])
all_hands += sorted(list(line for line in input_lines if is_two_pair(line.split(" ")[0])), reverse=True, key=lambda x: [possible_cards.index(c) for c in x.split(" ")[0]])
all_hands += sorted(list(line for line in input_lines if is_three_of_a_kind(line.split(" ")[0])), reverse=True, key=lambda x: [possible_cards.index(c) for c in x.split(" ")[0]])
all_hands += sorted(list(line for line in input_lines if is_full_house(line.split(" ")[0])), reverse=True, key=lambda x: [possible_cards.index(c) for c in x.split(" ")[0]])
all_hands += sorted(list(line for line in input_lines if is_four_of_a_kind(line.split(" ")[0])), reverse=True, key=lambda x: [possible_cards.index(c) for c in x.split(" ")[0]])
all_hands += sorted(list(line for line in input_lines if is_five_of_a_kind(line.split(" ")[0])), reverse=True, key=lambda x: [possible_cards.index(c) for c in x.split(" ")[0]])

total = 0
for card in all_hands:
    print(card)
    print(int(card.split(" ")[1].replace("\n", "")))
    # print((all_hands.index(card) + 1))
    total += int(card.split(" ")[1].replace("\n", "")) * (all_hands.index(card) + 1)
print(total)

all_hand_scores = sum(int(card.split(" ")[1].replace("\n", "")) * (all_hands.index(card) + 1) for card in all_hands)
print(all_hand_scores)
