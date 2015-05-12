#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
import random
import string
from pygame.locals import *

max_data_len = 100000

def readdata(fn):
    data = list()
    with open(fn, "rb") as f:
        byte = f.read(1)
        while byte:
            data.append(ord(byte))
            byte = f.read(1)
            if len(data)>max_data_len: break
    return data

def putbyte(sc, val, x, y, lbl = True):
    for i in range(8):
        if lbl: bit = (1 << 7) >> i
        else: bit = (1 << i)
        if bit & val: sc.set_at((x+i, y), (255, 255, 255))
        else: sc.set_at((x+i, y), (0, 0, 0))

def puttext(cx,cy,txt,color,screen):
    font = pygame.font.Font(None, 32)
    text = font.render(" ", 1, (10, 10, 10))
    text = font.render(txt, 1, color)
    textpos = text.get_rect()
    textpos.centerx = cx
    textpos.centery = cy
    screen.blit(text, textpos)
    return screen

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: \me sys_file"
        exit()
    fn = sys.argv[1]

    data = readdata(fn)
    data_len = len(data)
    print len(data),"bytes loaded.\nUse arrows, home/end, page_up/page_down, space for control, press TAB to screenshot, ESCAPE to exit."

    # init vis pars
    x_period = 32
    lbl = True
    phase = 0

    # init graphics
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    background = pygame.Surface((800, 600))
    background = background.convert()
    background.fill((80, 80, 80))
    black_bg = background.copy()
    screen.blit(background, (0, 0))
    pygame.display.flip()

    pygame.display.flip()
    pygame.display.set_caption('deVerbarius')

    # main draw cycle
    while 1:
        clock.tick(60)
        screen.blit(background, (0, 0))
        for z in range(data_len): 
            if 10 + ( z / x_period ) > 500: break
            putbyte(screen, data[z+phase], 10 + (z % x_period) * 8, 10 + ( z / x_period ), lbl)
        # puttext( 560, 100, "data shown: "+str(data_len), (10, 10, 10), screen )
        puttext( 560, 120, "bytes in line: "+str(x_period), (10, 10, 10), screen )
        puttext( 560, 140, "phase: "+str(phase), (10, 10, 10), screen )
        if lbl: puttext( 560, 160, "lower bit: left", (10, 10, 10), screen )
        else: puttext( 560, 160, "lower bit: right", (10, 10, 10), screen )
        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE): exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT: x_period = max(1, x_period-1)
                elif event.key == K_RIGHT: x_period = min(10000, x_period+1)
                elif event.key == K_DOWN: data_len = max(64, data_len >> 1)
                elif event.key == K_UP: data_len = min(600000, data_len*2)
                elif event.key == K_PAGEDOWN: phase = max(0, phase-1)
                elif event.key == K_PAGEUP: phase = min(10000, phase + 1)
                elif event.key == K_END: phase = max(0, phase-x_period)
                elif event.key == K_HOME: phase = min(10000, phase + x_period)
                elif event.key == K_SPACE: lbl = not lbl
                elif event.key == K_TAB: 
                    z_z = "screen"+("".join(random.choice(string.ascii_uppercase + string.digits) for x in range(8)))+".png"
                    pygame.image.save(screen, z_z)
                    print 'dumped', z_z
