import random
import re

def allowed_moves(board, color):
    """
        This is the first function you need to implement.

        Arguments:
        - board: The content of the board, represented as a list of strings.
                 The length of strings are the same as the length of the list,
                 which represents a 8x8 checkers board.
                 Each string is a row, from the top row (the black side) to the
                 bottom row (white side). The string are made of five possible
                 characters:
                 - '_' : an empty square
                 - 'b' : a square with a black disc
                 - 'B' : a square with a black king
                 - 'w' : a square with a white disc
                 - 'W' : a square with a white king
                 At the beginning of the game:
                 - the top left square of a board is always empty
                 - the square on it right always contains a black disc
        - color: the next player's color. It can be either 'b' for black or 'w'
                 for white.

        Return value:
        It must return a list of all the valid moves. Please refer to the
        README for a description of what are valid moves. A move is a list of
        all the squares visited by a disc or a king, from its initial position
        to its final position. The coordinates of the square must be specified
        using (row, column), with both 'row' and 'column' starting from 0 at
        the top left corner of the board (black side).

        Example:
        >> board = [
            '________',
            '__b_____',
            '_w_w____',
            '________',
            '_w______',
            '_____b__',
            '____w___',
            '___w____'
        ]

        The top-most black disc can chain two jumps and eat both left white
        discs or jump only over the right white disc. The other black disc
        cannot move because it does produces any capturing move.

        The output must thus be:
        >> allowed_moves(board, 'b')
        [
            [(1, 2), (3, 0), (5, 2)],
            [(1, 2), (3, 4)]
        ]
    """

    find_colorrows = [i for i,ltr in enumerate(board) if ((color in ltr) | (color.upper() in ltr))]
    interm_result_lower = map(lambda x: ([(x,ltr.start()) for ltr in re.finditer(color,board[x])]), find_colorrows)
    interm_result_upper = map(lambda x: ([(x,ltr.start()) for ltr in re.finditer(color.upper(),board[x])]), find_colorrows)
    concatlist=list(interm_result_upper)+list(interm_result_lower)
    find_color=[item for item in concatlist if item!=[]]
    #find_color.append([item for sublist in list(interm_result_upper) for item in sublist])
    mylist_moves=[]
    final=[]
    list_moves_interm=[i for i in find_color]
    list_moves=[[item] for sublist in concatlist for item in sublist]
    iterr=0
    test2=[]
    test4=[]
    capturingmoves = [] 
    test3=[]
    capturinglist=[]
    result = [] 

    def capturing(i,j,k,color,mymoves,list_moves):
        
        if color=='b':
                        if ((i<6) & (j>1)):
                            if ((board[i+1][j-1]!='_')  & (board[i+1][j-1]!=color) & (board[i+1][j-1]!=color.upper()) & (board[i+2][j-2]=='_')):
                                mymoves.append((i+2,j-2))
                                capturinglist.append(mymoves)

                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if (j<6) & (i<6):
                            if ((j>-1) & (board[i+1][j+1]!='_')  & (board[i+1][j+1]!=color) & (board[i+1][j+1]!=color.upper()) & (board[i+2][j+2]=='_')):
                                mymoves.append((i+2,j+2))
                                capturinglist.append(mymoves)

                        
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                                    
                        if ((i>1) & (j>1)):
                            if ((board[i][j]=='B') & (board[i-1][j-1]!='_')  & (board[i-1][j-1]!=color) & (board[i-1][j-1]!=color.upper()) & (board[i-2][j-2]=='_')):
                                mymoves.append((i-2,j-2))
                                capturinglist.append(mymoves)
 
                                
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if ((i>1) & (j<6)):
                            if ((board[i][j]=='B') & (board[i-1][j+1]!='_')  & (board[i-1][j+1]!=color) & (board[i-1][j+1]!=color.upper()) & (board[i-2][j+2]=='_')):
                                mymoves.append((i-2,j+2))
                                capturinglist.append(mymoves)
        elif color=='w':
        
                        if ((i>1) & (j<6)):
                            if ((board[i-1][j+1]!='_')  & (board[i-1][j+1]!=color) & (board[i-1][j+1]!=color.upper()) & (board[i-2][j+2]=='_')):
                                mymoves.append((i-2,j+2))
                                capturinglist.append(mymoves)

                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if ((i>1) & (j>1)):
                            if ((board[i-1][j-1]!='_')  & (board[i-1][j-1]!=color) & (board[i-1][j-1]!=color.upper()) & (board[i-2][j-2]=='_')):
                                mymoves.append((i-2,j-2))
                                capturinglist.append(mymoves)                                
                                
                                
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if ((i<6) & (j>1)):
                            if ((board[i][j]=='W') & (board[i+1][j-1]!='_')  & (board[i+1][j-1]!=color) & (board[i+1][j-1]!=color.upper()) & (board[i+2][j-2]=='_')):
                                mymoves.append((i+2,j-2))
                                capturinglist.append(mymoves)

                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if ((i<6) & (j<6)):
                            if ((board[i][j]=='W') & (board[i+1][j+1]!='_')  & (board[i+1][j+1]!=color) & (board[i+1][j+1]!=color.upper()) & (board[i+2][j+2]=='_')):
                                mymoves.append((i+2,j+2))
                                capturinglist.append(mymoves)           
                        
        return capturinglist

    def nextmove(list_moves,color,iterr,test2):
        if color=='b':
                    test2=[]
                    test1=[]
                    test3=[]
                    for k in range(len(list_moves)):
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        
                        test1=list_moves
                        test3=mylist_moves
                        mynewmoves = capturing(i,j,k,color,mymoves,list_moves)
                        if ((mynewmoves!=test1) & (mynewmoves!=test3) & (mynewmoves!=[])):
                            [capturingmoves.append(x) for x in mynewmoves if x not in test3] 
                            continue

                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1] 
                        
                                     
                        if ((i>1) & (j>1)):
                            if ((iterr==0) & (board[i][j]=='B') & (board[i-1][j-1]=='_')):
                                mymoves.append((i-1,j-1))
                                mylist_moves.append(mymoves)
                       
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]   
                            
                        if ((i>1) & (j<6)):
                            if ((iterr==0) & (board[i][j]=='B') & (board[i-1][j+1]=='_')):
                                mymoves.append((i-1,j+1))
                                mylist_moves.append(mymoves) 
                        
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        
                        if ((j<7) & (i<7)):
                            if ((iterr==0) & (board[i+1][j+1]=='_') ):
                                mymoves.append((i+1,j+1))
                                mylist_moves.append(mymoves) 

                            
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if ((j>0) & (i<7)):
                            if ((iterr==0) & (board[i+1][j-1]=='_') ):
                                mymoves.append((i+1,j-1))
                                mylist_moves.append(mymoves) 
                        test2=mylist_moves

        if color=='w':
                    test2=[]
                    test1=[]
                    test3=[]
                    for k in range(len(list_moves)):
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]

                        test1=list_moves
                        test3=mylist_moves
                        mynewmoves = capturing(i,j,k,color,mymoves,list_moves)
                        if ((mynewmoves!=test1) & (mynewmoves!=test3) & (mynewmoves!=[])):
                            [capturingmoves.append(x) for x in mynewmoves if x not in test3] 
                            continue
                                
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]

                        if ((i<7) & (j>1)): 
                            if ((board[i][j]=='W') & (iterr==0) &(board[i+1][j-1]=='_')):
                                mymoves.append((i+1,j-1))
                                mylist_moves.append(mymoves)
                        
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if ((i<7) & (j<7)):
                            if ((board[i][j]=='W') &(iterr==0) &(board[i+1][j+1]=='_')):
                                mymoves.append((i+1,j+1))
                                mylist_moves.append(mymoves)     
                                
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                            i=list_moves[k][-1][0]
                            j=list_moves[k][-1][1]
                        if ((i>0) & (j<7)):
                            if ((iterr==0) & (board[i-1][j+1]=='_')):
                                mymoves.append((i-1,j+1))
                                mylist_moves.append(mymoves) 

                            
                        if len(list_moves[k])==1:
                            mymoves=[list_moves[k][-1]]
                        else:
                            mymoves=list_moves[k]
                        i=list_moves[k][-1][0]
                        j=list_moves[k][-1][1]
                        if ((i>0) & (j>0)):
                            if ((iterr==0) & (board[i-1][j-1]=='_')):
                                mymoves.append((i-1,j-1))
                                mylist_moves.append(mymoves) 
                        test2=mylist_moves
                          

        ln2=[(len(i)) for i in (mylist_moves)]
        ln1=[(len(i)) for i in (list_moves)]
            
        iterr+=1
                    
        if capturingmoves==[]:    
            result = [] 
            [result.append(x) for x in  mylist_moves if x not in result] 
            result
        else:
            result = []
            [result.append(x) for x in capturingmoves if x not in result]
            result
        
        if (ln2!=ln1):
            nextmove(result,color,iterr,test2)
            return result
        else:
            return result
     
    return nextmove(list_moves,color,iterr,test2)

