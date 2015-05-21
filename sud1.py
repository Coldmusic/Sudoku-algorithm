import random
from random import randint

class Sudoku:

    def __init__(self):
        self.begin = -1
        self.prev1 = 0
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.matrix = [[0]*9 for i in range(9)]

    #Algorithm for creating a Sudoku puzzle, 
    #without missed numbers
    #Shuffles array with numbers from 1 to 9 so that the order 
    #will be randomized
    def initGrid(self):
        random.shuffle(self.nums); #Shuffle array with numbers
        prev1 = 0
        begin = -1
        for num in self.nums:
            self.begin += 1        #begin from this index in first array
            for k in range(9):
                if k%3 == 0:       #for every third array/line
                    self.prev1 = self.begin + k/3
                if self.prev1 > 8: #if index for width is out of range
                    self.prev1 = self.prev1 - 9
                self.matrix[k][self.prev1] = num
                self.prev1 += 3

    #Set missing numbers in Puzzle
    def setSpaces(self):
        rand = 0
        for i in self.matrix:
            for k in range(3):
                rand = randint(0, 8)
                i[rand] = 0

    
    def initPuzzle(self):
        self.initGrid()
        self.setSpaces()

    def printMatrix(self):
        st = ''
        for i in range(9):
            st = ''
            if i%3 == 0:
                print ' - ' * 9
            for k in range(9):
                if k%3 == 0:
                    st +=  '|'
                if self.matrix[i][k] == 0:
                    st += (' _ ')
                else: st += ( ' ' + str(self.matrix[i][k]) + ' ')
            print st
    
    
        
sud = Sudoku()
sud.initPuzzle()
sud.printMatrix()   
