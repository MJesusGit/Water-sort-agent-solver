from classes.Node import *
from classes.Frontier_Deque import *
from classes.Frontier_Heapq import *
from classes.Frontier_List import *
from classes.Node import *
from classes.State import *
from functionalities.Import import *

path_json='/home/adrian/Escritorio/intelligent-system/json_files/prueba.json'

problem = read_States_Txt(path_json, 1)
lista_sucesores = State().successor_fn(problem.initState)
for sucesor in lista_sucesores:
    print("\n")
    print(sucesor)
    for bottle in sucesor[1].bottles:
        bottle.toString()
    print("\n")

lista_sucesores = State().successor_fn(lista_sucesores[0][1])
