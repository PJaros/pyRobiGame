#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import KEYDOWN, QUIT, \
    K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN

import gameobjects

# pygame.init() -- Ein Bug verursacht hohe CPU-last. Einzeln initialisieren.
# https://github.com/pygame/pygame/issues/331
pygame.font.init()
pygame.display.init()

pygame.display.set_caption('Hello World!')
screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont("None", 30)
text = font.render('Hello World', True, (255, 100, 100))

fps = 30
REDRAW_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(REDRAW_EVENT, int(1000.0 / fps))


# robi = gameobjects.Robi([0, 0])
robi = gameobjects.AngleRobi([0, 0], 90.0, 0.05)

i = 0
draw_time_now = pygame.time.get_ticks()
key_time_now = pygame.time.get_ticks()
running = True
while running:
    key_time_before = key_time_now
    key_time_now = pygame.time.get_ticks()
    key_time_delta = key_time_now - key_time_before
    keyState = pygame.key.get_pressed()
    if keyState[K_LEFT]:
        robi.do_left(key_time_delta)
    elif keyState[K_RIGHT]:
        robi.do_right(key_time_delta)
    elif keyState[K_UP]:
        robi.do_up(key_time_delta)
    elif keyState[K_DOWN]:
        robi.do_down(key_time_delta)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == REDRAW_EVENT:
            draw_time_before = draw_time_now
            draw_time_now = pygame.time.get_ticks()
            draw_time_delta = draw_time_now - draw_time_before

            robi.do_step(draw_time_delta)

            screen.fill((0, 0, 0), pygame.Rect((0, 0, 400, 300)))
            robi.draw(screen)
            screen.blit(text, (100, 100))
            pygame.display.update()

    pygame.time.wait(10)
