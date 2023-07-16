import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
into = True
blanco = 255,255,255
azul = 0,0,255
speed = 0.1

playercords = [0, 0]

while into:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            into = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playercords[0] -= speed
    elif keys[pygame.K_RIGHT]:
        playercords[0] += speed
    elif keys[pygame.K_UP]:
        playercords[1] -= speed
    elif keys[pygame.K_DOWN]:
        playercords[1] += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen,  azul, tuple(playercords), 30)
    pygame.display.update()
pygame.quit()
