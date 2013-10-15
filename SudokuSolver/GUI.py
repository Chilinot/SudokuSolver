import sudoku

import tkinter
from tkinter.messagebox import showerror
import sys

class GUI:
    def generateEntryMatrix(self, frame):
        
        one_three = [0,1,2,6,7,8]
        two       = [3,4,5]
        
        matrix = [[] for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if (j in one_three and i not in two) or (j not in one_three and i in two):
                    e = tkinter.Entry(frame, width=3, justify=tkinter.CENTER, bg="gray")
                else:
                    e = tkinter.Entry(frame, width=3, justify=tkinter.CENTER)
                    
                e.grid(row=i,column=j)
                
                matrix[i].append(e)
            
        return matrix
    
    def solve(self):
        
        st = sudoku.SudokuTable()
        
        for i in range(9):
            for j in range(9):
                value = self.matrix[i][j].get()
                if value != '':
                    try:
                        value = int(value)
                    except(ValueError):
                        showerror("Error!", "You can only have numbers in the puzzle!")
                        return
                    if value <= 0 or value >= 10:
                        showerror("Error!", "You have entered an incorrect value in the table!")
                        return
                    st.addValue(i, j, value)
        
        solver = sudoku.Solver();
        solution = solver.findSolution(st);
        
        if solution == None:
            showerror("Warning!", "Something went wrong when trying to solve the sudoku!")
            return
        
        for i in range(9):
            for j in range(9):
                e = self.matrix[i][j]
                e.delete(0, tkinter.END)
                e.insert(0, str(solution._m_val[i][j]))
        
        return
    
    def main(self):
        
        root = tkinter.Tk()
        root.title("SudokuSolver")
        
        f_upper = tkinter.Frame(root); f_upper.grid(row=1,column=1)
        f_lower = tkinter.Frame(root, padx=10, pady=10); f_lower.grid(row=2,column=1);
        
        tkinter.Button(f_upper, text="Solve", command=self.solve).grid(row=1,column=1)
        tkinter.Button(f_upper, text="Quit",  command=lambda: sys.exit()).grid(row=1,column=2)
        
        self.matrix = self.generateEntryMatrix(f_lower)
        
        root.mainloop()
    
if __name__ == "__main__":
    GUI().main()