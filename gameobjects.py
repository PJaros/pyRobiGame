#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import math

robi_color = (255, 0, 0)
line_color = (255, 200, 200)


class Sprite:
    def __init__(self, pos):
        self.pos = pos
        
    def draw(self, screen):
        pass

    def step(self):
        pass

    def do_left(self, time_delta):
        pass

    def do_right(self, time_delta):
        pass

    def do_up(self, time_delta):
        pass

    def do_down(self, time_delta):
        pass

    def do_step(self, time_delta):
        pass

class Robi(Sprite):
    def __init__(self, pos):
        super(Robi, self).__init__(pos)
        self.size = (30, 30)
        self.motion = (0, 0)
        self.step_speed = 100 * 1.0

    def draw(self, screen):
        super(Robi, self).draw(screen)
        screen.fill(robi_color,
                    pygame.Rect(self.pos[0], self.pos[1],
                                self.size[0], self.size[1]))

    def do_step(self, time_delta):
        super(Robi, self).step()
        self.pos[0] += self.motion[0] * (time_delta / 1000)
        self.pos[1] += self.motion[1] * (time_delta / 1000)

    def do_left(self, time_delta):
        self.motion = (-self.step_speed, 0)

    def do_right(self, time_delta):
        self.motion = (self.step_speed, 0)

    def do_up(self, time_delta):
        self.motion = (0, -self.step_speed)

    def do_down(self, time_delta):
        self.motion = (0, self.step_speed)


class AngleRobi(Robi):
    def __init__(self, pos, angle, speed):
        super(AngleRobi, self).__init__(pos)
        self.angle = angle
        self.speed = speed
        self.angle_speed = 0.1
        self.current_speed = 0

    def draw(self, screen):
        super(AngleRobi, self).draw(screen)
        center = (self.pos[0] + (self.size[0] / 2),
                  self.pos[1] + (self.size[1]) / 2)
        x_motion = math.cos(math.pi / 180 * self.angle) * self.size[0]
        y_motion = math.sin(math.pi / 180 * self.angle) * self.size[1]
        pygame.draw.line(screen, line_color, center,
                         ((center[0] + x_motion), (center[1] + y_motion)), 2)

    def do_left(self, time_delta):
        self.angle -= self.angle_speed * time_delta

    def do_right(self, time_delta):
        self.angle += self.angle_speed * time_delta

    def do_up(self, time_delta):
        self.current_speed = self.speed

    def do_down(self, time_delta):
        self.current_speed = 0

    def do_step(self, time_delta):
        x_motion = math.cos(math.pi / 180 * self.angle) * self.current_speed
        y_motion = math.sin(math.pi / 180 * self.angle) * self.current_speed
        self.pos[0] += x_motion * time_delta
        self.pos[1] += y_motion * time_delta

