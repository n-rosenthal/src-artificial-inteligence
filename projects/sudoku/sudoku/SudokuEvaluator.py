"""
Implements methods for evaluating the components and the board of the 3-Sudoku game.

@author     rdcn
@version    1.1
@since      1.1
@date       2025-01-19
@see        `.board.SudokuBoard`
@see        `.gamestate.GameState`
"""

from sudoku.SudokuSplitter import Splitter, Board as Board, Position as Position;
from typing import List, Dict, Annotated, TypeVar, Optional, Tuple, Set, Counter, Any;

class Evaluator:
    """
    Implements static methods for evaluating the components and the board of the 3-Sudoku game.
    """
    def __init__(self) -> None:
        pass;
    
    @staticmethod
    def eval_line(line: List[Position]) -> int:
        """
        Evaluates a line of Sudoku positions.

        Parameters:
            line (List[Position]): A list of Sudoku positions representing a line.

        Returns:
            int: The number of invalid positions in the line. An invalid position is one
            where its value is not unique in the line. The number is subtracted from 9 to
            normalize the evaluation, so that a line with 9 unique values has a value of
            0 and a line with all values equal has a value of -9.
        """
        return len(set([x.value for x in line if x.value != 0])) - 9;
    
    @staticmethod
    def eval_lines(lines: List[List[Position]]) -> int:
        """
        Evaluates a list of lines of Sudoku positions. Useful for when analyzing all the rows, all the columns and all the squares of a board.

        Parameters:
            lines (List[List[Position]]): A 2D list of Sudoku positions representing the lines.

        Returns:
            int: The total number of invalid positions in the lines. An invalid position is one 
            where its value is not unique in its row, column or square. The number is normalized
            so that a board with 9 unique values has a value of 0 and a board with all values equal
            has a value of -81.
        """
        return sum([Evaluator.eval_line(line) for line in lines]);
    
    @staticmethod
    def eval_board(board: Board) -> int:
        """
        Evaluates a Sudoku board.

        Parameters:
            board (Board): A 2D list of Sudoku positions representing the board.

        Returns:
            int: The total number of invalid positions in the board. An invalid position is one
            where its value is not unique in its row, column or square. The number is normalized
            so that a board with 9 unique values has a value of 0 and a board with all values equal
            has a value of -81.
        """
        return Evaluator.eval_lines(Splitter.get_rows(board)) + Evaluator.eval_lines(Splitter.get_cols(board)) + Evaluator.eval_lines(Splitter.get_squares(board));
           
    @staticmethod
    def evaluate(board: Board) -> Dict[str, List[Tuple[int, int]]]:
        """
        Evaluates a Sudoku board and returns a dictionary of the evaluation results.

        Parameters:
            board (Board): A 2D list of Sudoku positions representing the board.

        Returns:
            Dict[str, List[Tuple[str, int]]]: A dictionary of the evaluation results of the 3-Sudoku game.
        """
        return {
            "rows": [(i, Evaluator.eval_line(Splitter.get_row(board, i))) for i in range(9)],
            "cols": [(i, Evaluator.eval_line(Splitter.get_col(board, i))) for i in range(9)],
            "squares": [(i, Evaluator.eval_line(Splitter.get_square(board, i))) for i in range(9)],
            "board": Evaluator.eval_board(board),
            "empty_pos" : len(Splitter.get_empty_positions(board)),
            "initial_values" : len(Splitter.get_initial_values(board)),
            "is_solved" : Evaluator.eval_board(board) == 0
        };
        
