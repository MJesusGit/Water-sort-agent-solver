
class Frontier_List():
    def __init__(self):
        self.frontier = list()

    def push(self, new_node):
        self.frontier.append(new_node)
        self.frontier = sorted(self.frontier, reverse=True)

    def pop(self):
        return self.frontier.pop()

    def __len__(self):
        return len(self.frontier)

    def is_Empty(self):
        if(len(self.frontier) == 0):
            return True
        else:
            return False