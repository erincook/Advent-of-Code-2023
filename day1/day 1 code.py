# Part 1
def find_first_last_digits():
    with open("advent of code 2023 day 1 input 1.txt", "r") as input_file:
        num_list = []
        total = 0
        # for each line in the input file, create a two-digit number consisting of the first numeral followed by the
        # second numeral
        for line in input_file:
            new_num = ""
            for i in range(len(line)):
                if line[i] in "0123456789":
                    new_num += line[i]
                    break
            for j in range(len(line)-1, -1, -1):
                if line[j] in "0123456789":
                    new_num += line[j]
                    break
            # turn the 2 digit number (currently string) into an integer and append to num_list
            num_list.append(int(new_num))
        # add up all the numbers thus created
        for num in num_list:
            total += num
    input_file.close()
    return total

# Part 2
def replace_with_digits():
    input_file = open("advent of code 2023 day 1 input 1.txt", "r")
    new_list = []
    num_list = []
    # create a dictionary that will be used to replace spelled-out numbers with numerals while preserving the first and
    # last letters of the spelled-out words (to account for overlaps)
    replacement_dict = {"one": "o1e", "two": "t2o", "three": "thr3e", "four": "fo4r", "five": "fi5e", "six": "s6x",
                        "seven": "se7en", "eight": "ei8ht", "nine": "ni9e"}
    # for each line in the input file, perform the replacement(s) described above, and append the result into a list
    for line in input_file:
        new_line = line.strip()
        for key, value in replacement_dict.items():
            if key in new_line:
                new_line = new_line.replace(key, value)
        new_list.append(new_line)
    # iterate through the list and find the first and last digit. could make this its own function and use it for both
    # part 1 and part 2, if i wanted to increase efficiency.
    for item in new_list:
        new_num = ""
        for char in item:
            if char in "0123456789":
                new_num += char
                break
        for j in range(len(item)-1, -1, -1):
            if item[j] in "0123456789":
                new_num += item[j]
                break
        num_list.append(int(new_num))
    # add up all the numbers
    total = 0
    for num in num_list:
        total += num
    input_file.close()
    return total

#print(find_first_last_digits())
print(replace_with_digits())