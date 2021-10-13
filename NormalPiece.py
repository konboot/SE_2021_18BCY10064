from Pieces import Piece
from Position import Position
class NormalPiece(Piece):
    def __init__(self, name, player, position,step=1):
        super().__init__(name, player, position,step)

    def move(self):
        self.oldPosition=self.currentPosition
        self.currentPosition=self.newPosition

    def isValidMove(self, move):
        move=move.lower()
        if move not in "flbr":
            print("Invalid Move", "Move Command for Piece should only be one of (F,B,L,R)")
            return False
        return True
    
    def predictMove(self,move):
        self.newPosition = Position.Position(self.currentPosition.row, self.currentPosition.column)
        move = move.lower()
        if move == "f":
            self.moveForward(self.newPosition)
        elif move == "b":
            self.moveBackward(self.newPosition)
        elif move == "l":
            self.moveLeft(self.newPosition)
        elif move == "r":
            self.moveRight(self.newPosition)

        