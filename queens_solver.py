from collections import defaultdict


def solve_queens(grid):
    def is_safe(row, col):
        # Check row and column
        for i in range(len(grid)):
            if grid[row][i] == "👑" or grid[i][col] == "👑":
                return False

        # Check diagonals
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if grid[i][j] == "👑":
                return False
        for i, j in zip(range(row, -1, -1), range(col, len(grid))):
            if grid[i][j] == "👑":
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

        queens_count = [0] * len(grid)
        return backtrack(list(color_regions.values()), queens_count, 0)

    def backtrack(regions, queens_count, color_index):
        if color_index == len(regions):
            return all(count == 1 for count in queens_count)

        for row, col in regions[color_index]:
            if queens_count[row] == 0 and is_safe(row, col):
                grid[row][col] = "👑"
                queens_count[row] += 1

                if backtrack(regions, queens_count, color_index + 1):
                    return True

                grid[row][col] = regions[color_index][0][1]  # Restore original color
                queens_count[row] -= 1

        return False

    if solve():
        return grid
    else:
        return None
