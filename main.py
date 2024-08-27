from random import *
from copy import *
import pygame
pygame.init()

grid = [
    [0,0,0,0],
    [0,2,0,0],
    [2,0,2,0],
    [2,2,4,8]
]
score = 0
randomize = 1
respawn = 1

pygame.display.set_caption("2048 !")
screen = pygame.display.set_mode((1080,720))

couleur = [248, 184, 102]

def reinit(grid):
    grid = init(grid)
    return grid

def init(grid):
    grid = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    score = 0
    grid_fake = []
    for i in range(4):
        for j in range(4):
            grid_fake.append([i,j])
    choix = choice(grid_fake)
    del(grid_fake[grid_fake.index(choix)])
    choix2 = choice(grid_fake)
    if randint(1,100) < 90:
        grid[choix[0]][choix[1]] = 2
    else:
        grid[choix[0]][choix[1]] = 4
    if randint(1,100) < 90:
        grid[choix2[0]][choix2[1]] = 2
    else:
        grid[choix2[0]][choix2[1]] = 4
    return grid

def spawn(grid):
    liste = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                liste.append([i,j])
    element = choice(liste)
    if randint(1,100) < 90:
        grid[element[0]][element[1]] = 2
    else:
        grid[element[0]][element[1]] = 4
    return grid

def aff(ggg):
    print("****************")
    for i in ggg:
        print(i)

def check(grid):
    ch = True
    for i in grid:
        for j in i:
            if j == 0:
                ch = False
    if not ch:
        perdu = True
        print("perdu !!!!")

def droite(grid):
    global score
    test = deepcopy(grid)
    grid_b = []
    for a in grid:
        if a[3] == 0:
            a[3] = a[2]
            a[2] = 0
        elif a[3] == a[2]:
            score += a[2] * 2
            a[3] = a[2] * 2
            a[2] = 0
        if a[2] == 0:
            if a[3] == 0:
               a[3] = a[1]
               a[1] = 0
            elif a[3] == a[1]:
                score += a[1] * 2
                a[3] = a[1] * 2
                a[1] = 0
            else:
                a[2] = a[1]
                a[1] = 0
        elif a[2] == a[1]:
            score += a[1] * 2
            a[2] = a[1] * 2
            a[1] = 0
        if a[1] == 0:
            if a[2] == 0:
                if a[3] == 0:
                    a[3] = a[0]
                    a[0] = 0
                elif a[3] == a[0]:
                    score += a[0] * 2
                    a[3] = a[0] * 2
                    a[0] = 0
                else:
                    a[2] = a[0]
                    a[0] = 0
            elif a[2] == a[0]:
                score += a[0] * 2
                a[2] = a[0] * 2
                a[0] = 0
            else:
                a[1] = a[0]
                a[0] = 0
        elif a[1] == a[0]:
            score += a[0] * 2
            a[1] = a[0] * 2
            a[0] = 0
        grid_b.append(a)

    if respawn and (test != grid_b):
        grid_b = spawn(grid_b)
    else:
        check(grid_b)
    return grid_b

def gauche(grid):
    global score
    test = deepcopy(grid)
    grid_b = []
    for a in grid:
        if a[0] == 0:
            a[0] = a[1]
            a[1] = 0
        elif a[0] == a[1]:
            score += a[1] * 2
            a[0] = a[1] * 2
            a[1] = 0
        if a[1] == 0:
            if a[0] == 0:
               a[0] = a[2]
               a[2] = 0
            elif a[0] == a[2]:
                score += a[2] * 2
                a[0] = a[2] * 2
                a[2] = 0
            else:
                a[1] = a[2]
                a[2] = 0
        elif a[1] == a[2]:
            score += a[2] * 2
            a[1] = a[2] * 2
            a[2] = 0
        if a[2] == 0:
            if a[1] == 0:
                if a[0] == 0:
                    a[0] = a[3]
                    a[3] = 0
                elif a[0] == a[3]:
                    score += a[3] * 2
                    a[0] = a[3] * 2
                    a[3] = 0
                else:
                    a[1] = a[3]
                    a[3] = 0
            elif a[1] == a[3]:
                score += a[3] * 2
                a[1] = a[3] * 2
                a[3] = 0
            else:
                a[2] = a[3]
                a[3] = 0
        elif a[2] == a[3]:
            score += a[3] * 2
            a[2] = a[3] * 2
            a[3] = 0
        grid_b.append(a)

    if respawn and (test != grid_b):
        grid_b = spawn(grid_b)
    else:
        check(grid_b)
    return grid_b




