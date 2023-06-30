import typing
from collections import deque, namedtuple

row = list[str]
grid = list[row]
Point = namedtuple("Point", ["y", "x"])

def __generate_starting_queue(first_letter: str, board: grid) -> deque:
    mainQueue: deque[Point] = deque()
    for y,array in enumerate(board):
        for x,letter in enumerate(array):
            if letter == first_letter:
                mainQueue.appendleft(Point(y,x))
    return mainQueue

def exists(board: grid, word: str) -> bool:
    """
    This method is intended to take in a grid of letters
    and then tell me if there is a path through it that spells out
    the word desired
    """
    word_array = word.split("")
    mainQueue = __generate_starting_queue(word_array[0], board)
    return False
