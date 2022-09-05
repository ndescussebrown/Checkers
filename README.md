# Checkers

This challenge was given to me as a tech exercise for an interview where I had to code the allowed_moves function that returns all allowed moves for checkers given a given board configuration. 

## Rules
- Each player begins with 12 colored discs as depicted in the previous image.
- The discs are positioned such that each player has a light square on the right side corner closest to him or her.
- Black moves first and players alternate henceforth.
- Moves are allowed only on the dark squares, so the discs always move diagonally. Regular discs are limited to forward moves (toward the opponent). Kings (see the last rule) can also move backward.
- There are 2 kinds of moves: **Capturing** and **Non-Capturing** moves.
- **Non-Capturing** moves may move only one square in diagonal to a vacant position.
- If more than 1 **Non-Capturing** moves exist, any of the moves can be played.
- A disc making a **Capturing** move leaps over one of the opponent's discs that is 1 square away from itself and lands in a straight diagonal line, which is 2 squares away from itself. A jump can make only 1 capture, but the same disc can capture multiple opponent discs by doing multiple jumps in a single move. **A disc can only make forward capturing moves** (english rules).
- A captured disc is removed from the board.
- If a **Capturing** move exists, the jump has to be made. If more than one capture exists, a choice can be made among **Capturing** moves.
- A disc reaching the opponent's side of the board is crowned as a King. King's move is similar to that of a regular disc's move but the restriction of forward only moves is lifted. Multiple King's may exist. When a disc reaches the opponent's side while capturing, **it is promoted King during the move and can continue to capture backwards during the same move. In some cases, a King can even go through the initial position it had when starting a capturing move**.

**Arguments**:

This function takes two arguments:
- ```board```: The content of the board, represented as a list of strings. The length of strings are the same as the length of the list, which represents a NxN checkers board. Each string is a row, from the top row (the black side) to the bottom row (white side). The string are made of five possible characters:
    - ```'_'``` : an empty square
    - ```'b'``` : a square with a black disc
    - ```'B'``` : a square with a black king
    - ```'w'``` : a square with a white disc
    - ```'W'``` : a square with a white king
- color: the next player's color. It can be either ```'b'``` for black or ```'w'``` for white.

**Output**:

The function ```allowed_moves``` returns a list of all the valid moves according to the previously described rules. A move is a list of all the squares visited by a disc or a king, from its initial position to its final position. The coordinates of the square must be specified by a tuple ```(row, column)```, with both ```row``` and ```column``` starting from 0 at the top left corner of the board (black side).

