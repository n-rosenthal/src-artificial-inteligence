"""
Defines the class necessary to represent a Sudoku board.
"""

import copy;
from typing import List, Dict, Annotated, TypeVar, Optional, Tuple, Set, Counter, Any;
from math import sqrt;
import numpy;

class Board:
    def __init__(self, grid: List[List[int]]) -> None:
        """
        Initializes the Board object.
        
        Parameters:
            grid (np.ndarray): A 9x9 numpy array representing the Sudoku grid.
        """
        
        self.grid               : List[List[int]]       = grid;
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
        return self.grid;
    
    def get_cols(self) -> List[List[int]]:
        """
        Returns the columns of the Sudoku grid as a list of lists.
        
        Returns:
            List[List[int]]: A list containing 9 lists, each representing a column of the Sudoku grid.
        """
        return [x for x in numpy.transpose(self.grid)];
    
    def get_squares(self) -> List[List[int]]:
        """
        Returns the squares of the Sudoku grid as a list of lists.
        
        Returns:
            List[List[int]]: A list containing 9 lists, each representing a square of the Sudoku grid.
        """
        squares : List[List[int]] = [];
        for i in range(3):
            for j in range(3):
                square = [];
                for k in range(3):
                    for l in range(3):
                        square.append(self.grid[i*3+k][j*3+l]);
                squares.append(square);
        return squares;
    
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
        
        return Board(grid);
    
    @staticmethod
    def fromFile(filepath: str) -> "Board":
        try:
            with open(filepath, "r") as f:
                return Board.fromString(f.read());
        except Exception as e:
            raise e;
    
    def get_lines(self, position: Tuple[int, int]) -> List[List[int]]:
        """
        Given a `position`, returns the row, column and square of the Sudoku grid corresponding to the position.
        
        Parameters:
            position (Tuple[int, int]): The position to be checked.
            
        Returns:
            Tuple[List[int], List[int], List[int]]: A tuple containing the row, column and square of the Sudoku grid corresponding to the position.
        """
        row, col, square = self.get_rows()[position[0]], self.get_cols()[position[1]], self.get_squares()[position[0]//3][position[1]//3];
        return row, col, square;
    
    
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


class Position:
    """
    A `Position` is a 2-uple of integers that abid certain properties.
    
    Attributes:
        x (int): The x-coordinate of the position.
        y (int): The y-coordinate of the position.
        value (int): The value of the position
    """
    def __init__(self, x: int, y: int, value: Any = None) -> None:
        """
        Creates a `Position` object.
        
        Parameters:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
            value (int): The value of the position
        """
        self.x : int = x;
        self.y : int = y;
        self.value : Any = value;
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.value})";
    
    def __repr__(self) -> str:
        return f"Position({self.x}, {self.y}, {self.value})";
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y;
    
    def __lt__(self, other) -> bool:
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2) < sqrt((self.x - other.x)**2 + (self.y - other.y)**2);
    
    def __gt__(self, other) -> bool:
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2) > sqrt((self.x - other.x)**2 + (self.y - other.y)**2);
    
    def __le__(self, other) -> bool:
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2) <= sqrt((self.x - other.x)**2 + (self.y - other.y)**2);
    
    def __ge__(self, other) -> bool:
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2) >= sqrt((self.x - other.x)**2 + (self.y - other.y)**2);
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.value));
    
    def __call__(self) -> Tuple[int, int, Any]:
        return self.x, self.y, self.value;
    
    #   Properties
    @property
    def MAX(self) -> Any:
        return float("inf");
    
    @property
    def MIN(self) -> Any:
        return -float("inf");

class SudokuPosition(Position):
    def __init__(self, x: int, y: int, value: Any = None) -> None:
        if x < self.MIN or x > self.MAX or y < self.MIN or y > self.MAX:
            raise ValueError(f"(x={x}, y={y}) : Invalid position: out of bounds.");
        elif value is not None and (value < self.MIN or value > self.MAX):
            raise ValueError(f"(value={value}) : Invalid value: out of bounds.");
        super().__init__(x, y, value);
        
    @property
    def MAX(self) -> Any:
        return 9;
    
    @property
    def MIN(self) -> Any:
        return 0;

    @staticmethod
    def EmptySudokuPosition(x: int, y: int) -> "SudokuPosition":
        return SudokuPosition(x, y, None);
    
    def __str__(self) -> str:
        return str(self.value);

