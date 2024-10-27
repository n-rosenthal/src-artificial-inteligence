"""Maximizes the value of the Validator function for the 3-Sudoku game."""
from Validator import Validator;
import numpy as np
import torch;

"""Example of a valid 3-Sudoku grid."""
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

EXAMPLE_SUDOKU:np.array = np.array([
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

"""A complete 9x9 Sudoku grid."""
VALID_SUDOKU_COMPLETED:np.array = [
    np.array([5, 3, 4, 6, 7, 8, 9, 1, 2]),
    np.array([6, 7, 2, 1, 9, 5, 3, 4, 8]),
    np.array([1, 9, 8, 3, 4, 2, 5, 6, 7]),
    np.array([8, 5, 9, 7, 6, 1, 4, 2, 3]),
    np.array([4, 2, 6, 8, 5, 3, 7, 9, 1]),
    np.array([7, 1, 3, 9, 2, 4, 8, 5, 6]),
    np.array([9, 6, 1, 5, 3, 7, 2, 8, 4]),
    np.array([2, 8, 7, 4, 1, 9, 6, 3, 5]),
    np.array([3, 4, 5, 2, 8, 6, 1, 7, 9])];

def getValue(grid: np.array) -> int:
    """Returns the value of the grid."""
    validator = Validator(grid);
    validator();
    return validator.value;

def getLenEmptyPositions(grid: np.array) -> int:
    """Returns the number of empty positions in the grid."""
    validator = Validator(grid);
    validator();
    return len(validator.empty_positions);


class Sudoku:
    import numpy as np;

    def __init__(self, grid: np.array):
        """
        Initializes the SudokuSolver object.
        
        Parameters:
            grid (np.ndarray): A 9x9 numpy array representing the Sudoku grid.
        """
        self.grid = grid;


    def __call__(self):
        validator = Validator(self.grid);
        validator();
        return validator.value;
    
    def makeMove(self, x: int, y: int, value: int):
        self.grid[x][y] = value;
        
    def __str__(self):
        return str(self.grid);
    
    def __repr__(self):
        return str(self.grid);
    
class NeuralNetworkSudoku:
    """Uses torch neural networks to solve the Sudoku."""
    import numpy as np;
    import torch;
    
    def __init__(self, grid: np.array):
        """
        Initializes the SudokuSolver object.
        
        Parameters:
            grid (np.ndarray): A 9x9 numpy array representing the Sudoku grid.
        """
        self.grid = grid;
        try:
            self.model = torch.load("sudoku.pt");
        except Exception as e:
            print(e);
            self.model = torch.nn.Sequential(
                torch.nn.Linear(9, 64),
                torch.nn.ReLU(),
                torch.nn.Linear(64, 64),
                torch.nn.ReLU(),
                torch.nn.Linear(64, 9)
            );
            torch.save(self.model, "sudoku.pt");
            
    def __call__(self):
        return self.solve();
        
        
    def solve(self):
        """Solves the Sudoku using a neural network."""
        sudoku = Sudoku(self.grid.copy());
        
        #   maximize the Sudoku() function
        #   minimize the number of empty positions
        
        #   Example
        value = Sudoku(VALID_SUDOKU_COMPLETED)();
        
        #   Example
        npos = getLenEmptyPositions(VALID_SUDOKU_COMPLETED);
        
        #   Example
        #   0.5*(value - 81) + 0.5*npos
        #   0.5*(81 - 81) + 0.5*npos
        #   0 + 0.5*npos
        #   0.5*npos
        
    def train(self):
        
        
        
        return sudoku;
        
        
    
if __name__ == "__main__":
    print(f"Kendra: {getValue(SUDOKU_DA_KENDRA)} npos: {getLenEmptyPositions(SUDOKU_DA_KENDRA)}");
    print(f"Example: {getValue(EXAMPLE_SUDOKU)} npos: {getLenEmptyPositions(EXAMPLE_SUDOKU)}");
    
    nns = NeuralNetworkSudoku(SUDOKU_DA_KENDRA);
    print(nns.solve());