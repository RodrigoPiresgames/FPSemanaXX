room_descriptions = [
                    [ "A", "B", "C", "D", "E"],
                    [ "F", "G", "H", "I", "J"],
                    [ "K", "L", "N", "L", "O"],
                    [ "P", "Q", "R", "S", "T"],
                    [ "U", "V", "W", "X", "Y"]
]

position = (2,2)

while(True):
    x,y = position
    description = room_descriptions[y][x]
    print(position, ":", description)

    print("What now?")
    command = input()

    if command == "north":
        print("You moved north!")
        y = y -1
    elif command == "south":
        print("You moved south!")
        y = y +1
    elif command == "east":
        print("You moved east!")
        y = x +1
    elif command == "west":
        print("You moved west!")
        y = x -1
    elif command == "goodbye":
        print("You moved north!")
        break
    else:
        print("I don't know what" + command "is!")
    
    position = (x,y)