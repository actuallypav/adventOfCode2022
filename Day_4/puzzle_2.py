inputFile = open("Day_4/input.txt", "r")
Tasks = inputFile.readlines()
sum_of_overlaps = 0

# loop through each set of two tasks
for task in Tasks:
    task.strip("\n")
    # split the tasks into sections
    sections_one, section_two = task.split(",")

    # split into lower and upper range
    section_one_lower, section_one_upper = sections_one.split("-")
    section_two_lower, section_two_upper = section_two.split("-")

    # check if either overlaps anywhere
    if int(section_one_lower) in range(
        int(section_two_lower), int(section_two_upper) + 1, 1
    ) or int(section_one_upper) in range(
        int(section_two_lower), int(section_two_upper) + 1, 1
    ):
        sum_of_overlaps += 1
    elif int(section_two_lower) in range(
        int(section_one_lower), int(section_one_upper) + 1, 1
    ) or int(section_two_upper) in range(
        int(section_one_lower), int(section_one_upper) + 1, 1
    ):
        sum_of_overlaps += 1

print("The sum of overlaps is: ", sum_of_overlaps)
