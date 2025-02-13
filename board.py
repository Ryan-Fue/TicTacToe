class Board:
    value = ""
    grid = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    @classmethod
    def getValue (cls):
        print("Please Input a value: ")
        while True:
            try:
                cls.value = int(input().strip())
                break
            except:
                print(f"That is not 1-9")
            
    
    @classmethod
    def generateBoard (cls):
        ...

    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,value):
        if value not in [1-9]:
            raise ValueError("Not 1-9")
        self._value = value
        

    

    


