import typing
from collections import deque, namedtuple

row = list[str]
grid = list[row]

def __generate_starting_queue() -> deque:
    mainQueue = deque()
    for y,array in enumerate(board):
        for x,letter in enumerate(array):
            if letter == word[:1]:
                deque.appendleft((x,y))
    return mainQueue

def exists(board: grid, word: str) -> bool:
    """
    This method is intended to take in a grid of letters
    and then tell me if there is a path through it that spells out
    the word desired
    """
    mainQueue = __generate_starting_queue()
