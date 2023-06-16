# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 07:04:17 2023

@author: bryan
"""

import pygame,os,sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((800, 600))

background = pygame.Color(100, 149, 237)

while True:
    RGB1 = random.randint(0,255)
    RGB2 = random.randint(0,255)
    RGB3 = random.randint(0,255)
    background = pygame.Color(RGB1, RGB2, RGB3)
    surface.fill(background)
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()
    fpsClock.tick(1)