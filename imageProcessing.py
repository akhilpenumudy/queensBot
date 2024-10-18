import tkinter as tk
from tkinter import colorchooser, simpledialog, messagebox
from queens_solver import solve_queens
import threading


class QueensGridGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Queens Solver")
        self.grid_size = 0
        self.cell_size = 50
        self.colors = [
            ("White", "#FFFFFF"),
            ("Red", "#FF0000"),
            ("Green", "#00FF00"),
            ("Blue", "#0000FF"),
            ("Yellow", "#FFFF00"),
            ("Magenta", "#FF00FF"),
            ("Cyan", "#00FFFF"),
            ("Maroon", "#800000"),
            ("Dark Green", "#008000"),
            ("Navy", "#000080"),
            ("Olive", "#808000"),
            ("Purple", "#800080"),
            ("Teal", "#008080"),
        ]
        self.current_color = self.colors[0][1]
        self.grid = []

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.master)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Grid size input
        tk.Button(main_frame, text="Create Grid", command=self.create_grid).pack(
            pady=10
        )

        # Color selection
        color_frame = tk.Frame(main_frame)
        color_frame.pack(pady=10)

        for i, (color_name, color_hex) in enumerate(self.colors):
            btn = tk.Button(
                color_frame,
                text=color_name,
                bg=color_hex,
                command=lambda c=color_hex: self.set_color(c),
            )
            btn.grid(row=i // 7, column=i % 7, padx=2, pady=2, sticky="ew")
            btn.config(fg="#000000")  # Set text color to black

        # Canvas for grid
        self.canvas_frame = tk.Frame(main_frame)
        self.canvas_frame.pack(expand=True, fill=tk.BOTH)

        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.pack(expand=True)

        # Status label
        self.status_label = tk.Label(main_frame, text="")
        self.status_label.pack(side=tk.BOTTOM, pady=5)

        # Solve button
        self.solve_button = tk.Button(
            main_frame, text="Solve", command=self.solve, state=tk.DISABLED
        )
        self.solve_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def create_grid(self):
        self.grid_size = simpledialog.askinteger(
            "Grid Size", "Enter grid size:", minvalue=1, maxvalue=20
        )
        if not self.grid_size:
            return

        self.canvas.delete("all")
        self.grid = [
            [self.colors[0][1] for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
        ]

        total_size = self.grid_size * self.cell_size
        self.canvas.config(width=total_size, height=total_size)

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=self.colors[0][1], outline="black"
                )

        self.canvas.bind("<Button-1>", self.on_click)

        # Enable the solve button after grid creation
        self.solve_button.config(state=tk.NORMAL)

        # Center the canvas
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def set_color(self, color):
        self.current_color = color

    def on_click(self, event):
        if not self.grid:
            return

        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
            x1, y1 = col * self.cell_size, row * self.cell_size
            x2, y2 = x1 + self.cell_size, y1 + self.cell_size
            self.canvas.create_rectangle(
                x1, y1, x2, y2, fill=self.current_color, outline="black"
            )
            self.grid[row][col] = self.current_color

    def solve(self):
        print("Solving...")
        self.solve_button.config(state=tk.DISABLED)
        self.status_label.config(text="Solving...")

        # Run the solver in a separate thread to avoid freezing the GUI
        threading.Thread(
            target=self._solve_thread, args=(self.grid,), daemon=True
        ).start()

    def _solve_thread(self, solver_grid):
        solution = solve_queens(solver_grid)

        if solution:
            self.master.after(0, self._update_grid_with_solution, solution)
        else:
            self.master.after(0, self._show_no_solution)

    def _update_grid_with_solution(self, solution):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if solution[i][j] == "👑":
                    x1, y1 = j * self.cell_size, i * self.cell_size
                    x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                    self.canvas.create_text(
                        (x1 + x2) / 2, (y1 + y2) / 2, text="👑", font=("Arial", 20)
                    )
                    self.grid[i][j] = "👑"
        self.status_label.config(text="Solution found!")
        self.solve_button.config(state=tk.NORMAL)
        messagebox.showinfo("Success", "Solution found and displayed on the grid")

    def _show_no_solution(self):
        self.status_label.config(text="No solution found")
        self.solve_button.config(state=tk.NORMAL)
        messagebox.showinfo(
            "No Solution", "No solution found for the current configuration"
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # Set a default window size
    app = QueensGridGUI(root)
    root.mainloop()
