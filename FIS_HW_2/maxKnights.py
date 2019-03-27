import sys
class MaxKnights():

    __slots__ = "sizeOfBoard", "board", "numberOfKnights"

    def __init__(self, sizeOfBoard):
        self.sizeOfBoard = sizeOfBoard
        self.numberOfKnights = 0
        # Initializes the board of nxn with 0s
        self.board = [[0 for x in range(self.sizeOfBoard)]for y in range(self.sizeOfBoard)]
        # Places Knights on a diagonal for initial iteration
        for x in range(self.sizeOfBoard):
            for y in range(self.sizeOfBoard):
                if x == y:
                    self.board[x][y] = "K"
                    # print(x,y)
                    self.knightMovesWithCoordinates(x,y)
                    self.numberOfKnights += 1
                    print(self.board)

        print(self.board)
        self.computeMaxNumberOfKnights()
        print(self.board)

    def knightMoves(self):
        flag = False
        for x in range(self.sizeOfBoard):
            for y in range(self.sizeOfBoard):
                if self.knightMovesWithCoordinates(x,y):
                    flag = True
        return flag

    def knightMovesWithCoordinates(self, xValue, yValue):
        # Increments value of all the spots the knight attacks with 1
        valuesToAdjust = [(1,2),(2,1)]
        flag = False
        for x,y in (valuesToAdjust):
            # for y in range(valuesToAdjust):
            if xValue + x < self.sizeOfBoard and yValue + y < self.sizeOfBoard and xValue + x >= 0 and yValue + y >= 0 \
                    and self.board[xValue + x][yValue + y] is not "K" :
                self.board[xValue + x][yValue + y] = int(self.board[xValue  + x][yValue + y])+1
                flag = True
            if xValue + x < self.sizeOfBoard and yValue - y < self.sizeOfBoard and xValue + x >= 0 and yValue - y >= 0 \
                    and self.board[xValue + x][yValue - y] is not "K":
                self.board[xValue + x][yValue - y] = int(self.board[xValue  + x][yValue - y]) + 1
                flag = True
            if xValue - x < self.sizeOfBoard and yValue - y < self.sizeOfBoard and xValue - x >= 0 and yValue - y >= 0 \
                    and self.board[xValue - x][yValue - y] is not "K":
                self.board[xValue - x][yValue - y] = int(self.board[xValue - x][yValue - y]) + 1
                flag = True
            if xValue - x < self.sizeOfBoard and yValue + y < self.sizeOfBoard and xValue - x >= 0 and yValue + y >= 0 \
                    and self.board[xValue - x][yValue + y] is not "K":
                self.board[xValue - x][yValue + y] = int(self.board[xValue - x][yValue + y]) + 1
                flag = True
        return flag

    def updateKnights(self):
        # updates list with K for all spots with zero attacks
        for x in range(self.sizeOfBoard):
            for y in range(self.sizeOfBoard):
                # print(x,y)
                if self.board[x][y] == 0:
                    self.board[x][y] = "K"
                    self.knightMovesWithCoordinates(x,y)
                    self.numberOfKnights += 1

    def printOutput(self):
        for x in range(self.sizeOfBoard):
            for y in range(self.sizeOfBoard):
                print(self.board[x][y],end='\t')


    def computeMaxNumberOfKnights(self):
        numberOfZeroes = 1
        while numberOfZeroes > 0 :
            self.updateKnights()
            numberOfZeroes = 0
            for x in range(self.sizeOfBoard):
                for y in range(self.sizeOfBoard):
                    if self.board[x][y] == 0:
                        numberOfZeroes += 1
        print("Max number of Knights in a ",self.sizeOfBoard,"x",self.sizeOfBoard, " matrix is ",self.numberOfKnights)
        self.printOutput()

def main():
    sizeOfBoard = (int)(sys.argv[1])
    MaxKnights(sizeOfBoard)

if __name__ == '__main__':
    main()