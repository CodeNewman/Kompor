'''
Created on Aug 22, 2017

@author: Coder_J
'''
import requests
import json
from stockbar_beta.beta_url_hs_lib import beta_url_hs

class beta_bar_query_hs(object):
    '''   kavout A股股票代码数据获取类 '''
    _symbols = []

    def __init__(self):
        '''    '''
        pass
        
    def query_stock_symbols(self, symbol_type='6'):
        '''  查询所有A股股票代码  '''
        url = beta_url_hs().get_symbol_url(symbol_type) 
        print(url)
        requests_symbols = requests.get(url, verify=False) 

        if  requests_symbols.status_code == 200:
            self._symbols = json.loads(requests_symbols.text)['data']['symbols']
            return self._symbols
        else:
            return []
        
    def query_stock_bar(self, symbols, days='1'):
        '''  获取指定代码的，A股的  '''
        url = beta_url_hs(symbols=symbols, endtime='last', period=days).get_price_url()       
        requests_symbols = requests.get(url, verify=False) 
        
        if  requests_symbols.status_code == 200:
            return json.loads(requests_symbols.text)['data']['prices']
        else:
            return []
        
        
        
        
        