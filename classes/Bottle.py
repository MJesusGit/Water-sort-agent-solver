#!/usr/bin/python3
#-*-coding: utf-8; mode:python-*-
import json
import sys

class Bottle():

    def __init__(self,MAX_amount=10):
        self.colours=[]
        self.MAX_amount=MAX_amount
        self.liquids=[]
        self.current_amount = 0

    def __len__(self):
        return len(self.liquids)

    def getColourLast(self):
        if self.current_amount > 0:
            return self.liquids[0][0]
        else:
            return None

    def getQuantityLast(self):
        if self.current_amount > 0:
            return self.liquids[0][1]
        else:
            return 0

    def insert_colour(self, new_colour):
        if(len(self.colours) > 0):
            if new_colour in self.colours:
                return
        
        if(new_colour > -1 ):
            self.colours.append(new_colour)
        else:
            print(f"ERROR: colour {new_colour} does not exist")
            sys.exit()
    
    def insert_liquid_import(self, new_liquid):
        if len(self.liquids)>0:
            if self.liquids[len(self.liquids)-1][0] == new_liquid[0]:
                print("ERROR: two equal colours in a row.")
                sys.exit()
        self.liquids.append(new_liquid)
        self.insert_colour(new_liquid[0])
        self.current_amount += new_liquid[1]
        if self.current_amount > self.MAX_amount:
            print("ERROR: more liquid amount than expected.")
            sys.exit()

    def insert_liquid(self, new_liquid):
        if len(self.liquids) > 0:
            self.liquids[0][1] += new_liquid[1]
        elif len(self.liquids) == 0:
            self.liquids.append(new_liquid)
            self.insert_colour(new_liquid[0])
        self.current_amount += new_liquid[1]

    def remove_liquid(self):
        removed_liquid = self.liquids[0]
        self.liquids.pop(0)
        found_colour = False
        for liquid in self.liquids:
            if liquid[0] == removed_liquid[0]:
                found_colour = True
                break
        if found_colour == False:
            self.colours.remove(removed_liquid[0])
        self.current_amount -= removed_liquid[1]
    
    def isPossible_to_add_quantity(self, new_bottle):
        return (self.current_amount + new_bottle.getQuantityLast()) <= self.MAX_amount
    
    def toString(self):
        colours_to_print = "\nColours: "
        for i in range(len(self.colours)):
            if(i == len(self.colours)-1):
                colours_to_print = colours_to_print + f"{self.colours[i]}"
            else:
                colours_to_print = colours_to_print + f"{self.colours[i]}, "
        print(colours_to_print)

        print(f"Maximum amount: {self.MAX_amount}")

        state_to_print = "State: "
        for i in range(len(self.liquids)):
            if(i == len(self.liquids)-1):
                state_to_print = state_to_print + f"{self.liquids[i]}"
            else:
                state_to_print = state_to_print + f"{self.liquids[i]}, "
        print(state_to_print)
