import pygame
import random

pygame.init()
screen_size = [1000, 800]
screen_size2 = (screen_size[0] / 2, screen_size[1] - 20)
screen = pygame.display.set_mode(screen_size)
into = True

blanco = 255,255,255
azul = 0,0,255
amarillo = 255, 255, 0
verde = 0, 255, 0

speed = 1

started = True

ronda = 1
st_zombies = 2
st_speed = 0.01

zombies = []

playercords = [200, 200]

def gameover(reason) :
    print("Game over")

def nuevaronda(n, zombies) :
    d_zombies = 0
    while d_zombies != n * st_zombies:
        print("a")
        zombies.append([random.randint(0, screen_size[0]), random.randint(10, 60)])
        d_zombies += 1

while into:
    if started :
        zombies = []
        nuevaronda(ronda, zombies)
        started = False
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
        if x[1] < screen_size2[1] :
            print(x[1], screen_size2[1])
            x[1] += st_speed * ronda * 4
        else :
            into = False
            gameover("Un zombi llego al final del mapa")
        pygame.draw.circle(screen, verde, tuple(x), 25)

    pygame.display.update()
pygame.quit()
