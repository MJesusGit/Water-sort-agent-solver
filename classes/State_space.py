#!/usr/bin/python3
#-*-coding: utf-8; mode:python-*-
from classes.Frontier_Heapq import *
import os
from classes.Node import *
from classes.State import *

class State_space():
    
    def __init__(self, strategy, problem):
        self.limit = 1000000
        self.strategy = strategy
        self.frontier = Frontier_Heapq()
        self.id = 0
        self.visited = []
        self.problem = problem
        self.nodes_created = {}

    def search(self):
        self.frontier.push(self.make_node(self.problem.initState))
        while True:
            if len(self.frontier) == 0:
                return None
            node = self.frontier.pop()
            if node.ID == 9411:##############
                print(f"{node.cost},{node.state},{node.ID_parent},{node.depth},{node.heuristic},{node.value}")#########3
            if node.state.isGoal() == True:
                return node
            if self.belong(node.state) == False:
                self.visited.append(node.state)
                self.insert_all(self.expand(node))

    def make_node(self, init_state):
        id = self.id
        cost = 0.0
        state = init_state
        id_parent = None
        action = None
        depth = 0
        heuristic = self.calculateHeuristic(state)
        value = self.valueStrategy(depth, cost, heuristic)
        node = Node(id, cost, state, id_parent, action, depth, heuristic, value)
        self.id += 1
        self.nodes_created[f'{node.ID}'] = node
        return node

    def insert_all(self, successors_list_node):
        for successor in successors_list_node:
            self.frontier.push(successor)

    def belong(self, state_outside):
        for state_inside in self.visited:
            if len(state_outside.bottles) != len(state_inside.bottles):
                continue
            equal = True
            for i in range(len(state_outside.bottles)):
                if state_outside.bottles[i].liquids != state_inside.bottles[i].liquids:
                    equal = False
                    break
            if equal == True:
                return True
            else:
                continue            
        return False

    def expand(self, node):
        successors_node_list = []
        for successor in State().successor_fn(node.state):
            id = self.id
            cost = node.cost + successor[2]
            state = successor[1]
            id_parent = node.ID
            action = successor[0]
            depth = node.depth + 1
            heuristic = self.calculateHeuristic(state)
            value = self.valueStrategy(depth, cost, heuristic)
            successors_node_list.append(Node(id, cost, state, id_parent, action, depth, heuristic, value))
            self.nodes_created[f'{node.ID}'] = node
            self.id += 1
        return successors_node_list

    def valueStrategy(self, depth, cost, heuristic):
        if self.strategy == 'BREADTH':
            return depth
        elif self.strategy == 'DEPTH':
            return 1.0/(depth + 1)
        elif self.strategy == 'UNIFORM':
            return cost
        elif self.strategy == 'GREEDY':
            return heuristic
        elif self.strategy == 'A*':
            return cost + heuristic
            
    def export(self, node_solution):
        string_solution = ""

        while node_solution != None:
            id = node_solution.ID
            cost = node_solution.cost
            state = node_solution.state
            id_parent = node_solution.ID_parent
            depth = node_solution.depth
            heuristic = node_solution.heuristic
            value = node_solution.value
            if node_solution.action is not None:
                node_action_1 = node_solution.action[0]
                node_action_2 = node_solution.action[1]
                node_action_3 = node_solution.action[2]
                string_solution = f"{string_solution}[{id}][{cost},{state},{id_parent},({node_action_1}, {node_action_2}, {node_action_3}),{depth},{heuristic},{value}]\n"
            else:
                node_action_1 = None
                node_action_2 = None
                node_action_3 = None
                string_solution = f"{string_solution}[{id}][{cost},{state},{id_parent},{None},{depth},{heuristic},{value}]\n"
            
            node_solution = self.nodes_created.get(node_solution.ID_parent)
        with open(f'{os.getcwd()}/Solutions/{self.problem.id}_{self.strategy}.json', "w") as file:
            file.write(string_solution)
        print(f"Solution exported on the path: {os.getcwd()}/Solutions/{self.problem.id}_{self.strategy}.json")

    def calculateHeuristic(self, state):
        observed_types = []
        h = 0.0
        for i in range(len(state.bottles)):
            if len(state.bottles[i].liquids) == 0:
                h += 1.0
            else:
                if state.bottles[i].getColourLast() not in observed_types:
                    observed_types.append(state.bottles[i].getColourLast())
                else:
                    h += 1.0
                h += len(state.bottles[i].liquids)
        return h - len(state.bottles)