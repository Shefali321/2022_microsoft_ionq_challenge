# Quantum Chinese Checkers

### Overview- This is a quantum variant of the classic game Chinese Checkers. Opponents try to move their pieces to the spaces on the opposite side of the board. They can move in all six hexagonal directions one space or jump over a neighboring piece. 

![board](https://github.com/Shefali321/2022_microsoft_ionq_challenge/blob/main/Quantum%20Chinese%20Checkers/templates/images/2022-01-30%2022_50_34-Window.png)

### Rules
- Goal: Get all of your pieces to the triangle at the opposite side
- Players can choose to break a piece’s move into a superposition of two other moves specified by direction
- Pieces can move over one space and jump over other pieces as well.
- When a whole piece tries to jump over a split piece, collapse of the board occurs<br>

The board is described with a dictioanry, where the keys are tuples with the 'x' and 'y' coordinates of each space. Then values of the dictionary are a list that contains as first element the probability of having a bead on the corresponding square (positives values for player 1 and negative values por player 2), and a second value that indicates the qbit that describes the state of the space. 

The hexagonal moves are performed according the figure below. The move selection checks whether the selected movements are out of bounds and wheter the final position is occupied or not (or maybe) for another bead.
![rules](https://github.com/Shefali321/2022_microsoft_ionq_challenge/blob/main/Quantum%20Chinese%20Checkers/templates/images/img123.png)

### iQuHack 2022- The most challenging part was setting up the idea and we would have liked to created more challenging quantum circuits, but were unsure of how to connect those with the game. Overall, it was a great experience! <br>
