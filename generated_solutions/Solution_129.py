import collections

def find_minimum_path(grid, k):
    N = len(grid)
    
    # Directions for movement: (delta_row, delta_col)
    # (-1, 0) Up, (1, 0) Down, (0, -1) Left, (0, 1) Right
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # current_min_paths stores the lexicographically smallest path of
    # the current length `L` ending at each cell (r, c).
    # It maps a (r, c) tuple to a list of values representing that path.
    current_min_paths = {}

    # Initialize for path length L = 1
    # Each cell's value is a path of length 1 ending at itself.
    for r in range(N):
        for c in range(N):
            current_min_paths[(r, c)] = [grid[r][c]]

    # Handle k=1 as a special case: we just need the single smallest value in the grid.
    # The initialization loop already populates current_min_paths with all paths of length 1.
    if k == 1:
        overall_min_path = None
        for path in current_min_paths.values():
            if overall_min_path is None or path < overall_min_path:
                overall_min_path = path
        return overall_min_path

    # Iterate from path length L = 2 up to k.
    # The loop runs k-1 times.
    for _ in range(2, k + 1): 
        next_min_paths = {} # Will store the best paths for the current length `L`
        
        # Iterate over all cells in the grid to find paths ending at them
        for r in range(N):
            for c in range(N):
                current_cell_value = grid[r][c]
                best_path_for_rc = None # Keep track of the best path ending at (r,c) for current length L

                # Check all four possible neighbors (previous cells in the path)
                for i in range(4):
                    pr, pc = r + dr[i], c + dc[i] # Coordinates of a potential previous cell

                    # Check if the neighbor is within grid boundaries
                    if 0 <= pr < N and 0 <= pc < N:
                        # If a lexicographically smallest path of length (L-1) exists
                        # to this neighbor (pr, pc)
                        if (pr, pc) in current_min_paths:
                            path_to_prev_cell = current_min_paths[(pr, pc)]
                            
                            # Extend this path by adding the current cell's value
                            candidate_path = path_to_prev_cell + [current_cell_value]

                            # Compare this candidate path with the best path found so far
                            # for (r, c) for the current length L.
                            # Python's list comparison works lexicographically.
                            if best_path_for_rc is None or candidate_path < best_path_for_rc:
                                best_path_for_rc = candidate_path
                
                # If at least one path was found for (r, c) for the current length L, store it.
                if best_path_for_rc is not None:
                    next_min_paths[(r, c)] = best_path_for_rc
        
        # After processing all cells for the current length L, update
        # current_min_paths to be ready for the next length (L+1).
        current_min_paths = next_min_paths

    # After iterating up to length k, current_min_paths contains all
    # lexicographically smallest paths of length k ending at any cell.
    # Now, find the overall minimum path among these.
    overall_min_path = None
    for path in current_min_paths.values():
        if overall_min_path is None or path < overall_min_path:
            overall_min_path = path
            
    return overall_min_path