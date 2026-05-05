class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dupes = [{f'col dict #{i}':0} for i in range(len(board))]      #must be kept as an external list of dictionaries for each one
        square_dupes = [{f'box dict #{i}':0} for i in range(len(board))]
        #print(square_dupes, type(square_dupes), type(square_dupes[1]), square_dupes[1])

        for i in range(len(board)):         #iterates over rows
            row_dupes = {}
            for j in range(len(board[0])):  #iterates over columns
                box_index = int((i//3)*3 + (j/3))
                #print('boxindex:', box_index, square_dupes[box_index])
                if board[i][j] != ".":
                    if board[i][j] in row_dupes.keys():         #if there's a dupe in this row
                        print("1")
                        return False
                    elif board[i][j] in col_dupes[j].keys():    #if there's a dupe in this column
                        print("2")
                        return False
                    elif board[i][j] in square_dupes[box_index].keys():          #if there's a dupe in this box
                        print("3")
                        return False
                    else:
                        row_dupes[board[i][j]] = 1      #else, add it to col, row and box dicts
                        col_dupes[j][board[i][j]] = 1
                        square_dupes[box_index][board[i][j]] = 1
 
        for col in col_dupes:
            print(col)

        return True