def haut(grid):
    global score
    test = deepcopy(grid)
    grid_b = []
    grid_c = deepcopy(grid_b)
    for a in [[grid[0][0],grid[1][0],grid[2][0],grid[3][0]],[grid[0][1],grid[1][1],grid[2][1],grid[3][1]],[grid[0][2],grid[1][2],grid[2][2],grid[3][2]],[grid[0][3],grid[1][3],grid[2][3],grid[3][3]]]:
        if a[0] == 0:
            a[0] = a[1]
            a[1] = 0
        elif a[0] == a[1]:
            score += a[1] * 2
            a[0] = a[1] * 2
            a[1] = 0
        if a[1] == 0:
            if a[0] == 0:
               a[0] = a[2]
               a[2] = 0
            elif a[0] == a[2]:
                score += a[2] * 2
                a[0] = a[2] * 2
                a[2] = 0
            else:
                a[1] = a[2]
                a[2] = 0
        elif a[1] == a[2]:
            score += a[2] * 2
            a[1] = a[2] * 2
            a[2] = 0
        if a[2] == 0:
            if a[1] == 0:
                if a[0] == 0:
                    a[0] = a[3]
                    a[3] = 0
                elif a[0] == a[3]:
                    score += a[3] * 2
                    a[0] = a[3] * 2
                    a[3] = 0
                else:
                    a[1] = a[3]
                    a[3] = 0
            elif a[1] == a[3]:
                score += a[3] * 2
                a[1] = a[3] * 2
                a[3] = 0
            else:
                a[2] = a[3]
                a[3] = 0
        elif a[2] == a[3]:
            score += a[3] * 2
            a[2] = a[3] * 2
            a[3] = 0
        grid_b.append(a)

    grid_c.append([grid_b[0][0],grid_b[1][0],grid_b[2][0],grid_b[3][0]])
    grid_c.append([grid_b[0][1],grid_b[1][1],grid_b[2][1],grid_b[3][1]])
    grid_c.append([grid_b[0][2],grid_b[1][2],grid_b[2][2],grid_b[3][2]])
    grid_c.append([grid_b[0][3],grid_b[1][3],grid_b[2][3],grid_b[3][3]])

    if respawn and (test != grid_c):
        grid_c = spawn(grid_c)
    else:
        check(grid_c)
    return grid_c


def bas(grid):
    global score
    test = deepcopy(grid)
    grid_b = []
    grid_c = deepcopy(grid_b)
    for a in [[grid[0][0],grid[1][0],grid[2][0],grid[3][0]],[grid[0][1],grid[1][1],grid[2][1],grid[3][1]],[grid[0][2],grid[1][2],grid[2][2],grid[3][2]],[grid[0][3],grid[1][3],grid[2][3],grid[3][3]]]:
        if a[3] == 0:
            a[3] = a[2]
            a[2] = 0
        elif a[3] == a[2]:
            score += a[2] * 2
            a[3] = a[2] * 2
            a[2] = 0
        if a[2] == 0:
            if a[3] == 0:
               a[3] = a[1]
               a[1] = 0
            elif a[3] == a[1]:
                score += a[1] * 2
                a[3] = a[1] * 2
                a[1] = 0
            else:
                a[2] = a[1]
                a[1] = 0
        elif a[2] == a[1]:
            score += a[1] * 2
            a[2] = a[1] * 2
            a[1] = 0
        if a[1] == 0:
            if a[2] == 0:
                if a[3] == 0:
                    a[3] = a[0]
                    a[0] = 0
                elif a[3] == a[0]:
                    score += a[0] * 2
                    a[3] = a[0] * 2
                    a[0] = 0
                else:
                    a[2] = a[0]
                    a[0] = 0
            elif a[2] == a[0]:
                score += a[0] * 2
                a[2] = a[0] * 2
                a[0] = 0
            else:
                a[1] = a[0]
                a[0] = 0
        elif a[1] == a[0]:
            score += a[0] * 2
            a[1] = a[0] * 2
            a[0] = 0
        grid_b.append(a)

    grid_c.append([grid_b[0][0],grid_b[1][0],grid_b[2][0],grid_b[3][0]])
    grid_c.append([grid_b[0][1],grid_b[1][1],grid_b[2][1],grid_b[3][1]])
    grid_c.append([grid_b[0][2],grid_b[1][2],grid_b[2][2],grid_b[3][2]])
    grid_c.append([grid_b[0][3],grid_b[1][3],grid_b[2][3],grid_b[3][3]])
    
    if respawn and (test != grid_c):
        grid_c = spawn(grid_c)
    else:
        check(grid_c)
    return grid_c

if randomize:
    grid = init(grid)
run = True
perdu = False

while run:

    screen.fill(couleur)

    for i in range(4):
        for j in range(len(grid[i])):
            screen.blit(pygame.image.load('chiffres/'+str(grid[i][j])+'.jpeg'), [j*60+200,i*60+200])

    font = pygame.font.SysFont("arial", 16)
    score_text = font.render(f"score : {score}", 1, (0,0,0))
    screen.blit(score_text, (20,20))
    
    pygame.display.flip()


    mort = True
    for i in grid:
        for j in i:
            if j == 0:
                mort = False
    if mort:
        print("fin du jeu")
        aff(grid)
        perdu = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("fin du jeu.")
            aff(grid)
            run = False

        elif event.type == pygame.KEYDOWN and not perdu:
            if event.key == pygame.K_RIGHT:
                grid = droite(grid)
            elif event.key == pygame.K_LEFT:
                grid = gauche(grid)
            elif event.key == pygame.K_UP:
                grid = haut(grid)
            elif event.key == pygame.K_DOWN:
                grid = bas(grid)
            elif event.key == pygame.K_SPACE:
                print("relancement du jeu")
                grid = reinit(grid)
