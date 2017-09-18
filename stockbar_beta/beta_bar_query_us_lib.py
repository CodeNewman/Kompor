'''
Created on Aug 22, 2017

@author: Coder_J
'''
import requests
import json
from beta_url_us_lib import beta_url_us

class beta_bar_query_us(object):
    '''    '''
    _symbols = []

    def __init__(self):
        '''    '''
        pass
        
    def query_stock_symbols(self):
        '''    '''
        url = beta_url_us().get_symbol_url() 
        requests_symbols = requests.get(url, verify=False) 

        if  requests_symbols.status_code == 200:
            self._symbols = json.loads(requests_symbols.text)['data']['symbols']
            return self._symbols
        else:
            return []
        
    def query_stock_bar(self, symbols, days):
        '''    '''
        url = beta_url_us().get_price_url(symbols, period=days)       
        requests_symbols = requests.get(url, verify=False) 
        
        if  requests_symbols.status_code == 200:
            return json.loads(requests_symbols.text)['data']['prices']
        else:
            return []
        
def main():
    query = beta_bar_query_us()
    print(query.query_stock_symbols())
#     print(query.query_stock_bar('AAPL', '', '1'))

if __name__ == "__main__":
    main()
        
        
        
        