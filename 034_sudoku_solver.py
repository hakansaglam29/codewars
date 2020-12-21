Write a function that will solve a 9x9 Sudoku puzzle. 
The function will take one argument consisting of the 2D puzzle array, 
with the value 0 representing an unknown square.







def sudoku(puzzle):
    def fix(board):
        for i in board:     
            for k in range(9):
                if type(i[k]) == list:
                    for x in i:
                        if x in tuple(i[k]): i[k].remove(x)
        for i in board:     
            for k in range(9):
                if type(i[k]) == list:
                    if len(i[k]) == 1: i[k] = i[k][0]
              
    for i in puzzle:     
        for k in range(len(i)):
            if i[k] == 0: i[k]=range(1,10)
            
    board_in_one_line = [type(i[k]) for k in range(9) for i in puzzle]

    while len(set(board_in_one_line))==2:
        
        fix(puzzle)
                                       
        puzzle=[list(map(lambda x:x[a],puzzle)) for a in range(9)]
    
        fix(puzzle)
                                           
        puzzle=[list(map(lambda x:x[a],puzzle)) for a in range(9)]
        
        puzzle=[list(map(lambda x:x[i:i+3],puzzle[k:k+3])) for k in range(0,9,3) for i in range(0,9,3)]   
        puzzle= [i[0]+i[1]+i[2] for i in puzzle]   

        fix(puzzle)   
                                
        puzzle=[list(map(lambda x:x[i:i+3],puzzle[k:k+3])) for k in range(0,9,3) for i in range(0,9,3)]
        puzzle= [i[0]+i[1]+i[2] for i in puzzle]
        
        board_in_one_line = [type(i[k]) for k in range(len(i)) for i in puzzle]
        
    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))
