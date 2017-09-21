'''
Created on Sep 19, 2017

@author: Coder_J
'''
import json

from configure.cn_setting import AWS_HOST_ADD
from crawl_lib.crawl import crawl

craw = crawl()

_token = '6fab4b8e8bd63ccd37d1a5130a32659e'

def get_hs_price(symbols, endTime = '', period = 65535):
    _url = AWS_HOST_ADD + '/cn/quote/prices/daily?symbols=%s&endTime=%s&period=%s&token=%s'
    symbols = str(symbols)[1 : -1].replace("'", "").replace(" ", "")
    endTime = str(endTime)
    period = str(period)
    url = _url % (symbols, endTime, period, _token)
    text = craw.craw_to_string(url)
    return json.loads(text)
    