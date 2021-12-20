#!/usr/bin/python3
#--coding: utf-8; mode:python--
import os
from classes.State import *

def export_method(list_of_bottles):
    '''It will show the solution of the problem'''
    try:
        string_export = "["
        for i in range(len(list_of_bottles)):
            if i == len(list_of_bottles)-1:
                string_export = f"{string_export}{list_of_bottles[i].state}]"
            else:
                string_export = f"{string_export}{list_of_bottles[i].state},"
        os.chdir("./files_exported")
        folder=os.getcwd()
        content=os.listdir(folder)
        file_number = 0
        if len(content)>0:
            for file in content:
                file_number = int(file[len(file)-6])
        else:
            file_number = 0
        file_number = file_number + 1
        with open(f'./exported_state_{file_number}.json', "w") as file:
            file.write(string_export)
    except ValueError:
        print(" ERROR: state could not be exported ")