from colorama import init as colorama_init;
from colorama import Fore, Back, Style;

class ColoredSudokuPosition(SudokuPosition):
    def __init__(self, x: int, y: int, value: Any = None, color: Any = Fore.RESET) -> None:
        super().__init__(x, y, value);
        self.color : Any = color;
        
    def __str__(self) -> str:
        return f"{self.color}{str(self.value)}{Style.RESET_ALL}";

class SudokuBoard:
    @property
    def txt_separator(self) -> str:
        return ",";
    
    def __init__(self) -> None:
        self.grid       : List[List[SudokuPosition]] = [[SudokuPosition.EmptySudokuPosition(i, j) for j in range(9)] for i in range(9)];
        self.utility    : int = -81;

    @staticmethod
    def fromFile(filepath: str) -> "SudokuBoard":
        """
        Creates a SudokuBoard object from a file containing a Sudoku grid string.

        Parameters:
            filepath (str): The path to the file containing the Sudoku grid string.

        Returns:
            SudokuBoard: The SudokuBoard object created from the Sudoku grid string.

        Raises:
            Exception: If there is an error reading the file.
        """
        try:
            with open(filepath, "r") as f:
                return SudokuBoard.fromString(f.read());
        except Exception as e:
            print(e);
    
    @staticmethod
    def fromString(grid: str) -> "SudokuBoard":
        """
        Creates a SudokuBoard object from a string representation of the Sudoku grid.

        Parameters:
            grid (str): A string representing the Sudoku grid where each line corresponds
                        to a row and values are separated by spaces.

        Returns:
            SudokuBoard: A SudokuBoard object initialized with the given grid string.

        Raises:
            ValueError: If any of the grid values are not integers or are out of bounds.
        """
        s : SudokuBoard = SudokuBoard();
        s_lines = grid.split("\n");
        if len(s_lines) != 9:
            raise ValueError(f"(height={len(s_lines)}) : Invalid grid height; must be 9.");
        
        for i, line in enumerate(s_lines):
            if len(line.split(s.txt_separator)) != 9:
                raise ValueError(f"(width={len(line.split(s.txt_separator))}) : Invalid grid width; must be 9.");
            s.grid[i] = [SudokuPosition(i, j, int(x)) for j, x in enumerate(line.split(s.txt_separator))];
            
        s.utility = -SEvaluator.eval_board(s);
        return s;
        
    @staticmethod
    def fromList(grid: List[List[int]]) -> "SudokuBoard":
        """
        Creates a SudokuBoard object from a 2D list representation of the Sudoku grid.

        Parameters:
            grid (List[List[int]]): A 2D list representing the Sudoku grid where each sublist
                                    corresponds to a row containing integer values.

        Returns:
            SudokuBoard: A SudokuBoard object initialized with the given grid list.
        """
        s : SudokuBoard = SudokuBoard();
        s.grid = [[SudokuPosition(i, j, x) for j, x in enumerate(row)] for i, row in enumerate(grid)];
        s.utility = -s.eval(s.grid);
        return s;

    def get_value(self, x: int, y: int) -> int:
        return self.grid[x][y].value;
    
    def set_value(self, x: int, y: int, value: int) -> None:
        self.grid[x][y] = SudokuPosition(x, y, value);
        self.utility = -SEvaluator.eval_board(self);
        
    def copy(self) -> "SudokuBoard":
        sb : SudokuBoard = SudokuBoard();
        for i in range(9):
            for j in range(9):
                sb.grid[i][j] = self.grid[i][j];
        sb.utility = self.utility;
        return sb;
        
    def __str__(self) -> str:
        return "\n".join([" ".join([str(x.value) for x in row]) for row in self.grid]);
    
    def __repr__(self) -> str:
        return str(self.grid);
    
    def __eq__(self, other) -> bool:
        return self.grid == other.grid;


    @property
    def rows(self) -> List[List[SudokuPosition]]:
        return SSplitter.get_rows(self);
    
    @property
    def cols(self) -> List[List[SudokuPosition]]:
        return SSplitter.get_cols(self);
    
    @property
    def squares(self) -> List[List[SudokuPosition]]:
        return SSplitter.get_squares(self);
    
    def __dict__(self):
        return {
            i : [x.value for x in row] for i, row in enumerate(self.grid)
        } + {
            "utility"           : SEvaluator.eval_board(self),
            "empty_positions"   : len(SSplitter.get_empty_positions(self)),
        }

