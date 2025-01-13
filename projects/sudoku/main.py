from sudoku.board import Board;
from sudoku.gamestate import GameState;

class SudokuSolver:
    def __init__(self, board: Board) -> None:
        self.board = board;
        
    def solve(self) -> None:
        explored = set();
        queue = [GameState(self.board)];
        
        while self.board.empty_positions != []:
            state = queue.pop(0);
            explored.add(state);
            for position in state.legal_moves:
                for value in range(1, 10):
                    new_state = state.next_state(position, value);
                    if new_state is not None and new_state not in explored:
                        if new_state.board.empty_positions == []:
                            self.board = new_state.board;
                            return;
                        queue.append(new_state);
                        explored.add(new_state);
                        queue.sort(key=lambda x: x.cost);
                        queue.reverse();
                        
        for state in explored:
            if state.board.empty_positions == []:
                self.board = state.board;
                return;
            for position in state.legal_moves:
                for value in range(1, 10):
                    new_state = state.next_state(position, value);
                    if new_state is not None and new_state not in explored:
                        if new_state.board.empty_positions == []:
                            self.board = new_state.board;
                            return;
                        queue.append(new_state);
                        explored.add(new_state);
                        queue.sort(key=lambda x: x.cost);
                        queue.reverse();
                        break;
                    else:
                        break;
                else:
                    continue;
                break;
            else:
                continue;
            break;
        else:
            for state in queue:
                if state.board.empty_positions == []:
                    self.board = state.board;
                    return;
                for position in state.legal_moves:
                    for value in range(1, 10):
                        new_state = state.next_state(position, value);
                        if new_state is not None and new_state not in explored:
                            if new_state.board.empty_positions == []:
                                self.board = new_state.board;
                                return;
                            queue.append(new_state);
                            explored.add(new_state);
                            queue.sort(key=lambda x: x.cost);
                            queue.reverse();
                            break;
                        else:
                            break;
                    else:
                        continue;
                    break;
                else:
                    continue;
                break;
                    
        print("No solution found.");
if __name__ == "__main__":
    game = GameState.fromFile(r"sudoku/data/sudoku_2.txt");
    solver = SudokuSolver(game.board);
    solver.solve();
    print(solver.board);