inputFile = open("Day_3/input.txt", "r")
Rucksacks = inputFile.readlines()
sum_of_priorities = 0

# get each rucksack one by one
for rucksack in Rucksacks:
    rucksack = rucksack.replace("\n", "")
    # check the rucksack exists
    if len(rucksack) != 0:
        # divide the rucksack into compartments
        rucksack_size = len(rucksack) // 2
        compartment_one = rucksack[0:rucksack_size]
        compartment_two = rucksack[-rucksack_size : len(rucksack)]

        # check if item exists in both compartments
        for item in compartment_one:
            if item in compartment_two:
                # check the priority of the item
                if item.isupper() == True:
                    # add the priority to the item
                    sum_of_priorities += ord(item) - 38
                    # once share item is found exit loop
                    break
                else:
                    sum_of_priorities += ord(item) - 96
                    break

# output
print("The sum of the priorities is: " + str(sum_of_priorities))
