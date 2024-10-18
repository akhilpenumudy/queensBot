from collections import defaultdict


def solve_queens(grid):
    def is_safe(row, col):
        # Check row and column
        for i in range(len(grid)):
            if grid[row][i] == "👑" or grid[i][col] == "👑":
                return False

        # Check diagonals
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == "👑":
                    if abs(row - i) == abs(col - j):
                        return False

        # Check adjacent cells (including diagonally)
        for i in range(max(0, row - 1), min(len(grid), row + 2)):
            for j in range(max(0, col - 1), min(len(grid), col + 2)):
                if grid[i][j] == "👑":
                    return False

        return True

    def solve():
        color_regions = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid)):
                color_regions[grid[i][j]].append((i, j))

        return backtrack(list(color_regions.values()), 0, 0)

    def backtrack(regions, row, col):
        if row == len(grid):
            return all(any(grid[i][j] == "👑" for i, j in region) for region in regions)

        if col == len(grid):
            return backtrack(regions, row + 1, 0)

        color = grid[row][col]
        if grid[row][col] == "👑":
            return backtrack(regions, row, col + 1)

        if is_safe(row, col):
            grid[row][col] = "👑"
            if backtrack(regions, row, col + 1):
                return True
            grid[row][col] = color

        return backtrack(regions, row, col + 1)

    if solve():
        return grid
    else:
        return None
