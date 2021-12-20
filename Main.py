#!/usr/bin/python3
#--coding: utf-8; mode:python--

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
    print("3. Exit")
    print("----------------------------------------------------------------------\n")  

def menu_strategies():

    while True:
           
        print_Menu()       
        user_option = int(input("Select the strategy you want to analyze: "))

        if user_option in range(6):
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
                menu_main_functionality('GREEDY')
            elif user_option == 4:
                print("GREEDY ALGORITHM")
                menu_main_functionality('A*')
            elif user_option==5:
                print("Bye!")
                break  
        else:
            print('ERROR: valid option 1 to 6')

        

def menu_main_functionality(strategy):
    path_json="/home/adrian/Escritorio/intelligent-system/json_files/p0.json"###########
    problem = Problem(0, [], State([]))

    problem = read_States_Txt(path_json, 1)#############

    while True:
        print_menu_funcionalities()
        user_option = int(input("Select a functionality: "))
        if user_option in range(4):
            if user_option ==0:
                
                path_json = input("Introduce the path of the problem:")

                problem = read_States_Txt(path_json, 1)

                for bottle in problem.initState.bottles:
                    bottle.toString()

            elif user_option==1:
                initial_node = read_problem(path_json)
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
                    test_frontier(dq_frontier)
                    #Test heapque frontier
                    test_frontier(hq_frontier)
                    #Test list frontier
                    test_frontier(list_frontier)
            elif user_option == 2:
                state_space = State_space(strategy, problem)
                node_solution = state_space.search()
                state_space.export(node_solution)
            elif user_option == 3:
                print("Bye!")
                break         
        else:
            print('ERROR: valid option 1 to 4')

def test_frontier(frontier):
    number_nodes = 1
    id_node = 1
    minimum_time = 0
    maximum_time = 0
    sum_times = 0
    average_time = 0
    while resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6 < 0.025:
        try:
            previous_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6
            node = frontier.pop()
            number_nodes -= 1
            random_heuristic = uniform(0.0, 1000.0)
            random_value = uniform(0.0, 1000.0)
            random_cost = uniform(0.0, 1000.0)
            node = Node(id_node, random_cost, State([[1,2,3],[1,2]]), node.ID, [1,2,3], node.depth + 1, random_heuristic, random_value)
            while True:
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
                average_time = sum_times/id_node-1                  
        except MemoryError:
            print("Memory consumed: " + str((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6)-previous_memory) + " GB" + "\nNumber of elements stored: " + str(number_nodes) + " elements\n" + "\nMinimum insertion time: " + str(minimum_time) + " seconds\n" + "\nMaximum insertion time: " + str(maximum_time) + " seconds\n" + "\nAverage insertion time: " + str(average_time) + " seconds\n")
            break
    print("Memory consumed: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6) + " GB" + "\nNumber of elements stored: " + str(number_nodes) + " elements\n" + "\nMinimum insertion time: " + str(minimum_time) + " seconds\n" + "\nMaximum insertion time: " + str(maximum_time) + " seconds\n" + "\nAverage insertion time: " + str(average_time) + " seconds\n")
    
if __name__ =='__main__':
    main()