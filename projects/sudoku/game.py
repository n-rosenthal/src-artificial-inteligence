"""Define the necessary classes for representing Sudoku games."""

import numpy as np;
import random;
from Validator import Validator;
from listfun import swap, sremove, sremove_empty, snum_constraints, sconstraints, dist;

class Sudoku:
    """A Sudoku grid is a 9x9 grid of numbers."""
    def __init__(self, grid: np.array):
        self.grid   = grid;
        self.value  = self._getValue();
        
    def _getValue(self) -> int:
        """
        Returns the value of the Sudoku grid according to the Validator function.
        
        Returns:
            int: The value of the Sudoku grid.
        """
        validator = Validator(self.grid);
        return validator.value;
    
    def move(self, position: tuple[int, int], value: int) -> None:
        """
        Updates the Sudoku grid with the given position and value.
        
        Args:
            position (tuple[int, int]): The position to update.
            value (int): The value to update with.
        """
        self.grid[position[0]][position[1]] = value;
        self.value = self._getValue();
        
    def __str__(self) -> str:
        return str(self.grid);
    
    def __repr__(self) -> str:
        return str(self.grid);
    
    def __call__(self) -> int:
        return self.value;

    @property
    def empty_positions(self) -> list[tuple[int, int]]:
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    yield (i, j);
        return [];

ITER:int = 0;

def solve(sudoku: Sudoku) -> Sudoku:
    """Solves the Sudoku using heuristics."""
    #   If is already solved, returns itself.
    if(sudoku() == 81):
        return sudoku;
    
    #   Get all empty positions.
    empty_positions = Validator(sudoku.grid).empty_positions;
    
    #   Get a random empty position.
    position = random.choice(empty_positions);
    
    #   Get all valid values for the empty position.
    valid_values = Validator(sudoku.grid).getValidValues(position[0][0], position[0][1]);
    
    #   Get a random valid value.
    value = random.choice(valid_values);
    
    #   Update the Sudoku grid with the valid value.
    sudoku.move(position[0], value);
    
    ITER += 1;
    print(f"Iteration: {ITER}");
    
    #   Recursively solve the Sudoku.
    return solve(sudoku);

if __name__ == "__main__":
    SUDOKU_DA_KENDRA:np.array = np.array([
        np.array([0,4,0,0,0,2,0,1,0]),
        np.array([0,0,0,8,3,0,0,9,0]),
        np.array([6,0,0,0,4,0,8,0,0]),
        np.array([8,2,0,0,0,0,4,6,9]),
        np.array([0,5,0,0,9,0,0,8,0]),
        np.array([1,0,9,0,0,0,0,0,5]),
        np.array([3,8,0,0,0,5,0,0,6]),
        np.array([0,0,0,7,6,0,0,5,0]),
        np.array([5,1,0,0,0,0,0,4,0])
    ]);
    
    sudoku = Sudoku(SUDOKU_DA_KENDRA);
    solution = solve(sudoku);
    print(solution());