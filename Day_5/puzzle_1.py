import re

inputFile = open("Day_5/input.txt", "r")
input_string = inputFile.readlines()
stacks = []
crates = []
space_no = 0
crate_val = ""

# create the initial stack automatically
# i saw a feew soluutions that have hardcoded it,
# although I wasn't sure how to do it myself efficiently
# I did it with the method below

while input_string != "\n":
    for line in input_string:
        line = line.replace("[", "").replace("]", "").replace("\n", "")
        for char in line:
            if char != " ":
                if space_no != 0:
                    empty_crate = space_no // 4
                    space_no = 0
                    for i in range(0, empty_crate):
                        crates.append(" ")
                crate_val = char
                crates.append(crate_val)
            else:
                space_no += 1

        stacks.append(crates)

print(stacks)
