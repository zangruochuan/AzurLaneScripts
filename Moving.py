# -*- coding: utf-8 -*-
import cv2


def template_matching(screenshot, template):
    image_path = 'resource/image/'
    mid_air = cv2.imread(image_path + template)
    h, w = mid_air.shape[:2]
    result = cv2.matchTemplate(screenshot, mid_air, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    strmin_val = str(min_val)
    print("匹配度：" + strmin_val)
    cv2.rectangle(screenshot, min_loc, (min_loc[0] + w, min_loc[1] + h), (0, 0, 255))
    pos = (min_loc[0] + w / 2, min_loc[1] + h / 2)
    print(pos)

    # cv2.imshow("match", screenshot)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return pos, min_val


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
