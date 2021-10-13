from Pieces import Piece
from Position import Position
class Hero2(Piece):
    def __init__(self, name, player, position):
        super().__init__(name,player,position,2)
    
    def move(self):
        self.oldPosition=self.currentPosition
        self.currentPosition=self.newPosition
    
    def isValidMove(self, move):
        move = move.lower()
        if move not in ["fl","fr","bl","br"]:
            print("Invalid Move", "Move Command for Bishop should only be one of (FL,FR,BL,BR)")
            return False
        return True

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
        