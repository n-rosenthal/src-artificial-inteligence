"""
Defines a gamestate class for the 3-Sudoku game.
"""

from .board import SudokuBoard as Board, SudokuPosition as Position, SEvaluator as Evaluator, SSplitter as Splitter, SBoardUtils as SudokuUtils, ColoredSudokuBoard as ColoredBoard;
from typing import List, Dict, Annotated, TypeVar, Optional, Tuple, Set, Counter;
import numpy;

class GameState:
    """
    Defines a gamestate class for the 3-Sudoku game.
    """
    def __init__(self, board: Board, parent: "GameState" = None) -> None:
        if board is None:
            raise ValueError("Board cannot be None.");
        
        self.board      : Board = board;
        self.utility    : int = Evaluator.eval_board(board);
        self.parent     : GameState = parent;
        self.children   : List[GameState] = [];

        if parent is not None:
            parent.children.append(self);
        
    def next_state(self, position: Position, value: int) -> Optional["GameState"]:
        new_board = self.board.copy();
        new_board.set_value(position.x, position.y, value);
        return GameState(new_board, self);
    
    def __repr__(self) -> str:
        return f"GameState({self.board})";
    
    def __str__(self) -> str:
        return f"GameState({self.board})";
    
    def __hash__(self) -> int:
        return hash(self.board);
    
    def __eq__(self, other) -> bool:
        return self.board == other.board