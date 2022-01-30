# BOARD CLASS

# 5x5, top left is (1,1)
# board is a dictionary with the following format:
#   (x,y): [[<occupants>],[<qubits>]]
# occupants:
#   1    - whole team 1 piece
#   -1   - whole team 2 piece
#   0.5  - half team 1 piece
#   -0.5 - half team 2 piece
# qubits:
#   contains qubit ids corresponding to half pieces in occupants (probably #1-11)

# import qsharp
# import qsharp.azure
# from ChineseCheckers import MeasureSpace

class BoardClass:
    def __init__(self):
        self.data = {}
        for x in range(1,6):
            for y in range(1,6):
                self.data[(x,y)] = [[0],[0]]
      
    def start(self):
            self.data[(1,1)] = [[1.0],[]]
            self.data[(1,2)] = [[1.0],[]]
            self.data[(2,1)] = [[1.0],[]]

            self.data[(4,5)] = [[-1.0],[]]
            self.data[(5,4)] = [[-1.0],[]]
            self.data[(5,5)] = [[-1.0],[]]
    
    qids = [[1,2,3,4,5,6,7,8,9,10,11],[]]

    moves = {
        "top_left" : (0,-1),
        "top_right" : (-1,0),
        "right" : (-1,1),
        "bottom_right" : (0,1),
        "bottom_left" : (1,0),
        "left" : (1,-1)
    }

    # def record_move(coords1,coords2):

    # Function that moves a whole piece by swapping the state of the spaces from 0 to 1 and vice versa
    def whole_move(self,coords1,coords2):
        # self.data[coords1][0], self.data[coords2][0] = self.data[coords2][0], self.data[coords1][0]
        self.data[coords1], self.data[coords2] = self.data[coords2], self.data[coords1]
    
    # piecedata is a tuple that contains (p,qid)
    #   p = probability that the piece makes this move
    #   # = qubit id
    def half_move(self,final_coords, player, p,qid):
        # i = self.data[coords1][1].index(qid)
        self.data[final_coords][0] = p * player
        self.data[final_coords][1] = qid

    def measureHQbit():
        state = MeasureSpace()
        return state

    def collapse():
        state = MeasureSpace()
        return state

    # Function that checks if a piece is allowed to make a whole move and then performs it
    def base_move(self,current_position,p,qid,movement,split_movement=None):
        if p > 0 and p < 1 and split_movement == None:
            print ("Error: Provide 2 final positions for a quantum move")

        new_position = (current_position[0] + self.moves[movement][0], current_position[1] + self.moves[movement][1])
        if abs(self.data[current_position][0][0]) == 1: # if it is a whole bead
            if self.data[new_position][0][0] == 0: # if there is nothing where it is landing
                print("Movement allowed")
                # make actual transformation
                self.whole_move(self, current_position, new_position)

            elif abs(self.data[new_position][0][0]) == 1: # if there is a whole bead where it is landing
                # print("try a jump!")
                # self.jump(self,current_position,p,qid,tag,movement)
                print("Space is occupied. You lost your turn!")

            else: # quantum stuff where it is landing
                print("quantum stuff!")
                # TODO: collapse. Are we calling Measure Data?

        elif self.data[current_position][0][0] == 0: # nothing to move
            print("nothing to move!")

        else: # if there are splits where it is landing --> forces a measurement (?)
            print("quantum stuff!")

            if self.data[new_position][0][0] == 0: # empty space at destination
                # Check that both split positions are allowed
                new_split_position = (current_position[0] + self.moves[split_movement][0], current_position[1] + self.moves[split_movement][1])
                if self.data[new_split_position][0][0] == 0: # if there is nothing where it is landing
                    # Get Player
                    if (self.data[current_position][0] < 0): 
                        player = -1
                    else if (self.data[current_position][0] > 0): 
                        player = 1

                    self.half_move(self,new_position, player, p,qid)
                    self.half_move(self,new_split_position,player, p,qid)

                    # Reset current position 
                    self.data[current_position] = [[0],[0]]

            if abs(self.data[new_position][0][0]) == 1: # full space at destination
                print("Space is occupied. You lost your turn!")

            else: # quantum stuff --> We do not allow for more than one piece in the same square
                # self.half_move(self,current_position,new_position,p,qid)
                pass

    # # Function for splitting a piece into a superposition
    # def split(self,current_position,movement1,movement2):
    #     # self.base_move(self, current_position, movement1)
    #     # self.base_move(self, current_position, movement2)
    #     qid1 = self.qids[0].pop(0)
    #     qid2 = self.qids[0].pop(0)
    #     self.qids[1].append(qid1)
    #     self.qids[1].append(qid2)
    #     tag1 = "0"
    #     tag2 = "1"
    #     self.base_move(self,current_position,0.5,qid1,tag1,movement1)
    #     self.base_move(self,current_position,0.5,qid2,tag2,movement2)

    # Function to check if either player has won
    # def check_win(self, player):
    #     out = 0
    #     bool_list = []
    #     if (player == 1):
    #         bool_list.append(self.data[(3,5)][0] == (1))
    #         bool_list.append(self.data[(4,4)][0] == (1))
    #         bool_list.append(self.data[(4,5)][0] == (1))
    #         bool_list.append(self.data[(5,3)][0] == (1))
    #         bool_list.append(self.data[(5,4)][0] == (1))
    #         bool_list.append(self.data[(5,5)][0] == (1))
    #         if (bool_list == [True, True, True, True, True, True]):
    #             out = 1
    #     elif (player == -1):
    #         bool_list.append(self.data[(1,1)][0] == (-1))
    #         bool_list.append(self.data[(1,2)][0] == (-1))
    #         bool_list.append(self.data[(1,3)][0] == (-1))
    #         bool_list.append(self.data[(2,1)][0] == (-1))
    #         bool_list.append(self.data[(2,2)][0] == (-1))
    #         bool_list.append(self.data[(3,1)][0] == (-1))
    #         if (bool_list == [True, True, True, True, True, True]):
    #             out = -1
    #     return out