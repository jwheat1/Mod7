# JWchapter1.py
import time
import JWglobalvariables

def chapter1():
    JWglobalvariables.game_state['current_chapter'] = 1
    print("Chapter 1: The station floated in silence, its lights flickering like a dying star.")
    time.sleep(2)

    while True:
        print("\nYou are in the Docking Bay.")
        print("Actions:")
        print("1. Explore docking bay")
        print("2. Check communication room")
        print("3. Restore partial power")
        print("4. Move to Main Hallway")

        choice = input("Choose an action (1-4): ")

        if choice == "1":
            print("You find a broken robot lying against the wall. It flickers briefly, then goes dark.")
            JWglobalvariables.game_state['hasCreatureData'] = True
            time.sleep(2)
        elif choice == "2":
            print("You check the communication room, but there is no signal detected.")
            time.sleep(2)
        elif choice == "3":
            print("You restore partial power. Lights flicker on in one sector of the station.")
            JWglobalvariables.game_state['hasBackupPowerCell'] = True
            time.sleep(2)
        elif choice == "4":
            print("You move towards the Main Hallway...")
            JWglobalvariables.game_state['current_chapter'] = 2
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please choose 1-4.")

