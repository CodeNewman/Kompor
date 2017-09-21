'''
Created on Aug 31, 2017

@author: Coder_J
'''
import pymysql
import sys
import os
import sys
import multiprocessing
import datetime
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from dao.mysql_dao import mysql_dao
from configure.area_config import AREA_KEY
from crawl_to_cassandra.basic_10jqka import flush
from crawl_lib.kavout import get_hs_price
from tools.format_print import jprint as print


db = mysql_dao()

def craw_quote_hs(codes):
    for code in codes:
        print('getting code', code)
        sql = 'INSERT INTO `quote_hs_bar` (`code`, `date`, `open`, `high`, `low`, `close`, `vol`, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_vol`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        try:
            symbols = [code,]
            val = get_hs_price(symbols, period=65535)
            if val['status'] is not 0:
                print('error code ->', code, val)
                continue;

            prices_array = val['data']['prices'][str(code)]
                
            for stock in prices_array:
                try:
                    if str(stock['tradedate']).startswith('2017'):
                        date = str(stock['tradedate'])
                        date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
                         
                        element = (
                            stock['symbol'],
                            date,
                            stock['topen'],
                            stock['thigh'],
                            stock['tlow'],
                            stock['tclose'],
                            stock['vol'],
                            stock['adj_topen'],
                            stock['adj_thigh'],
                            stock['adj_tlow'],
                            stock['adj_tclose'],
                            stock['adj_vol']
                            )
                        db.insert(sql, element)
                        print('code', code, date, '->Inserted')
                     
                except pymysql.err.IntegrityError:
        #             print('code \t', code, '\t', stock['tradedate'], '\t :already has')
                    pass
        except pymysql.err.InternalError as err:
            print('code \t', code, '\t\t :InternalError')
            print(repr(err))
            pass
        except KeyError:
            print('code \t', code, '\t\t :KeyError')
            try:
                sql_update = 'UPDATE code SET effective = \'F\' WHERE code = %s;'
                db.insert(sql_update, (code,))
                print('F is inserted')
            except:
                pass
            pass
        except TimeoutError as err:
            print('code \t', code, '\t\t :TimeoutError')
            print(repr(err))
            pass
        except:
            print('\t\t', code, '\t\t :OtherError')
            print(sys.exc_info()[0])
            pass

def worker_hs(codes, name):
    craw_quote_hs(codes)
    print('\t\t\t\t\t', name, ' is completed !-------------------------------------------------!')

def filt_codes(codes, start):
    result = []
    for code in codes:
        if str(code).startswith(start):
            result.append(code)
    
    return result

def main():
    codes_hs = flush(AREA_KEY).get_db_symbols()
    # craw_quote_hs(codes_hs)
    print('daily kavout value length is ', len(codes_hs))
    print('working ... ...')
    hs_work_names = [
        '000',
        '002',
        '300',
        '600',
        '601',
        '603'
        ]
    prs = []
    for x in hs_work_names:
        p = multiprocessing.Process(target = worker_hs, args = (filt_codes(codes_hs, x), x, ))
        prs.append(p)
    
    for p in prs:
        p.start()
    
if __name__ == '__main__':
    main()