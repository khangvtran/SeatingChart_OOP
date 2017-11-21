

class Seat():
    """
    Superclass seat
    instantiate object with default argument for price as $1
    initialize attribute taken to be False
    getExtra is an abstract class. All subclass will have to implement it
    """
    def __init__(self, price = 1):
        self._price = price
        self._taken = False
        
    def getExtra(self):
        raise NotImplementedError
    
    def getPrice(self):
        return self._price
    
    def getExtra(self):
        return self._perks
    
    def isTaken(self):
        return self._taken    
    

        
    

class Premium(Seat):
    def __init__(self, price):
        super().__init__(price)
        self._perks = "a glass of Carbenet Sauvignon or Chardonay or Champaign"

    def __repr__(self):
        if not self.isTaken() : return "$"+str(self._price)
        else : return "X"     
    
    
class Choice(Seat):
    def __init__(self, price):
        super().__init__(price)
        self._perks = "10% off for all refreshment purchased"

    def __repr__(self):
        if not self.isTaken() : return "$"+str(self._price)
        else : return "X"     



class Regular(Seat):
    def __init__(self, price):
        super().__init__(price)
        self._perks = ". Please upgrade to Premium and Choice to enjoy the perks"
        

    def __repr__(self):
        if not self.isTaken() : return "$"+str(self._price)
        else : return "X" 
            




"""
seat1 = Premium(100)
print(seat1)
seat2 = Choice(60)
print(seat2)
seat3 = Regular(30)
print(seat3)
"""
