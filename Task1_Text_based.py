import time

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark forest.")
    time.sleep(1)
    print("You can hear the sound of a river to the east and see a path leading to the west.")
    time.sleep(1)
    print("Which way do you want to go? (east/west)")

def forest():
    print("You follow the path and arrive at a clearing in the forest.")
    time.sleep(1)
    print("You see a cabin to the north and a cave to the south.")
    time.sleep(1)
    print("Where do you want to go? (north/south)")

def river():
    print("You follow the sound of the river and arrive at its bank.")
    time.sleep(1)
    print("You can see a boat on the other side.")
    time.sleep(1)
    print("Do you want to swim across or look for another way? (swim/look)")

def cave():
    print("You enter the dark cave and hear strange noises.")
    time.sleep(1)
    print("It's too dark to see anything, but you can feel a draft coming from deeper inside.")
    time.sleep(1)
    print("Do you want to continue into the cave or turn back? (continue/turn back)")

def cabin():
    print("You approach the old cabin and hear a faint voice coming from inside.")
    time.sleep(1)
    print("You can't make out what it's saying.")
    time.sleep(1)
    print("Do you want to enter the cabin or ignore the voice? (enter/ignore)")

def ending():
    print("Congratulations! You have reached the end of the adventure.")

def main():
    intro()
    direction = input("Which way do you want to go? (east/west): ").lower()

    if direction == "east":
        river_choice = input("You arrive at the river. Do you want to swim across or look for another way? (swim/look): ").lower()
        if river_choice == "swim":
            print("You start swimming across the river...")
            time.sleep(2)
            print("You made it across the river and continue on your journey.")
            forest()
        else:
            print("You decide to look for another way.")
            time.sleep(1)
            print("You encounter a pack of wolves and have to turn back.")
            intro()
    else:
        forest_choice = input("You arrive at a clearing in the forest. Where do you want to go? (north/south): ").lower()
        if forest_choice == "north":
            cabin_choice = input("You approach the old cabin. Do you want to enter the cabin or ignore the voice? (enter/ignore): ").lower()
            if cabin_choice == "enter":
                print("You enter the cabin and find a treasure chest. You win!")
                ending()
            else:
                print("You ignore the voice and continue on your journey.")
                time.sleep(1)
                print("You encounter a group of friendly travelers and join them on their adventure.")
                ending()
        else:
            cave_choice = input("You enter the dark cave. Do you want to continue into the cave or turn back? (continue/turn back): ").lower()
            if cave_choice == "continue":
                print("You venture deeper into the cave and find a hidden treasure. You win!")
                ending()
            else:
                print("You decide to turn back and continue on your journey.")
                time.sleep(1)
                print("You encounter a group of friendly travelers and join them on their adventure.")
                ending()

if __name__ == "__main__":
    main()
