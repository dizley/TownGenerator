'''
Created on Dec 1, 2014

@author: Disley
'''

from random import randint

class dN():
    '''
    classdocs
    '''


    def __init__(self, N):
        '''
        Constructor
        '''
        self.N = N
        
    def roll(self):
        return randint(1, self.N)