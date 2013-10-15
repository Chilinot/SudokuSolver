import sudoku

import tkinter
import sys

class GUI:
    def generateEntryMatrix(self, frame):
        
        matrix = [[] for i in range(9)]
        
        for i in range(9):
            for j in range(9):
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
                    st.addValue(i, j, int(value))
        
        solver = sudoku.Solver();
        solution = solver.findSolution(st);
        
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
        f_lower = tkinter.Frame(root); f_lower.grid(row=2,column=1)
        
        tkinter.Button(f_upper, text="Solve", command=self.solve).grid(row=1,column=1)
        tkinter.Button(f_upper, text="Quit",  command=lambda: sys.exit()).grid(row=1,column=2)
        
        self.matrix = self.generateEntryMatrix(f_lower)
        
        root.mainloop()
    
if __name__ == "__main__":
    GUI().main()