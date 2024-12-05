def day_2_part_1():
    game_dict = {}                                                     # dictionary with all marble values
    check_dict = {}                                                    # dictionary tracking validity of each game
    with open("day 2 input.txt", "r") as input_file:
        temp_list = []
        lines_list = [line.strip().split(":") for line in input_file]  # get rid of \n and split game id from the rest
        for i in range(len(lines_list)):                               # for each line
            game_ID = lines_list[i][0][5:]                             # set game_ID equal to just the numeral (str)
            game_dict[game_ID] = {"green": [], "red": [], "blue": []}  # initialize the game_dict entry for that game_ID
            lines_list[i][1] = lines_list[i][1].split(";")             # split each game into the separate "bag pulls"
            temp_list = [a_string.split(",") for a_string in lines_list[i][1]]  # further split each bag pull by color
            for a_list in temp_list:                                   # this loop adds each # of marbles to the
                for b_string in a_list:                                # appropriate color list in game_dict
                    if " green" in b_string:
                        game_dict[game_ID]["green"].append(b_string[1:-6])
                    elif " blue" in b_string:
                        game_dict[game_ID]["blue"].append(b_string[1:-5])
                    elif " red" in b_string:
                        game_dict[game_ID]["red"].append(b_string[1:-4])
    for key, value in game_dict.items():                               # set each game to "true" (valid) until a number
        check_dict[key] = True
        for num in value["red"]:                                       # is too high
            if int(num)>12:
                check_dict[key] = False
        for num in value["green"]:
            if int(num)>13:
                check_dict[key] = False
        for num in value["blue"]:
            if int(num)>14:
                check_dict[key] = False
    total = 0
    for key, value in check_dict.items():
        if value:
            total += int(key)

    input_file.close()
    return total

def day_2_part_2():
    game_dict = {}                                                     # dictionary with all marble values
    power_dict = {}                                                    # dictionary with power values
    with open("day 2 input.txt", "r") as input_file:
        temp_list = []
        lines_list = [line.strip().split(":") for line in input_file]  # get rid of \n and split game id from the rest
        for i in range(len(lines_list)):                               # for each line
            game_ID = lines_list[i][0][5:]                             # set game_ID equal to just the numeral (str)
            game_dict[game_ID] = {"green": [], "red": [], "blue": []}  # initialize the game_dict entry for that game_ID
            lines_list[i][1] = lines_list[i][1].split(";")             # split each game into the separate "bag pulls"
            temp_list = [a_string.split(",") for a_string in lines_list[i][1]]  # further split each bag pull by color
            for a_list in temp_list:                                   # this loop adds each # of marbles to the
                for b_string in a_list:                                # appropriate color list in game_dict
                    if " green" in b_string:
                        game_dict[game_ID]["green"].append(int(b_string[1:-6]))
                    elif " blue" in b_string:
                        game_dict[game_ID]["blue"].append(int(b_string[1:-5]))
                    elif " red" in b_string:
                        game_dict[game_ID]["red"].append(int(b_string[1:-4]))

        for game_ID, marble_dict in game_dict.items():                 # find max number of each color marble per game
            power_dict[game_ID] = {"green": -1, "blue": -1, "red": -1, "total_power": -1}
            for color_key in marble_dict:
                power_dict[game_ID][color_key] = max(marble_dict[color_key])
        for game_ID, power_list in power_dict.items():
            power_dict[game_ID]["total_power"] = (power_dict[game_ID]["green"] *
                                            power_dict[game_ID]["blue"] * power_dict[game_ID]["red"])
        overall_power = 0
        for game_ID in power_dict:
            overall_power += power_dict[game_ID]["total_power"]
        return overall_power

    input_file.close()

#print(day_2_part_1())
print(day_2_part_2())