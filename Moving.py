# -*- coding: utf-8 -*-
import cv2
from common.template_matching import template_matching

def find_enemy(screenshot):
    pos, val = template_matching(screenshot, 'boss.png')
    if val < 0.2:
        print('boss')
        return pos
    pos, val = find_specialenemy(screenshot)
    if val < 0.2:
        print('specialEnemy')
        return pos
    pos, val = template_matching(screenshot, 'mid-air.png')
    if val < 0.06:
        print('mid-air')
        return pos
    pos, val = template_matching(screenshot, 'mid-defense.png')
    if val < 0.15:
        print('mid-defense')
        return pos
    pos, val = template_matching(screenshot, 'mid-main.png')
    print('mid-main')
    return pos

def find_specialenemy(screenshot):
    pos, val = template_matching(screenshot,'specialEnemy1.jpg')
    if val < 0.2:
        pos = pos[0],pos[1]+30
        return pos, val
    pos, val = template_matching(screenshot, 'specialEnemy2.jpg')
    pos = pos[0],pos[1]+30
    return pos, val

def attack(screenshot):
    pos, val = template_matching(screenshot, 'attack.png')
    return pos, val


def escape(screenshot):
    return template_matching(screenshot, 'escape.png')


def ambush(screenshot):
    pos, val = template_matching(screenshot, 'ambush.png')
    return pos, val


def finished(screenshot):
    pos, val = template_matching(screenshot, 'finished.png')
    return pos, val


def accept(screenshot):
    pos, val = template_matching(screenshot, 'accept.png')
    return pos, val


def find_stage(screenshot, stage):
    pos, val = template_matching(screenshot, stage + '.png')
    pos = (pos[0] - 88, pos[1])
    return pos, val


def go(screenshot):
    return template_matching(screenshot, 'go.png')

def find_page(screenshot, image):
    pos, val = template_matching(screenshot,image)
    if val < 0.1:
        return True
    else:
        return False

def find_ship(screenshot, team_leader):
    pos, val = template_matching(screenshot,team_leader+'.jpg')
    pos = pos[0],pos[1]+60
    return pos, val

def find_mapbottomedge(screenshot):
    pos, val = template_matching(screenshot,'bottomedge.jpg')
    return pos

def is_harborfull(screenshot):
    pos, val = template_matching(screenshot,'harborfull.jpg')
    if val<0.1:
        return True
    return False

