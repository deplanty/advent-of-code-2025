from typing import Generator, Any

from .index import Index


def iter_index_in_field(field: list[list[Any]]) -> Generator[Index, Any, Any]:
    for i in range(len(field)):
        for j in range(len(field[i])):
            yield Index(i, j)
