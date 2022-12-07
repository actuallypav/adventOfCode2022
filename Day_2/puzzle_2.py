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
    enemyChoice, playerOutcome = choice[0], choice[-1]
    if(enemyChoice == "A"):
        if(playerOutcome == "X"):
            #lose 0 with scissors
            totalScore += 3
        elif(playerOutcome == "Y"):
            #draw 3 with rock
            totalScore += 4
        else:
            #win 6 with paper
            totalScore += 8
    elif(enemyChoice == "B"):
        if(playerOutcome == "X"):
            #lose 0 with rock
            totalScore += 1
        elif(playerOutcome == "Y"):
            #draw 3 with paper
            totalScore += 5
        else:
            #win 6 with scissors
            totalScore += 9
    elif(enemyChoice == "C"):
        if(playerOutcome == "X"):
            #lose 0 with paper
            totalScore += 2
        elif(playerOutcome == "Y"):
            #draw 3 with scissors
            totalScore += 6
        else:
            #win 6 with rock
            totalScore += 7

print("The total score is: " + str(totalScore))

