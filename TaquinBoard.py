import sys
sys.setrecursionlimit(990000000)
#board = [7,2,4,5,0,6,8,3,1]
#board = [1,2,3,4,5,6,7,0,8]
board = [2,0,3,1,5,6,4,7,8]
solution = [1,2,3,4,5,6,7,8,0]

visited = []
toExplore = [board]


def moveRight(board,emptyPos):
    newBoard = board.copy() 
    if(emptyPos%3 == 2):
        return 
    newBoard[emptyPos],newBoard[emptyPos+1]=newBoard[emptyPos+1],newBoard[emptyPos]
    return newBoard 
def moveLeft(board,emptyPos):
    newBoard = board.copy() 
    if(emptyPos%3 == 0):
        return   
    newBoard[emptyPos],newBoard[emptyPos-1]=newBoard[emptyPos-1],newBoard[emptyPos]
    return newBoard 

def moveUp(board,emptyPos):
    newBoard = board.copy() 
    if(emptyPos+3>8):
        return   
    newBoard[emptyPos],newBoard[emptyPos+3]=newBoard[emptyPos+3],newBoard[emptyPos]
    return newBoard 

def moveDown(board,emptyPos): 
    newBoard = board.copy() 
    if(emptyPos-3<0):
        return   
    newBoard[emptyPos],newBoard[emptyPos-3]=newBoard[emptyPos-3],newBoard[emptyPos]
    return newBoard      

def genChilds(board):
    emptyPos = board.index(0)
    childs = []
    upChild = moveUp(board,emptyPos)
    downChild = moveDown(board,emptyPos)
    RightChild = moveRight(board,emptyPos)
    LeftChild = moveLeft(board,emptyPos)
    if(RightChild and RightChild not in visited):    
        childs.append(RightChild)
    if(LeftChild and LeftChild  not in visited):    
        childs.append(LeftChild)
    if(upChild and upChild not in visited ):
        childs.append(upChild); 
    if(downChild and downChild  not in visited ):    
        childs.append(downChild)
    
    return childs    

def notVisited(board):
    return not board in visited 

def formatBoard(board):
    print()
    print()
    print('________')
    for x in range(0,len(board)) :
        print(board[x],'|',end = '')
        if(x%3 == 2):
            print()
            print('________')
def formatSolution(list):
    for board in list:
        formatBoard(board)      

def solveBFS(board):
    #nodes not to visit again: 
    visited = [board]
    #nodes waiting to be explored
    toExplore = [board]
    #counter of visited nodes
    visitedNode =0
    found = False 
    while(len(toExplore)and not found):
        state = toExplore.pop()
        childs = genChilds(state)
        for childNode in childs: 
            if(not childNode in visited):
                if(childNode ==[1,2,3,4,5,6,7,8,0] ):
                    found = True
                    break 
                visitedNode = visitedNode +1 
                toExplore.append(childNode)
                visited.append(childNode)
    print("solution found after ",visitedNode, "nodes")       


#visited: list of already visited nodes  
# path: stack to save the solution path  
# prof: current depth
# maxProf: maximum depth to search within   
def  solveLimitedDFS(board,visited,path,prof,maxProf):
    if(prof>maxProf):
        return False
    visited.append(board)
    if(board == solution):
        print("found")
        return True
    if(not board):
        return False    
    childs = genChilds(board)
    if(not childs):
        return False
    for child in childs: 
        if(child not in visited):  
            path.append(child)
            if(solveLimitedDFS(child,visited,path,prof+1,maxProf)):
                return True 
            path.pop()
    return False        
            
     

def solveIterDFS(board):
    visited = list()
    maxProf =1
    while(True):
        print("en profMax= ",maxProf)
        path = [board]
        visited = []
        if(solveLimitedDFS(board,visited,path,0,maxProf)):
            print("solution requires",maxProf, "steps: ")
            formatSolution(path)
            print("with ", len(visited), " visited nodes")
            break 
        maxProf = maxProf+1 


visited = list()
#solveDFS([1,2,3,4,5,0,6,7,8],visited,0)
#solveIterDFS(board)
solveIterDFS(board)

    










