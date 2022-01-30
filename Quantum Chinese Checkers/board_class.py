# BOARD CLASS

# 5x5, top left is (1,1)
# board is a dictionary with the following format:
#   (x,y): [[<occupants>],[<qubits>],[<tags>]]
# occupants:
#   1    - whole team 1 piece
#   -1   - whole team 2 piece
#   0.5  - half team 1 piece
#   -0.5 - half team 2 piece
# qubits:
#   contains qubit ids corresponding to half pieces in occupants (probably #1-11)
# tags:
#   all strings
#   2-7 are whole
#   strings of 0s and 1s are parts of pieces in superposition

import qsharp
import qsharp.azure
from ChineseCheckers import MeasureSpace

class BoardClass:
    def __init__(self):
        self.data = {}
        for x in range(1,6):
            for y in range(1,6):
                self.data[(x,y)] = [[],[],[]]
        self.hist_data = self.data
      
    def start(self):
            self.data[(1,1)] = [[1],[], ["2"]]
            self.data[(1,2)] = [[1],[], ["3"]]
            self.data[(1,3)] = [[1],[], ["4"]]
            self.data[(2,1)] = [[1],[], ["5"]]
            self.data[(2,2)] = [[1],[], ["6"]]
            self.data[(3,1)] = [[1],[], ["7"]]

            self.data[(3,5)] = [[-1],[], ["-2"]]
            self.data[(4,4)] = [[-1],[], ["-3"]]
            self.data[(4,5)] = [[-1],[], ["-4"]]
            self.data[(5,3)] = [[-1],[], ["-5"]]
            self.data[(5,4)] = [[-1],[], ["-6"]]
            self.data[(5,5)] = [[-1],[], ["-7"]]
    
    whole_tags = ["2","3","4","5","6","7","-2","-3","-4","-5","-6","-7"]
    qids = [[1,2,3,4,5,6,7,8,9,10,11],[]]

    moves_list = []

    moves = {
        "top_left" : (0,-1),
        "top_right" : (-1,0),
        "right" : (-1,1),
        "bottom_right" : (0,1),
        "bottom_left" : (1,0),
        "left" : (1,-1)
    }

    # quality is an array of moves{} entries, either one or two elements long (regular vs split)
    def record_move(self,quality,qid,tag_in,tags_out):
        self.moves_list.append((quality,qid,tag_in,tags_out))

    def record_hist(self):
        self.hist_data = self.data

    def measureHQbit():
        state = MeasureSpace()
        return state

    def get_state():
        state_arr = []
        for i in range(len(self.qids[1])):
            state_arr.append(MeasureSpace())

    def collapse(self):
        
        for move in self.moves_list:
            if (move[4][0] in self.whole_tags):
                hist_base_move

        # end
        self.hist_data = self.data
        self.qids[0] = self.qids[0] + self.qids[1]
        self.qids[1] = []

    # Function that moves a whole piece by swapping the state of the spaces from 0 to 1 and vice versa
    def whole_move(self,coords1,coords2):
        self.data[coords1], self.data[coords2] = self.data[coords2], self.data[coords1]
    
    # piecedata is a tuple that contains (p,qid)
    #   p = probability that the piece makes this move
    #   # = qubit id
    def half_move(self,coords1,coords2,p,qid,tag):
        i = self.data[coords1][1].index(qid)
        self.data[coords1][0].pop(i)
        self.data[coords1][1].pop(i)
        self.data[coords2][0].append(p)
        self.data[coords2][1].append(qid)
        self.data[coords1][2].pop(i)
        self.data[coords2][2].append(tag)

    # Function that checks if a piece is allowed to make a jump and then performs it
    def jump(self,current_position,p,qid,tag,movement):
        jump_position = (current_position[0] + 2*self.moves[movement][0], current_position[1] + 2*self.moves[movement][1])
        if abs(self.data[current_position][0][0]) == 1: # if it is a whole bead
            if self.data[jump_position][0] == []: # if there is nothing where it lands
                print("Movement allowed")
                self.whole_move(self,current_position, jump_position)
                self.record_move(self,[self.moves[movement]],qid,tag,[tag]])
            elif abs(self.data[jump_position][0][0]) == 1: # if there is a whole bead where it is landing
                print("not allowed bud")
            else:
                print("quantum stuff!")
                self.collapse(self)
                self.jump(self,current_position,p,qid,tag,movement)
        elif self.data[current_position][0] == []: # nothing to move
            print("nothing to move!")
        else: # is a quantum thing
            print("quantum stuff!")
            if self.data[jump_position][0] == []:
                print("movement allowed")
                self.half_move(self,current_position, jump_position, p, qid, tag)
                tag_in = ""
                tags_out = [""]
                self.record_move(self,[self.moves[movement]],qid,tag,[tag])
            elif abs(self.data[jump_position][0][0]) == 1:
                print("movement not allowed")
            else: # even more quantum stuff
                print("quantum stuff!")
                ps_product = 1
                for pj in self.data[jump_position][0]:
                    ps_product = ps_product*pj
                pjump = p*ps_product
                pstop = (1 - pjump)*abs(p)/p
                tag1 = tag + "0"
                tag2 = tag + "1"
                self.half_move(self,current_position,jump_position,pjump,qid,tag1)
                self.half_move(self,current_position,current_position,pstop,qid,tag2) # uses half move to not move
                self.record_move(self,[self.moves[movement]],qid,tag,[tag1,tag2])
                
    # Function that checks if a piece is allowed to make a whole move and then performs it
    def base_move(self,current_position,p,qid,tag,movement):
        new_position = (current_position[0] + self.moves[movement][0], current_position[1] + self.moves[movement][1])
        if abs(self.data[current_position][0][0]) == 1: # if it is a whole bead
            if self.data[new_position][0] == []: # if there is nothing where it is landing
                print("Movement allowed")
                # make actual transformation
                self.whole_move(self,current_position,new_position)
                tag_in = ""
                tags_out = [""]
                self.record_move(self,[self.moves[movement]],qid,tag_in,[tags_out])
            elif abs(self.data[new_position][0][0]) == 1: # if there is a whole bead where it is landing
                print("try a jump!")
                self.jump(self,current_position,p,qid,tag,movement)
            else: # quantum stuff where it is landing
                print("quantum stuff!")
                self.collapse(self)
                self.base_move(self,current_position,p,qid,tag,movement)
        elif self.data[current_position][0] == []: # nothing to move
            print("nothing to move!")
        else: # if there are splits where it is landing --> forces a measurement (?)
            print("quantum stuff!")
            if self.data[new_position][0] == []: # empty space at destination
                self.half_move(self,current_position,new_position,p,qid,tag)
            elif abs(self.data[new_position][0][0]) == 1: # full space at destination
                self.jump(self,current_position,p,qid,tag,movement)
            else: # quantum stuff
                ps_product = 1
                for pj in self.data[new_position][0]:
                    ps_product = ps_product*pj
                pjump = p * (1 - ps_product)
                tag1 = tag + "0"
                tag2 = tag + "1"
                self.jump(self,current_position,pjump,qid,tag1,movement)
                self.half_move(self,current_position,new_position,p*ps_product,qid,tag2)

    # Function for splitting a piece into a superposition
    def split(self,current_position,movement1,movement2):
    
        qid1 = self.qids[0].pop(0)
        qid2 = self.qids[0].pop(0)
        self.qids[1].append(qid1)
        self.qids[1].append(qid2)
        tag1 = "0"
        tag2 = "1"
        self.base_move(self,current_position,0.5,qid1,tag1,movement1)
        self.base_move(self,current_position,0.5,qid2,tag2,movement2)

    # Function to check if either player has won
    def check_win(self, player):
        out = 0
        bool_list = []
        if (player == 1):
            bool_list.append(self.data[(3,5)][0] == (1))
            bool_list.append(self.data[(4,4)][0] == (1))
            bool_list.append(self.data[(4,5)][0] == (1))
            bool_list.append(self.data[(5,3)][0] == (1))
            bool_list.append(self.data[(5,4)][0] == (1))
            bool_list.append(self.data[(5,5)][0] == (1))
            if (bool_list == [True, True, True, True, True, True]):
                out = 1
                print("Player 1 wins!)")
        elif (player == -1):
            bool_list.append(self.data[(1,1)][0] == (-1))
            bool_list.append(self.data[(1,2)][0] == (-1))
            bool_list.append(self.data[(1,3)][0] == (-1))
            bool_list.append(self.data[(2,1)][0] == (-1))
            bool_list.append(self.data[(2,2)][0] == (-1))
            bool_list.append(self.data[(3,1)][0] == (-1))
            if (bool_list == [True, True, True, True, True, True]):
                out = -1
                print("Player 2 wins!")
        return out

    def hist_base_move(self,current_position,p,qid,tag,movement):
        new_position = (current_position[0] + self.moves[movement][0], current_position[1] + self.moves[movement][1])
        if abs(self.hist_data[current_position][0][0]) == 1: # if it is a whole bead
            if self.hist_data[new_position][0] == []: # if there is nothing where it is landing
                print("Movement allowed")
                # make actual transformation
                self.hist_data[current_position], self.hist_data[new_position] = self.hist_data[new_position], self.hist_data[current_position]
            elif abs(self.data[new_position][0][0]) == 1: # if there is a whole bead where it is landing
                print("try a jump!")
                self.hist_jump(self,current_position,movement)

    def hist_jump(self,current_position,movement):
        jump_position = (current_position[0] + 2*self.moves[movement][0], current_position[1] + 2*self.moves[movement][1])
        if self.hist_data[jump_position][0] == []: # if there is nothing where it lands
            print("Movement allowed")
            self.hist_data[current_position], self.hist_data[jump_position] = self.hist_data[jump_position], self.hist_data[current_position]
        elif abs(self.hist_data[jump_position][0][0]) == 1: # if there is a whole bead where it is landing
            print("not allowed bud")
