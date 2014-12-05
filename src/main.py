'''
Created on Dec 1, 2014

@author: Disley
'''

from dice import d4, d6, d10
from dice.dN import dN
from tables import common_curiosity, significant_features, features_of_interest, whos_in_charge
from House import House
from random import randint, gauss, choice
from math import cos, sin, pi
import pygame, sys
from pygame.locals import QUIT
from copy import copy, deepcopy

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
    
    town_size = 10 + d10.roll()
    houses = [House(d6.roll()) for x in range(0, town_size)]
    feature = d4.roll()
    d12 = dN(12)
    d3 = dN(3)
    num_features = d3.roll()
    other_features = [d12.roll() for x in range(0, num_features)]
    
    houses_groups = dict()
    
    for house in houses:
        if house.number in houses_groups:
            houses_groups[house.number] += 1
            house.letter = chr(64 + houses_groups[house.number])
        else:
            houses_groups[house.number] = 1
            
    print(houses_groups)
    
    houses_commonalities = dict()
    
    for key, value in houses_groups.items():
        if(key < feature):
            if(value > 30): value = 30
            houses_commonalities[key] = common_curiosity[value*key]
        else:
            reroll = 0
            for x in range(0, value):
                reroll += d6.roll()
            if(reroll > 30): reroll = 30
            houses_commonalities[key] = common_curiosity[reroll]
            
    print(houses_commonalities)
    significant_feature = significant_features[feature][d4.roll()]
    print(significant_feature)
    small_features = []
    for other_feature in other_features:
        small_features.append((other_feature, features_of_interest[other_feature]))
    print(small_features)
    
    in_charge = whos_in_charge[d10.roll()]
    print(in_charge)
    
    w, h = 50, 50
    draw_w, draw_h = 35, 35
    
    num_squares = len(houses) + 1 + num_features
    
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
#                     pygame.draw.rect(windowSurfObj, (0, 0, 0), (new_x, new_y, draw_w, draw_h))
                new_center = (new_x, new_y)
#                 new_center = (400, 400)
                r_vector = random_polar(100, 0, 180)
                new_x = new_center[0] + r_vector[0]*cos((pi/180)*r_vector[1])
                new_y = new_center[1] + r_vector[0]*sin((pi/180)*r_vector[1])
        else:
            squares.append((new_x, new_y, w, h))
#             pygame.draw.rect(windowSurfObj, (0, 0, 0), (new_x, new_y, draw_w, draw_h))

    font = pygame.font.Font(None, 22)

    for house in houses:
        house_rect = choice(squares)
        squares.remove(house_rect)
        house.set_position(house_rect[0], house_rect[1])
        
        if(house.number == 1):
            house_color = (10, 10, 10)
        elif(house.number == 2):
            house_color = (240, 10, 10)
        elif(house.number == 3):
            house_color = (10, 240, 240)
        elif(house.number == 4):
            house_color = (130, 130, 240)
        elif(house.number == 5):
            house_color = (200, 200, 10)
        else:
            house_color = (240, 10, 240)            
        
        pygame.draw.rect(windowSurfObj, house_color, (house_rect[0], house_rect[1], draw_w, draw_h))
        number = font.render(str(house.number) + ": " + house.letter, 1, (255, 255, 255))
        windowSurfObj.blit(number, (house_rect[0]+3, house_rect[1]+10))
        
    for house in houses:
        print(len(houses))
        print("House {0}:{1} contains: {2}".format(house.number, house.letter, house.description))
        tmp_houses = copy(houses)
        tmp_houses.remove(house)
        house.finalize_regarding(tmp_houses)
        print(house.relationship + " Regarding " + house.regarding.lower() + " which is house: {0}:{1}".format(house.regarding_num,house.regarding_letter))
        
    feature_rect = choice(squares)
    squares.remove(feature_rect)
    pygame.draw.rect(windowSurfObj, (0, 255, 0), (feature_rect[0], feature_rect[1], draw_w, draw_h))
    number = font.render(str(feature), 1, (255, 255, 255))
    windowSurfObj.blit(number, (feature_rect[0]+13, feature_rect[1]+10))
    
    for other_feature in other_features:
        other_rect = choice(squares)
        squares.remove(other_rect)
        pygame.draw.rect(windowSurfObj, (0, 0, 255), (other_rect[0], other_rect[1], draw_w, draw_h))
        number = font.render(str(other_feature), 1, (255, 255, 255))
        windowSurfObj.blit(number, (other_rect[0]+13, other_rect[1]+10))
            
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
    