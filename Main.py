#!/usr/bin/python3
#--coding: utf-8; mode:python--

from curses.ascii import isdigit
from json import *
from os import stat
from classes.Bottle import *
from functionalities.Import import *
from classes.State import *
from classes.Problem import *
from functionalities.Export import*
from classes.Frontier_Deque import*
from classes.Frontier_Heapq import*
from classes.Frontier_List import*
from classes.State_space import *
import resource
import time

def main():
    menu_strategies()
   
def print_Menu():
    print("Welcome to our water sort agent solver\nSelect the option you want to:")
    print("0. BREADTH ALGORITHM")
    print("1. DEPTH ALGORITHM")
    print("2. UNIFORM COST ALGORITHM")
    print("3. A* ALGORITHM")
    print("4. GREEDY  ALGORITHM")
    print("5. Exit")
    print("----------------------------------------------------------------------\n")

def print_menu_funcionalities():
    print("0. Import json")
    print("1. Test frontier")
    print("2. Export the solution")
    print("3. Back")
    print("----------------------------------------------------------------------\n")  

def menu_strategies():

    while True:
        while True:
            print_Menu() 
            try:
                user_option = int(input("Select the strategy you want to analyze: "))
                break
            except:
                print("\nERROR: You have to choose an option between 0 and 5.\n")
        if user_option not in range(6) and isdigit(user_option) == False:
            print("\nERROR: You have to choose an option between 0 and 5.\n")
            continue
        else:
            if user_option ==0:
                print("BREADTH ALGORITHM")
                menu_main_functionality('BREADTH')
            elif user_option==1:
                print("DEPTH ALGORITHM")
                menu_main_functionality('DEPTH')
            elif user_option == 2:
                print("UNIFORM COST ALGORITHM")
                menu_main_functionality('UNIFORM')
            elif user_option == 3:
                print("A* ALGORITHM")
                menu_main_functionality('A')
            elif user_option == 4:
                print("GREEDY ALGORITHM")
                menu_main_functionality('GREEDY')
            elif user_option==5:
                print("Bye!")
                break  

        

def menu_main_functionality(strategy):
    problem = Problem(0, [], State([]))
    already_imported = False
    while True:
        while True:
            print_menu_funcionalities()
            try:
                user_option = int(input("Select a functionality: "))
                break
            except:
                print("\nERROR: You have to choose an option between 0 and 3.\n")
        if user_option not in range(4) and isdigit(user_option) == False:
            print("\nERROR: You have to choose an option between 0 and 3.\n")
            continue
        elif (user_option == 1 or user_option == 2) and already_imported == False:
            print("\nERROR: You have to import a problem before selecting option 1 or 2.\n")
        else:
            if user_option == 0:
                    
                path_json = input("Introduce the path of the problem:")
                problem = read_States_Txt(path_json, 1)
                if problem is not None:
                    print("Problem imported successfully!")
                    already_imported = True
                else:
                    already_imported = False

            elif user_option==1:
                random_heuristic = "{0:.2f}".format(uniform(0.0, 1000.0))
                random_value = "{0:.2f}".format(uniform(0.0, 1000.0))
                initial_node = Node(0, 0.0, problem.initState, None, None, 0, random_heuristic, random_value)
                if(initial_node == None):
                    continue
                else:
                    dq_frontier = Frontier_Deque()
                    hq_frontier = Frontier_Heapq()
                    list_frontier = Frontier_List()
                    dq_frontier.push(initial_node)
                    hq_frontier.push(initial_node)
                    list_frontier.push(initial_node)
                    #Test deque frontier
                    #test_frontier(dq_frontier)
                    #Test heapque frontier
                    test_frontier(hq_frontier)
                    #Test list frontier
                    #test_frontier(list_frontier)
            elif user_option == 2:
                state_space = State_space(strategy, problem)
                node_solution = state_space.search()
                if node_solution == 1:
                    print(f"\nERROR: Maximum depth ({problem.max_depth}) reached.\n")
                else:
                    state_space.export(node_solution)
            elif user_option == 3:
                print("Bye!")
                break         

def test_frontier(frontier):
    number_nodes = 1
    id_node = 1
    minimum_time = 0
    maximum_time = 0
    sum_times = 0
    average_time = 0
    while resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6 < 0.1:
        try:
            node = frontier.pop()
            number_nodes -= 1
            successors = State().successor_fn(node.state)
            depth = node.depth + 1
            for successor in successors:
                random_heuristic = "{0:.2f}".format(uniform(0.0, 1000.0))
                random_value = "{0:.2f}".format(uniform(0.0, 1000.0))
                node = Node(id_node, node.cost+successor[2], successor[1], node.ID, successor[0], depth, random_heuristic, random_value)
                pre_time = time.time()
                frontier.push(node)
                post_time = time.time()
                current_time = post_time-pre_time
                sum_times += current_time
                if(id_node == 1):
                    minimum_time = current_time
                    maximum_time = current_time
                else:
                    if(current_time < minimum_time):
                        minimum_time = current_time
                    if(current_time > maximum_time):
                        maximum_time = current_time
                number_nodes += 1
                id_node += 1
                average_time = sum_times/(id_node-1)
        except MemoryError:
            print("Memory consumed: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6) + " GB" + "\nNumber of elements stored: " + str(number_nodes) + " elements" + "\nMinimum insertion time: " + str(minimum_time) + " seconds" + "\nMaximum insertion time: " + str(maximum_time) + " seconds" + "\nAverage insertion time: " + str(average_time) + " seconds\n")
    print("Memory consumed: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6) + " GB" + "\nNumber of elements stored: " + str(number_nodes) + " elements" + "\nMinimum insertion time: " + str(minimum_time) + " seconds" + "\nMaximum insertion time: " + str(maximum_time) + " seconds" + "\nAverage insertion time: " + str(average_time) + " seconds\n")
    
if __name__ =='__main__':
    main()