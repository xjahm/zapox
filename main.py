import pygame
pygame.init()
screen_size = [1000, 800]
screen_size2 = (screen_size[0] / 2, screen_size[1] / 2)
screen = pygame.display.set_mode(screen_size)
into = True
blanco = 255,255,255
azul = 0,0,255
amarillo = 255, 255, 0
speed = 1

ronda = 1
zombies = 0
st_zombies = 10
st_speed = 0.01

zombies = []

playercords = [200, 200]

def gameover(reason) :
    print("Game over")

while into:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            into = False
    
    keys = pygame.key.get_pressed()
    if playercords[0] < 1000 and playercords[1] < 800 and playercords[0] > 0 and playercords[1] > 0 :
        if keys[pygame.K_LEFT]:
            playercords[0] -= speed
        elif keys[pygame.K_RIGHT]:
            playercords[0] += speed
        elif keys[pygame.K_UP]:
            playercords[1] -= speed
        elif keys[pygame.K_DOWN]:
            playercords[1] += speed

    screen.fill((255, 255, 255))
    
    #   Player
    pygame.draw.circle(screen,  azul, tuple(playercords), 30)
    
    #   Treasure
    pygame.draw.circle(screen, amarillo, screen_size2, 20)

    for x in zombies :
        print(x)

    pygame.display.update()
pygame.quit()