from random import randint;

class ColoredSudokuBoard(SudokuBoard):
    @property
    def txt_separator(self) -> str:
        return " ";
    
    def __str__(self) -> str:
        return "\n".join([" ".join([str(x) for x in row]) for row in self.grid]);
    
    def __repr__(self) -> str:
        return str(self.grid);
    
    def __init__(self, grid: List[List[ColoredSudokuPosition]] | None = None) -> None:
        self.grid : List[List[ColoredSudokuPosition]] = [[ColoredSudokuPosition(x=_, y=_, value=randint(1, 9)) for _ in range(9)] for _ in range(9)];
        if grid is None:
           self.grid = [[ColoredSudokuPosition(x=_, y=_, value=randint(1, 9)) for _ in range(9)] for _ in range(9)];
        else:
            for i in range(9):
                for j in range(9):
                    self.grid[i][j] = ColoredSudokuPosition(i, j, grid[i][j].value, grid[i][j].color);
    
    @staticmethod
    def fromSudokuBoard(board: SudokuBoard) -> "ColoredSudokuBoard":
        return ColoredSudokuBoard([[ColoredSudokuPosition(x=i, 
                                                          y=j, 
                                                          value=board.grid[i][j].value,
                                                          color=SEvaluator.get_color(board.grid[i][j], board)) for j in range(9)] for i in range(9)]);
                    
        

class SSplitter:
    """
    Defines methods for obtaining the rows, columns and squares of a Sudoku board.
    """
    @staticmethod
    def get_rows(board: SudokuBoard) -> List[List[SudokuPosition]]:
        """
        Returns the rows of the Sudoku board as a list of lists.
        
        Returns:
            List[List[SudokuPosition]]: A list containing 9 lists, each representing a row of the Sudoku board.
        """
        return board.grid;
        
    @staticmethod
    def get_cols(board: SudokuBoard) -> List[List[SudokuPosition]]:
        """
        Returns the columns of the Sudoku board as a list of lists.
        
        Returns:
            List[List[SudokuPosition]]: A list containing 9 lists, each representing a column of the Sudoku board.
        """
        return [x for x in numpy.transpose(board.grid)];
        
    @staticmethod
    def get_squares(board: SudokuBoard) -> List[List[SudokuPosition]]:
        """
        Returns the squares of the Sudoku board as a list of lists.
        
        Returns:
            List[List[SudokuPosition]]: A list containing 9 lists, each representing a square of the Sudoku board.
        """
        return [board.grid[i][j:j+3] for i in range(0, 9, 3) for j in range(0, 9, 3)];
        
    @staticmethod
    def get_empty_positions(board: SudokuBoard) -> List[Tuple[int, int]]:
        """
        Returns a list of empty positions in the Sudoku board.

        Parameters:
            board (SudokuBoard): The Sudoku board to be checked.

        Returns:
            List[Tuple[int, int]]: A list of tuples representing the empty positions
            in the board where the value is zero.
        """
        return [(i, j) for i in range(9) for j in range(9) if board.grid[i][j].value == 0];
    
    @staticmethod
    def row(board: SudokuBoard, position: Tuple[int, int]) -> List[SudokuPosition]:
        return board.grid[position[0]];
    
    @staticmethod
    def col(board: SudokuBoard, position: Tuple[int, int]) -> List[SudokuPosition]:
        return [board.grid[i][position[1]] for i in range(9)];
    
    @staticmethod
    def square(board: SudokuBoard, position: Tuple[int, int]) -> List[SudokuPosition]:
        return SSplitter.get_squares(board)[SEvaluator.which_square(position[0], position[1])];      


