inputFile = open("input.txt", "r")
currentCalories = 0
maxCalories = 0
Foods = inputFile.readlines()


for food in Foods:
    food = food.replace("\n", "")
    if len(food) == 0:
        if maxCalories < currentCalories:
            maxCalories = currentCalories
    else:
        currentCalories = currentCalories + int(food)

print("The most calories an Elf is carrying is: " + str(maxCalories))
