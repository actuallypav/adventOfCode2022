#A, X = Rock
#B, Y = Paper
#C, Z = Scissors

#A > Z
#B > X
#C > Y

#read the text file
inputFile = open("input.txt", "r")
Choices = inputFile.readlines()
totalScore = 0

#loop line by line
for choice in Choices:
    choice = choice.replace("\n","")
    #split the choices
    enemyChoice, playerChoice = choice[0], choice[-1]
    if(enemyChoice == "A"):
        if(playerChoice == "X"):
            #draw 3 rock
            totalScore += 4
        elif(playerChoice == "Y"):
            #win 6 paper
            totalScore += 8
        else:
            #loss 0 scissor
            totalScore += 3
    elif(enemyChoice == "B"):
        if(playerChoice == "Y"):
            #draw 3 paper
            totalScore += 5
        elif(playerChoice == "Z"):
            #win 6 sissor
            totalScore += 9
        else:
            #loss 0 rock
            totalScore += 1
    elif(enemyChoice == "C"):
        if(playerChoice == "Z"):
            #draw 3 scissor
            totalScore += 6
        elif(playerChoice == "X"):
            #win 6 rock
            totalScore += 7
        else:
            #loss 0 paper
            totalScore += 2

print("The total score is: " + str(totalScore))

