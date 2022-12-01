# Read the text file
inputFile = open("input.txt", "r")
currentCalories = 0
maxCalories = 0
Foods = inputFile.readlines()

# Loop line by line
for food in Foods:
    food = food.replace("\n", "")
    # Are we switching to another elf?
    if len(food) == 0:
        # Is this elf carrying more than the maximum that has been carried?
        if maxCalories < currentCalories:
            maxCalories = currentCalories
            # Reset current calories to nothing
        currentCalories = 0
        print(maxCalories)
    else:
        currentCalories = currentCalories + int(food)

# Answer
print("The most calories an Elf is carrying is: " + str(maxCalories))
