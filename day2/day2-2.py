from rich import print


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


def get_number_from_game(game_name: str):
    return int(game_name.replace("Game ", "").replace(":", ""))


input_file = open("day2/input.txt", "r")
input_lines = input_file.readlines()

powers = 0

for line in input_lines:
    max_red = 0
    max_green = 0
    max_blue = 0
    for set in (split_line := line.split(":"))[1].split(";"):
        sorted_set = ColorSet(set)
        max_red = max(sorted_set.red, max_red)
        max_green = max(sorted_set.green, max_green)
        max_blue = max(sorted_set.blue, max_blue)
    powers += max_red * max_green * max_blue

print(powers)
