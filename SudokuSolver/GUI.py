import sudoku

import tkinter
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sys
import time

def current_milli_time(): 
    return int(round(time.time() * 1000))

class GUI:
    
    def __init__(self):
        '''
        Initiates the GUI
        '''
        root = tkinter.Tk()
        root.title("SudokuSolver")
        
        f_upper = tkinter.Frame(root)
        f_lower = tkinter.Frame(root, padx=10, pady=10)
        f_upper.grid(row=1,column=1)
        f_lower.grid(row=2,column=1)
        
        tkinter.Button(f_upper, text="Save",  command=self.save).grid(     row=0,column=0)
        tkinter.Button(f_upper, text="Load",  command=self.load).grid(     row=0,column=1)
        tkinter.Button(f_upper, text="Clear", command=self.clear).grid(    row=0,column=2)
        tkinter.Button(f_upper, text="Solve", command=self.solve).grid(    row=0,column=3)
        tkinter.Button(f_upper, text="Quit",  command=self.terminate).grid(row=0,column=4)
        
        self.matrix = self.generateEntryMatrix(f_lower)
        
        root.mainloop()
    
    def generateEntryMatrix(self, frame):
        '''
        Generates a matrix of Entry-widgets with a total of 81 objects (9x9).
        
        PARAMETERS:
            Frame - the frame that the matrix should be displayed in.
        
        RETURNS:
            2D-list : A two-dimensional list that is the matrix generated.
        '''
        
        one_three = [0,1,2,6,7,8]   # "Blockrow" one and three
        two       = [3,4,5]         # "Blockrow" two
        
        matrix = [[] for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                e = tkinter.Entry(frame, width=3, justify=tkinter.CENTER)
                if (j in one_three and i not in two) or (j not in one_three and i in two):
                    e.config(bg="gray")
                e.grid(row=i,column=j)
                matrix[i].append(e)
            
        return matrix
    
    def save(self):
        '''
        Saves the current board/matrix into a textfile.
        '''
        try:
            file = open(asksaveasfilename(defaultextension='.sudoku', filetypes=[('Default', '.sudoku')]), 'w')
        except(Exception):
            return
        
        for i in range(9):
            for j in range(9):
                file.write(self.matrix[i][j].get() + ',')
            file.write('\n')
    
    def load(self):
        '''
        Loads a given savefile into the board/matrix.
        '''
        try:
            file = open(askopenfilename(defaultextension='.sudoku', filetypes=[('Default', '.sudoku')]), 'rU')
        except(Exception):
            return
        
        counter_row = 0
        for row in file:
            
            counter_c = 0
            for c in row.split(',')[:-1]:
                e = self.matrix[counter_row][counter_c]
                e.delete(0, tkinter.END)
                e.insert(0, c)
                counter_c += 1
                
            counter_row += 1
    
    def clear(self):
        '''
        Empties/resets the board/matrix.
        '''
        for row in self.matrix:
            for entry in row:
                entry.delete(0, tkinter.END)
    
    def solve(self):
        '''
        Solves the current sudoko in the matrix by using the sudoku-module.
        When the sudoku has been solved, it writes the solution onto the board and displays a success window
        that also shows the amount of time it took to solve it.
        '''
        
        st = sudoku.SudokuTable(frame=self)
        
        for i in range(9):
            for j in range(9):
                value = self.matrix[i][j].get()
                if value != '':
                    try:
                        value = int(value)
                    except(ValueError):
                        showerror("Error", "You can only have numbers in the puzzle!")
                        return
                    if value <= 0 or value >= 10:
                        showerror("Error", "You have entered an incorrect value in the table!")
                        return
                    st.addValue(i, j, value)
        
        start    = current_milli_time()
        solver   = sudoku.Solver();
        solution = solver.findSolution(self, st);
        time     = (current_milli_time() - start)/1000
        
        if solution == None:
            showerror("Warning", "Something went wrong when trying to solve the sudoku!")
            return
        
        for i in range(9):
            for j in range(9):
                e = self.matrix[i][j]
                e.delete(0, tkinter.END)
                e.insert(0, str(solution._m_val[i][j]))
                
        showinfo("Success", "The solution was found in %f seconds." %time)
        
        return
    
    def terminate(self):
        '''
        Terminates the program.
        '''
        sys.exit()
        
    def setValue(self, i, j, value):
        e = self.matrix[i][j]
        e.delete(0, tkinter.END)
        e.insert(0, value)
        time.sleep(1)
    
if __name__ == "__main__":
    GUI()