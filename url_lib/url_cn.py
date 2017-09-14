'''
Created on Sep 13, 2017

@author: Coder_J
'''
from configure.cn_setting import LINE
from configure.area_config import AREA_KEY
"""
url example
http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/
http://d.10jqka.com.cn/v2/line/hs_600000/00/last.js
"""

_code_url  = "http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/%s/ajax/1/"
_share_url = "http://d.10jqka.com.cn/v2/%s/%s_%s/%s%s/%s.js" 


def get_code_url(page = 1):
    page = str(page)
    return _code_url %(page)


def get_share_url(cycle_cycle = LINE, \
                  area = AREA_KEY, \
                  symbol = None, \
                  share_type = None, \
                  transaction_cyle = None, \
                  year = None
                  ):
    area = str(area.name)
    
    if symbol and share_type and transaction_cyle and year :
        return _share_url % (cycle_cycle, area, symbol, share_type, transaction_cyle, year)
    else:        
        print("get_share_url args error ,disable value None !")
        print("args ->", (symbol , share_type , transaction_cyle , year))
        return None
    
    