class SEvaluator:
    @staticmethod
    def eval_line(line: List[SudokuPosition]) -> int:
        """
        Evaluates a line of Sudoku positions.

        Parameters:
            line (List[SudokuPosition]): A list of Sudoku positions representing a line.

        Returns:
            int: The number of invalid positions in the line. An invalid position is one
            where its value is not unique in the line. The number is subtracted from 9 to
            normalize the evaluation, so that a line with 9 unique values has a value of
            0 and a line with all values equal has a value of -9.
        """
        return len(set([x.value for x in line if x.value != 0])) - 9;
    
    @staticmethod
    def eval_board(board: List[List[SudokuPosition]]) -> int:
        """
        Evaluates a Sudoku board.

        Parameters:
            board (List[List[SudokuPosition]]): A 2D list of Sudoku positions representing the board.

        Returns:
            int: The total number of invalid positions in the board. An invalid position is one
            where its value is not unique in its row, column or square. The number is normalized
            so that a board with 9 unique values has a value of 0 and a board with all values equal
            has a value of -81.
        """
        return sum([SEvaluator.eval_line(row) for row in board.rows] + \
                   [SEvaluator.eval_line(col) for col in board.cols] + \
                   [SEvaluator.eval_line(square) for square in board.squares]);
        
    def check_line(line: List[SudokuPosition], index: int) -> bool:
        """
        Checks if the value pointed by `index` is anywhere else in the line.

        Parameters:
            line (List[SudokuPosition]): A list of Sudoku positions representing a line.
            index (int): The index of the position to be checked.

        Returns:
            bool: True if the value pointed by `index` is not unique in the line, False otherwise.
        """
        return len([x for x in line if x == line[index].value]) > 1;
    
    @staticmethod
    def get_constraints(board: SudokuBoard, position: Tuple[int, int]) -> Set[int]:
        """
        Returns a set of values that are not allowed for a given position on the Sudoku board.

        Parameters:
            board (SudokuBoard): The Sudoku board to be checked.
            position (Tuple[int, int]): The position on the board to be checked.

        Returns:
            Set[int]: A set of values that are not allowed for the given position.

        """
        return set([x.value for x in SSplitter.row(board, position) + SSplitter.col(board, position) + SSplitter.square(board, position)]);
    
    @staticmethod
    def possible_values(board: SudokuBoard, position: Tuple[int, int]) -> List[int]:
        """
        Returns a list of values that are possible for a given position on the Sudoku board.

        Parameters:
            board (SudokuBoard): The Sudoku board to be checked.
            position (Tuple[int, int]): The position on the board to be checked.

        Returns:
            List[int]: A list of values that are possible for the given position.
        """
        if board.grid[position[0]][position[1]].value != 0:
            return [];
        return [x for x in range(1, 10) if x not in SSplitter.get_constraints(board, position)];
    
    @staticmethod
    def which_square(x: int, y: int) -> int:
        """
        Returns the number of the square that the given position belongs to.
        
        A Sudoku board is divided into 9 squares, each containing 3x3 positions.
        The squares are numbered from 0 to 8, row by row from top to bottom and
        from left to right.
        
        Parameters:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
        
        Returns:
            int: The number of the square that the given position belongs to.
        """
        return (x // 3) * 3 + (y // 3);
    
    @staticmethod
    def get_squares(board: SudokuBoard) -> List[List[SudokuPosition]]:
        """
        Returns a list of lists of Sudoku positions representing the squares of a Sudoku board.
        
        A Sudoku board is divided into 9 squares, each containing 3x3 positions.
        The squares are numbered from 0 to 8, row by row from top to bottom and
        from left to right.
        
        Parameters:
            board (SudokuBoard): The Sudoku board to be checked.
        
        Returns:
            List[List[SudokuPosition]]: A list of lists of Sudoku positions representing the squares of the board.
        """
        return [[board.grid[x][y] for y in range(9)] for x in range(9)];
    
    @staticmethod
    def legal_moves(board: SudokuBoard) -> Set[SudokuPosition]:
        """
        Returns a set of all legal moves in a Sudoku board.
        
        A legal move is a position on the board where the value is 0 and the value is not already constrained by the row, column or square.
        
        Parameters:
            board (SudokuBoard): The Sudoku board to be checked.
        
        Returns:
            Set[SudokuPosition]: A set of all legal moves in the board.
        """
        legal_moves = set();
        for empty_pos in SSplitter.get_empty_positions(board):
            if board.grid[empty_pos[0]][empty_pos[1]].value == 0:
                for value in set(range(1, 10)) - SEvaluator.get_constraints(board, empty_pos):
                    legal_moves.add(SudokuPosition(empty_pos[0], empty_pos[1], value));
        return legal_moves;
    
    @staticmethod
    def constraintness(move: SudokuPosition, board: SudokuBoard) -> int:
        """
        Calculates the number of constraints for a given move on the Sudoku board.

        Parameters:
            move (SudokuPosition): The move for which to calculate the constraints.

        Returns:
            int: The number of values that are not allowed for the given move.
        """
        return len(SSplitter.get_constraints(board, move));
    
    @staticmethod
    def csorted_legal_moves(board: SudokuBoard) -> List[SudokuPosition]:
        """
        Returns a list of all legal moves in a Sudoku board, sorted by the number of constraints for each move.
        
        A legal move is a position on the board where the value is 0 and the value is not already constrained by the row, column or square.
        
        Parameters:
            board (SudokuBoard): The Sudoku board to be checked.
        
        Returns:
            List[SudokuPosition]: A list of all legal moves in the board, sorted by the number of constraints for each move.
        """
        return sorted(SEvaluator.legal_moves(board), key=lambda x: SEvaluator.constraintness(x, board), reverse=True);
    
    @staticmethod
    def is_solved(board: SudokuBoard) -> bool:
        """
        Checks if a Sudoku board is solved.
        
        Parameters:
            board (SudokuBoard): The Sudoku board to be checked.
        
        Returns:
            bool: True if the board is solved, False otherwise.
        """
        return SEvaluator.eval_board(board) == 0;

    @staticmethod
    def lvalues(positions: List[SudokuPosition]) -> List[int]:
        return [x.value for x in positions];

    @staticmethod
    def get_color(position: SudokuPosition, board: SudokuBoard) -> Any:
        """
        Returns the color of a position in a Sudoku board.
        
        Parameters:
            position (SudokuPosition): The position to be checked.
            board (SudokuBoard): The Sudoku board to be checked.
        
        Returns:
            Any: The color of the position.
        """
        if board.grid[position.x][position.y].value == 0:
            return Fore.WHITE;
        else:
            #   check row for same value
            row = SEvaluator.lvalues(SSplitter.row(board, (position.x, position.y)));
            if SEvaluator.check_line(row, position.y) > 0:
                return Fore.RED;
            else:
                return Fore.GREEN;

class SBoardUtils:
    @staticmethod
    def print_evaluation(board: SudokuBoard) -> None:
        evaluation: str = f"""
                1  2  3      4  5  6      7  8  9
                
            
        1       {board.grid[0][0]}  {board.grid[0][1]}  {board.grid[0][2]}      {board.grid[0][3]}  {board.grid[0][4]}  {board.grid[0][5]}      {board.grid[0][6]}  {board.grid[0][7]}  {board.grid[0][8]}      {SEvaluator.eval_line(board.grid[0])}       utility={SEvaluator.eval_board(board)}
        2       {board.grid[1][0]}  {board.grid[1][1]}  {board.grid[1][2]}      {board.grid[1][3]}  {board.grid[1][4]}  {board.grid[1][5]}      {board.grid[1][6]}  {board.grid[1][7]}  {board.grid[1][8]}      {SEvaluator.eval_line(board.grid[1])}       empty positions={len(SSplitter.get_empty_positions(board))}
        3       {board.grid[2][0]}  {board.grid[2][1]}  {board.grid[2][2]}      {board.grid[2][3]}  {board.grid[2][4]}  {board.grid[2][5]}      {board.grid[2][6]}  {board.grid[2][7]}  {board.grid[2][8]}      {SEvaluator.eval_line(board.grid[2])}
        
        4       {board.grid[3][0]}  {board.grid[3][1]}  {board.grid[3][2]}      {board.grid[3][3]}  {board.grid[3][4]}  {board.grid[3][5]}      {board.grid[3][6]}  {board.grid[3][7]}  {board.grid[3][8]}      {SEvaluator.eval_line(board.grid[3])}
        5       {board.grid[4][0]}  {board.grid[4][1]}  {board.grid[4][2]}      {board.grid[4][3]}  {board.grid[4][4]}  {board.grid[4][5]}      {board.grid[4][6]}  {board.grid[4][7]}  {board.grid[4][8]}      {SEvaluator.eval_line(board.grid[4])}
        6       {board.grid[5][0]}  {board.grid[5][1]}  {board.grid[5][2]}      {board.grid[5][3]}  {board.grid[5][4]}  {board.grid[5][5]}      {board.grid[5][6]}  {board.grid[5][7]}  {board.grid[5][8]}      {SEvaluator.eval_line(board.grid[5])}
        
        7       {board.grid[6][0]}  {board.grid[6][1]}  {board.grid[6][2]}      {board.grid[6][3]}  {board.grid[6][4]}  {board.grid[6][5]}      {board.grid[6][6]}  {board.grid[6][7]}  {board.grid[6][8]}      {SEvaluator.eval_line(board.grid[6])}
        8       {board.grid[7][0]}  {board.grid[7][1]}  {board.grid[7][2]}      {board.grid[7][3]}  {board.grid[7][4]}  {board.grid[7][5]}      {board.grid[7][6]}  {board.grid[7][7]}  {board.grid[7][8]}      {SEvaluator.eval_line(board.grid[7])}
        9       {board.grid[8][0]}  {board.grid[8][1]}  {board.grid[8][2]}      {board.grid[8][3]}  {board.grid[8][4]}  {board.grid[8][5]}      {board.grid[8][6]}  {board.grid[8][7]}  {board.grid[8][8]}      {SEvaluator.eval_line(board.grid[8])}
        
                {SEvaluator.eval_line(numpy.transpose(board.grid)[0])}  {SEvaluator.eval_line(numpy.transpose(board.grid)[1])}  {SEvaluator.eval_line(numpy.transpose(board.grid)[2])}      {SEvaluator.eval_line(numpy.transpose(board.grid)[3])}  {SEvaluator.eval_line(numpy.transpose(board.grid)[4])}  {SEvaluator.eval_line(numpy.transpose(board.grid)[5])}      {SEvaluator.eval_line(numpy.transpose(board.grid)[6])}  {SEvaluator.eval_line(numpy.transpose(board.grid)[7])}  {SEvaluator.eval_line(numpy.transpose(board.grid)[8])}
        """
        print(evaluation);
        
    @staticmethod
    def print_board(board: Board) -> None:
        print("     1 2 3 4 5 6 7 8 9", end="\n\n");
        for i in range(9):
            print(f"{i + 1}", end="    ");
            print(" ".join(map(str, board.grid[i])), end="   ");
            print(f"{SEvaluator.eval_line(board.grid[i])}", end="  ");
            
            match i:
                case 0:
                    print(f"utility : {SEvaluator.eval_board(board)}", end="");
                case 2:
                    print(f"empty positions : {len(SSplitter.get_empty_positions(board))}", end="");
                case 3:
                    print(f"invalid positions : * * *", end="");
                case 6:
                    for i in range(0, 3):
                        print(f"{SEvaluator.eval_line(SEvaluator.get_squares(board)[i])}", end=" ");
                case 7:
                    for i in range(3, 6):
                        print(f"{SEvaluator.eval_line(SEvaluator.get_squares(board)[i])}", end=" ");
                case 8:
                    for i in range(6, 9):
                        print(f"{SEvaluator.eval_line(SEvaluator.get_squares(board)[i])}", end=" ");
                        
            print("");
            
        
