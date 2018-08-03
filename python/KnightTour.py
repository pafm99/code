# Visit each cell in a chess board exactly once
class KnightTour:
    # Constructor
    def __init__(self, boardSize):
        self.boardSize = boardSize
        # 2 Dimensional Array for possible moves on the board
        self.xMoves = [ 2, 1, -1, -2, -2, -1, 1, 2]
        self.yMoves = [ 1, 2, 2, 1, -1, -2, -2, -1]
        # -1 to be able to track whether we have visited that cell or not
        self.solutionMatrix = [[-1 for x in range(boardSize)] for x in range(boardSize)]

    def solveKnightTourProblem(self):
        # Starting Point
        self.solutionMatrix[0][0] = 0
       #(stepCounter, x-coordinate, y-coordinate)
        if self.solveProblem(1, 0, 0):
            self.showSolution()
        else:
            print('No feasible solution found ...')

    def solveProblem(self, stepCount, x, y):
        if stepCount == (self.boardSize * self.boardSize):
            return True

        for i in range(self.boardSize):
            nextX = x + self.xMoves[i]
            nextY = y +  self.yMoves[i]

            if self.isValidMove(nextX, nextY):
                self.solutionMatrix[nextX][nextY] = stepCount
                if self.solveProblem(stepCount+1, nextX, nextY):
                    return True
                #backtrack    
                self.solutionMatrix[nextX][nextY] = -1
        return False

    def isValidMove(self, x, y):
        # if out of bounds in x
        if x < 0 or x >= self.boardSize:
            return False
        # if out of bounds in y
        if y < 0 or y >= self.boardSize:
            return False
        # if position already visited
        if self.solutionMatrix[x][y] > -1:
            return False
        return True

    def showSolution(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                print(self.solutionMatrix[i][j], end=" "),
            print('\n')

if __name__ == "__main__":
    KnightTour = KnightTour(8)
    KnightTour.solveKnightTourProblem()
