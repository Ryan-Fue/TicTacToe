from board import *

def main():
    while True:
        Board.startGame()
        while True:
            choice = input("Play again?(Y/N) ")
            if choice == "N":
                return
            elif choice == "Y":
                break
            else:
                print("That is not Y or N!!!")
            



if __name__ == "__main__":
    main()