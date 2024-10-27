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

def sconstraints(iter: list, elem: any) -> list:
    """Returns a new list with all elements of `iter` that are not equal to `elem`
    
    Args:
        iter (list): The list to search in
        elem (any): The element to remove from the list
    
    Returns:
        list: The list with `elem` removed
    """
    temp = [x for x in iter if x != elem];
    return sremove_empty(temp);

def snum_constraints(iter: list, elem: any) -> int:
    """Returns the number of elements in `iter` that are not equal to `elem`
    
    Args:
        iter (list): The list to search in
        elem (any): The element to remove from the list
    
    Returns:
        int: The number of elements in `iter` that are not equal to `elem`
    """
    return len(sconstraints(iter, elem));

def sremove(iter: list, elem: any) -> list:
    """Returns a new list with all elements of `iter` that are equal to `elem`
    
    Args:
        iter (list): The list to search in
        elem (any): The element to remove from the list
    
    Returns:
        list: The list with `elem` removed
    """
    temp = [x for x in iter if x == elem];
    return sremove_empty(temp);

def sremove_empty(iter: list) -> list:
    """Returns a new list without all empty elements of `iter`
    
    Args:
        iter (list): The list to search in
    
    Returns:
        list: The list without empty elements
    """
    return [x for x in iter if x != 0];

def main():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    print(sconstraints(l, 5))
    
    
if __name__ == "__main__":
    main();