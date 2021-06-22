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

player_image = pygame.image.load("spinning.png").convert_alpha()

arrow=pygame.Rect(0,0,10,10)
arrow_key = pygame.image.load("arrow.png").convert_alpha()

screen.blit(arrow_key ,arrow) 
pygame.display.update()


angle=0
change=0



while True:
  screen.blit(background_image,[0,0])
  screen.blit(arrow_key,[180,120])
  #angle=angle+change
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
    if event.type == pygame.KEYUP:
      if  event.key == pygame.K_ESCAPE:
       change= 0
           
    if event.type == pygame.KEYDOWN:
              
      if event.key == pygame.K_LEFT:
        change=3
      if event.key==pygame.K_RIGHT:
          change=-3
   
  
  angle += change
  
  pygame.draw.rect(screen, (255,255,255), player)
  
   
  newimage=pygame.transform.rotate(player_image,angle) 
  
  screen.blit(newimage ,player)
  pygame.display.update()
  clock.tick(30)
