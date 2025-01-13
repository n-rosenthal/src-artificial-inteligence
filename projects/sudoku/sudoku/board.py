"""
Defines the class necessary to represent a Sudoku board.
"""

import copy;
from typing import List, Dict, Annotated, TypeVar, Optional, Tuple, Set, Counter;
import numpy;

class Board:
    def __init__(self, grid: numpy.array) -> None:
        """
        Initializes the Board object.
        
        Parameters:
            grid (np.ndarray): A 9x9 numpy array representing the Sudoku grid.
        """
        
        self.grid = grid;
        self.initial_values     : List[Tuple[int,int]] = [];
        self.empty_positions    : List[Tuple[int,int]] = [];
        self.utility            : int = self.eval(self.grid);
        
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.initial_values.append((i, j));
                else:
                    self.empty_positions.append((i, j));
        
        self.value = 81 - len(self.empty_positions);
        
        
    def __call__(self) -> str:
        return f"""
            Value: {self.value}
            Grid:\n {self.grid}
            Empty positions: {len(self.empty_positions)} \n {self.empty_positions}
            Invalid positions: {len(self.invalid_positions)} \n {self.invalid_positions}"""

    def _chkLine(self, line: List[int]) -> int:
        """
        Returns 0 if the line is valid, else the sum of the invalid positions.
        
        Parameters:
            line (List[int]): The line to be checked.
            
        Returns:
            int: 0 if the line is valid, else the sum of the invalid positions.
        """
        if len(line) != 9:
            raise ValueError("Line must be of length 9.");
        if len(set(line)) != 9:
            return 9 - len(set(line));
        return 0;
    
    def eval(self, grid: numpy.array) -> int:
        """
        Returns the evaluation of the Sudoku grid.
        
        Parameters:
            grid (np.ndarray): A 9x9 numpy array representing the Sudoku grid.
            
        Returns:
            int: The evaluation of the grid.
        """
        return sum([self._chkLine(line) for line in grid]);
    
    
    def get_rows(self) -> List[List[int]]:
        """
        Returns the rows of the Sudoku grid as a list of lists.
        
        Returns:
            List[List[int]]: A list containing 9 lists, each representing a row of the Sudoku grid.
        """
        return numpy.split(self.grid, 9);
    
    def get_cols(self) -> List[List[int]]:
        """
        Returns the columns of the Sudoku grid as a list of lists.
        
        Returns:
            List[List[int]]: A list containing 9 lists, each representing a column of the Sudoku grid.
        """
        return numpy.split(self.grid.T, 9);
    
    def get_squares(self) -> List[List[int]]:
        """
        Returns the squares of the Sudoku grid as a list of lists.
        
        Returns:
            List[List[int]]: A list containing 9 lists, each representing a square of the Sudoku grid.
        """
        return [
            [self.grid[x:x+3, y:y+3].flatten() for y in range(0, 9, 3) for x in range(0, 9, 3)]]
        
    
    def __str__(self):
        return str(self.grid) + str(-self.utility);
    
    @staticmethod
    def fromArray(grid: numpy.array) -> "Board":
        """
        Creates a Board object from a 9x9 numpy array.
        
        Parameters:
            grid (np.ndarray): A 9x9 numpy array representing the Sudoku grid.
            
        Returns:
            Board: A Board object.
        """
        return Board(grid);
    
    @staticmethod
    def fromString(grid: str) -> "Board":
        """
        Creates a Board object from a string representation of the Sudoku grid.
        
        Parameters:
            grid (str): A string representing the Sudoku grid.
            
        Returns:
            Board: A Board object.
        """
        #   Guess the separator
        separator : str = "";
        separators : List[str] = [",", ";", " ", "\t", "\n"];
        for sep in separators:
            if sep in grid:
                separator = sep;
                break;
        
        #   Convert the string to a numpy array
        grid = [[ int(x) for x in line.split(separator) ] for line in grid.split("\n") ]
        
        return Board(numpy.array(grid));
    
    
    def set_value(self, x: int, y: int, value: int) -> None:
        """
        Sets the value at a specific position in the Sudoku grid.
        
        Parameters:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
            value (int): The value to be set.
        """
        if x < 0 or x > 8 or y < 0 or y > 8:
            raise ValueError("Invalid position.");
        if value < 0 or value > 9:
            raise ValueError("Invalid value.");
        
        self.grid[x][y] = value;
        utility = self.eval(self.grid);
        self.utility = utility;
        
    def copy(self) -> "Board":
        return Board(self.grid.copy());


    

