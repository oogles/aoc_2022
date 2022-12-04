from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_line):
        
        set1, set2 = input_line.split(',')
        set1_min, set1_max = set1.split('-')
        set2_min, set2_max = set2.split('-')
        
        set1 = set(range(int(set1_min), int(set1_max) + 1))
        set2 = set(range(int(set2_min), int(set2_max) + 1))
        
        return (set1, set2)
    
    def _part1(self, input_data):
        
        count = 0
        for set1, set2 in input_data:
            if set1.issubset(set2) or set1.issuperset(set2):
                count += 1
        
        return count
    
    def _part2(self, input_data):
        
        count = 0
        for set1, set2 in input_data:
            if set1.intersection(set2):
                count += 1
        
        return count
