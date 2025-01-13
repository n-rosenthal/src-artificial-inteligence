"""
Defines a gamestate class for the 3-Sudoku game.
"""

from .board import Board;
from typing import List, Dict, Annotated, TypeVar, Optional, Tuple, Set, Counter;
import numpy;

class GameState:
    def __init__(self, board: Board) -> None:
        self.board = board;
        self.cost = -self.board.utility;
        
        self.parent = None;
        self.children : Set[GameState] = set();
        
    @staticmethod
    def fromFile(filename: str) -> "GameState":
        try:
            with open(filename, "r") as f:
                return GameState(Board.fromString(f.read()));
        except Exception as e:
            raise e;
    
    def __str__(self) -> str:
        return str( (self.board, self.cost) );
    
    def __repr__(self) -> str:
        return self.__str__();
    
    def __eq__(self, other) -> bool:
        return self.board == other.board;
    
    def __hash__(self) -> int:
        return hash(self.board);
    
    def __lt__(self, other) -> bool:
        return self.cost < other.cost;
    
    def __gt__(self, other) -> bool:
        return self.cost > other.cost;
    
    @property
    def rows(self) -> List[List[int]]:
        """
        Returns the rows of the Sudoku grid as a list of lists.

        Returns:
            List[List[int]]: A list containing 9 lists, each representing a row of the Sudoku grid.
        """
        return self.board.get_rows();
    
    @property
    def cols(self) -> List[List[int]]:
        """
        Returns the columns of the Sudoku grid as a list of lists.

        Returns:
            List[List[int]]: A list containing 9 lists, each representing a column of the Sudoku grid.
        """
        return self.board.get_cols();
    
    @property
    def squares(self) -> List[List[int]]:
        """
        Returns the squares of the Sudoku grid as a list of lists.

        Returns:
            List[List[int]]: A list containing 9 lists, each representing a square 
            of the Sudoku grid.
        """
        return self.board.get_squares();
    
    @property
    def empty_positions(self) -> List[Tuple[int, int]]:
        """
        Returns a list of all empty positions in the Sudoku grid.
        
        Returns:
            List[Tuple[int, int]]: A list of tuples representing the empty positions in the grid.
        """
        return self.board.empty_positions;
    
    @property
    def legal_moves(self) -> Set[Tuple[int, int]]:
        """
        Returns all the legal moves for the current state of the game.
        """
        return set(self.empty_positions);
    
    def is_right(self, position: Tuple[int, int]) -> bool:
        """
        Checks if `position` does not violate the Sudoku rules.
        
        Parameters:
            position (Tuple[int, int]): The position to be checked.
            
        Returns:
            bool: True if the position is valid, False otherwise.
        """
        col, row, square =  self.cols[position[1]], \
                            self.rows[position[0]], \
                            self.squares[position[0]//3][position[1]//3];
        return True if all(self.board._chkLine(col) == 0 and self.board._chkLine(row) == 0 and self.board._chkLine(square) == 0) else False;
        
    def is_valid_move(self, position: Tuple[int, int], value: int) -> bool:
        if position not in self.legal_moves or value < 1 or value > 9:
            return False;
        return True;
    
    def next_state(self, position: Tuple[int, int], value: int) -> "GameState":
        if not self.is_valid_move(position, value):
            return None;
        new_board = self.board.copy();
        new_board.set_value(position[0], position[1], value);
        return GameState(new_board);
    
    def backtrack(self) -> "GameState":
        return self.parent;
