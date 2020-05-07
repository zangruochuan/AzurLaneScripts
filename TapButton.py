# -*- coding: utf-8 -*-
from common.template_matching import template_matching, image_reader
from common.auto_adb import auto_adb


def sortout(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, '整理.jpg')
    if val < 0.05:
        adb.tap_scale(pos)


def onekey_retire(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, '一键退役.jpg')
    if val < 0.05:
        adb.tap_scale(pos)


def cancel(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, '取消.jpg')
    if val < 0.05:
        adb.tap_scale(pos)


def confirm(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, image_reader('确定橙'))
    if val < 0.05:
        adb.tap_scale(pos)
    pos, val = template_matching(screenshot, image_reader('确定蓝'))
    if val < 0.05:
        adb.tap_scale(pos)


def switch(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, image_reader('切换'))
    if val < 0.05:
        adb.tap_scale(pos)


def attack(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, image_reader('迎击'))
    if val < 0.05:
        adb.tap_scale(pos)


def attack_confirm(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, image_reader('出击'))
    if val < 0.05:
        adb.tap_scale(pos)


def start_mission(screenshot, adb: auto_adb):
    pos, val = template_matching(screenshot, image_reader('立即前往'))
    if val < 0.05:
        adb.tap_scale(pos)

def escape(screenshot,adb:auto_adb):
    pos,val = template_matching(screenshot, image_reader('规避'))
    if val<0.05:
        adb.tap_scale(pos)