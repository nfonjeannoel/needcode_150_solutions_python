from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row_ind in range(9):
            for col_ind in range(9):
                item = board[row_ind][col_ind]
                if item == '.':
                    continue
                box_ind = ((row_ind // 3) * 3) + (col_ind // 3)
                if item in rows[row_ind] or item in cols[col_ind] or item in boxes[box_ind]:
                    return False
                rows[row_ind].add(item)
                cols[col_ind].add(item)
                boxes[box_ind].add(item)

        return True


if __name__ == "__main__":
    solution = Solution()
    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.isValidSudoku(board))  # Output: True
