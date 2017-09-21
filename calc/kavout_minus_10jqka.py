'''
Created on Sep 19, 2017

@author: Coder_J
'''
import multiprocessing

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from configure.area_config import AREA_KEY
from crawl_to_cassandra.basic_10jqka import flush
from dao.mysql_dao import mysql_dao
from tools.format_print import jprint as print

def calculate_difference(symbol, db):
    increase = '65535'
    
    symbol = str(symbol)
    sql_view_hs_all_bar = "select * from view_hs_all_bar where code = %s ORDER BY date desc limit " + increase + ";"
    sql_insert_to_diff = "INSERT INTO `stock_kompor`.`diff_hs_bar` \
        (`code`, `date`, `open`, `high`, `low`, `close`, `vol`, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_vol`) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    sql_update_to_diff = "UPDATE `stock_kompor`.`diff_hs_bar` \
        SET `code`=%s, `date`=%s, `open`=%s, `high`=%s, `low`=%s, `close`=%s, `vol`=%s, \
        `adj_open`=%s, `adj_high`=%s, `adj_low`=%s, `adj_close`=%s, `adj_vol`=%s \
        WHERE (`code`=%s) AND (`date`=%s);"
    val = db.fetchall(sql_view_hs_all_bar, (symbol, ))
    for row in val:
        code = row['code']
        date = str(row['date'])
        try:
            diff_open        = round( float( row['qu_open'] )       - float( row['jq_open'] )        ,4)
            diff_high        = round( float( row['qu_high'] )       - float( row['jq_high'] )        ,4)
            diff_low         = round( float( row['qu_low'] )        - float( row['jq_low'] )         ,4)
            diff_close       = round( float( row['qu_close'] )      - float( row['jq_close'] )       ,4)
            diff_vol         = round( float( row['qu_vol'] )        - float( row['jq_vol'] )         ,4)
            diff_adj_open    = round( float( row['qu_adj_open'] )   - float( row['jq_adj_open'] )    ,4)
            diff_adj_high    = round( float( row['qu_adj_high'] )   - float( row['jq_adj_high'] )    ,4)
            diff_adj_low     = round( float( row['qu_adj_low'] )    - float( row['jq_adj_low'] )     ,4)
            diff_adj_close   = round( float( row['qu_adj_close'] )  - float( row['jq_adj_close'] )   ,4)
            diff_adj_vol     = round( float( row['qu_adj_vol'] )    - float( row['jq_adj_vol'] )     ,4)
        except:
            print('diff error', row)
            continue
        
        element = [code, date, diff_open, diff_high, diff_low, diff_close, diff_vol, \
                   diff_adj_open, diff_adj_high, diff_adj_low, diff_adj_close, diff_adj_vol]
        condition = [code, date]
        
        db.safe_updata_value(sql_insert_to_diff, sql_update_to_diff, element, condition)

def calc_diff(row, index1, index2):
    pass

def worker(symbols, work_id):
    db = mysql_dao()
    
    for symbol in symbols:
        calculate_difference(symbol, db)
    
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