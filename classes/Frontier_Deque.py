from collections import deque

class Frontier_Deque():
    
    def __init__(self):
        self.frontier = deque()

    def push(self, new_node):
        self.frontier.append(new_node)
        self.frontier = deque(sorted(self.frontier))

    def pop(self):
        return self.frontier.popleft()

    def __len__(self):
        return len(self.frontier)
    
    def is_Empty(self):
        if(len(self.frontier) == 0):
            return True
        else:
            return False