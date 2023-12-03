# only 12 red cubes, 13 green cubes, and 14 blue cubes?

inp = open("input.txt", "r")

part_1 = 0
part_2 = 0

#active iteration of lines in file starting from 1
active_line = 1

colors_stock = {
    "r": 12,
    "g": 13,
    "b": 14
}


#returns organize dict from raw game
def group_cubes_colors(game):
    game = game.split("\n")[0]
    gameID = game.split(":")
    gameInfo = gameID[1]
    gameID = gameID[0]

    #the length of each color (eg. red => 3)
    color_len = {
        "r": 3,
        "b": 4,
        "g": 5
    }

    # an dictionary of empty list for each colors
    organize_game = {
        "r": [],
        "b": [],
        "g": []
    }

    i = 1
    active_digit = ""
    active_color = ""

    #go through each characters in the game 
    while i < len(gameInfo):

        #if a charcter is digit concat character to active_digit
        if gameInfo[i].isdigit():
            active_digit += gameInfo[i]
            i += 1

        # if a character startswith r,g,b concat the caracter to active_color and color in organize_game
        elif gameInfo[i] in color_len.keys():

            active_color = gameInfo[i]
            organize_game[gameInfo[i]].append(active_digit)
            active_digit = ""

            i += color_len[gameInfo[i]]

        else:
            i += 1

    return organize_game

# returns if game is possible
def game_is_possible(organize_games):

    for color, count in colors_stock.items():
        for i in organize_games[color]:
            if int(i) > count:
                return False

    return True

#returns  power of game
def get_power(organize_game):
    power = 1
    for color in colors_stock.keys():
       power *= max([int(i) for i in organize_game[color]])
    
    return power

for i in inp:
    
    groupped = group_cubes_colors(i)
    if game_is_possible(groupped):
        part_1 += active_line
    
    part_2 += get_power(groupped)

    active_line += 1

print("Part:1", part_1)
print("Part 2: ",part_2)