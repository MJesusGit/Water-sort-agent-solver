#!/usr/bin/python3
#-*-coding: utf-8; mode:python-*-

class Node():

    def __init__(self, ID, cost, state, ID_parent, action, depth, heuristic, value):
        self.ID = ID
        self.cost = cost
        self.state = state
        self.ID_parent = ID_parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic
        self.value = value

    def __lt__(self, newNode):
        return (self.value, self.ID) < (newNode.value, newNode.ID)

    def toString(self):
        return self.ID, self.cost, self.state, self.ID_parent, self.action, self.depth, self.heuristic, self.value