
class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")

        if row >= 8:
            raise ValueError("row not on board")

        if column < 0:
            raise ValueError("column not positive")

        if column >= 8:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):

        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError

        if self.row == another_queen.row or self.column == another_queen.column:
            return True

        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True

        else:
            return False


white_queen = Queen(2,2)
black_queen = Queen(2,2)
print(white_queen.can_attack(black_queen))