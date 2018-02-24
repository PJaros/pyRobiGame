#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import pygame

class Sprite:
    def __init__(self, pos):
        self.pos = pos
        
    def draw(self, screen):
        pass

    def step(self):
        pass

class Robi(Sprite):
    def __init__(self, pos):
        super(Robi, self).__init__(pos)
        self.size = (30, 30)
        self.v = (0, 0)
        
    def draw(self, screen):
        super(Robi, self).draw(screen)

        screen.fill((255, 0, 0),
                    pygame.Rect(self.pos[0], self.pos[1],
                                self.size[0], self.size[1]))

    def set_motion(self, v):
        self.v = v

    def step(self):
        super(Robi, self).step()
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        print(f"pos: {self.pos}")
