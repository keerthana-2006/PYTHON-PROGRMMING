#Docstrings
#   """ """ -are used for multi-line comment,refer the given example code
# It is used to increase the user readability of the program.

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    
    Example:
    >>> calculate_area(5, 3)
    15
    """
    return length * width

print(calculate_area.__doc__)
help(calculate_area)
