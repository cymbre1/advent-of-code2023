from rich import print

POSSIBLE_RED = 12
POSSIBLE_GREEN = 13
POSSIBLE_BLUE = 14


class ColorSet:
    def __init__(self, colors: str):
        if (red_index := colors.find("red")) >= 2:
            self.red = int(str(colors[red_index - 3]) + str(colors[red_index - 2])) if red_index >= 3 and (colors[red_index - 3].isdecimal()) else int(colors[red_index - 2])
        else:
            self.red = 0

        if (green_index := colors.find("green")) >= 2:
            self.green = (
                int(str(colors[green_index - 3]) + str(colors[green_index - 2])) if green_index >= 3 and (colors[green_index - 3].isdecimal()) else int(colors[green_index - 2])
            )
        else:
            self.green = 0

        if (blue_index := colors.find("blue")) >= 2:
            self.blue = int(str(colors[blue_index - 3]) + str(colors[blue_index - 2])) if blue_index >= 3 and (colors[blue_index - 3].isdecimal()) else int(colors[blue_index - 2])
        else:
            self.blue = 0

    def check_if_possible(self):
        return self.red <= POSSIBLE_RED and self.blue <= POSSIBLE_BLUE and self.green <= POSSIBLE_GREEN


def get_number_from_game(game_name: str):
    return int(game_name.replace("Game ", "").replace(":", ""))


input_file = open("day2/input.txt", "r")
input_lines = input_file.readlines()

id_sum = 0

for line in input_lines:
    game_is_possible = True
    for set in (split_line := line.split(":"))[1].split(";"):
        if not ColorSet(set).check_if_possible():
            game_is_possible = False
    if game_is_possible:
        id_sum += get_number_from_game(split_line[0])

print(id_sum)
