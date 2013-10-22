import sys

	
class Option:  # one position with one option
	global value

class OptionList:  # one position with all its options
	def __init__(self):
		self.options = list()

class SudokuTable: # (object)
	def __init__(self, frame, st = None):
		'''
		Constructor for the SudokuTable-object.
		'''
		
		self.frame = frame
		
		self._m_val = [[int for j in range(9)] for i in range(9)]
		self._m_OptionMatrix =[[OptionList() for j in range(9)] for i in range(9)]
		
		for i in range(9):
			for j in range(9):
				self._m_val[i][j] = 0 if st == None else st._m_val[i][j]
	
	def addValue(self, i, j, value):
		'''
		Sets the value of a position at the given coordinates.
		
		PARAMETERS:
			i - The row coordinate.
			j - The column coordinate.
		'''
		self._m_val[i][j] = value
		self.frame.setValue(i,j,value)

	def getLowestNumberOfOptionsList(self):
		'''
		Loops over each OptionList generated and returns the one with the lowest amount of alternatives.
		
		RETURNS:
			The OptionList with the lowest amount of alternatives in the grid.
		'''
		self.computeAllOptions()
		minCount = 999999  #initiate minimum number of option counting as max value of integer, here is 999999
		minOp = OptionList()
		
		for i in range(9):
			for j in range(9):
				if len(self._m_OptionMatrix[i][j].options) < minCount and len(self._m_OptionMatrix[i][j].options) != 0:
					minOp = self._m_OptionMatrix[i][j]
					minCount = len(minOp.options)
		
		return minOp

	def findPossibilities(self, i, j):
		'''
		Loops over each column, row and block and collects creates a new OptionList-object that
		contains every integer possibility for that position.
		
		PARAMETERS:
			i - The row coordinate.
			j - The column coordinate.
		
		RETURNS:
			Returns the new OptionList created containing all possibilities for that position in the grid.
		'''
		op = OptionList()
		
		if self._m_val[i][j] != 0:
			return op
		
		l = list()
		
		# Check the numbers on this row
		for x in range(9):
			if self._m_val[i][x] != 0:
				if (self._m_val[i][x]) not in l:
					l.append(self._m_val[i][x])
		
		# Check the numbers on this column
		for y in range(9):
			if self._m_val[y][j] != 0:
				if (self._m_val[y][j]) not in l:
					l.append(self._m_val[y][j])
		
		# Check the numbers in my BLOCK
		rowBlock = int(i / 3)
		colBlock = int(j / 3)
		y = int(rowBlock * 3)
		while y < (rowBlock + 1) * 3:
			x = int(colBlock * 3)
			while x < (colBlock + 1) * 3:
				if self._m_val[y][x] != 0:
					if (self._m_val[y][x]) not in l:
						l.append(self._m_val[y][x])
				x += 1
			y += 1
		
		if len(l) != 9:
			idx = 1
			while idx <= 9:
				# all the indices that are not in the list are a potential option!
				if idx not in l:
					opt = Option()
					opt.i = i
					opt.j = j
					opt.value = idx
					op.options.append(opt)
					op.i = i
					op.j = j
					
				idx += 1
		return op

	def isSolved(self):
		'''
		Calculates if the current solution is correct by comparing 
		each row, column and block to a pre-set checksum.
		
		RETURNS:
			Boolean - True if the solution is correct, otherwise false.
		'''
		checkSum = 45 # 9+8+7...+ 1
		
		# Check row and column sums
		for j in range(9):
			rowSum = 0
			colSum = 0
			
			for i in range(9):
				rowSum += self._m_val[i][j]
				colSum += self._m_val[j][i]
				
			if rowSum != checkSum or colSum != checkSum:
				return False
		
		# Check block sum
		
		for by in range(3):
			for bx in range(3):
				sum = 0
				
				for y in range(3):
					for x in range(3):
						sum += self._m_val[y + by * 3][x + bx * 3]
						
				if sum != checkSum:
					return False
				
		return True

	def computeAllOptions(self):
		'''
		Loops over each position in the SudokuTable and calls findPossibilites for each one.
		'''
		for i in range(9):
			for j in range(9):
				self._m_OptionMatrix[i][j] = self.findPossibilities(i, j)

	def computeAllSingles(self):
		'''
		Checks all OptionList-objects for single alternatives, if found, it puts the alternative in the table.
		'''
		while len(self.getLowestNumberOfOptionsList().options) == 1:
			
			for i in range(9):
				for j in range(9):
					opt = self.findPossibilities(i, j)
					if len(opt.options) == 1:
						self._m_val[i][j] = opt.options[0].value

class Node(object):
	def __init__(self, frame, st = None):
		'''
		Constructor for the Node-object.
		'''
		self._m_SudokuTable = SudokuTable(frame, st)
		self._m_children = list()
		
		self.frame = frame

	# For each new option we create a child with a new sodoku table
	def addOption(self, op):
		'''
		Creates a new SudokuTable by copying this nodes SudokuTable, then sets the value using the data in the
		options parameter to the new SudokuTable and creates a new child-Node with that table.
		
		PARAMETERS:
			op - Option-object
		'''
		# Create new table
		newTable = SudokuTable(self.frame, self._m_SudokuTable)
		
		# Add new option to this table
		newTable.addValue(op.i, op.j, op.value)
		
		# Create new node with the new table
		newNode = Node(self.frame, newTable)
		
		self._m_children.append(newNode)

class Solver(object):
	def __init__(self):
		'''
		Constructor for Solver-object.
		'''
		self.FinalSolution = None
	
	def findSolution(self, frame, st):
		'''
		Tries to find the solution for the given SudokuTable-object.
		
		PARAMETERS:
			SudokuTable - SudokuTable-object to solve.
		
		RETURNS:
			SudokutTable-object with solution if found, else it returns None.
		'''
		
		root = Node(frame, st)
		
		# HERE WE GOO! Creates a lot of nodes, one for each alternative.
		self.investigateOptions(root)
		
		# Checks if the solution was found in any of the nodes.
		solution = None
		if self.FinalSolution != None:
			solution = self.FinalSolution._m_SudokuTable
			
		return solution

	def investigateOptions(self, root):
		'''
		
		'''
		root._m_SudokuTable.computeAllSingles()
		
		if root._m_SudokuTable.isSolved():
			self.FinalSolution = root
		else:
			root._m_SudokuTable.computeAllOptions()
			optionList = root._m_SudokuTable.getLowestNumberOfOptionsList()
			# If there are no options there is no solution
			if len(optionList.options) == 0:
				#solutionNode = null;
				return  # ...
			OptionIndex = 0
			
			for op in optionList.options: 
			#op is an option
			
				# A new child node with a new sodoku table is created for each option
				root.addOption(op)				
				
				# now we investigate each child
				self.investigateOptions(root._m_children[OptionIndex])
				if self.FinalSolution != None and self.FinalSolution._m_SudokuTable.isSolved():
					return 
				root._m_children[OptionIndex] = None
				OptionIndex += 1
