# JWstartgame.py
import JWglobalvariables
import JWchapter1
import JWchapter2
import JWchapter3
import JWchapter4
import JWchapter5

def main():
    while not JWglobalvariables.game_state['game_ended']:
        chapter = JWglobalvariables.game_state['current_chapter']
        if chapter == 1:
            JWchapter1.chapter1()   # Call the function from JWchapter1
        elif chapter == 2:
            JWchapter2.chapter2()
        elif chapter == 3:
            JWchapter3.chapter3()
        elif chapter == 4:
            JWchapter4.chapter4()
        elif chapter == 5:
            JWchapter5.chapter5()
        else:
            print("Invalid chapter. Ending the game.")
            JWglobalvariables.game_state['game_ended'] = True

if __name__ == "__main__":
    main()