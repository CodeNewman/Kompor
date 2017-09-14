'''
Created on Sep 1, 2017

@author: Coder_J
'''
import requests
import json

from requests.models import Response
from bs4 import BeautifulSoup


class crawl(object):
    '''
    crawler
    '''

    def craw_to_string(self, url):
        '''  爬出文本数据  '''
        
        result = ''
        r= Response() 
        try:
            r = requests.get(url)
        except:
            pass

        index = 0
        while r.status_code != 200:
            try:
                r = requests.get(url)
            except:
                pass
                
            if index >= 5:
                break
            index += 1
            
        if r.status_code == 200:
            result = str(r.text)
            
        return result
            
    def craw_to_json(self, url):
        '''  爬出json数据  '''
        result = ''
        text = self.craw_to_string(url)
        
        index = text.find("(");
        title = text[0:index]
        text = text[index + 1:-1]
        if len(text) != 0:
            json_value = json.loads(text)
            json_value['title'] = title
            result = json_value
        
        return result
    
    def craw_to_list(self, url):
        '''  爬出数据数组  '''
        
        data = []
        try:
            for d in str(self.craw_to_json(url)['data']).split(';'):
                data.append(d)
        except:
            pass
        return data
    
    def craw_to_bs4(self, url):
        html = self.craw_to_string(url)
        soup = BeautifulSoup(html)
        return soup