import pygame


pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((600,600))

BLUE=(0,0,255)

player=pygame.Rect(150,200,200,200)

player_image = pygame.image.load("spinning.png").convert_alpha()

arrow=pygame.Rect(0,0,10,10)
arrow_key = pygame.image.load("arrow.png").convert_alpha()

screen.blit(arrow_key ,arrow) 
pygame.display.update()

angle=0
speed=0

while True:
    screen.fill((0,0,0))
    screen.blit(arrow_key,[180,120])
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
           speed= 0
             
      if event.type == pygame.KEYDOWN:      
        if event.key == pygame.K_LEFT:
            speed=3
        if event.key==pygame.K_RIGHT:
            speed=-3
     
    angle += speed  
     
    newimage=pygame.transform.rotate(player_image,angle) 
    screen.blit(newimage ,player)
    
    pygame.display.update()
    clock.tick(30)
