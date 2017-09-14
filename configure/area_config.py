'''
Created on Sep 13, 2017

@author: Coder_J
'''
import enum


AREA_DICTS_KEY = enum.Enum("AREA_DICTS_KEY",(
    'hs',    # 上交所
    'usa',   # 美国
    ))


AREA_KEY = AREA_DICTS_KEY.hs
