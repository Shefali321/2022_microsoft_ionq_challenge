import qsharp
import qsharp.azure
from ChineseCheckers import MeasureSpace

from board_class_simple import BoardClass_Simple

board = BoardClass_Simple()

board.start()

# Lines for testing
print("INITIAL BOARD")
# print(board.data)
# board.base_move((2,1), 1.0, 0, 'bottom_right')
# print(board.data)
print("PERFORMING QUANTUM MOVE")
board.base_move((1,2), 0.5, 1, 'bottom_right', 'bottom_left')
#print(board.data)
board.base_move((4,5), 0.5, 2, 'top_right', 'top_left')
print(board.data)