# encoding * utf-8 *
"""
Testing Asteroid Hazard
"""
# imports
import os
import pygame as pg
from shmup.config import *
import shmup.inputhandler as inputhandler
import shmup.scene.gamescene
import shmup.entity
import shmup.level
import shmup.gui.textgui

pg.init()
screen = pg.display.set_mode(RESOLUTION)
inputhandler.setup(DEBUG_MAP)
mainscene = shmup.scene.gamescene.GameScene()

shmup.entity.HighPointToken.setup(mainscene)

mainscene.load(reset=True)
# HUD = shmup.gui.textgui.TextGUI(mainscene)

print(os.getcwd(), __file__)

playing = True
clock = pg.time.Clock()
# shmup.entity.Asteroid(50, 50)
# a = shmup.entity.HighPointToken(50, 50)
# print(a.image, a.rect, a.IMAGE)
while playing:
    # for i in mainscene.enemy:
    #    print(i.position)
    dt = clock.tick(FPS) / 1000
    for event in inputhandler.get():
        if event.key == "debug1" and event.down:
            shmup.entity.Asteroid(50, 50)
        elif event.key == "debug2" and event.down:
            shmup.entity.HealthToken(200, 0)
        elif event.key == "debug3" and event.down:
            shmup.entity.HighPointToken(200, 0)
        mainscene.handle_input(event)
        if mainscene.final:
            playing = False
            break
    mainscene.update(dt)
    if mainscene.final:
        playing = False
        break
    mainscene.draw(screen)
    # pg.display.set_caption(str(mainscene.player.health))
    # HUD.draw(screen)
    pg.display.flip()
