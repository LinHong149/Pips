class PipsPuzzle:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[None for _ in range(cols)] for _ in range(rows)]
        self.regions = []

    def add_region(self, cells, constraint_type='sum_eq', target_value=None):
        """
        Adds a region constraint.

        constraint_type options:
            - 'sum_eq' → sum of cell values == target_value
            - 'sum_lt' → sum of cell values < target_value
            - 'sum_gt' → sum of cell values > target_value
            - 'all_eq' → all cell values equal (no target_value needed)
        """
        if constraint_type not in ('sum_eq', 'sum_lt', 'sum_gt', 'all_eq'):
            raise ValueError("Invalid constraint_type")

        if constraint_type != 'all_eq' and target_value is None:
            raise ValueError("target_value must be provided for sum constraints")

        region = {
            'cells': cells,
            'constraint_type': constraint_type,
            'target_value': target_value
        }
        self.regions.append(region)

    def place_domino(self, start, end, value1, value2):
        """Place a domino on the board between two cells."""
        (r1, c1), (r2, c2) = start, end
        self.board[r1][c1] = value1
        self.board[r2][c2] = value2

    def is_valid(self):
        """Check whether all region constraints are satisfied."""
        for region in self.regions:
            cells = region['cells']
            values = [
                self.board[r][c] if self.board[r][c] is not None else 0
                for r, c in cells
            ]

            constraint = region['constraint_type']
            target = region['target_value']

            if constraint == 'sum_eq':
                if sum(values) != target:
                    return False
            elif constraint == 'sum_lt':
                if sum(values) >= target:
                    return False
            elif constraint == 'sum_gt':
                if sum(values) <= target:
                    return False
            elif constraint == 'all_eq':
                unique_values = set(values)
                if len(unique_values) > 1:
                    return False
            else:
                raise ValueError(f"Unsupported constraint type: {constraint}")

        return True
    

# puzzle = PipsPuzzle(rows=5, cols=5)

# print("Initial board:")
# for i in range(puzzle.rows):
#     for j in range(puzzle.cols):
#         print(puzzle.board[i][j], end=' ')
#     print()

# # Sum of cells must equal 4
# puzzle.add_region([(0,0), (0,1), (1,0)], constraint_type='sum_eq', target_value=4)

# # Sum of cells must be less than 10
# puzzle.add_region([(1,2), (1,3), (2,2)], constraint_type='sum_lt', target_value=10)

# # Sum of cells must be greater than 6
# puzzle.add_region([(2,3), (3,3), (3,2)], constraint_type='sum_gt', target_value=6)

# # All cells in the region must be equal (no target value needed!)
# puzzle.add_region([(3,0), (3,1)], constraint_type='all_eq')

# # Place dominoes
# puzzle.place_domino((0,0), (0,1), 2, 2)
# puzzle.place_domino((1,0), (1,1), 2, 2)

# print("Board after placing dominoes:")
# for i in range(puzzle.rows):
#     for j in range(puzzle.cols):
#         print(puzzle.board[i][j], end=' ')
#     print()

# for region in puzzle.regions:
#     print(region['cells'], region['constraint_type'], region['target_value'])

# # Check puzzle validity
# print(puzzle.is_valid())  # True or False