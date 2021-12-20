from heapq import heappush, heappop

class Frontier_Heapq():
    
    def __init__(self):
        self.frontier = []

    def push(self, new_node): 
        heappush(self.frontier, new_node)

    def pop(self):
        return heappop(self.frontier)

    def __len__(self):
        return len(self.frontier)
        
    def is_Empty(self):
        if(len(self.frontier) == 0):
            return True
        else:
            return False