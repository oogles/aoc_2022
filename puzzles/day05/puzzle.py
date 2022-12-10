from copy import deepcopy

from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = None
    strip_whitespace = False
    
    def process_input_data(self, input_data):
        
        crate_input, move_input = input_data.split('\n\n')
        crate_input = crate_input.split('\n')
        move_input = move_input.split('\n')
        
        # Establish number of stacks by processing the last line in
        # the crate input, removing spaces and counting the remaining 
        # characters (stacks number in the single digits only)
        stack_labels = crate_input.pop()
        num_stacks = len(stack_labels.replace(' ', ''))
        
        # Knowing the number of stacks, parse the grid of crates to
        # build FILO stacks of crates
        crates = {}
        for line in crate_input:
            for i in range(num_stacks):
                # The crates are in fixed positions within each line,
                # separated by 4 characters, with an initial offset of 1
                crate_index = i * 4 + 1
                crate = line[crate_index]
                if crate != ' ':  # there may not be a crate at this position in this stack
                    stack_label = str(i + 1)
                    crates.setdefault(stack_label, [])
                    crates[stack_label].insert(0, crate)
        
        # Parse move instructions into a 3-tuple of the number of crates
        # to move, the label of the stack to move them from, and the
        # label of the stack to move them to.
        moves = []
        for line in move_input:
            if not line:  # ignore blank lines
                continue
            
            # Ignore "move " and separate the number of crates to be
            # moved from the "from" and "to" stack numbers
            num, remainder = line[5:].split(' from ')
            from_stack, to_stack = remainder.split(' to ')
            
            moves.append((int(num), from_stack, to_stack))
        
        return crates, moves
    
    def _part1(self, input_data):
        
        crates, moves = input_data
        
        # Move crates one-by-one from/to the designated stacks
        for num, from_stack, to_stack in moves:
            for i in range(num):
                to_move = crates[from_stack].pop()
                crates[to_stack].append(to_move)
        
        # Find the crates on the top of each stack
        top_crates = []
        for k in sorted(crates.keys()):
            top_crates.append(crates[k][-1])
        
        return ''.join(top_crates)
    
    def _part2(self, input_data):
        
        crates, moves = input_data
        
        # Move crates all together from/to the designated stacks
        for num, from_stack, to_stack in moves:
            to_move = crates[from_stack][-num:]
            del crates[from_stack][-num:]
            crates[to_stack].extend(to_move)
        
        # Find the crates on the top of each stack
        top_crates = []
        for k in sorted(crates.keys()):
            top_crates.append(crates[k][-1])
        
        return ''.join(top_crates)
