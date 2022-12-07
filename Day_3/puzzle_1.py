inputFile = open("input.txt", "r")
Compartments = inputFile.readlines()
sum_of_priorities = 0

for compartment in Compartments:
    rucksack = compartment.replace("\n", "")
    if len(rucksack != 0):
        compartment_length = len(compartment) // 2
        compartment_one = rucksack[0:compartment_length]
        compartment_two = rucksack[-compartment_length : len(rucksack)]

        for item in compartment_one:
            if item in compartment_two:
                if item.isupper() == True:
                    sum_of_priorities += ord(item) - 38
                else:
                    sum_of_priorities += ord(item) - 96
