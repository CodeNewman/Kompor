'''
Created on Aug 22, 2017

@author: Coder_J
'''

class beta_url_us(object):
    '''
    classdocs
    '''
    _base_url = 'http://121.43.168.179:8087/quote/'
    _price_daily = _base_url + 'prices/daily'

    
    def get_symbol_url(self):
        return  self._base_url + 'symbols/nyseandnasdaq'
    
    def get_price_url(self, symbols, period='1'):
        return self._price_daily + '?&symbols=' + symbols + '&period=' + period
    

def main():
    url = beta_url_us()
    print(url.get_symbol_url())
    print(url.get_price_url('AAPL', '1'))

if __name__ == "__main__":
    main()