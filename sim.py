
import random as rnd
from typing import Sized

class Voter():
    def __init__(self):
        self.lean = "_"
    
    def __init__(self, lean):
        self.lean = lean
    
    def set_lean(self, voter_lean):
        self.lean = voter_lean

class Community():
    def __init__(self):
        self.voter_list = [] # a community is a collection of voters
        self.voter_districts = [] # a community is also a collection of districts, voters belong in districts
        self.voter_lean_blue = 0
        self.voter_lean_red = 0
        self.voter_lean_grey = 0
    
    def Add_Voter(self, voter):
        self.voter_list.append(voter)
    
    def Add_District(self, district):
        self.voter_districts.append(district)
    
    def Get_Voter_String(self):
        Voter_String = ""
        for v in self.voter_list:
            Voter_String = Voter_String + v.lean
        return Voter_String
    
    def Get_Community_Lean(self):
        self.voter_lean_blue = 0
        self.voter_lean_red = 0
        self.voter_lean_grey = 0
        
        for voter in self.voter_list:
            if voter.lean == "+":
                self.voter_lean_blue = self.voter_lean_blue + 1
            elif voter.lean == "-":
                self.voter_lean_red = self.voter_lean_red + 1
            else:
                self.voter_lean_grey = self.voter_lean_grey + 1
        
        if self.voter_lean_blue >= self.voter_lean_red and self.voter_lean_blue >= self.voter_lean_grey:
            community_lean = "Blue"
        elif self.voter_lean_red >= self.voter_lean_blue and self.voter_lean_red >= self.voter_lean_grey:
            community_lean = "Red"
        elif self.voter_lean_grey >= self.voter_lean_blue and self.voter_lean_grey >= self.voter_lean_red:
            community_lean = "Grey"
        
        return community_lean


