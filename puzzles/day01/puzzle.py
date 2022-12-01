from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = '\n\n'
    
    def process_input_item(self, input_item):
        
        # Each "item" is a group of line-separated integers.
        # Calculate the sum of each group.
        return sum(map(int, input_item.split('\n')))
    
    def _part1(self, input_data):
        
        input_data.sort()
        
        return input_data.pop()
    
    def _part2(self, input_data):
        
        input_data.sort()
        
        return sum(input_data[-3:])
