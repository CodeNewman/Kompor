'''
Created on Sep 13, 2017

@author: Coder_J
'''
import os
import sys
import enum

import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from configure.area_config import AREA_DICTS_KEY, AREA_KEY
from configure.cn_setting import LINE, OFF_SHARE, DAY, CN_CASSANDRA_KEYSPACE,\
    CN_CASSANDRA_HOSTS, CN_CASSANDRA_PASSWD, CN_CASSANDRA_PORT,\
    CN_CASSANDRA_USER, CN_TABLES_STOCK_RATIO_FROM_10JQKA,\
    CN_TABLES_STOCK_BASIC_FROM_10JQKA
from crawl_stock.crawl import crawl
from url_lib import url_cn
from dao.casd_dao import CassandraDao

import warnings
warnings.filterwarnings("ignore")

CRAWL_PAGE_TYPE = enum.Enum("CRAWL_PAGE_TYPE", (
    'json',
    'text',
    'html',
    ))

crawler = crawl()

class flush(object):
    '''
    classdocs
    '''


    def __init__(self, area = None, keyspace = CN_CASSANDRA_KEYSPACE):
        '''
        Constructor
        '''
        self.cassandra_dao = CassandraDao(CN_CASSANDRA_USER, CN_CASSANDRA_PASSWD, CN_CASSANDRA_HOSTS, CN_CASSANDRA_PORT)
        self.area = None
        self.keyspace = keyspace
        
        if area in AREA_DICTS_KEY:
            self.area = area
    
    
    def craw_ratio(self):
        print('crawl symbols :')
        if self.area is AREA_DICTS_KEY.hs:
            url = "http://d.10jqka.com.cn/v6/time/hs_1A0001/last.js"
            json = crawler.craw_to_json(url)
            last_date = json['hs_1A0001']['date']
            
            stocks = [last_date, ]
            page_number = 1
            while(True):
                url = url_cn.get_code_url(page_number)
                page_stock, is_tail = self.crawl_hs(url, CRAWL_PAGE_TYPE.html)
                stocks.append(page_stock)
                if is_tail:
                    break
                else:
                    page_number += 1
            print('crawl symbols completed !', end='\n')
            return stocks


    def crawl_hs(self, url, crawl_page_type):
        if crawl_page_type is CRAWL_PAGE_TYPE.html:
            soup = crawler.craw_to_bs4(url)
            tbody = soup.table.tbody
            trs = tbody.findAll("tr")
            _page = []            
            for tr in trs:
                _row = []
                for td in tr.findChildren():
                    _row.append(td.get_text())
                _page.append(_row)

            count = soup.div.span.get_text()
            cmp_count = str(count).split("/")
            is_tail = cmp_count[0] == cmp_count[1]
            print('The progress of stock crawl', count)

            return _page, is_tail


    def insert_to_db(self, stocks):
        sql = "UPDATE " + CN_TABLES_STOCK_RATIO_FROM_10JQKA + " SET \
                name                  = ?, \
                price                 = ?, \
                size_ratio            = ?, \
                rise_fall             = ?, \
                pace_ratio            = ?, \
                changed_hands_ratio   = ?, \
                than                  = ?, \
                amplitude_ratio       = ?, \
                turnover              = ?, \
                shares_outstanding    = ?, \
                current_market        = ?, \
                pe_ratio              = ?  \
            where \
                symbol = ? and \
                date = ? "

        date = stocks[0]
        date = datetime.datetime.strptime(date,'%Y%m%d')
        elements = []
        del stocks[0]
        for page in stocks:
            for row in page:
                try:
                    symbol                = row[1]
                    name                  = row[3]
                    price                 = row[5]
                    size_ratio            = row[6]
                    rise_fall             = row[7]
                    pace_ratio            = row[8]
                    changed_hands_ratio   = row[9]
                    than                  = row[10]
                    amplitude_ratio       = row[11]
                    turnover              = row[12]
                    shares_outstanding    = row[13]
                    current_market        = row[14]
                    pe_ratio              = row[15]
                    
                    elements.append(
                        [name, price, size_ratio, rise_fall, pace_ratio, \
                         changed_hands_ratio, than, amplitude_ratio, turnover, \
                         shares_outstanding, current_market, pe_ratio, symbol, date])
                except Exception as e:
                    print(e)
                    pass
        if elements:
            self.cassandra_dao.batch_execute_prepared_one_sql(sql, elements, keyspace=self.keyspace ,slice_length=100)
            print('insert to db completed !')


    def get_db_symbols(self):
        symbols = []
        sql = "SELECT SYMBOL FROM " + CN_TABLES_STOCK_RATIO_FROM_10JQKA
        result_set = self.cassandra_dao.execute_sql(sql, keyspace=self.keyspace)
        for result in result_set:
            symbols.append(result.symbol)
        return symbols;    


    def crawl_quote(self):
        if self.area is AREA_DICTS_KEY.hs:
            symbols = self.get_db_symbols()
#             print(symbols)
            self.crawl_basic_from_10jqka(symbols, AREA_DICTS_KEY.hs)
    

    def crawl_basic_from_10jqka(self, symbols, area):
        sql = "UPDATE " + CN_TABLES_STOCK_BASIC_FROM_10JQKA + " SET \
                rt       = ?, \
                total    = ?, \
                start    = ?, \
                year     = ? \
            where \
                symbol = ? and \
                name = ? "
        elements = []
        
        for symbol in symbols:
            url = url_cn.get_share_url(LINE, area, symbol, OFF_SHARE, DAY, 'last')
            data = crawler.craw_to_json(url)
            print("crawling :", symbol, end=" : ")
            try:                    
                del data["data"]
                elements.append([
                    str(data["rt"]),
                    str(data["total"]),
                    datetime.datetime.strptime(data["start"],'%Y%m%d'),                        
                    str(data["year"]),
                    str(symbol),
                    str(data["name"]).replace(" ", ""),
                    ])
                print(data["name"], end="\n")
            except:
                print("Exception", )
                print(sys.exc_info())
                pass

        print("inserting to db.", end = "\n")
        if elements:
            self.cassandra_dao.batch_execute_prepared_one_sql(sql, elements, keyspace=self.keyspace ,slice_length=100)
            print('insert to db completed !', end = "\n")
    
def main():
    print('start 10jqka worker !')
    crawl = flush(AREA_KEY)
#     stocks = crawl.craw_ratio()
#     crawl.insert_to_db(stocks)
    crawl.crawl_quote()
    print('crawl 10jqka has Completed !')

if __name__ == "__main__":
    main()