import sys

	
class Option:  # one position with one option
	global value

class OptionList:  # one position with all its options
	def __init__(self):
		self.options = list()

class SudokuTable: # (object)
	def __init__(self, st = None):  #initiate
		
		self._m_val = [[int for j in range(9)] for i in range(9)]
		self._m_OptionMatrix =[[OptionList() for j in range(9)] for i in range(9)]
		i = 0
		
		for i in range(9):
			for j in range(9):
				self._m_val[i][j] = 0 if st == None else st._m_val[i][j]
        
	def addValue(self, i, j, value):  
		self._m_val[i][j] = value

	def getLowestNumberOfOptionsList(self):
		self.computeAllOptions()
		minCount = 999999  #initiate minimum number of option counting as max value of integer, here is 999999
		minOp = OptionList()
		i = 0
		while i < 9:
			j = 0
			while j < 9:
				if len(self._m_OptionMatrix[i][j].options) < minCount and len(self._m_OptionMatrix[i][j].options) != 0:
					minOp = self._m_OptionMatrix[i][j]
					minCount = len(minOp.options)
				j += 1
			i += 1
		return minOp

	def findPossibilities(self, i, j):
		op = OptionList()
		if self._m_val[i][j] != 0:
			return op
		l = list()
		# Check the numbers on this row
		x = 0
		while x < 9:
			if self._m_val[i][x] != 0:
				if (self._m_val[i][x]) not in l:
					l.append(self._m_val[i][x])
			x += 1
		# Check the numbers on this column
		y = 0
		while y < 9:
			if self._m_val[y][j] != 0:
				if (self._m_val[y][j]) not in l:
					l.append(self._m_val[y][j])
			y += 1
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
		checkSum = 45 # 9+8+7...+ 1
		# Check row and column sums
		j = 0
		while j < 9:
			rowSum = 0
			colSum = 0
			i = 0
			while i < 9:
				rowSum += self._m_val[i][j]
				colSum += self._m_val[j][i]
				i += 1
			if rowSum != checkSum or colSum != checkSum:
				return False
			j += 1
		# Check block sum
		by = 0
		while by < 3:
			bx = 0
			while bx < 3:
				sum = 0
				y = 0
				while y < 3:
					x = 0
					while x < 3:
						sum += self._m_val[y + by * 3][x + bx * 3]
						x += 1
					y += 1
				if sum != checkSum:
					return False
				bx += 1
			by += 1
		return True

	def computeAllOptions(self):
		i = 0
		while i < 9:
			j = 0
			while j < 9:
				self._m_OptionMatrix[i][j] = self.findPossibilities(i, j)
				j += 1
			i += 1

	def computeAllSingles(self):
		NbLowestOptions = len(self.getLowestNumberOfOptionsList().options)
		while NbLowestOptions < 2 and NbLowestOptions != 0:
			i = 0
			while i < 9:
				j = 0
				while j < 9:
					opt = self.findPossibilities(i, j)
					if len(opt.options) == 1:
						self._m_val[i][j] = opt.options[0].value
					j += 1
				i += 1
			NbLowestOptions = len(self.getLowestNumberOfOptionsList().options)

class Node(object):
	def __init__(self, st = None):
	
		if st is None:
			self._m_SudokuTable = SudokuTable()
			self._m_children = list()
		else:
			self._m_SudokuTable = SudokuTable(st)
			self._m_children = list()

	# For each new option we create a child with a new sodoku table
	def addOption(self, op):
		# Create new table
		newTable = SudokuTable(self._m_SudokuTable)
		# Add new option to this table
		newTable.addValue(op.i, op.j, op.value)
		# Create new node with the new table
		newNode = Node(newTable)
		self._m_children.append(newNode)

class Solver(object):
	def __init__(self):
		self.FinalSolution = None
	def findSolution(self, SudokuTable):
		root = Node(SudokuTable)
		self.investigateOptions(root)
		solution = None
		if self.FinalSolution != None:
			solution = self.FinalSolution._m_SudokuTable
		return solution

	def investigateOptions(self, root):

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
