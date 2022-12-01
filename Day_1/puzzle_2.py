# Read the text file
inputFile = open("input.txt", "r")
currentCalories = 0
Foods = inputFile.readlines()
top_3 = [0, 0, 0]
# Loop line by line
for food in Foods:
    food = food.replace("\n", "")
    # Are we switching to another elf?
    if len(food) == 0:
        # Is this elf carrying more than the any of the top 3?
        if min(top_3) < currentCalories:
            third = top_3.index(min(top_3))
            top_3[third] = int(currentCalories)
        # Reset current calories to nothing
        currentCalories = 0
    else:
        currentCalories = currentCalories + int(food)

# Answer
print("The top 3 calories are: " + str(top_3))
print("The total is: " + str(sum(top_3)))
