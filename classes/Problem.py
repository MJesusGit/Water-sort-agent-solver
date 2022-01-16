#!/usr/bin/python3
#-*-coding: utf-8; mode:python-*-

class Problem():
    def __init__(self,id_problem,bottleSize,initState):
        self.id=id_problem
        self.bottleSize=bottleSize
        self.initState=initState
        self.max_depth=1000000
