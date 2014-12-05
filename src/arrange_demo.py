'''
Created on Dec 1, 2014

@author: Disley
'''

import pygame, sys
from pygame.locals import QUIT
from dice import d10
from random import randint, gauss
from math import sin, cos, pi

def random_polar(r_sigma, min_theta, max_theta):
    r = gauss(0, r_sigma)
    theta = randint(min_theta, max_theta)
    
    return (r, theta)

def test_collision(rect1, possibles):
    collide = False
    for rect2 in possibles:
#         print("Checking possible collision...")
        xlength = abs(rect2[0] - rect1[0])
        xhalfwidth1 = rect1[2]/2
        xhalfwidth2 = rect2[2]/2
        
        xgapBetween = xlength - xhalfwidth1 - xhalfwidth2
        
        if(xgapBetween < 0):
            xCollide = True
        else:
            xCollide = False
            
        ylength = abs(rect2[1] - rect1[1])
        yhalfwidth1 = rect1[3]/2
        yhalfwidth2 = rect2[3]/2
        
        ygapBetween = ylength - yhalfwidth1 - yhalfwidth2
        
        if(ygapBetween < 0):
            yCollide = True
        else:
            yCollide = False
            
        if(xCollide and yCollide):
            collide = True
            break
        
    return collide

if __name__ == '__main__':
    pygame.init()
    windowSurfObj = pygame.display.set_mode((800, 800))
    windowSurfObj.fill(pygame.Color(255, 255, 255))
    
    w, h = 50, 50
    draw_w, draw_h = 35, 35
    
    num_squares = 13 + d10.roll()
    
    squares = []
        
    for i in range(0, num_squares):
        center = (400, 400)
        r_vector = random_polar(85, 0, 180)
        new_x = center[0] + r_vector[0]*cos((pi/180)*r_vector[1])
        new_y = center[1] + r_vector[0]*sin((pi/180)*r_vector[1])
        
        if(squares):
            collision = True
            while collision:
                if(not test_collision((new_x, new_y, w, h), squares) and 0 < new_x < 800-w and 0 < new_y < 800-h):
                    collision = False
                    squares.append((new_x, new_y, w, h))
                    pygame.draw.rect(windowSurfObj, (0, 0, 0), (new_x, new_y, draw_w, draw_h))
                new_center = (new_x, new_y)
#                 new_center = (400, 400)
                r_vector = random_polar(100, 0, 180)
                new_x = new_center[0] + r_vector[0]*cos((pi/180)*r_vector[1])
                new_y = new_center[1] + r_vector[0]*sin((pi/180)*r_vector[1])
        else:
            squares.append((new_x, new_y, w, h))
            pygame.draw.rect(windowSurfObj, (0, 0, 0), (new_x, new_y, draw_w, draw_h))
            
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()