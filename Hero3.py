from Pieces import Piece
from Position import *
class Hero3(Piece):
    def __init__(self, name, player, position):
        super().__init__(name, player,position,1)

    def move(self):
        self.oldPosition=self.currentPosition
        self.currentPosition=self.newPosition
    
    def isValidMove(self,move):
        move=move.lower()
        if move not in ["fl","fr","bl","br","lf","rf","lb","rb"]:
            print("Invalid Move", "Move Command for Hero3 should only be one of (FL,FR,BL,BR,LF,RF,LB,RB)")
            return False
        return True

    def moveFrontLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        moveRowFactor = -2 if self.belongsToPlayer1() else 2
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))
    
    def moveFrontRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        moveRowFactor = -2 if self.belongsToPlayer1() else 2
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))

    def moveBackLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        moveRowFactor = 2 if self.belongsToPlayer1() else -2
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))

    def moveBackRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        moveRowFactor = 2 if self.belongsToPlayer1() else -2
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))
    
    def moveLeftFront(self, position):
        moveColFactor = -2 if self.belongsToPlayer1() else 2
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))
    
    def moveRightFront(self, position):
        moveColFactor = 2 if self.belongsToPlayer1() else -2
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))

    def moveLeftBack(self, position):
        moveColFactor = -2 if self.belongsToPlayer1() else 2
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))

    def moveRightBack(self, position):
        moveColFactor = 2 if self.belongsToPlayer1() else -2
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))
    
    def predictMove(self, move):
        self.newPosition = Position.Position(self.currentPosition.row,self.currentPosition.column)
        move = move.lower()
        if move == "fl":
            self.moveFrontLeft(self.newPosition)
        elif move == "fr":
            self.moveFrontRight(self.newPosition)
        elif move == "bl":
            self.moveBackLeft(self.newPosition)
        elif move == "br":
            self.moveBackRight(self.newPosition)
        elif move == "lf":
            self.moveLeftFront(self.newPosition)
        elif move == "rf":
            self.moveRightFront(self.newPosition)
        elif move == "lb":
            self.moveLeftBack(self.newPosition)
        elif move == "rb":
            self.moveRightBack(self.newPosition)
        
   