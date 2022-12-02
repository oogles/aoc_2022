from ..aoc import Puzzle

points = {
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3,  # scissors
    'win': 6,
    'draw': 3,
    'loss': 0
}


def calculate_points(rounds, col2_map, outcomes_map):
    
    total = 0
    for round in rounds:
        col1, col2 = round.split(' ')
        col2 = col2_map[col2]
        
        outcome = outcomes_map[(col1, col2)]
        
        total += points[outcome] + points[col2]
    
    return total


class P(Puzzle):
    
    def _part1(self, input_data):
        
        # Map the second column to a rock, paper, scissors option.
        # X -> A (rock), Y -> B (paper), Z -> C (scissors)
        col2_map = {
            'X': 'A',  # rock
            'Y': 'B',  # paper
            'Z': 'C'   # scissors
        }
        
        # Map each combination of column values to the result of
        # the round - win, draw, or loss
        outcomes_map = {
            ('A', 'A'): 'draw',  # rock vs rock
            ('A', 'B'): 'win',   # rock vs paper
            ('A', 'C'): 'loss',  # rock vs scissors
            ('B', 'A'): 'loss',  # paper vs rock
            ('B', 'B'): 'draw',  # paper vs paper
            ('B', 'C'): 'win',   # paper vs scissors
            ('C', 'A'): 'win',   # scissors vs rock
            ('C', 'B'): 'loss',  # scissors vs paper
            ('C', 'C'): 'draw'   # scissors vs scissors
        }
        
        return calculate_points(input_data, col2_map, outcomes_map)
    
    def _part2(self, input_data):
        
        # Map the second column to a result of the round - win, draw, or loss
        col2_map = {
            'X': 'loss',
            'Y': 'draw',
            'Z': 'win'
        }
        
        # Map each combination of column values to the option required to
        # achieve the given result - rock, paper, or scissors
        outcomes_map = {
            ('A', 'loss'): 'C',  # rock vs scissors (scissors loses)
            ('A', 'draw'): 'A',  # rock vs rock
            ('A', 'win'): 'B',   # rock vs paper (paper wins)
            ('B', 'loss'): 'A',  # paper vs rock (rock loses)
            ('B', 'draw'): 'B',  # paper vs paper
            ('B', 'win'): 'C',   # paper vs scissors (scissors wins)
            ('C', 'loss'): 'B',  # scissors vs paper (paper loses)
            ('C', 'draw'): 'C',  # scissors vs scissors
            ('C', 'win'): 'A'    # scissors vs rock (rock wins)
        }
        
        return calculate_points(input_data, col2_map, outcomes_map)
