from math import copysign

from ..aoc import Puzzle


def follow(instructions, num_knots):
    
    knots = [[0, 0] for _ in range(num_knots)]
    head = knots[0]
    tail = knots[-1]
    tail_positions = set()
    
    for line in instructions:
        direction, count = line.split()
        count = int(count)
        
        # Update the x-coordinate if moving horizontally,
        # or the y-coordinate if moving vertically
        coord = 0 if direction in ('L', 'R') else 1
        
        # Increment the relevant coordinate if moving right/up,
        # decrement if moving left/down
        step = 1
        if direction in ('L', 'D'):
            count *= -1
            step = -1
        
        for _ in range(0, count, step):
            head[coord] += step
            
            # If either coordinate of the next knot exceeds a distance
            # of 1 from the previous one, it needs to move to catch up.
            # If a knot moves in this way and isn't aligned on the
            # *other* coordinate, also move in that direction (resulting
            # in a diagonal move. Only move a single step in either
            # direction.
            previous_knot = head
            for current_knot in knots[1:]:  # skip `head`
                x_delta = previous_knot[0] - current_knot[0]
                y_delta = previous_knot[1] - current_knot[1]
                if abs(x_delta) > 1:
                    current_knot[0] += copysign(1, x_delta)
                    if y_delta:
                        current_knot[1] += copysign(1, y_delta)
                elif abs(y_delta) > 1:
                    current_knot[1] += copysign(1, y_delta)
                    if x_delta:
                        current_knot[0] += copysign(1, x_delta)
                
                previous_knot = current_knot
            
            # Store the tail's position (as a copy, so all records
            # aren't updated as the position changes)
            tail_positions.add(tuple(tail))
    
    return len(tail_positions)


class P(Puzzle):
    
    def _part1(self, input_data):
        
        return follow(input_data, num_knots=2)
    
    def _part2(self, input_data):
        
        return follow(input_data, num_knots=10)
