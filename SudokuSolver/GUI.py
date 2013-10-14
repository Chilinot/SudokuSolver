import tkinter

def main():
    
    root = tkinter.Tk()
    root.title("SudokuSolver")
    
    cv = tkinter.Canvas(root, width = 350, height = 350)
    cv.pack(side = tkinter.LEFT)
    
    root.mainloop()
    
    return
    
if __name__ == "__main__":
    main()