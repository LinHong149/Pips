from PipsPuzzle import PipsPuzzle
    

puzzle = PipsPuzzle(rows=5, cols=5)

print("Initial board:")
for i in range(puzzle.rows):
    for j in range(puzzle.cols):
        print(puzzle.board[i][j], end=' ')
    print()

# Sum of cells must equal 4
puzzle.add_region([(0,0), (0,1), (1,0)], constraint_type='sum_eq', target_value=4)

# Sum of cells must be less than 10
puzzle.add_region([(1,2), (1,3), (2,2)], constraint_type='sum_lt', target_value=10)

# Sum of cells must be greater than 6
puzzle.add_region([(2,3), (3,3), (3,2)], constraint_type='sum_gt', target_value=6)

# All cells in the region must be equal (no target value needed!)
puzzle.add_region([(3,0), (3,1)], constraint_type='all_eq')

# Place dominoes
puzzle.place_domino((0,0), (0,1), 2, 2)
puzzle.place_domino((1,0), (1,1), 2, 2)

print("Board after placing dominoes:")
for i in range(puzzle.rows):
    for j in range(puzzle.cols):
        print(puzzle.board[i][j], end=' ')
    print()

for region in puzzle.regions:
    print(region['cells'], region['constraint_type'], region['target_value'])

# Check puzzle validity
print(puzzle.is_valid())  # True or False