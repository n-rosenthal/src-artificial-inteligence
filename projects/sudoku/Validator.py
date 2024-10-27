"""Implements an optimized validator for the 3-Sudoku game."""

import numpy as np;
import copy;
import random;

class Validator:
    """The Validator is responsible for
        - Validating the Sudoku grid
        - Finding invalid positions
        - Finding invalid values
    """
    
    __slots__ = ['grid','invalid_positions', 'empty_positions', 'value'];
    
    def __init__(self, grid: np.ndarray):
        """
        Initializes the Validator object.
        
        Parameters:
            grid (np.ndarray): A 9x9 numpy array representing the Sudoku grid.
        """
        self.grid = grid;
        self.invalid_positions:list[tuple[tuple[int,int], tuple[int,int]]] = [];
        self.empty_positions:list[tuple[int,int]] = [];
        self.value = 0;
        
        # Find empty positions
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.empty_positions.append(((i, j), (i, j)));
                    self.value = self.value - 1;
        
        # Compute values
        self.validate();
        self.invalid_positions = sorted(self.invalid_positions, key=lambda x: (x[0][0], x[0][1], x[1][0], x[1][1]));
        self.value = self.value -len(self.invalid_positions) + 81;
        
                    
    def validate(self) -> bool:
        """Validates the Sudoku grid."""
        return self._validate_rows() and self._validate_columns() and self._validate_boxes();
    
    def _validate_rows(self) -> bool:
        """Validates the rows of the Sudoku grid."""
        rtn = True;
        
        for i in range(9):
            curr_row = self.grid[i];
            
            for j in range(9):
                curr_value = curr_row[j];
                
                for k in range(j + 1, 9):
                    if curr_value == curr_row[k] and curr_value != 0:
                        self.invalid_positions.append(((i, j), (i, k)));
                        rtn = False;
        
        return rtn;
    
    def _validate_columns(self) -> bool:
        """Validates the columns of the Sudoku grid."""
        rtn = True;
        
        for i in range(9):
            curr_column = [self.grid[j][i] for j in range(9)];
            
            for j in range(9):
                curr_value = curr_column[j];
                
                for k in range(j + 1, 9):
                    if curr_value == curr_column[k] and curr_value != 0:
                        self.invalid_positions.append(((i, j), (k, i)));
                        rtn = False;
        
        return rtn;
    
    def _validate_boxes(self) -> bool:
        """Validates the boxes of the Sudoku grid."""
        rtn = True;
        
        for i in range(3):
            for j in range(3):
                curr_box = [self.grid[x][y] for x in range(i * 3, i * 3 + 3) for y in range(j * 3, j * 3 + 3)];
                
                for k in range(9):
                    curr_value = curr_box[k];
                    
                    for l in range(k + 1, 9):
                        if curr_value == curr_box[l] and curr_value != 0:
                            self.invalid_positions.append(((i * 3 + k // 3, j * 3 + k % 3), (i * 3 + l // 3, j * 3 + l % 3)));
                            rtn = False;
        
        return rtn;
    
    def __call__(self):
        return f"""
            Value: {self.value}
            Grid:\n {self.grid}
            Empty positions: {len(self.empty_positions)} \n {self.empty_positions}
            Invalid positions: {len(self.invalid_positions)} \n {self.invalid_positions}"""
    
def getValidSudoku() -> np.array:
    """Returns a valid 9x9 Sudoku grid."""
    grid = np.zeros((9, 9), dtype=int);
    for i in range(9):
        for j in range(9):
            grid[i][j] = random.randint(1, 9);
    return grid;

VALID_SUDOKU:np.array = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]];

VALID_SUDOKU_COMPLETED:np.array = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]];

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


if __name__ == "__main__":
    validator = Validator(SUDOKU_DA_KENDRA);
    print(validator())
    
    
    exit();
    #   Get the lowest possible value
    min:int = 1000;
    grid:np.array;
    
    
    for i in range(1000000):
        curr = Validator(getValidSudoku());
        curr();
        
        if curr.value < min:
            min = curr.value;
            grid = curr;
            
    print(grid());
    
    #   Get the highest possible value
    max:int = 0;
    
    for i in range(1000000):
        curr = Validator(getValidSudoku());
        curr();
        
        if curr.value > max:
            max = curr.value;
            grid = curr;
            
    print(grid());
    
    