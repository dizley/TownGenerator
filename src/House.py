'''
Created on Dec 1, 2014

@author: Disley
'''

from dice import d4, d6, d20
from dice.dN import dN
from tables import relationships

class House():
    '''
    classdocs
    '''


    def __init__(self, roll):
        '''
        Constructor
        '''
        self.number = roll
        self.letter = 'A'
        d8 = dN(8)
        self.occupants_roll = d8.roll()
        self.init_occupants(self.occupants_roll)
        self.relationship_roll = d20.roll()
        self.init_relationship(self.relationship_roll)
        self.regarding_roll = d6.roll()
        self.init_regarding(self.regarding_roll)
            
    def init_occupants(self, roll):
        if(roll) == 1:
            self.adults = 2
            d7 = dN(7)
            self.children = d7.roll() - 1
            self.description = "Couple with {0} children.".format(self.children)
        elif(roll) == 2:
            self.adults = 1
            d7 = dN(7)
            self.children = d7.roll() - 1
            self.description = "Single adult with {0} children".format(self.children)
        elif(roll) == 3:
            self.adults = 1
            self.children = 0
            self.description = "Bachelor/Bachelorette"
        elif(roll) == 4:
            d8 = dN(8)
            reroll = d8.roll()
            if(reroll == 4): reroll = 1
            self.init_occupants(reroll)
            specialist = d4.roll()
            if(specialist == 1):
                self.description = "Magic-User " + self.description
            elif(specialist == 2):
                self.description = "Cleric " + self.description
            elif(specialist == 3):
                self.description = "Specialist " + self.description
            elif(specialist == 4):
                self.description = "Fighter " + self.description
        elif(roll) == 5:
            self.adults = 1
            self.children = 0
            self.description = "Widow/Widower"
        elif(roll) == 6:
            self.adults = d6.roll()
            self.children = 0
            self.description = "{0} associates".format(self.adults)
        elif(roll) == 7:
            self.adults = d4.roll()
            self.children = d6.roll() - 1
            self.description = "Extended family"
        elif(roll) == 8:
            self.adults = d4.roll() + 1
            self.children = 0
            self.description = "{0} friends and lovers".format(self.adults)
            
    def init_relationship(self, roll):
        self.relationship = relationships[roll]
        
    def init_regarding(self, roll):
        if(roll > 3): location = "furthest"
        else: location = "nearest"
        
        self.regarding_sort_type = location
        
        if(roll == 1 or roll == 5):
            even_or_odd = "odd"
        elif(roll == 2 or roll == 6):
            even_or_odd = "even"
        else:
            even_or_odd = "matching"
            
        self.regarding_num_type = even_or_odd
            
        d4_roll = d4.roll()
        suffixes = ["th", "st", "nd", "rd", "th"]
        
        self.regarding_d4_roll = d4_roll
        
        self.regarding = "The {0} {1} {2} number".format(str(d4_roll) + suffixes[d4_roll], location,even_or_odd)
        
    def set_position(self, x, y):
        self.x = x
        self.y = y    
    
    def finalize_regarding(self, houses):
        distances = []
        for house in houses:
            if(self.regarding_num_type == "odd"):
                if house.number%2:
                    distances.append(((house.x - self.x)**2 + (house.y - self.y)**2, house.number, house.letter))
            elif(self.regarding_num_type == "even"):
                if not house.number%2:
                    distances.append(((house.x - self.x)**2 + (house.y - self.y)**2, house.number, house.letter))
            elif(self.regarding_num_type == "matching"):
                if house.number == self.number:
                    distances.append(((house.x - self.x)**2 + (house.y - self.y)**2, house.number, house.letter))

        if distances:
            if(self.regarding_sort_type == "furthest"):
                sorted_by_distance = sorted(distances, key=lambda tup: tup[0], reverse=True)
            else:
                sorted_by_distance = sorted(distances, key=lambda tup: tup[0])
                
            if(self.regarding_d4_roll > len(sorted_by_distance)):
                self.regarding_num = sorted_by_distance[-1][1]
                self.regarding_letter = sorted_by_distance[-1][2]
            else:
                self.regarding_num = sorted_by_distance[self.regarding_d4_roll-1][1]
                self.regarding_letter = sorted_by_distance[self.regarding_d4_roll-1][2]
        else:
            self.regarding_num = self.number
            self.regarding_letter = self.letter
            
#         print((regarding_num, regarding_letter))
            
        