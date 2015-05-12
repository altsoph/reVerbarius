#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

def put_digit(sfc, cx, cy, val, bits, wx=16, wy=8, pady=4):
    for z in range(1, bits+1):
        fillif0 = 1
        if val & (1 << (z - 1)): fillif0 = 0
        pygame.draw.rect(sfc, (255, 255, 255), (cx, cy-wy*z-pady*(z-1), wx, wy), fillif0)

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

    # init graphics
    pygame.init()
    screen = pygame.display.set_mode((win_w, win_h))
    clock = pygame.time.Clock()
    background = pygame.Surface((win_w, win_h))
    background = background.convert()
    background.fill(bg_color)
    screen.blit(background, (0, 0))
    pygame.display.flip()

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

            put_digit(screen, cx-35-8, 55, (th - th % 10) / 10, 2)
            put_digit(screen, cx-15-8, 55, (th % 10), 4)
            put_digit(screen, cx+15-8, 55, (tm - tm % 10)/10, 3)
            put_digit(screen, cx+35-8, 55, (tm % 10), 4)

            pygame.display.flip()
            if not f: print th, tm

            c_head = frame_head
            c_head[0] = th
            c_head[1] = tm
            c_head[2] = f

            for i in range(128):
                fh.write(chr(c_head[i]))

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
            for i in range(30*64): fh.write(chr(c_data[i]))
            z = z+1
