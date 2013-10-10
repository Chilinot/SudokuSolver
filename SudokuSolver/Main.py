import sys

class Main:
    
    def input(self, msg, legal):
        while True:
            try:
                value = int(raw_input(msg))
                if value not in legal:
                    raise ValueError()
                break
            except ValueError:
                print('\nIncorrect entry, needs to be an integer or in the list: ' + str(legal) + '\n' +
                      'Please try again.')
        return value
    
    def printBoard(self):
        
        counter_y = 0
        
        print("+---+---+---+")
        for row in self.matrix:
            if counter_y == 3:
                print("+---+---+---+")
                counter_y = 0
            
            string = "|"
            
            counter_x = 0
            for position in row:
                if counter_x == 3:
                    string    += "|"
                    counter_x  = 0
                
                if len(position) == 1:
                    string += str(position[0])
                else:
                    string += " "
                    
                counter_x += 1
            counter_y += 1
            
            print(string + "|")
        print("+---+---+---+")
    
    def askForStartValues(self):
        print('\nPlease enter the starting value(s):\n' +
              'Usage:\n' + 
              'Value  = Number in the slot.\n' +
              'Column = The column of that number.\n' +
              'Row    = The row of that number.')
        
        while True:
            legal  = [x for x in range(10) if x != 0]
            value  = self.input("\nValue:  ", legal)
            column = self.input("Column: ",   legal)
            row    = self.input("Row:    ",   legal)
            
            self.setValue(row, column, value)
            
            if self.input('\nDo you have more numbers? 1 = yes, 0 = no: ', [0,1]) == 1:
                continue
            else:
                break
        
        return
    
    def setValue(self, x, y, value):
        self.matrix[y][x] = [value]
    
    """
    Checks every position in the given row (y-axis) for single numbers, if it finds a position that only contains a 
    single value, it removes that value from the list of alternatives for the given position.
    """
    def checkRow(self, y, l):
        
        for column in self.matrix[y]:
            
            if column == l:
                continue
            
            if len(column) == 1 and column[0] in l:
                l.remove(column[0])
        
        return
    
    """
    The same as checkRow, but goes over each position in a column.
    """
    def checkColumn(self, x, l):
        
        for i in range(len(self.matrix)):
            position = self.matrix[i][x]
            
            if position == l:
                continue
            
            if len(position) == 1 and position[0] in l:
                l.remove(position[0])
        
        return
    
    """
    Same as checkRow and checkColumn, but goes over every position in a block (3x3).
    """
    def checkBlock(self, x, y, l):
        
        # Move the pointers to the upper-left-corner of the block.
        pointer_x = (x/3) * 3 
        pointer_y = (y/3) * 3
        
        for i in range(3):
            for j in range(3):
                position = self.matrix[pointer_y + i][pointer_x + j]
                
                if position == l:
                    continue
                
                if len(position) == 1 and position[0] in l:
                    l.remove(position[0])
        
        return
    
    def checkOptions(self, x, y, l):
        
        self.checkRow(y, l)
        self.checkColumn(x, l)
        self.checkBlock(x, y, l)
        
        if len(l) > 1:
            self.unfinished_positions += 1
        
        print("Alternatives left:",x,y,l) # Debug
        
        return
    
    def isUniqueAlternative(self, x, y, value):
        
        self.isUniqueRow(y, value)
        self.isUniqueColumn(x, value)
        self.isUniqueBlock(x, y, value)
        
        return
    
    def checkAndAddUnique(self):
        
        for row in self.matrix:
            for column in row:
                if len(column) > 1:
                    for alternative in column:
                        self.isUniqueAlternative(row.index(column), self.matrix.index(row), alternative)
        
        return
    
    def calculateBoard(self):
        
        print("\ncalculateBoard - Recursion #" + str(self.tries)) # debug
        
        # Prevent possible endless loop.
        if self.tries >= 15:
            
            self.checkAndAddUnique()
            
            #print("WARNING! Aborting calculateBoard since it has been called 15 or more times!")
            return
        else:
            self.tries += 1
        
        self.unfinished_positions = 0
        
        for row in self.matrix:
            for column in row:
                if len(column) > 1: # If there are more than 1 alternative in the list
                    self.checkOptions(row.index(column), self.matrix.index(row), column)
                
        if self.unfinished_positions != 0:
            self.calculateBoard()
            
        print("Sudoku has been solved!")
        
        return
    
    def readSavefile(self):
        
        save = None
        
        while True:
            try:
                save = open(raw_input("\nPlease enter the name of the file: "), 'rU')
                break
            except IOError:
                if self.input("Error! File not found! Enter 1 to try again, or 0 to abort: ", [0,1]) == 0:
                    return
        
        counter = 0
        for line in save:
            l = line.split(',')
            for c in l:
                try:
                    i = int(c)
                    self.setValue(l.index(c), counter, i)
                except ValueError:
                    continue
            counter += 1
            
        print("File loaded successfully!")
    
    def createMatrix(self):
        # Creates a three-dimensional list. Row, column and possible integers for each position [1-9].
        self.matrix = [[[x for x in range(10) if x != 0] for i in range(9)] for j in range(9)]
        return
        
    def menu(self):
        while 1:
            choice = self.input("\nMENU:\n" +
                                "1. Enter starting values.\n" + 
                                "2. Calculate the solution.\n" + 
                                "3. Reset board.\n" +
                                "4. Print board.\n" +
                                "5. Read from file.\n" +
                                "9. Terminate program.\n" + 
                                "CHOICE: ", [1,2,3,4,5,9])
            
            # Enter starting values
            if choice == 1:
                self.askForStartValues()
           
            # Calculate the solution
            elif choice == 2:
                self.tries = 0
                self.calculateBoard()
            
            # Reset board
            elif choice == 3:
                self.createMatrix()
            
            # Print board
            elif choice == 4:
                self.printBoard()
            
            # Read from file
            elif choice == 5:
                self.readSavefile()
            
            # Terminate program
            elif choice == 9:
                self.terminate()
                
    def terminate(self):
        print("Terminating program...")
        sys.exit()
    
    def main(self):
        print('Welcome to SudokuSolver!')
        self.createMatrix()
        self.menu()
        
        
if __name__ == '__main__':
    Main().main()