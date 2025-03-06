# Contoh List di dalam List
i = [2,3,4,5]
print(i[0])

k = [[3,5,1],[6,1,8],[9,10,4]]
print(k)
print(k[1])
print(k[1][0])
print(k[-1][-2:])

EMPTY = "-"
board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)] #membuat satu list
#     board.append(row) #membuat 8 list
#     print(row)
#print(board)

EMPTY = "-"
LIMALIMA = "LIMA"
ROOK = "ROOK"
KNIGHT = "KNIGHT"
PAWN = "PAWN"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

#isi dengan ROOK
board[0][0] = ROOK
board[5][5] = LIMALIMA
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

#isi dengan KNIGHT
board[4][2] = KNIGHT

#isi dengan PAWN
board[3][4] = PAWN


for j in range(8):
    print(board[j])
# print("\n")