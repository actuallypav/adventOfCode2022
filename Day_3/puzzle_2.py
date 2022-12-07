sum_of_priorities = 0

with open("Day_3/input.txt", "r") as infile:
    rucksacks = infile.readlines()

    # check every 3 rucksacks
    for i in range(0, len(rucksacks), 3):
        (rucksack_one, rucksack_two, rucksack_three) = rucksacks[i : i + 3]
        group = [rucksack_one, rucksack_two, rucksack_three]
        # get the smallest rucksack per group
        smallest_rucksack = min(group)
        # remove smallest rucksack from the group
        group.remove(smallest_rucksack)

        # check every item in the smallest rucksack
        for item in smallest_rucksack:
            # check the item is in both of the other rucksacks
            if item in group[0] and item in group[1]:
                if item.isupper() == True:
                    # add the priority to the total
                    sum_of_priorities += ord(item) - 38
                    # once share item is found exit loop
                    break
                else:
                    sum_of_priorities += ord(item) - 96
                    break

print("The total priority of the groups is: " + str(sum_of_priorities))
