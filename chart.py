from seat import *

class Chart():
    
    def __init__(self):
        self._seatingChart = [ ]               # initate the List (of lists)
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
                        self._seatingChart.append(rowList)    # apend the list of object into seatingChart
                        
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
        numRow = len(self._seatingChart)
        numCol = len(self._seatingChart[0])
        
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
                print("%5s"  %(self._seatingChart[row][col]), end = "")
            print()
                



#### Testing Area ####
chartTest = Chart()
