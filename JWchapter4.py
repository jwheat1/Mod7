# JWchapter4.py
import time
import JWglobalvariables

def chapter4():
    JWglobalvariables.game_state['current_chapter'] = 4
    print("Chapter 4: The control room door is sealed, requiring a security override.")
    time.sleep(2)

    while True:
        print("\nYou are at the control room door.")
        print("Actions:")
        print("1. Use clues from the data log")
        print("2. Force the door")
        print("3. Search nearby offices for a backup power cell")
        print("4. Return to the Greenhouse")

        choice = input("Choose an action (1-4): ")

        if choice == "1":
            if JWglobalvariables.game_state['hasDataLog']:
                print("You use the clues from the data log and input the security code. The door opens!")
                JWglobalvariables.game_state['hasControlRoomKey'] = True
                time.sleep(2)
                print("You gain access to the control room.")
                JWglobalvariables.game_state['current_chapter'] = 5  # Move to Chapter 5
                break
            else:
                print("You need to find the data log first!")
                time.sleep(2)
        elif choice == "2":
            print("You try to force the door open... but an alarm triggers! The creature reappears!")
            JWglobalvariables.creature.update_health(30)  # Creature is angry and attacks!
            print(f"Creature remaining health: {JWglobalvariables.creature.get_health()}")
            time.sleep(2)
        elif choice == "3":
            if JWglobalvariables.game_state['hasBackupPowerCell']:
                print("You find a backup power cell and use it to override the door's security system.")
                JWglobalvariables.game_state['hasControlRoomKey'] = True
                time.sleep(2)
                print("You gain access to the control room.")
                JWglobalvariables.game_state['current_chapter'] = 5  # Move to Chapter 5
                break
            else:
                print("You need to find the backup power cell first!")
                time.sleep(2)
        elif choice == "4":
            print("You return to the Greenhouse.")
            JWglobalvariables.game_state['current_chapter'] = 3
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please choose 1-4.")