import tkinter as tk
from typing import List, Any


class Application(tk.Tk):
    def __init__(self, cell_size: int = 25):
        super().__init__()

        self._cell_size = cell_size

        self.title("Drawing")

        self.canvas = tk.Canvas(self, background="#ffffff")
        self.canvas.pack(fill="both", expand=True)

    def draw_cmap(self, table: List[List[Any]], color_map: dict[Any, str]):
        for row in range(len(table)):
            for column in range(len(table[row])):
                value = table[row][column]
                if value in color_map:
                    self.canvas.create_rectangle(
                        column * self._cell_size,
                        row * self._cell_size,
                        (column + 1) * self._cell_size,
                        (row + 1) * self._cell_size,
                        fill=color_map[value],
                    )

    def draw_lines(self, table: List[List[Any]]):
        rows = len(table)
        columns = len(table[0])

        # Draw horizontal lines
        for r in range(rows + 1):
            self.canvas.create_line(
                0,
                r * self._cell_size,
                self._cell_size * columns,
                r * self._cell_size,
            )

        # Draw vertical lines
        for c in range(columns + 1):
            self.canvas.create_line(
                c * self._cell_size,
                0,
                c * self._cell_size,
                self._cell_size * rows,
            )

    def draw_indices(self, table: List[List[Any]], pad: int = 1):
        for row in range(len(table)):
            for column in range(len(table[row])):
                self.canvas.create_text(
                    pad + column * self._cell_size,
                    pad + row * self._cell_size,
                    anchor="nw",
                    fill="#808080",
                    text=f"{row}, {column}",
                    font=("", 5),
                )

    def draw_values(self, table: List[List[Any]]):
        for row in range(len(table)):
            for column in range(len(table[0])):
                self.canvas.create_text(
                    (column + 0.5) * self._cell_size,
                    (row + 0.5) * self._cell_size,
                    anchor="center",
                    fill="#252525",
                    text=str(table[row][column]),
                    font=("", 8),
                )


def draw_table(table: List[List[Any]], cmap: dict[Any, str] = dict()):
    app = Application()
    if cmap:
        app.draw_cmap(table, cmap)
    app.draw_lines(table)
    app.draw_indices(table)
    app.draw_values(table)
    app.mainloop()


if __name__ == "__main__":
    table = [[(r, c) for c in range(10)] for r in range(5)]
    draw_table(table, {(1, 1): "#f3af77"})