class ConstraintsFinder:
    """
    Static methods for finding, counting and presenting constraints for positions in a Sudoku board.
    
    Methods:
    --------
        get_constraints(board: Board, position: Tuple[int, int]) -> Set[int]
            Given an empty position in the board, returns a set of values that cannot be in that position.
        get_constraints(positions: List[Tuple[int, int]]) -> Dict[Tuple[int, int], Set[int]]
            Given a list of empty positions in the board, returns a dictionary of sets of values that cannot be in those positions.
        constraints_map(board: Board) -> List[List[int]]
            Given a Sudoku board, returns a matrix of constraints for each position in the board (0, if the position wasn't empty on `board`).
        get_most_constrained(board: Board) -> Tuple[Tuple[int, int], int]
            Given a Sudoku board, returns the position with the most constraints and its number of constraints
        constraints_sort(board: Board) -> List[Tuple[Tuple[int, int], int]]
            Given a Sudoku board, returns a list of tuples of positions and their number of constraints sorted by number of constraints in descending order
    
    Examples:
    --------
        Get the constraints for a specific position:
        >>> constraints = ConstraintsFinder.get_constraints(board, (0, 0));
        
        Get the constraints for all positions
        >>> all_constraints = ConstraintsFinder.get_constraints(board);
        
        Get a matrix of constraints for a given board
        >>> constraints_matrix = ConstraintsFinder.constraints_map(board);
        
        Get the most constrained position in a given board
        >>> position = ConstraintsFinder.get_most_constrained(board);
        
        Get the list of empty positions of a given board, sorted in descended order by number of constraints.
        >>> positions = ConstraintsFinder.constraints_sort(board);
        >>> positions == sorted(board.get_empty_positions(), lambda x: len(ConstraintsFinder.get_constraints(board, x)), reversed=True);
    """
    def __init__(self) -> None:
        """
        Empty builder for the ConstraintsFinder class. Initializes the ConstraintsFinder object.

        Does nothing, as the object contains only static methods and no instance variables are needed.
        """
        pass;
    
    @staticmethod
    def get_constraints(board: Board, position: Tuple[int, int] | Position | None) -> Set[int] | Dict[Tuple[int, int], Set[int]]:
        """
        Given an empty position in the board, returns a set of values that cannot be in that position.
        
        Parameters:
        -----------
            board (Board):
                A 2D list of Sudoku positions representing the board.
            position (Tuple[int, int] | Position | None):
                A tuple representing the position of the empty position in the board.

        Returns:
        --------
            Set[int], if position is a tuple
                A set of values that cannot be in the empty position in the board.
            Dict[Tuple[int, int], Set[int]], if position is None
                A dictionary of sets of values that cannot be in the empty positions in the board.
        """
        if position is None:
            empty_positions = Splitter.get_empty_positions(board);
            return {pos: ConstraintsFinder.get_constraints(board, pos) for pos in empty_positions};
        else:
            return set(range(1, 10)) - set(Splitter.get_row(board, position[0]) + Splitter.get_col(board, position[1]) + Splitter.get_square(board, position[0], position[1]));
        
    @staticmethod
    def constraints_map(board: Board) -> List[List[int]]:
        """
        Given a Sudoku board, returns a matrix of constraints for each position in the board (0, if the position wasn't empty on `board`).
        
        Parameters:
        -----------
            board (Board):
                Sudoku grid positions representing the board.

        Returns:
        --------
            List[List[int]]:
                A matrix of constraints for each position in the board.
        """
        return [[ConstraintsFinder.get_constraints(board, (i, j)) for j in range(9)] for i in range(9)];
        
    @staticmethod
    def get_most_constrained(board: Board) -> Tuple[Tuple[int, int], int]:
        """
        Given a Sudoku board, returns the position with the most constraints and its number of constraints.
        
        Parameters:
        -----------
            board (Board):
                A 2D list of Sudoku positions representing the board.

        Returns:
        --------
            Tuple[Tuple[int, int], int]:
                A tuple containing the position with the most constraints and its number of constraints.
        """
        return max(ConstraintsFinder.get_constraints(board).items(), key=lambda x: len(x[1]));
        
    @staticmethod
    def constraints_sort(board: Board) -> List[Tuple[Tuple[int, int], int]]:
        """
        Given a Sudoku board, returns a list of tuples of positions and their number of constraints sorted by number of constraints in descending order.
        
        Parameters:
        -----------
            board (Board):
                A 2D list of Sudoku positions representing the board.

        Returns:
        --------
            List[Tuple[Tuple[int, int], int]]:
                A list of tuples containing the positions and their number of constraints sorted by number of constraints in descending order.
        """
        return sorted(ConstraintsFinder.get_constraints(board).items(), key=lambda x: len(x[1]), reverse=True);
    
                    
                
        
    