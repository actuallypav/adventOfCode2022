inputFile = open("Day_6/input.txt", "r")
Buffer = inputFile.read()
no_before_start_packet = 0
start_packet = []

# loop throught the characters
for char in Buffer:
    if len(start_packet) < 4:
        start_packet.append(char)
        no_before_start_packet += 1
    else:
        if len(start_packet) == len(set(start_packet)):
            print(no_before_start_packet)
            break
        start_packet.append(char)
        start_packet.pop(0)
        no_before_start_packet += 1
