def dist(iter: list, a: any, b: any) -> int:
    """Returns the distance between two elements in a list

    Args:
        iter (list): The list to search in
        a (any): The first element
        b (any): The second element

    Returns:
        int: The distance between the two elements
    """
    try:
        return abs(iter.index(a) - iter.index(b));
    except ValueError:
        return len(iter)**len(iter);

def swap(iter: list, a: any, b: any) -> list:
    """Swaps two elements in a list

    Args:
        iter (list): The list to search in
        a (any): The first element
        b (any): The second element

    Returns:
        list: The list with the elements swapped
    """
    iter[a], iter[b] = iter[b], iter[a];
    return iter;

def possibilities(iter: list, elem: any) -> list:
    try:
        index = iter.index(elem);
    except ValueError:
        return [];
    
    if(index == 0):
        return [index + 1];
    elif(index == len(iter) - 1):
        return [index - 1];
    else:
        return [index - 1, index + 1];
    
def choose(iter: list, elem: any) -> tuple[list, any]:
    if(possibilities(iter, elem) == []):
        return (iter, elem);
    else:
        return max(possibilities(iter, elem), key=lambda x: dist(iter, elem, x));

def main():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    print(choose(l, 5));
    
    print(choose([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0));
    
    
if __name__ == "__main__":
    main();