#!/usr/bin/python3

import pygame, os, math
from pygame.locals import *

grille = [[0] * 4 for i in
          range(4)]  # grille ou on appliquera les algo stockera seulement les valeurs qui seront dans les rectangles
# la grille est initialisée a 0 partout
mar = 30  # marge des rectangles
cot = 60  # longueur du coté

def choisir_num(x, y): #a suivre --> commande pour ecrire un chiffre
    print("def")





def click_inter_grille(grille):  # prend une grille en parametre (tableau n*n)
    if pygame.mouse.get_pressed()[0]:  # renvoie 1 si le le click gauche est activé
        click = pygame.mouse.get_pos()  # on stock les coordonées du click
        if (screen.get_at(click) == color):  # ne fait quelque chose que si l'on a cliqué sur du blanc
            global x
            global y
            x = math.floor((
                (click[1]/ (cot + mar))-2))  # les coordonées sont inversées quand on passe de la grille a l'interface
            y = math.floor(((click[0]/ (cot + mar))-4))

            pygame.draw.rect(screen, colorclick, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                                         cot))  # change de couleur pendant le click


pygame.init()
WINDOW_SIZE = [1080, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Futoshiki")   #titre de la fenetre



Icone = pygame.image.load("assets/icone.jpg")  #lecture de l'icone
pygame.display.set_icon(Icone)   #mettre l'icone
running = True #Vérifie si la fenetre doit rester ouverte
screen.fill((0, 105, 102))  # met le fond en vert
color = (255, 255, 255)  # couleur que l'on utilise pour les rectangles
colorclick = (255, 255, 35) # couleur quand on click sur un rectangle
imagetitre = pygame.image.load("assets/titreFutoshiki.png").convert_alpha() #Lecture du titre Futoshiki
difficulte = 4 #taille de grille
x = -1
y= -1


G1 = pygame.image.load("assets/G1.png").convert_alpha()  #Lecture des grands numéros cliquable
G2 = pygame.image.load("assets/G2.png").convert_alpha()
G3 = pygame.image.load("assets/G3.png").convert_alpha()
G4 = pygame.image.load("assets/G4.png").convert_alpha()

clickable_area_G1 = pygame.Rect((320, 575), (100, 100))  #Zone cliquable des numéros
rect_surf_G1 = pygame.Surface(clickable_area_G1.size)
clickable_area_G2 = pygame.Rect((445, 575), (100, 100))
rect_surf_G2 = pygame.Surface(clickable_area_G2.size)
clickable_area_G3 = pygame.Rect((570, 575), (100, 100))
rect_surf_G3 = pygame.Surface(clickable_area_G3.size)
clickable_area_G4 = pygame.Rect((695, 575), (100, 100))
rect_surf_G4 = pygame.Surface(clickable_area_G4.size)

P1 = pygame.image.load("assets/P1.png").convert_alpha()  #Lecture des petits numéros qui vont sur la grille
P2 = pygame.image.load("assets/P2.png").convert_alpha()
P3 = pygame.image.load("assets/P3.png").convert_alpha()
P4 = pygame.image.load("assets/P4.png").convert_alpha()

for x in range(difficulte):
    for y in range(difficulte):
        pygame.draw.rect(screen, color, pygame.Rect(x * (cot + mar) + 390, y * (cot + mar) + 200, cot,
                                                    cot))  # dessine la "grille de dimension n"
        # sous formes de n*n rectangles avec une marge "mar"

x = -1
y = -1
while running:
    screen.blit(imagetitre, (290, 20))  #Affichage du titre Futoshiki

    screen.blit(G1, (320, 575))  #Affichage des grands numéros cliquable
    screen.blit(G2, (445, 575))
    screen.blit(G3, (570, 575))
    screen.blit(G4, (695, 575))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONUP:  # quand je relache le bouton
            if event.button == 1 and x != -1 and y != -1 :  # 1= clique gauche et vérifie qu'une case est été précedement
                # cliquée avant de mettre un numéro, si la val est tjs -1 alors c'est pas le cas

                if clickable_area_G1.collidepoint(event.pos):
                    pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                                                cot))
                    screen.blit(P1, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                     cot))
                    grille[x][y] = 1
                    print("1 clické")
                if clickable_area_G2.collidepoint(event.pos):
                    pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                                                cot))
                    screen.blit(P2, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                     cot))
                    grille[x][y] = 2
                    print("2 clické")
                if clickable_area_G3.collidepoint(event.pos):
                    pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                                                cot))
                    screen.blit(P3, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                     cot))
                    grille[x][y] = 3
                    print("3 clické")
                if clickable_area_G4.collidepoint(event.pos):
                    pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                                                cot))
                    screen.blit(P4, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                     cot))
                    grille[x][y] = 4
                    print("4 clické")



    click_inter_grille(grille)

    pygame.display.flip()

for element in grille:  # test pour voir sur quels rectangles on a clické
    print(element)
