from ..aoc import Puzzle

class TreeNode:
    
    def __init__(self, name, size=None, parent=None):
        
        self.name = name
        self._size = size
        
        self.parent = parent
        self.children = {}
    
    @property
    def size(self):
        
        if self.children:
            return sum([c.size for c in self.children.values()])
        
        return self._size
    
    @property
    def path(self):
        
        path = [self.name]
        
        node = self
        while node.parent:
            path.insert(0, node.parent.name)
            node = node.parent
        
        return path
    
    def add(self, name, size=None):
        
        if self._size:
            raise Exception('Attempting to add to a non-directory.')
        
        node = TreeNode(name, size, parent=self)
        self.children[name] = node
        
        return node


class P(Puzzle):
    
    def process_input_data(self, input_data):
        
        root = TreeNode('/')
        cwd = root
        
        for line in input_data:
            parts = line.split()
            
            if parts[0] == '$':
                if parts[1] == 'cd':
                    dir_name = line.split()[-1]
                    if dir_name == '/':  # jump to root
                        cwd = root
                    elif dir_name == '..':  # move back a level
                        cwd = cwd.parent
                    elif dir_name in cwd.children:  # an existing subdirectory
                        cwd = cwd.children[dir_name]
                    else:  # a new subdirectory
                        cwd = cwd.add(dir_name)
            else:
                size, file_name = parts
                if size == 'dir':
                    size = None
                else:
                    size = int(size)
                
                cwd.add(file_name, size)
        
        # Find the total size of all directories in the file tree,
        # potentially counting files twice (when directories contain
        # inner directories)
        dir_sizes = {
            '/': root.size
        }
        
        def traverse(node):
            
            for child in node.children.values():
                if child.children:  # child node is a directory
                    # Get the full path to the directory, to account for
                    # directories with the same name at different paths
                    path = '/'.join(child.path)
                    dir_sizes[path] = child.size
                    traverse(child)
        
        traverse(root)
        
        return dir_sizes
    
    def _part1(self, input_data):
        
        # Find the sum of directories sizes not over 100000
        total = 0
        for size in input_data.values():
            if size <= 100000:
                total += size
        
        return total
    
    def _part2(self, input_data):
        
        total_space = 70000000
        used_space = input_data['/']
        
        required_space = 30000000
        unused_space = total_space - used_space
        difference = required_space - unused_space
        
        suitable_directories = []
        for size in input_data.values():
            if size >= difference:
                suitable_directories.append(size)
        
        return min(suitable_directories)
