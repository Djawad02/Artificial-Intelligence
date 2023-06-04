                                                  #ASSIGNMENT # 3
                                                    #Dania Jawad
                                                     #20i-0569
                                                       #CS-B

#define chessBord with its elements
chessBord = []


#function to display the chessBord
def getBrd():
    chessBord = [ [8,'BRK','BKN' , 'BBP','BQN', 'BKG','BBP','BKN', 'BRK'],
              [7,'BPN','BPN' , 'BPN','BPN', 'BPN','BPN','BPN', 'BPN'],
              [6,'---','---' , '---','---', '---','---','---', '---'],
              [5,'---','---' , '---','---', '---','---','---', '---'],
              [4,'---','---' , '---','---', '---','---','---', '---'],
              [3,'---','---' , '---','---', '---','---','---', '---'],
              [2,'WPN','WPN' , 'WPN','WPN', 'WPN','WPN','WPN', 'WPN'],
              [1,'WRK','WKN' , 'WBP','WQN', 'WKG','WBP','WKN', 'WRK'],
              ['*',' a ',' b ',' c ',' d ',' e ',' f ',' g ',' h '] ]
    
    return chessBord

def displayBrd(chessBord):
    for i in chessBord:
        for pie in i:
            print(pie, end = " ")
        print()

#function for all possible moves of the rook
def movesForRK(chessBord, piece, row, col):
    print()
    if piece == 'WRK':
        print("Possible moves of WRK: ")

        movs = []
        for i in range(1,9):    
            move1 = 97
            coln = ord(col) - 97
            move3 = str(row)
        #vertical moves
        for i in range(row + 1, 9):
            move2 = str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
        for i in range(row - 1, 0, -1):
            move2= str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
            
        #horizontal moves
        for i in range(coln - 1, -1, -1):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+move3)
        for i in range(coln + 1, 8):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+ move3)
            # print((move1+move2), end = " ")

        return movs
    
    elif piece == 'BRK':
        print("Possible moves of BRK: ")
        movs = []
        for i in range(1,9):    
            move1 = 97
            coln = ord(col) - 97
            move3 = str(row)
        #vertical moves
        for i in range(row + 1, 9):
            move2 = str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
        for i in range(row - 1, 0, -1):
            move2= str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
            
        #horizontal moves
        for i in range(coln - 1, -1, -1):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+move3)
        for i in range(coln + 1, 8):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+ move3)
            # print((move1+move2), end = " ")

        return movs

#function for all possible moves of the pawn
def movesForPN(chessBord, piece, row, coln):
    print()
    if piece == 'WPN':
        print("Possible moves of WPN: ")
        movs = []
        if row == 2:        #pawn has two possible moves at the start
            move1 = coln
            move2 = str(row+1)
            move3 = str(row+2)
            coln = ord(coln) - 97
            # print((move1+move2), (move1+move3))
            if chessBord[row+1][coln] == '---': 
                movs.append(move1+move2)
            if chessBord[row+2][coln] == '---':
                movs.append(move1+move3)
        else:           #if pawn has initially moved
            move1 = coln
            move2 = str(row+1)
            # print((move1+move2))
            coln = ord(coln) - 97
            if chessBord[int(row)+1][int(coln)] == '---':
                movs.append(move1+move2)
        return movs
    elif piece == 'BPN':
        print("Possible moves of BPN: ")
        movs = []
        if row == 7:        #pawn has two possible moves at the start
            move1 = coln
            move3 = str(row-2)
            move2 = str(row-1)
            coln = ord(coln) - 97
            # print((move1+move2), (move1+move3))    
            if chessBord[row-2][coln] == '---': 
                movs.append(move1+move3)   
            if chessBord[row-3][coln] == '---':
                movs.append(move1+move2)    
        else:       #if pawn has initially moved
            move1 = coln
            move2 = str(row-1)
            # print((move1+move2))
            coln = ord(coln) - 97
            if chessBord[row-1][coln] == '---':
                movs.append(move1+move2)
        return movs 
    
