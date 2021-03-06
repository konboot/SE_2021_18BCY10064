import pygame as p 
import Board

WIDTH = HEIGHT = 512
DIMENSION = 5
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wp', 'bp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = Board.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks =[]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE 
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected =() #unselected
                    playerClicks =[] #selected the same row
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks)==2:
                    move = Board.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()  # Resets user inputs
                    playerClicks = []

        drawGameState(screen,gs)        
        clock.tick(MAX_FPS)
        p.display.flip()
            
    
'''
GRAPHICS
'''
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)
'''
SQUARES
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            #piece = board[r][c]
            #if piece != "--":
                #screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
'''
PIECES
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''POSITIONS'''
class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def updatePosition(self, rowSteps, colSteps):
        self.row+=rowSteps
        self.column+=colSteps
    
    def updateRow(self, steps):
        self.row+=steps

    def updateCol(self, steps):
        self.column+=steps
    
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.column
    
    def __str__(self):
        return "Row: "+str(self.row)+" Column: "+str(self.column)
class Piece:
    def __init__(self, name, player, position,steps):
        self.name = name
        self.player = player
        self.currentPosition = position
        self.oldPosition = position
        self.newPosition = None
        self.steps = steps
        self.alive = True

    def prepareMove(self, move):
        self.predictMove(move)

    def move(self):
        pass

    def isValidMove(self, move):
        pass

    def predictMove(self, move):
        pass

    def getNewPosition(self):
        return self.newPosition

    def getOldPosition(self):
        return self.oldPosition

    def getCurrentPosition(self):
        return self.currentPosition

    def getName(self):
        return self.name

    def getPlayer(self):
        return self.player

    def isAlive(self):
        return self.alive

    def kill(self):
        self.alive=False

    def killPiece(self, piece, board):
        if self.isEnemy(piece):
            piece.kill()
            if piece.belongsToPlayer1():
                board.removedPlayer1Piece()
            else:
                board.removedPlayer2Piece()
    
    def isEnemy(self, piece):
        return not piece.player==self.player

    def belongsToPlayer1(self):
        return self.player==1
    
    def belongsToPlayer2(self):
        return self.player==2
    
    def moveLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        position.updateCol(self.getStepsToMove(moveColFactor))
    
    def moveRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        position.updateCol(self.getStepsToMove(moveColFactor))

    def moveForward(self, position):
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updateRow(self.getStepsToMove(moveRowFactor))
    
    def moveBackward(self, position):
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updateRow(self.getStepsToMove(moveRowFactor))

    def moveFrontLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))
    
    def moveFrontRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        moveRowFactor = -1 if self.belongsToPlayer1() else 1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))

    def moveBackLeft(self, position):
        moveColFactor = -1 if self.belongsToPlayer1() else 1
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))

    def moveBackRight(self, position):
        moveColFactor = 1 if self.belongsToPlayer1() else -1
        moveRowFactor = 1 if self.belongsToPlayer1() else -1
        position.updatePosition(self.getStepsToMove(moveRowFactor),self.getStepsToMove(moveColFactor))
    
    def getStepsToMove(self, factor):
        return factor * self.steps
        
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
            
class Hero1(NormalPiece):
    def __init__(self, name, player, position):
        super().__init__(name, player, position,2)
        
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

if __name__ =="__main__":
    main()
