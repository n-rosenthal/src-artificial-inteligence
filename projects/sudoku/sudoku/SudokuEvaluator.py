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