#function for all possible moves of the knight
def movesForKN(chessBord, piece, row, coln):
    print()
    if piece == 'WKN':
        print("Possible moves of WKN: ")
        movs = []
        move1 = coln
        move2 = str(row+2)
        move3 = str(row+1)
        move4 = str(row-1)
        move5 = str(row-2)
        coln = ord(coln) - 97
        move6 = coln+2
        move7 = coln+1
        move8 = coln-1
        move9 = coln-2
        move6 = chr(move6+97)
        move7 = chr(move7+97)
        move8 = chr(move8+97)
        move9 = chr(move9+97)
        if row >=1 and row<8 and coln>=1 and coln<8:
            if chessBord[row+2][coln+1] == '---':
                movs.append(move7+move2)
            if chessBord[row+2][coln-1] == '---':
                movs.append(move8+move2)
            if chessBord[row-2][coln+1] == '---':
               movs.append(move7+move5)
            if chessBord[row-2][coln-1] == '---':
                movs.append(move8+move5)
            if chessBord[row+1][coln+2] == '---':
                movs.append(move6+move3)
            if chessBord[row+1][coln-2] == '---':
                movs.append(move9+move3)
            if chessBord[row-1][coln+2] == '---':
                movs.append(move6+move4)
            if chessBord[row-1][coln-2] == '---':
                movs.append(move9+move4)

        return movs
    
    elif piece == 'BKN':
        print("Possible moves of BKN: ")
        movs = []
        move1 = coln
        move2 = str(row+2)
        move3 = str(row+1)
        move4 = str(row-1)
        move5 = str(row-2)
        coln = ord(coln) - 97
        move6 = coln+2
        move7 = coln+1
        move8 = coln-1
        move9 = coln-2
        move6 = chr(move6+97)
        move7 = chr(move7+97)
        move8 = chr(move8+97)
        move9 = chr(move9+97)
        if row >=1 and row<8 and coln>=1 and coln<8:
            if chessBord[row+2][coln+1] == '---':
                movs.append(move7+move2)
            if chessBord[row+2][coln-1] == '---':
                movs.append(move8+move2)
            if chessBord[row-2][coln+1] == '---':
               movs.append(move7+move5)
            if chessBord[row-2][coln-1] == '---':
                movs.append(move8+move5)
            if chessBord[row+1][coln+2] == '---':
                movs.append(move6+move3)
            if chessBord[row+1][coln-2] == '---':
                movs.append(move9+move3)
            if chessBord[row-1][coln+2] == '---':
                movs.append(move6+move4)
            if chessBord[row-1][coln-2] == '---':
                movs.append(move9+move4)
        return movs
    
