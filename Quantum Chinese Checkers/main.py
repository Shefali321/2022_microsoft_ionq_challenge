from board_class import BoardClass

board = BoardClass()

board.start()

print("Splitting (3,1) downwards")
board.split((3,1),"bottom_left","bottom_right")

print(board.data[3,1])
print(board.data[3,2])
print(board.data[4,1])

print("(2,2) attempts to jump a piece in superposition")
board.move((2,2),None,"bottom_left")