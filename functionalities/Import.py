#!/usr/bin/python3
#--coding: utf-8; mode:python--
# pylint: disable=invalid-name
from random import uniform
from classes.Bottle import *
from classes.Node import *
from classes.State import *
from classes.Problem import *


def read_States_Txt(input, type_input):
    """To read json of the first and third subtasks"""
    try:
        ''' json first subtask'''
        if type_input == 0:
            with open(input, "r") as fileState:
                for line in fileState:
                    return line_to_bottles(str(line))
        
        elif type_input == 1:
            with open(input, "r") as file_problem:
                problem_dict = json.load(file_problem)
            problem=Problem(str(problem_dict["id"]),str(problem_dict["bottleSize"]),State(line_to_bottles(str(problem_dict["initState"]),problem_dict["bottleSize"])))
            return problem
    except FileNotFoundError:
        print("ERROR: READING FILE .json")

def line_to_bottles(line,MAX_amount=None):
    """Identify the bottles, liquids , colors and quantity"""
    line = line.replace(" ", "")
    open_caracter = "["
    close_caracter = "]"
    comma = ","
    counter = 0
    start_liquid = False
    is_colour = True
    list_of_bottles = []
    if MAX_amount is not None:
        bottle = Bottle(MAX_amount)
    else:
        bottle = Bottle()
    is_liquid = []
    is_true= True
    is_false= False
    for caracter in line:
        if caracter == open_caracter:
            counter = counter + 1
            if counter == 1:
                pass
            elif counter == 2:
                if MAX_amount is not None:
                    bottle = Bottle(MAX_amount)
                else:
                    bottle = Bottle()
            elif counter == 3:
                start_liquid = is_true
        elif caracter == close_caracter:
            counter = counter - 1
            if counter == 2:
                start_liquid = is_false
                is_colour = is_true
                bottle.insert_liquid_import(is_liquid)
                is_liquid = []
            elif counter == 1:
                list_of_bottles.append(bottle)
            elif counter == 0:
                return list_of_bottles
        elif caracter == comma:
            if start_liquid == is_true:
                is_colour = not is_colour
        elif caracter.isnumeric:
            if is_colour:
                is_liquid.append(int(caracter))
            elif not is_colour:
                is_liquid.append(int(caracter))
        elif caracter.isspace():
            continue
    return None



    

