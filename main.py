import typing
from collections import deque, namedtuple

row = list[str]
grid = list[row]

def exists(board: grid, word: str) -> bool:
