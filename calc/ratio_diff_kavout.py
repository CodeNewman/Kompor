'''
Created on Sep 20, 2017

@author: Coder_J
'''
import os
import sys
import multiprocessing

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from configure.area_config import AREA_KEY
from crawl_to_cassandra.basic_10jqka import flush
from dao.mysql_dao import mysql_dao
from tools.format_print import jprint as print

SQL_SELECT = "SELECT k.`code`, k.date, k.`open`, k.high, k.low, k.`close`, k.vol, \
k.adj_open, k.adj_high, k.adj_low, k.adj_close, k.adj_vol, d.`open`, d.high, d.low, \
d.`close`, d.vol, d.adj_open, d.adj_high, d.adj_low, d.adj_close, d.adj_vol \
FROM  quote_hs_bar as k, diff_hs_bar as d where k.`code` = d.`code` and \
k.date = d.date and d.code = %s ORDER BY k.date desc LIMIT ##;"
SQL_INSERT = "INSERT INTO `stock_kompor`.`diff_ratio_hs_bar` (`code`, `date`, `open`, \
`high`, `low`, `close`, `vol`, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_vol`) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
SQL_UPDATE = "UPDATE `stock_kompor`.`diff_ratio_hs_bar` SET `code`=%s, `date`=%s, \
`open`=%s, `high`=%s, `low`=%s, `close`=%s, `vol`=%s, `adj_open`=%s, `adj_high`=%s, \
`adj_low`=%s, `adj_close`=%s, `adj_vol`=%s WHERE (`code`=%s) AND (`date`=%s);"

def calc_ratio_diff(symbol, db):
    increase = '65535'
    sql_select = SQL_SELECT.replace('##', increase)
    
    val = db.fetchall(sql_select, (symbol,))
    for row in val:        
        code              = row['code']
        date              = str(row['date'])
        ratio_open        = calc_ratio(row, 'open',      'd.open')
        ratio_high        = calc_ratio(row, 'high',      'd.high')
        ratio_low         = calc_ratio(row, 'low',       'd.low')
        ratio_close       = calc_ratio(row, 'close',     'd.close')
        ratio_vol         = calc_ratio(row, 'vol',       'd.vol')
        ratio_adj_open    = calc_ratio(row, 'adj_open',  'd.adj_open')
        ratio_adj_high    = calc_ratio(row, 'adj_high',  'd.adj_high')
        ratio_adj_low     = calc_ratio(row, 'adj_low',   'd.adj_low')
        ratio_adj_close   = calc_ratio(row, 'adj_close', 'd.adj_close')
        ratio_adj_vol     = calc_ratio(row, 'adj_vol',   'd.adj_vol')

        element = [code, date, ratio_open, ratio_high, ratio_low, ratio_close, ratio_vol, \
                   ratio_adj_open, ratio_adj_high, ratio_adj_low, ratio_adj_close, ratio_adj_vol]
                    
        condition = [code, date]
        
        if check_zero(element) is not True:
            db.safe_updata_value(SQL_INSERT, SQL_UPDATE, element, condition)

def calc_ratio(row, index1, index2):
    result = None
    try:
        result = round( float( row[index2] ) / float( row[index1] )  , 10)
    except:
        pass
    return result


def check_zero(element):    
    for x in range(len(element)):
        if x > 2 and element[x] != 0:
            return False
    return True


def worker(symbols, work_id):
    db = mysql_dao()
    
    for symbol in symbols:
        calc_ratio_diff(symbol, db)
    print('calculator completed ! work_id ->', work_id)

def main():
    symbols = flush(AREA_KEY).get_db_symbols()
    print('start diff price, length is', len(symbols))
    work_index = 0

    step = 65535

    for index in range(0, len(symbols), step):
        work_index += 1
        work_sy =symbols[index : index + step]
        p = multiprocessing.Process(target = worker, args = (work_sy, work_index))
        p.start()
    
    print('diff price task has', work_index, 'process.')

if __name__ == '__main__':
    main()