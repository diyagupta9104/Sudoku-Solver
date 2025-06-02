import tkinter as tk
from tkinter import messagebox
import math

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.originals = [[False for _ in range(9)] for _ in range(9)]

        self.draw_grid()
        self.add_buttons()

    def draw_grid(self):
        for i in range(9):
            for j in range(9):
                bg_color = "#b0c7d2" if ((i // 3 + j // 3) % 2 == 0) else "#b6d19b"
                entry = tk.Entry(self.root, width=2, font=('Arial', 20, 'bold'),justify='center', bg=bg_color, fg="red")
                entry.grid(row=i, column=j, padx=2, pady=2)
                self.entries[i][j] = entry

    def add_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve, bg="#85F089", fg="black", font=('Arial', 12, 'bold'))
        solve_button.grid(row=9, column=3, columnspan=3, pady=10)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_board, bg="#e6817a", fg="black", font=('Arial', 12, 'bold'))
        clear_button.grid(row=10, column=3, columnspan=3 , pady = 10)

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(fg="red", bg="#b0c7d2" if ((i // 3 + j // 3) % 2 == 0) else "#b6d19b")
                self.originals[i][j] = False

    def read_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val == '' or not val.isdigit():
                    row.append(0)
                else:
                    row.append(int(val))
                    self.originals[i][j] = True
            board.append(row)
        return board

    def write_board(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(board[i][j]))
                if not self.originals[i][j]:
                    self.entries[i][j].config(fg="white", bg="#4CAF50")  # Green for solved cells
                else:
                    self.entries[i][j].config(fg="black")

    def solve(self):
        board = self.read_board()
        if self.sudoku_solver(board, 0, 0, 9):
            self.write_board(board)
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku.")

    def is_valid(self, board, i, j, num, n):
        for x in range(n):
            if board[i][x] == num or board[x][j] == num:
                return False

        rn = int(math.sqrt(n))
        si = i - i % rn
        sj = j - j % rn

        for x in range(si, si + rn):
            for y in range(sj, sj + rn):
                if board[x][y] == num:
                    return False

        return True

    def sudoku_solver(self, board, i, j, n):
        if i == n:
            return True
        if j == n:
            return self.sudoku_solver(board, i + 1, 0, n)
        if board[i][j] != 0:
            return self.sudoku_solver(board, i, j + 1, n)

        for num in range(1, 10):
            if self.is_valid(board, i, j, num, n):
                board[i][j] = num
                if self.sudoku_solver(board, i, j + 1, n):
                    return True
                board[i][j] = 0  # backtrack

        return False

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

# Example to solve
'''board = [
        [0 , 0 , 7 , 1 , 0 , 0 , 0 , 6 , 0],
        [1 , 0 , 5 , 2 , 0 , 8 , 0 , 0 , 0],
        [6 , 0 , 0 , 0 , 0 , 7 , 1 , 2 , 0],
        [3 , 1 , 2 , 4 , 0 , 5 , 0 , 0 , 8],
        [0 , 0 , 6 , 0 , 9 , 0 , 2 , 0 , 0],
        [0 , 0 , 0 , 0 , 0 , 3 , 0 , 0 , 1],
        [0 , 0 , 1 , 0 , 0 , 4 , 9 , 8 , 6],
        [8 , 0 , 3 , 9 , 0 , 6 , 0 , 0 , 0],
        [0 , 6 , 0 , 0 , 8 , 2 , 7 , 0 , 3]
        ]'''