# -*- coding: utf-8 -*-
import cv2
from common.template_matching import template_matching,image_reader

def find_enemy(screenshot):
    pos, val = template_matching(screenshot, image_reader('boss'))
    if val < 0.2:
        print('boss')
        return pos
    # pos, val = find_specialenemy(screenshot)
    # if val < 0.2:
    #     print('specialEnemy')
    #     return pos
    pos, val = template_matching(screenshot, image_reader('mid-air'))
    if val < 0.06:
        print('mid-air')
        return pos
    pos, val = template_matching(screenshot, image_reader('mid-defense'))
    if val < 0.08:
        print('mid-defense')
        return pos
    pos, val = template_matching(screenshot, image_reader('mid-main'))
    print('mid-main')
    return pos

def find_specialenemy(screenshot):
    pos, val = template_matching(screenshot,image_reader('specialEnemy1'))
    if val < 0.2:
        pos = pos[0],pos[1]+30
        return pos, val
    pos, val = template_matching(screenshot, image_reader('specialEnemy2'))
    pos = pos[0],pos[1]+30
    return pos, val

def attack(screenshot):
    pos, val = template_matching(screenshot, image_reader('出击'))
    return pos, val

def ambush(screenshot):
    pos, val = template_matching(screenshot, image_reader('伏击'))
    return pos, val


def finished(screenshot):
    pos, val = template_matching(screenshot, image_reader('S胜'))
    return pos, val


def accept(screenshot):
    pos, val = template_matching(screenshot, 'accept.png')
    return pos, val


def find_stage(screenshot, stage):
    pos, val = template_matching(screenshot, image_reader(stage))
    pos = (pos[0] - 88, pos[1])
    return pos, val


def go(screenshot):
    return template_matching(screenshot, image_reader('迎击'))

def find_page(screenshot, image):
    pos, val = template_matching(screenshot,image)
    if val < 0.1:
        return True
    else:
        return False

def find_ship(screenshot, team_leader):
    pos, val = template_matching(screenshot,image_reader(team_leader))
    pos = pos[0],pos[1]+60
    return pos, val

def find_mapbottomedge(screenshot):
    pos, val = template_matching(screenshot, image_reader('bottomedge'))
    return pos

def is_harborfull(screenshot):
    pos, val = template_matching(screenshot,image_reader('harborfull'))
    if val<0.1:
        return True
    return False

