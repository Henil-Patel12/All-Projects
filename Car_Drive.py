def display_road():
    print("|" + " " * 28 + "|")
    for i in range(10):
        print("|" + " " * 28 + "|")
    print("|" + " " * 28 + "|")

def display_car(position):
    road = ["|" + " " * 28 + "|"]
    for i in range(10):
        if i == 5:
            road.append("|" + " " * (position - 1) + "*" + " " * (27 - position) + "|")
        else:
            road.append("|" + " " * 28 + "|")
    road.append("|" + " " * 28 + "|")
    for line in road:
        print(line)

def update_position(position, direction):
    if direction == "right":
        return min(position + 1, 27)
    elif direction == "left":
        return max(position - 1, 1)
    else:
        return position

def play_game():
    position = 14
    while True:
        display_road()
        display_car(position)
        direction = input("Enter direction (left, right, or quit): ")
        if direction == "quit":
            break
        position = update_position(position, direction)

play_game()
