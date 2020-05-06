# -*- coding: utf-8 -*-
from common import template_matching

def sortout(screenshot):
    pos, val = template_matching(screenshot,'整理.jpg')
    return pos

def onekey_retire(screenshot):
    pos, val = template_matching(screenshot,'一键退役.jpg')
    return pos

def cancel(screenshot):
    pos, val = template_matching(screenshot,'取消.jpg')
    return pos

def confirm(screenshot):
    pos, val = template_matching(screenshot,'确定.jpg')
    return pos