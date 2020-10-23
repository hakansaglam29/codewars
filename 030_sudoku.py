# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all
# cells of the grid with digits from 1 to 9, so that each column, each row,
# and each of the nine 3x3 sub-grids (also known as blocks) contain all of 
# the digits from 1 to 9. 

board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]

def valid_solution(board):
    dik = [list(map(lambda x:x[a],board)) for a in range(len(board))]
# dik = []
# for a in range(len(board))
#   dik.extend(list(map(lambda x:x[a],board)))  
    k_dokuz=[list(map(lambda x:x[i:i+3],board[k:k+3])) for k in range(0,9,3)\
         for i in range(0,9,3)]
    
# k_dokuz = []
# for k in range(0,9,3):   
#     for i in range(0,9,3):
#         k_dokuz.extend(list(map(lambda x:x[i:i+3],board[k:k+3])))    
    
    k_dokuz= [i[0]+i[1]+i[2] for i in k_dokuz]
    
    board=[list(map(lambda x:x[i:i+3],k_dokuz[k:k+3])) for k in range(0,9,3)\
         for i in range(0,9,3)]
    
    board= [i[0]+i[1]+i[2] for i in board]
    
# y_k_dokuz = []
# for i in k_dokuz:
#    y_k_dokuz += [i[0]+i[1]+i[2]]   
 
    for i in board,dik,k_dokuz: 
        for k in i: 
            if set(k)!={1,2,3,4,5,6,7,8,9}: 
                return False 
    return True
# print(valid_solution(board))

print(valid_solution(board))