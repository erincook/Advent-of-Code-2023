def day_6_part_1(input_filename):                               # pass in input filename
    with open(input_filename, "r") as input_file:               # open file
        input_list = [lines.split() for lines in input_file]    # set up initial list - each line, sep. by whitespace
        tuple_list = []                                         # initialize "tuple_list"
        print(input_list)
        for i in range(1, len(input_list[0])):                  # starting with the numerical values, make a tuple for
            my_tuple = int(input_list[0][i]), int(input_list[1][i]) # each race - 1: time, 2: distance - as ints
            tuple_list.append(my_tuple)                         # store each tuple in "tuple_list"
        print(tuple_list)

        # calculate possible "hold button down time"/"distance travelled" combinations
        # note: button held for 0 seconds will always result in no movement (speed 0), as will holding the button
        # for the whole time duration of the race (no time for boat to move, regardless of speed built up)
        race_dict = {}                                          # initialize race_dict
        for race in tuple_list:                                 # outer loop - repeat for every race
            race_dict[race] = {}                                # use race tuple as dict key
            for num_secs in range(1, race[0]):                  # for # of seconds 1 to "length of race"-1
                speed = num_secs                                # in mm/ms.  speed builds 1 mm/ms, per ms held.
                movement_time = race[0] - num_secs              # amount of time for boat to move is total time - amt of
                distance = movement_time * speed                # time button is held. // distance = time * speed, in mm
                record_distance = race[1]                       # record distance is second number in race tuple
                # build out race_dict with information calc'd above
                race_dict[race][num_secs] = {"distance": distance, "can_win": record_distance < distance}

        win_list = []                                           # make a list of the number of ways to win for each race
        for race in race_dict:                                  # for each race in the dict
            ways_to_win = 0                                     # initialize the counter "ways_to_win"
            for entry in race_dict[race]:                       # for each # of seconds holding the button down
                if race_dict[race][entry]["can_win"]:           # if that attempt would result in a win
                    ways_to_win += 1                            # increment the counter
            win_list.append(ways_to_win)                        # append the count to the list
        print(win_list)

        product = 1                                             # initialize a product amount
        for win_ways in win_list:                               # loop through the ways to win list and multiply
            product *= win_ways                                 # them all together
        return product                                          # return that product


    input_file.close()

#print(day_6_part_1("day 6 input.txt"))

# Part 2
# new time: 35937366
# new record distance: 212206012011044

total_time = 35937366
record_distance = 212206012011044

# check the halfway point
# half_time = total_time / 2
# half_time_distance = half_time ** 2        # half-time seconds becomes speed in mm/ms, travel is other half of race
# print(half_time_distance)
# print(half_time_distance > record_distance)

# check 1/4
quarter_time = total_time // 4
# quarter_time_distance = quarter_time * (total_time - quarter_time)
# print(quarter_time_distance)
# print(quarter_time_distance > record_distance)

# check 1/8
eighth_time = total_time // 8
# eighth_time_distance = eighth_time * (total_time - eighth_time)
# print(eighth_time_distance)
# print(eighth_time_distance > record_distance)

new_time_1 = (quarter_time + eighth_time) // 2
# new_time_1_distance = new_time_1 * (total_time - new_time_1)
# print(eighth_time)
# print(new_time_1_distance)
# print(new_time_1)
# print(new_time_1_distance > record_distance)

new_time_2 = (new_time_1 + quarter_time) // 2
# new_time_2_distance = new_time_2 * (total_time - new_time_2)
# print(new_time_2)
# print(new_time_2_distance > record_distance)

