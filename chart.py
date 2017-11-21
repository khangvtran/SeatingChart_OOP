from seat import *

class Chart():
    
    def __init__(self):
        self._chart = [ ]               # initate the List (of lists)
        keepReading = True                     
        while(keepReading):
            try:
                fileName = input("Enter a file name or hit Enter to use lab7input2.txt: ")
                if fileName == "" : fileName = "lab7input2.txt"
               
                with open(fileName, "r") as inFile:
                    firstLine = inFile.readline().split()     #Process the 3 prices here
                    premiumPrice = int(firstLine[0])
                    choicePrice = int(firstLine[1])
                    regularPrice = int(firstLine[2])
                                        
                    for line in inFile:                       # Process each line after the first one
                        rowList = []
                        for price in line.split():            # Process each price in the line
                            price = int(price)                # create seat object appropriately to each price
                            if price == premiumPrice : rowList.append(Premium(price))   
                            elif price == choicePrice : rowList.append(Choice(price))
                            else : rowList.append(Choice(price))
                        self._chart.append(rowList)    # apend the list of object into seatingChart
                        
                        #print(rowList, end = " ")
                        #print()                           
                # PRINT METHOD GOES HERE
                self.print()
                keepReading = False
                
            except FileNotFoundError as e:
                print("Can't open" + str(e))
                print()
                keepReading  = True
            
    def print(self):
        numRow = len(self._chart)
        numCol = len(self._chart[0])
        
        print("Price Chart".center((numCol+1)*5))
        print("Column".center((numCol+1)*5))             # print 'Column'   
        print("   ", end="") 
        for i in range(1,numCol+1) : print("   ",i, end="") 
        print( )
        print("Row  ", end="")  # Print the Row headers
        for i in range(1,numCol+1) : print("=====", end="")    
        print()
        
        for row in range(numRow):
            print(str(row+1) + "  | ", end = "")
            for col in range(numCol):
                print("%5s"  %(self._chart[row][col]), end = "")
            print()
                
    def buySeat(self):
        takenSeat = [ ]
        seatCount = 0
        totalPrice = 0
        
        print("Available seats are shown with price")
        keepPrompting = True
        while keepPrompting:
            seat = input("Enter row,col for seat %d or enter 0 to end: " %(seatCount+1))
            if(seat == "0"): keepPrompting = False
            else:
                try:
                    #print("abc")
                    seat = seat.split(",")
                    row = int(seat[0]) - 1
                    col = int(seat[1]) - 1
                    
                    if row < 0 or col < 0 : raise IndexError

                    if self._chart[row][col].isTaken():
                        print("Sorry, that seat is not available.")
                    else:
                        takenSeat.append((row+1, col+1))
                        seatCount += 1;
                        totalPrice += self._chart[row][col].getPrice()
                        self._chart[row][col].setTaken()
                #print(totalPrice)
                except ValueError:
                    print("Row and column must be numbers")
                except IndexError:
                    print("Invalid row or column")  
                    
        # print price
        print("Your total: $%d" %totalPrice)
        # print location  
        print("Your %d seat(s) at " %(seatCount), end = "")
        for seat in takenSeat:
            print(seat, end = " ")
        print("are marked with 'X'")
        #print updated chart
        self.print()
        
        
        
        

"""
#### Testing Area ####
chartTest = Chart()
chartTest.buySeat()

"""