#function for all possible moves of the bishop
def movesForBS(chessBord, piece, row, col):
    print()
    if piece == 'WBP':
        print("Possible moves of WBP: ")
        movs = []
        coln = ord(col)
        row = int(row)
        move1 = str(row+1)
        move2 = str(row-1)
        move3 = coln+1
        move4 = coln-1
        move3 = chr(move3+97)
        move4 = chr(move4+97)
        #going up and right
        for i in range(1, 10):
            move2 = str(row+i)
            if row + i < 9 and coln + i < 105:
                if chessBord[row+i][coln - 96 + i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going up and left
        for i in range(1, 10):
            move2 = str(row-i)
            if row - i >0 and coln + i < 96:
                if chessBord[row-i][coln - 96 - i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going down and left
        for i in range(1, 10):
            move1 = str(row-i)
            if row - i > 0 and coln + i < 105:
                if chessBord[row-i][coln - 96 + i] == '---':
                    movs.append(chr(coln - i)+ move1)
        #going down and right
        for i in range(1, 10):
            move1 = str(row-i)
            if row + i < 9 and coln - i > 96:
                if chessBord[row+i][coln - 96 - i] == '---':
                    movs.append(chr(coln - i)+ move1)
        return movs
    
    elif piece == 'BBP':
        print("Possible moves of BBP: ")
        movs = []
        coln = ord(col)
        row = int(row)
        move1 = str(row+1)
        move2 = str(row-1)
        move3 = coln+1
        move4 = coln-1
        move3 = chr(move3+97)
        move4 = chr(move4+97)
        #going up and right
        for i in range(1, 10):
            move2 = str(row+i)
            if row + i < 9 and coln + i < 105:
                if chessBord[row+i][coln - 96 + i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going up and left
        for i in range(1, 10):
            move2 = str(row-i)
            if row - i >0 and coln + i < 96:
                if chessBord[row-i][coln - 96 - i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going down and left
        for i in range(1, 10):
            move1 = str(row-i)
            if row - i > 0 and coln + i < 105:
                if chessBord[row-i][coln - 96 + i] == '---':
                    movs.append(chr(coln - i)+ move1)
        #going down and right
        for i in range(1, 10):
            move1 = str(row-i)
            if row + i < 9 and coln - i > 96:
                if chessBord[row+i][coln - 96 - i] == '---':
                    movs.append(chr(coln - i)+ move1)
        return movs

#function for all possible moves of king
def movesForKG(chessBord, piece, row, col):
    print()
    if piece == 'WKG':
        print("Possible moves of WKG: ")
        movs = []
        move5 = str(row+1)
        move1=col
        move2 = str(row-1)
        coln = ord(col) - 97
        move4 = coln+1  
        move3 = coln-1
        move7 = str(row)
        move6 = str(row+1)
        move3=chr(move3+97)
        move4 = chr(move4+97)
        if row +1 <= 8:
            if chessBord[row+1][coln] == '---': #upper tile
                movs.append(move1 + move5)
            if chessBord[row-1][coln] == '---': #lower tile
                movs.append(move1+ move2)
            if chessBord[row][coln-1] == '---': #left tile
                # move1 = str(ord(move1) - 97)
                movs.append(move3+move7)
            if chessBord[row][coln+1] == '---': #right tile
                # move4 = str(chr(move4+97))
                movs.append(move4+move7)
            # #diagonal moves
            if chessBord[row+1][coln+1] == '---':
                movs.append(move4+move6)
            if chessBord[row-1][coln-1] == '---':
                movs.append(move3+move2)
            if chessBord[row-1][coln+1] == '---':
                movs.append(move4+move2)
            if chessBord[row+1][coln-1] == '---':
                movs.append(move3+move6)
        return movs
    elif piece == 'BKG':
        print("Possible moves of BKG: ")
        movs = []
        move5 = str(row+1)
        move1=col
        move2 = str(row-1)
        coln = ord(col) - 97
        move4 = coln+1  
        move3 = coln-1
        move7 = str(row)
        move6 = str(row+1)
        move3=chr(move3+97)
        move4 = chr(move4+97)
        if row +1 <= 8:
            if chessBord[row+1][coln] == '---': #upper tile
                movs.append(move1 + move5)
            if chessBord[row-1][coln] == '---': #lower tile
                movs.append(move1+ move2)
            if chessBord[row][coln-1] == '---': #left tile
                # move1 = str(ord(move1) - 97)
                movs.append(move3+move7)
            if chessBord[row][coln+1] == '---': #right tile
                # move4 = str(chr(move4+97))
                movs.append(move4+move7)
            # #diagonal moves
            if chessBord[row+1][coln+1] == '---':
                movs.append(move4+move6)
            if chessBord[row-1][coln-1] == '---':
                movs.append(move3+move2)
            if chessBord[row-1][coln+1] == '---':
                movs.append(move4+move2)
            if chessBord[row+1][coln-1] == '---':
                movs.append(move3+move6)
        return movs
    

#function for all possible moves of the queen
def movesForQN(chessBord, piece, row, col):
    print()
    if piece == 'WQN':
        print("Possible moves of WQN: ")
        movs = []
        
        for i in range(1,9):    
            move1 = 97
            coln = ord(col) - 97
            move3 = str(row)
        #vertical moves
        # print("vertical moves: ")
        for i in range(row + 1, 9):
            move2 = str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
        for i in range(row - 1, 0, -1):
            move2= str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
            
        #horizontal moves
        for i in range(coln - 1, -1, -1):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+move3)
        for i in range(coln + 1, 8):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+ move3)
            # print((move1+move2), end = " ")

        #diagonal moves
        coln = ord(col)
        row = int(row)
        # print("Diagonal moves:")
        #going up and right
        for i in range(1, 10):
            move2 = str(row+i)
            if row + i < 9 and coln + i < 105:
                if chessBord[row+i][coln - 96 + i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going up and left
        for i in range(1, 10):
            move2 = str(row-i)
            if row - i >0 and coln + i < 96:
                if chessBord[row-i][coln - 96 - i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going down and left
        for i in range(1, 10):
            move1 = str(row-i)
            if row - i > 0 and coln + i < 105:
                if chessBord[row-i][coln - 96 + i] == '---':
                    movs.append(chr(coln + i)+ move1)
        #going down and right
        for i in range(1, 10):
            move2 = str(row+i)
            if row + i < 9 and coln - i > 96:
                if chessBord[row+i][coln - 96 - i] == '---':
                    movs.append(chr(coln - i)+ move2)

        return movs
    
    elif piece == 'BQN':
        print("Possible moves of BQN: ")
        movs = []
        for i in range(1,9):    
            move1 = 97
            coln = ord(col) - 97
            move3 = str(row)
        #vertical moves
        for i in range(row + 1, 9):
            move2 = str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
        for i in range(row - 1, 0, -1):
            move2= str(i)
            if chessBord[i-1][coln] == '---':
                movs.append(chr(move1+ coln)+ move2)
            
        #horizontal moves
        for i in range(coln - 1, -1, -1):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+move3)
        for i in range(coln + 1, 8):
            if chessBord[row-1][i] == '---':
                movs.append(chr(move1 + i)+ move3)
            # print((move1+move2), end = " ")
        
        #diagonal moves
        coln = ord(col)
        row = int(row)
        #going up and right
        for i in range(1, 10):
            move2 = str(row+i)
            if row + i < 9 and coln + i < 105:
                if chessBord[row+i][coln - 96 + i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going up and left
        for i in range(1, 10):
            move2 = str(row-i)
            if row - i >0 and coln + i < 96:
                if chessBord[row-i][coln - 96 - i] == '---':
                    movs.append(chr(coln + i)+ move2)
        #going down and left
        for i in range(1, 10):
            move1 = str(row-i)
            if row - i > 0 and coln + i < 105:
                if chessBord[row-i][coln - 96 + i] == '---':
                    movs.append(chr(coln + i)+ move1)
        #going down and right
        for i in range(1, 10):
            move2 = str(row+i)
            if row + i < 9 and coln - i > 96:
                if chessBord[row+i][coln - 96 - i] == '---':
                    movs.append(chr(coln - i)+ move2)
        return movs

#function to check if a move is valid or not
def checkValidity(chessBord, piece, row, col,theMov):
    #white pieces
    if piece == 'WPN':
        mvsPawn =[]
        r1 = int(row)
        mvsPawn = movesForPN(chessBord, piece, r1, col)
        for i in range(len(mvsPawn)):
            val = mvsPawn[i]
            if val == theMov:
                return True
            
        return False
    
    elif piece == 'WRK':
        mvsRook =[]
        r1 = int(row)
        mvsRook = movesForRK(chessBord, piece, r1, col)
        for i in range(len(mvsRook)):
            val = mvsRook[i]
            if val == theMov:
                return True
            
        return False
    
    elif piece =='WKN':
        mvsKnight =[]
        r1 = int(row)
        mvsKnight= movesForKN(chessBord, piece, r1, col)
        for i in range(len(mvsKnight)):
            val = mvsKnight[i]
            if val == theMov:
                return True
            
        return False
    elif piece =='WQN':
        mvsQueen =[]
        r1 = int(row)
        mvsQueen= movesForQN(chessBord, piece, r1, col)
        for i in range(len(mvsQueen)):
            val = mvsQueen[i]
            if val == theMov:
                return True
            
        return False
    elif piece =='WBP':
        mvsBishop =[]
        r1 = int(row)
        mvsBishop= movesForBS(chessBord, piece, r1, col)
        print(mvsBishop)
        for i in range(len(mvsBishop)):
            print(mvsBishop[i], end = " ")
        
        print(theMov)

        for i in range(len(mvsBishop)):
            val = mvsBishop[i]
            if val == theMov:
                return True
            
        return False
    elif piece =='WKG':
        mvsKing =[]
        r1 = int(row)
        mvsKing= movesForKG(chessBord, piece, r1, col)
        print(mvsKing)
        for i in range(len(mvsKing)):
            print(mvsKing[i], end = " ")
        
        print(theMov)

        for i in range(len(mvsKing)):
            val = mvsKing[i]
            if val == theMov:
                return True
            
        return False
        

        #black pieces
    if piece == 'BPN':
        mvsPawn =[]
        r1 = int(row)
        mvsPawn = movesForPN(chessBord, piece, r1, col)
        for i in range(len(mvsPawn)):
            val = mvsPawn[i]
            if val == theMov:
                return True
            
        return False
    
    elif piece == 'BRK':
        mvsRook =[]
        r1 = int(row)
        mvsRook = movesForRK(chessBord, piece, r1, col)
        for i in range(len(mvsRook)):
            val = mvsRook[i]
            if val == theMov:
                return True
            
        return False
    
    elif piece =='BKN':
        mvsKnight =[]
        r1 = int(row)
        mvsKnight= movesForKN(chessBord, piece, r1, col)

        for i in range(len(mvsKnight)):
            val = mvsKnight[i]
            if val == theMov:
                return True
            
        return False
    elif piece =='BQN':
        mvsQueen =[]
        r1 = int(row)
        mvsQueen= movesForQN(chessBord, piece, r1, col)
        for i in range(len(mvsQueen)):
            val = mvsQueen[i]
            if val == theMov:
                return True
            
        return False
    elif piece =='BBP':
        mvsBishop =[]
        r1 = int(row)
        mvsBishop= movesForBS(chessBord, piece, r1, col)
        for i in range(len(mvsBishop)):
            val = mvsBishop[i]
            if val == theMov:
                return True
            
        return False
    elif piece =='BKG':
        mvsKing =[]
        r1 = int(row)
        mvsKing= movesForKG(chessBord, piece, r1, col)
        for i in range(len(mvsKing)):
            val = mvsKing[i]
            if val == theMov:
                return True
            
        return False
    
def placePiece(chessBord, piece, OldRow, OldCol,row, col):
    coln = ord(col) - 96
    OldCol = ord(OldCol) - 96
    OldRow = 8-int(OldRow)
    row = 8-int(row)

    chessBord[OldRow][OldCol] = chessBord[int(row)][coln] 
    chessBord[int(row)][coln] = piece
    # print(chessBord[int(OldRow)][OldCol])
    print()
    return chessBord

#function which will allow user to move piece
def movingPieces(chessBord, color,movnPiece):  
    # if color == 'white':
    mvsPawn = []
    print("Enter the piece(row,col) you want to move:")
    r1 = int(input())
    c1 = str(input())
    print("Enter where(row,col) to move")
    r2 = int(input())
    c2 = str(input())
    
    r1= str(r1)
    r2 = str(r2)
    playersMov = (c2+r2)
    # print("players move",playersMov)
    if checkValidity(chessBord,movnPiece,r1,c1,playersMov):
        print("Valid move")
        placePiece(chessBord, movnPiece, r1, c1,r2,c2)
    else:
        print("Invalid move")
    
    displayBrd(chessBord)
    
def kingPosition(chessBord, color):
    if color == 'white':
        for i in range(9):
            for j in range(9):
                if chessBord[i][j] == 'WKG':
                    return i,j
    else:
        for i in range(9):
            for j in range(9):
                if chessBord[i][j] == 'BKG':
                    return i,j

def checkk(chessBord, color,r,c) :
    c = ord(c) - 97
    if color == 'white':
        for i in range(9):
            for j in range(9):
                if chessBord[i][j] == chessBord[r][c]:
                    return True
                elif chessBord[i+1][j+1] == chessBord[r][c] : 
                    return True
                elif chessBord[i+1][j-1] == chessBord[r][c] :
                    return True
                elif chessBord[i-1][j+1] == chessBord[r][c]: 
                    return True
                elif chessBord[i-1][j-1] == chessBord[r][c] :
                    return True
                else:
                    return False


def checkMate(chessBord, color):
    king = kingPosition(chessBord, color)
    col = chr(king[1]+96)
    row = 8-king[0]
    print()
    print("The king is at: ",col+str(row))

    if checkk(chessBord, color,row,col):
        print()
        # print("The king is at checkmate")
    # else:
    #     print("The king is safe")

def evaluateBoard(chessBord,val):
    print("The points: ",val)
    print()
    Wpoints = 0
    Bpoints = 0
    for i in range(9):
        for j in range(9):
           Wpoints =  8*1 + 2*3 + 2*3 + 2*5 + 1*9 + 1*10000
           Bpoints =  8*1 + 2*3 + 2*3 + 2*5 + 1*9 + 1*10000
            
    return Wpoints,Bpoints
        

def main():
    
    print("\t\t\t\t\t**Welcome to the Chess**")
    mvsRook = []
    mvsPawn = []
    mvKing = []
    mvsKnight = []
    mvsQueen = []
    mvsBishop = []
    chessBoard1 = []

    value = [('PN',1),('QN',9),('BP',3),('KN',3),('RK',5),('KG',10000)]
    #yahn sy loop chalay ga
    print("The current board:")
    print()
    
    chessBord = getBrd()
    displayBrd(chessBord)
    print()

    c = evaluateBoard(chessBord,value)

    print("The white points and black points are: ",c[0],c[1])
    print("the initial board has value of: ",c[0]-c[1])
    print()
    print()
    print("Choose a colour Black or White:")
    player = input()
    print()

    while True:
        if player == 'white':
            print("White piece!")
            print("Choose a piece to move:(eg WPN, etc) ")
            movPiece = input()
            if movPiece.startswith("W"):
                movingPieces(chessBord,player,movPiece)
                checkMate(chessBord, player)
                print()
            else: 
                print("Invalid piece. Try again")
                movPiece = input()
                movingPieces(chessBord,player,movPiece)
                checkMate(chessBord, player)
                print()

            player = 'black'
        else:
            print("Black piece!")
            print("Choose a piece to move:(eg BPN etc) ")
            movPiece = input()
            if movPiece.startswith("B"):
                movingPieces(chessBord,player,movPiece)
                checkMate(chessBord, player)
                print()
            else: 
                print("Invalid piece. Try again")
                movPiece = input()
                movingPieces(chessBord,player,movPiece)
                checkMate(chessBord, player)
                print()
            player = 'white'

    print()
    print("The final board: ")
    displayBrd(chessBord)

if __name__ == "__main__":
    main()






