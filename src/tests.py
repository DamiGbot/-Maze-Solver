import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols: int = 12
        num_rows: int = 10

        m1 = Maze(0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells_large(self):
        num_cols: int = 16
        num_rows: int = 12

        m1 = Maze(0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

if __name__ == "__main__":
    unittest.main()