# JWchapter5.py
import time
import JWglobalvariables

def chapter5():
    JWglobalvariables.game_state['current_chapter'] = 5
    print("Chapter 5: The truth flickered across the main screen in cold blue letters.")
    time.sleep(2)

    while True:
        print("\nYou are at the main computer terminal.")
        print("Actions:")
        print("1. Read the final message")
        print("2. Send report back to Earth (Good ending)")
        print("3. Delete all data (Secret ending)")
        print("4. Shut down the station permanently (Neutral ending)")

        choice = input("Choose an action (1-4): ")

        if choice == "1":
            print("The final message reveals that the experiment went wrong, and the crew evacuated.")
            time.sleep(2)
            print("You now have three choices for how to proceed.")
        elif choice == "2":
            print("You send the report back to Earth. Mission complete – good ending.")
            JWglobalvariables.game_state['game_won'] = True
            JWglobalvariables.game_state['game_ended'] = True
            break
        elif choice == "3":
            print("You delete all data on the station, erasing all evidence of the experiment.")
            print("This is the secret ending. No one will ever know what happened.")
            JWglobalvariables.game_state['game_ended'] = True
            break
        elif choice == "4":
            print("You shut down the station permanently, cutting all power. The station goes dark.")
            print("A neutral ending, leaving the mystery unsolved.")
            JWglobalvariables.game_state['game_ended'] = True
            break
        else:
            print("Invalid choice. Please choose 1-4.")