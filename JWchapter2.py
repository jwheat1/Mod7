# JWchapter2.py
import time
import JWglobalvariables

def chapter2():
    JWglobalvariables.game_state['current_chapter'] = 2
    print("Chapter 2: The hallway echoed with metallic groans, as if the station itself was breathing.")
    time.sleep(2)

    while True:
        print("\nYou are in the Laboratory area.")
        print("Actions:")
        print("1. Search the lab")
        print("2. Listen to data log")
        print("3. Ignore lab and continue to next sector")
        print("4. Return to Docking Bay")

        choice = input("Choose an action (1-4): ")

        if choice == "1":
            print("You find a data log hidden among overturned equipment.")
            JWglobalvariables.game_state['hasDataLog'] = True
            time.sleep(2)
        elif choice == "2":
            if JWglobalvariables.game_state['hasDataLog']:
                print("You listen to the data log. The crew argued about a dangerous experiment.")
            else:
                print("You need to find the data log first!")
            time.sleep(2)
        elif choice == "3":
            print("You ignore the lab and continue down the hallway...")
            JWglobalvariables.game_state['current_chapter'] = 3
            time.sleep(2)
            break
        elif choice == "4":
            print("You return to the Docking Bay...")
            JWglobalvariables.game_state['current_chapter'] = 1
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please choose 1-4.")