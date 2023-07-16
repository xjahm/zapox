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

speed = 0.1

started = True

ronda = 1
st_zombies = 2
st_speed = 0.01

zombies = []

playercords = [200, 200]

def gameover(reason) :
    print("Game over, round: "+ronda)

def nuevaronda(n, zombies) :
    d_zombies = 0
    while d_zombies != n * st_zombies:
        zombies.append([random.randint(0, screen_size[0]), random.randint(10, 60)])
        d_zombies += 1

def escercano(x, z, r) :
    con1 = False
    con2 = False
    if round(x[0]) < round(z[0]) + r and round(x[0]) > round(z[0]) - r :
        con1 = True
    if round(x[1]) < round(z[1]) + r and round(x[1]) > round(z[1]) - r :
        con2 = True
    if con1 and con2 :
        return True
    else :
        return False


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
        elif keys[pygame.K_a]:
            speed += 0.001
        elif keys[pygame.K_d]:
            speed -= 0.001


    screen.fill((255, 255, 255))
    
    #   Player
    pygame.draw.circle(screen,  azul, tuple(playercords), 30)
    
    #   Treasure
    pygame.draw.circle(screen, amarillo, screen_size2, 20)

    if len(zombies) != 0 :
        for x in zombies :

            if escercano(playercords, x, 3) :
                zombies.remove(x)
            elif x[1] < screen_size2[1] :
                x[1] += st_speed * ronda * 4
            else :
                into = False
                gameover("Un zombi llego al final del mapa")
            pygame.draw.circle(screen, verde, tuple(x), 30)
    else :
        ronda += 1
        nuevaronda(ronda, zombies)

    pygame.display.update()

pygame.quit()
