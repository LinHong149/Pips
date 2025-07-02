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
    