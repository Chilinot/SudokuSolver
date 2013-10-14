
#Wentings main startup function

#import solving logic:
import sudoku

def main():

        # Create Sudoku table manually        
        st = sudoku.SudokuTable();
        
        # Easy example, using only filling ones.
        # Testrun resulted immediately
        st.addValue(0, 0, 6)
        st.addValue(0, 3, 1)
        st.addValue(0, 5, 8)
        st.addValue(0, 6, 2)
        st.addValue(0, 8, 3)
        st.addValue(1, 1, 2)
        st.addValue(1, 4, 4)
        st.addValue(1, 7, 9)
        st.addValue(2, 0, 8)
        st.addValue(2, 2, 3)
        st.addValue(2, 5, 5)
        st.addValue(2, 6, 4)
        st.addValue(3, 0, 5)
        st.addValue(3, 2, 4)
        st.addValue(3, 3, 6)
        st.addValue(3, 5, 7)
        st.addValue(3, 8, 9)
        st.addValue(4, 1, 3)
        st.addValue(4, 7, 5)
        st.addValue(5, 0, 7)
        st.addValue(5, 3, 8)
        st.addValue(5, 5, 3)
        st.addValue(5, 6, 1)
        st.addValue(5, 8, 2)
        st.addValue(6, 2, 1)
        st.addValue(6, 3, 7)
        st.addValue(6, 6, 9)
        st.addValue(6, 8, 6)
        st.addValue(7, 1, 8)
        st.addValue(7, 4, 3)
        st.addValue(7, 7, 2)
        st.addValue(8, 0, 3)
        st.addValue(8, 2, 2)
        st.addValue(8, 3, 9)
        st.addValue(8, 5, 4)
        st.addValue(8, 8, 5)
        print("This is an Easy Example!")
        '''
        # Medium example 1, using Nodes in shallow level.
        # Testrun resulted within 30 seconds
        st.addValue(0, 1, 9)
        st.addValue(0, 8, 1)
        st.addValue(2, 0, 3)
        st.addValue(2, 4, 9)
        st.addValue(2, 6, 2)
        st.addValue(2, 8, 4)
        st.addValue(3, 0, 8)
        st.addValue(3, 3, 5)
        st.addValue(3, 5, 4)
        st.addValue(3, 6, 9)
        st.addValue(3, 8, 3)
        st.addValue(4, 2, 9)
        st.addValue(5, 1, 3)
        st.addValue(5, 6, 5)
        st.addValue(5, 7, 8)
        st.addValue(5, 8, 7)
        st.addValue(6, 7, 4)
        st.addValue(6, 8, 9)
        st.addValue(7, 2, 3)
        st.addValue(7, 4, 6)
        st.addValue(7, 7, 5)
        st.addValue(8, 0, 9)
        st.addValue(8, 2, 4)
        st.addValue(8, 6, 1)
        st.addValue(8, 7, 3)		
        print("This is a Medium Example 1!")
        
        # Medium example 2, using Nodes.
        # Testrun resulted within 90 seconds
        st.addValue(0, 4, 1)
        st.addValue(1, 5, 2)
        st.addValue(2, 3, 8)
        st.addValue(2, 4, 9)
        st.addValue(2, 8, 5)
        st.addValue(3, 7, 8)
        st.addValue(4, 1, 7)
        st.addValue(4, 2, 1)
        st.addValue(4, 4, 2)
        st.addValue(5, 2, 8)
        st.addValue(5, 3, 4)
        st.addValue(5, 7, 9)
        st.addValue(5, 8, 1)
        st.addValue(6, 0, 8)
        st.addValue(6, 1, 5)
        st.addValue(6, 2, 7)
        st.addValue(6, 4, 4)
        st.addValue(7, 0, 4)
        st.addValue(7, 2, 9)
        st.addValue(7, 3, 7)
        st.addValue(7, 4, 3)
        st.addValue(7, 7, 2)
        st.addValue(8, 0, 2)
        st.addValue(8, 2, 6)
        st.addValue(8, 4, 8)
        print("This is a Medium Example 2!")
        
        # Hard example 1, using Nodes in deeper level.
        # Testrun about one hour without reaching result
        st.addValue(0, 5, 8)
        st.addValue(0, 6, 1)
        st.addValue(1, 0, 8)
        st.addValue(1, 5, 5)
        st.addValue(1, 7, 3)
        st.addValue(1, 8, 9)
        st.addValue(2, 0, 5)
        st.addValue(3, 1, 7)
        st.addValue(4, 2, 8)
        st.addValue(5, 5, 7)
        st.addValue(6, 1, 3)
        st.addValue(6, 3, 5)
        st.addValue(7, 0, 4)
        st.addValue(7, 1, 2)
        st.addValue(7, 7, 5)
        st.addValue(7, 8, 1)
        st.addValue(8, 0, 1)
        st.addValue(8, 1, 8)
        st.addValue(8, 7, 9)
        st.addValue(8, 8, 3)
        print("This is a Hard Example 1!","Caution: Very long Runtime!!! It took one hour without reaching result")

        # Hard example 2
        # Not tested yet
        st.addValue(0, 0, 1)
        st.addValue(0, 3, 2)
        st.addValue(0, 5, 4)
        st.addValue(1, 2, 3)
        st.addValue(1, 6, 9)
        st.addValue(2, 0, 4)
        st.addValue(2, 3, 9)
        st.addValue(3, 4, 4)
        st.addValue(3, 5, 9)
        st.addValue(4, 2, 8)
        st.addValue(5, 1, 9)
        st.addValue(5, 5, 8)
        st.addValue(6, 4, 9)
        st.addValue(6, 8, 6)
        st.addValue(7, 0, 9)
        st.addValue(7, 2, 5)
        st.addValue(7, 3, 4)
        st.addValue(8, 0, 8)
        st.addValue(8, 5, 1)
        st.addValue(8, 8, 9)
        print("This is a Hard Example 2!")
        
        # Expert example
        # Not tested yet
        st.addValue(0, 3, 3)
        st.addValue(0, 4, 9)
        st.addValue(1, 2, 9)
        st.addValue(2, 1, 8)
        st.addValue(2, 3, 7)
        st.addValue(2, 5, 4)
        st.addValue(3, 3, 2)
        st.addValue(4, 3, 8)
        st.addValue(5, 4, 1)
        st.addValue(6, 0, 1)
        st.addValue(6, 7, 5)
        st.addValue(7, 2, 7)
        st.addValue(7, 3, 1)
        st.addValue(7, 5, 5)
        st.addValue(8, 3, 9)
        print("This is an Expert Example!")
        '''
        
        
        import time

        current_milli_time = lambda: int(round(time.time() * 1000))
        
        start = current_milli_time()
        solver = sudoku.Solver();
        solution = solver.findSolution( st );
        print("It took " + str((current_milli_time() - start)/1000) + " seconds to complete.")
        
        # print out values
        for i in range(9):
                for j in range(9):
                        print( solution._m_val[i][j] )

                        

if __name__ == "__main__":
    main()



