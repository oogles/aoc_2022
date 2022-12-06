from ..aoc import Puzzle


def _find_marker(marker_length, stream):
    
    for i in range(len(stream)):
        buffer_start = max(i - marker_length, 0)
        buffer = stream[buffer_start:i]
        if len(set(buffer)) == marker_length:
            return i
    
    raise Exception('marker not found')


class P(Puzzle):
    
    input_delimiter = None
    
    def _part1(self, input_data):
        
        return _find_marker(4, input_data)
    
    def _part2(self, input_data):
        
        return _find_marker(14, input_data)
