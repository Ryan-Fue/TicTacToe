import os
import random

class Board:
    value = 0
    grid = [" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "]
    turn = 0
    markers = [" ⭕️"," ❌"]

    @classmethod
    def getValue (cls):
        print("Please Input a value: ")
        while True:
                try:
                    cls.value = int(input().strip())
                    if cls.value not in range(1,10):
                        print(f"That is not 1-9")
                    elif (cls.grid[cls.value-1] in cls.markers):
                        print("That spot is taken!")
                    else:
                        break
                except:
                    print(f"That is not 1-9")
        return cls.value
            
    
    @classmethod
    def generateBoard (cls):
        # Clears terminal
        os.system('cls' if os.name == "nt" else 'clear')

        # Updates board if not first turn or spot is taken
        if (cls.turn !=0) and (cls.turn %2 == 1):
            cls.grid[cls.value-1] = " ❌"
        elif (cls.turn !=0) and (cls.turn %2 == 0):
            cls.grid[cls.value-1] = " ⭕️"

        # Prints out the board
        for i in range(3):
            print(cls.grid[(i)*3]+"|"+cls.grid[(i)*3+1]+"|"+cls.grid[(i)*3+2])
            if i != 2:
                print("-----------")
        print("")
    
    @classmethod
    def startGame(cls):
        cls.grid = [" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "]
        cls.turn = 0
        Board.generateBoard()
        cls.turn = random.randint(1,2)
        print(f"Player{cls.markers[cls.turn%2]} goes first!")
        for _ in range(9):
            Board.getValue()
            Board.generateBoard()
            if Board.checkWin():
                print(f"Player{cls.markers[cls.turn%2]} wins!")
                return
            cls.turn+=1
        print("TIE!")
            


    

    @classmethod
    def checkWin(cls):
        result = False

        # Checks rows and columns
        for i in range(3):
            if (cls.grid[i*3] == cls.grid[i*3+1] == cls.grid[i*3+2]) \
            or (cls.grid[i] == cls.grid[i+3] == cls.grid[i+6]):
                result = True
        
        # Checks diagonals
        if (cls.grid[0] == cls.grid[4] == cls.grid[8]) \
            or (cls.grid[2] == cls.grid[4] == cls.grid[6]):
                result = True

        return result
    

        

    

    


