# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:36:00 2021

@author: dell
"""

import pygame


pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Asteroid")
background_image = pygame.image.load("bg2.jpg").convert()


BLUE=(0,0,255)

player=pygame.Rect(150,200,200,200)

#Code to Upload image of spinner here

arrow=pygame.Rect(0,0,10,10)
#Code to upload image of arrow

screen.blit(arrow_key ,arrow) 
pygame.display.update()


angle=0
speed=0



while True:
  
    #blit image of back ground  and arrow.
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
    if event.type == pygame.KEYUP:
      #Write Codee Here:
       change= 0
           
    if event.type == pygame.KEYDOWN:
              
      if event.key == pygame.K_LEFT:
        speed=3
      if event.key==pygame.K_RIGHT:
          speed=-3
   
  
  angle += change
  
  pygame.draw.rect(screen, (255,255,255), player)
  
   
  newimage=pygame.transform.rotate(player_image,angle) 
  
  screen.blit(newimage ,player)
  pygame.display.update()
  clock.tick(30)
