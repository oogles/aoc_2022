import string

from ..aoc import Puzzle


priorities = string.ascii_lowercase + string.ascii_uppercase


class P(Puzzle):
    
    def _part1(self, input_data):
        
        total = 0
        for items in input_data:
            per_component = len(items) // 2
            compartment1 = items[:per_component]
            compartment2 = items[per_component:]
            
            common_items = set(compartment1).intersection(compartment2)
            item_priorities = [priorities.index(i) + 1 for i in common_items]
            
            total += sum(item_priorities)
        
        return total
    
    def _part2(self, input_data):
        
        total = 0
        for n in range(0, len(input_data), 3):  # increment by 3
            elf1_items, elf2_items, elf3_items = input_data[n:n + 3]
            
            common_items = set(elf1_items).intersection(elf2_items, elf3_items)
            badge = common_items.pop()
            if common_items:
                raise Exception('multiple common items?')
            
            total += priorities.index(badge) + 1
        
        return total
