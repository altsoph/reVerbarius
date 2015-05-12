#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from math import sin, cos, radians
import math

if __name__ == "__main__":
    fn = "res.sys"
    frame_data = list()
    for i in range(30*64): frame_data.append(0)
    frame_head = list()
    for i in range(128): frame_head.append(255)

    # screen props
    win_w = 240
    win_h = 64
    cx = win_w/2
    cy = win_h/2
    bg_color = (0, 0, 0)

    # hands sizes
    hour_w = 4
    hour_l = 15
    minute_w = 2
    minute_l = 20

    # init graphics
    pygame.init()
    screen = pygame.display.set_mode((win_w, win_h))
    clock = pygame.time.Clock()
    background = pygame.Surface((win_w, win_h))
    background = background.convert()
    background.fill(bg_color)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    font = pygame.font.Font(None, 12)

    z = 0
    m = 0
    f = 0
    th = 0
    tm = 0

    with open(fn, "wb") as fh:
        while z < 24*60*10:
            f = z % 10
            t = (z - f) / 10
            tm = t % 60
            th = (t - tm) / 60

            clock.tick(60)
            screen.blit(background, (0, 0))


            screen.blit(font.render("NEW YORK", 0, (255, 255, 255)), (21,4))
            screen.blit(font.render("MOSCOW", 0, (255, 255, 255)), (102,4))
            screen.blit(font.render("LONDON", 0, (255, 255, 255)), (182,4))

            minute = tm
            hour = th + minute / 60.
            if hour > 12: hour = hour - 12
            hour_angle = hour * 30

            angle = radians(-hour_angle)
            rotated_x = round(cx - hour_l * sin(angle))
            rotated_y = round(cy - hour_l * cos(angle))
            rotated_x1 = round(cx - (hour_l+2) * sin(angle))
            rotated_y1 = round(cy - (hour_l+2) * cos(angle))
            pygame.draw.line(screen, (255, 255, 255), (cx,cy), (rotated_x, rotated_y), hour_w)
            minute_angle = minute * 6
            angle = radians(-minute_angle)
            rotated_x = round(cx - minute_l * sin(angle))
            rotated_y = round(cy - minute_l * cos(angle))
            pygame.draw.line(screen, (255, 255, 255), (cx, cy), (rotated_x, rotated_y), minute_w)

            hour = th + minute / 60.
            hour = (hour + 24 - 8) % 24
            hour_angle = hour * 30
            angle = radians(-hour_angle)
            rotated_x = round(cx - hour_l * sin(angle))
            rotated_y = round(cy - hour_l * cos(angle))
            rotated_x1 = round(cx - (hour_l+2) * sin(angle))
            rotated_y1 = round(cy - (hour_l+2) * cos(angle))
            pygame.draw.line(screen, (255, 255, 255), (cx-80, cy), (rotated_x-80, rotated_y), hour_w)
            minute_angle = minute * 6
            angle = radians(-minute_angle)
            rotated_x = round(cx - minute_l * sin(angle))
            rotated_y = round(cy - minute_l * cos(angle))
            pygame.draw.line(screen, (255, 255, 255), (cx-80, cy), (rotated_x-80, rotated_y), minute_w)

            hour = th + minute / 60.
            hour = (hour + 24 - 3) % 24
            hour_angle = hour * 30
            angle = radians(-hour_angle)
            rotated_x = round(cx - hour_l * sin(angle))
            rotated_y = round(cy - hour_l * cos(angle))
            rotated_x1 = round(cx - (hour_l+2) * sin(angle))
            rotated_y1 = round(cy - (hour_l+2) * cos(angle))
            pygame.draw.line(screen, (255, 255, 255), (cx+80, cy), (rotated_x+80, rotated_y), hour_w)
            minute_angle = minute * 6
            angle = radians(-minute_angle)
            rotated_x = round(cx - minute_l * sin(angle))
            rotated_y = round(cy - minute_l * cos(angle))
            pygame.draw.line(screen, (255, 255, 255), (cx+80, cy), (rotated_x+80, rotated_y), minute_w)

            pygame.display.flip()
            if not f: print th, tm

            c_head = frame_head
            c_head[0] = th
            c_head[1] = tm
            c_head[2] = f
            for i in range(128): fh.write(chr(c_head[i]))

            c_data = frame_data
            for i in range(30):
                for j in range(64):
                    val = 0
                    for k in range(8):
                        if screen.get_at((i*8 + k, j)).r > 0:
                            val += 1
                        val <<= 1
                    val >>= 1
                    c_data[i+j*30] = val
            for i in range(30*64):
                fh.write(chr(c_data[i]))
            z = z+1
