from runes import architecture
from copy import deepcopy

def adjacent_cells(row, col, grid):
    """Generates a list of adjacent cells, given a position and grid of cells.
    
    Arguments:
        row, col    -- position of the current cell in the grid
        grid        -- grid of cells
    """
    
    adjacents = []
    
    coordinates = ((row-1, col), (row-1, col+1), (row, col+1), (row+1, col+1), 
        (row+1, col), (row+1, col-1), (row, col-1), (row-1, col-1))
    for rr, cc in coordinates:
        if rr<0 or cc<0:
            adjacents.append(None)
        elif rr>=21:
            adjacents.append(None)
        elif cc>=80:
            adjacents.append(None)
        else:
            adjacents.append(grid[rr][cc])
    
    return adjacents

class Map():
    def __init__(self, default, cells=()):
        # Initialize map with default cell
        self.map = [[deepcopy(default) for _ in range(80)] for _ in range(21)]
        
        # Load pre-specified cells
        for row, col, cell in cells:
            self.map[row][col] = cell
        
        # Build adjacents
        for row in range(21):
            for col in range(80):
                self.map[row][col].adjacent = adjacent_cells(row, col, self.map)
    
    def render(self):
        return [[cell.render() for cell in row].append('\n') for row in self.map]
