#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import KEYDOWN, QUIT, \
    K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN

import gameobjects as go

# pygame.init() -- Ein Bug verursacht hohe CPU-last. Einzeln initialisieren.
# https://github.com/pygame/pygame/issues/331
pygame.font.init()
pygame.display.init()

pygame.display.set_caption('Hello World!')
screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont("None", 19)
text = font.render('Hello World', 0, (255, 100, 100))

fps = 60
REDRAW_ID = pygame.USEREVENT + 1 # OOP wäre hübsch gewesen :-P
pygame.time.set_timer(REDRAW_ID, int(1000.0/fps))

robi = go.Robi([0, 0])

i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_LEFT:
                robi.set_motion((-1, 0))
                print("left")
            elif event.key == K_RIGHT:
                robi.set_motion((1, 0))
                print("right")
            elif event.key == K_UP:
                robi.set_motion((0, -1))
                print("left")
            elif event.key == K_DOWN:
                robi.set_motion((0, 1))
                print("right")
        elif event.type == QUIT:
            running = False
        elif event.type == REDRAW_ID:
            robi.step()

            screen.fill((0, 0, 0), pygame.Rect((0, 0, 400, 300)))
            robi.draw(screen)
            screen.blit(text, (100, 100))
            pygame.display.update()

    pygame.time.wait(1)
