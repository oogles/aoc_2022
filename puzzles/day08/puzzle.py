from ..aoc import Puzzle


def look(matrix, row, col, direction):
    
    target_height = matrix[row][col]
    
    if direction == 'left':
        step_start = col - 1
        step_end = -1
        step = -1
    elif direction == 'right':
        step_start = col + 1
        step_end = len(matrix[0])
        step = 1
    elif direction == 'up':
        step_start = row - 1
        step_end = -1
        step = -1
    elif direction == 'down':
        step_start = row + 1
        step_end = len(matrix)
        step = 1
    
    # Assume the view in the given direction will be blocked
    blocked = True
    
    view_distance = 0
    for i in range(step_start, step_end, step):
        view_distance += 1
        
        if direction in ('left', 'right'):
            # Row stays static, column shifts
            h = matrix[row][i]
        else:
            # Column stays static, row shifts
            h = matrix[i][col]
        
        if h >= target_height:
            # A taller tree exists in this direction, blocking
            # the view of this tree
            break
    else:
        # Didn't find a taller tree, so it is not blocked
        blocked = False
    
    return view_distance, blocked


def is_visible(*args):
    
    _, blocked = look(*args)
    
    return not blocked


class P(Puzzle):
    
    def _part1(self, input_data):
        
        visible_trees = 0
        
        for i, line in enumerate(input_data):
            for j in range(len(line)):
                if is_visible(input_data, i, j, 'left'):
                    visible_trees += 1
                elif is_visible(input_data, i, j, 'right'):
                    visible_trees += 1
                elif is_visible(input_data, i, j, 'up'):
                    visible_trees += 1
                elif is_visible(input_data, i, j, 'down'):
                    visible_trees += 1
        
        return visible_trees
    
    def _part2(self, input_data):
        
        best_score = 0
        
        for i, line in enumerate(input_data):
            for j in range(len(line)):
                view_distance_left, _ = look(input_data, i, j, 'left')
                view_distance_right, _ = look(input_data, i, j, 'right')
                view_distance_up, _ = look(input_data, i, j, 'up')
                view_distance_down, _ = look(input_data, i, j, 'down')
                
                scenic_score = view_distance_left * view_distance_right * view_distance_up * view_distance_down
                
                if scenic_score > best_score:
                    best_score = scenic_score
        
        return best_score
