'''
Created on Sep 1, 2017

@author: Coder_J
'''
import os
import sys
import multiprocessing
import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from crawl_to_cassandra.basic_10jqka import flush
from crawl_lib.crawl import crawl
from dao.mysql_dao import mysql_dao
from configure.cn_setting import DAY, LINE, OFF_SHARE,\
    CN_MYSQL_TABLES_STOCK_BASIC_FROM_10JQKA, CN_MYSQL_DB
from url_lib import url_cn
from configure.area_config import AREA_DICTS_KEY, AREA_KEY
from tools.common import filt_codes

crawler = crawl()
tool = mysql_dao()

class basic(object):
    
    def __init__(self, area = None):
        '''
        Constructor
        '''
        self.area = None
        
        if area in AREA_DICTS_KEY:
            self.area = area
        
    def crawl_basic_from_10jqka(self, symbols):
        inserl_sql = "INSERT INTO "+CN_MYSQL_DB+"."+CN_MYSQL_TABLES_STOCK_BASIC_FROM_10JQKA+" \
            (symbol, name, type, effective, rt, start, year, title) VALUES \
            (%s, %s, %s, NULL, %s, %s, %s, %s);"
        update_sql = "UPDATE "+CN_MYSQL_DB+"."+CN_MYSQL_TABLES_STOCK_BASIC_FROM_10JQKA+" \
            SET symbol=%s, name=%s, type=%s, effective=NULL, rt=%s, start=%s, year=%s, title=%s \
            WHERE (symbol=%s);"
        
        for symbol in symbols:
            url = url_cn.get_share_url(LINE, AREA_KEY, symbol, OFF_SHARE, DAY, 'last')
            data = crawler.craw_to_json(url)
            try:                    
                del data["data"]
                start = datetime.datetime.strptime(data["start"],'%Y%m%d')
                start = str(start)[0:10]
                element = [
                    str(symbol),
                    str(data["name"]).replace(" ", ""),
                    'hs',
                    str(data["rt"]),
                    start,
                    str(data["year"]),
                    str(data["title"]),
                    ]
                
                flag = tool.insert_value_to_db(inserl_sql, element, symbol)
                if flag == "IntegrityError":
                    element.append(symbol)
                    tool.update_value_to_db(update_sql, element, symbol)
                
            except:
                print("Exception")
                print(sys.exc_info())
                pass
                
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def worker_hs(symbols, name):
    print('\t\t\t\t\t', name, ' is started !!')
    item = basic()
    item.crawl_basic_from_10jqka(symbols)
    print('\t\t\t\t\t', name, ' is completed !-------------------------------------------------!')

def main():
    codes_hs = flush(AREA_KEY).get_db_symbols()

    hs_work_names = [
        '000',
        '002',
        '300',
        '600',
        '601',
        '603'
        ]
    
    for x in hs_work_names:
        p = multiprocessing.Process(target = worker_hs, args = (filt_codes(codes_hs, x), x, ))
        p.start()

if __name__ == '__main__':
    main()