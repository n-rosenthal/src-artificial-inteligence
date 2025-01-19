"""
Implements methods for getting the components (rows, columns and squares) of a Sudoku board.

@author     rdcn
@version    1.1
@since      1.1
@date       2025-01-19
@see        `.board.SudokuBoard`
@see        `.gamestate.GameState`
@see        `.SudokuEvaluator`
"""

from sudoku.board import SudokuBoard as Board, SudokuPosition as Position;
from typing import List, Dict, Annotated, TypeVar, Optional, Tuple, Set, Counter, Any;
from numpy import ndarray, transpose, partition, hsplit, vsplit, hstack, vstack;

class Splitter:
    """
    Implements methods for getting the components (rows, columns and squares) of a Sudoku board.
    """
    
    @staticmethod
    def get_rows(board: Board) -> List[List[Position]]:
        """
        Returns the rows of the Sudoku board as a list of lists.
        
        Returns:
            List[List[Position]]: A list containing 9 lists, each representing a row of the Sudoku board.
        """
        return board.grid;
    
    @staticmethod
    def get_cols(board: Board) -> List[List[Position]]:
        """
        Returns the columns of the Sudoku board as a list of lists.
        
        Returns:
            List[List[Position]]: A list containing 9 lists, each representing a column of the Sudoku board.
        """
        return transpose(board.grid);
    
        
    def get_squares(board: Board) -> List[List[Position]]:
        """
        Returns the squares of the Sudoku board as a list of lists.
        
        Returns:
            List[List[Position]]: A list containing 9 lists, each representing a square of the Sudoku board.
        """
        return [
            [board.grid[i][j] for j in range(0, 3) for i in range(0,3)],
            [board.grid[i][j] for j in range(3, 6) for i in range(0,3)],
            [board.grid[i][j] for j in range(6, 9) for i in range(0,3)],
            [board.grid[i][j] for j in range(0, 3) for i in range(3,6)],
            [board.grid[i][j] for j in range(3, 6) for i in range(3,6)],
            [board.grid[i][j] for j in range(6, 9) for i in range(3,6)],
            [board.grid[i][j] for j in range(0, 3) for i in range(6,9)],
            [board.grid[i][j] for j in range(3, 6) for i in range(6,9)],
            [board.grid[i][j] for j in range(6, 9) for i in range(6,9)]
        ];
    
    @staticmethod
    def get_empty_positions(board: Board) -> List[Tuple[int, int]]:
        """
        Returns a list of empty positions in the Sudoku board.

        Parameters:
            board (Board): The Sudoku board to be checked.

        Returns:
            List[Tuple[int, int]]: A list of tuples representing the empty positions in the board.
        """
        return [(i, j) for i in range(9) for j in range(9) if board.grid[i][j].value == 0];
    
    @staticmethod
    def get_initial_values(board: Board) -> List[Tuple[int, int]]:
        """
        Returns a list of initial values in the Sudoku board.

        Parameters:
            board (Board): The Sudoku board to be checked.

        Returns:
            List[Tuple[int, int]]: A list of tuples representing the initial values in the board.
        """
        return [(i, j) for i in range(9) for j in range(9) if board.grid[i][j].value != 0];


    @staticmethod
    def flatten(board: Board) -> List[Position]:
        """
        Flattens the Sudoku board into a single list of positions.

        Parameters:
            board (Board): The Sudoku board to be flattened.

        Returns:
            List[Position]: A list of all positions in the Sudoku board, in row-major order.
        """
        return [item for sublist in board.grid for item in sublist];  
    
    
    @staticmethod
    def get_row(board: Board, index: int) -> List[Position]:
        """
        Returns the row of the Sudoku board at the given index.

        Parameters:
            board (Board): The Sudoku board to be checked.
            index (int): The index of the row to be returned.

        Returns:
            List[Position]: A list of positions representing the row at the given index.
        """
        return board.grid[index];
    
    @staticmethod
    def get_col(board: Board, index: int) -> List[Position]:
        """
        Returns the column of the Sudoku board at the given index.

        Parameters:
            `board` (Board): The Sudoku board to be checked.
            `index` (int): The index of the column to be returned.

        Returns:
            `List[Position]`: A list of positions representing the column at the given index.
        """
        return transpose(board.grid)[index];
    
    @staticmethod
    def get_square(board: Board, index: int) -> List[Position]:
        """
        Returns the square of the Sudoku board at the given index.

        Parameters:
            `board` (Board): The Sudoku board to be checked.
            `index` (int): The index of the square to be returned.

        Returns:
            `List[Position]`: A list of positions representing the square at the given index.
        """
        return Splitter.get_squares(board)[index];
    
    @staticmethod
    def which_square(position: Position | Tuple[int, int]) -> int:
        """
        Returns the index of the square that contains the given position.

        Parameters:
            `position` (Position | Tuple[int, int]): The position to be checked.

        Returns:
            `int`: The index of the square that contains the given position.
        """
        if isinstance(position, Position):
            position = (position.x, position.y);
        return (position[0] // 3) * 3 + (position[1] // 3);