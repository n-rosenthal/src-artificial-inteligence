import numpy as np

def s_get_row(iter: np.array, x: int) -> list:
    """Returns a list with all the elements in the same row as `x` in `iter`"""
    return iter[x, :];

def s_get_col(iter: np.array, y: int) -> list:
    """Returns a list with all the elements in the same column as `y` in `iter`"""
    return iter[:, y];

def s_get_block(iter: np.array, index: int) -> list:
    """Returns a list with all the elements in the same block as `index` in `iter`"""
    return iter[index // 3 * 3 : index // 3 * 3 + 3, index % 3 * 3 : index % 3 * 3 + 3];

def s_which_block(iter: np.array, x: int, y: int) -> int:
    """Returns the block index of the element at position `x`, `y` in `iter`"""
    return x // 3 * 3 + y // 3;

def s_value_line(iter: np.array) -> int:
    """Sums 1 for each non-zero element in `iter`
    
    Args:
        iter (np.array): The array to sum
    
    Returns:
        int: The sum of 1 for each non-zero element
    """
    return sum(1 for x in iter.flatten() if x != 0);

def s_value_block(iter: np.array) -> int:
    """Sums 1 for each non-zero element in the `iter` 3x3 block
    
    Args:
        iter (np.array): The array to sum
    
    Returns:
        int: The sum of 1 for each non-zero element
    """
    return sum(1 for x in iter.flatten() if x != 0);

def s_pos_value(iter: np.array, x: int, y: int) -> int:
    """Returns the value of the element at position `x`, `y`:
    row value + column value + block value
    
    Args:
        iter (np.array): The array to sum
        x (int): The x position
        y (int): The y position
    
    Returns:
        int: The sum of 1 for each non-zero element
    """
    this = iter[x, y];
    if this == 0:
        return s_value_line(s_get_row(iter, x)) + s_value_line(s_get_col(iter, y)) + s_value_block(s_get_block(iter, s_which_block(iter, x, y)));
    else:
        return s_value_line(s_get_row(iter, x)) + s_value_line(s_get_col(iter, y)) + s_value_block(s_get_block(iter, s_which_block(iter, x, y)))

def s_values_map(iter: np.array) -> np.array:
    """Returns a 9x9 array with the value of each element in `iter`"""
    return np.array([[s_pos_value(iter, x, y) for y in range(9)] for x in range(9)]);

def max(iter: np.array) -> tuple[int, int]:
    """Returns the x, y positions of the maximum element in a 2x2 matrix
    
    Args:
        iter (np.array): The array to search
    
    Returns:
        tuple[int, int]: The x, y positions
    """
    return np.unravel_index(iter.argmax(), iter.shape);

def main():
    """Main function"""
    sudoku:np.array = np.array([
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

    print(sudoku);

    print(s_values_map(sudoku));
    
    print(max(s_values_map(sudoku)));
    
    
    
if __name__ == "__main__":
    main();