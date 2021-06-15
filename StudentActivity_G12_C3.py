# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:26:20 2021

@author: dell
"""

import pygame,sys

#initialising pygame and its functions 
-----------------
# creating game window and title
screen = pygame.display.set_mode((400,600))
pygame.display.set---------------

# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()
screen.fill((0,0,0))
--------------------------


#Creating Players 
------------------------------
player_image = pygame.image.load("player.png").convert_alpha()
screen.blit(player_image , player)
pygame.display.update()


angle=0
change=0

press=False

while True:
  screen.blit(background_image,[0,0])
  #event loop to check which key is print
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
        ---------------
      if event.key == pygame.K_UP:
        press=False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        ---------------
      if event.key ==pygame.K_RIGHT:
        change = -30
      if event.key == pygame.K_UP:
        press=True;   
        
  angle += change
  angle=angle % 360
  -------------------------

 
  ------------------------
  
  
  pygame.display.update()






