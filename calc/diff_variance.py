'''
Created on Sep 21, 2017

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


db_stock_col_grade = [
    'open', 'high', 'low', 'close', 'vol', \
    'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_vol', ]


SQL_SELECT = "SELECT %s FROM diff_hs_bar WHERE `code` = %s and diff_hs_bar.date LIKE '2017______' ORDER BY date ASC"

SQL_INSERT = "INSERT INTO `stock_kompor`.`diff_variance_hs_bar` (`code`, `year`, `open`, \
`high`, `low`, `close`, `vol`, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_vol`) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

SQL_UPDATE = "UPDATE `stock_kompor`.`diff_variance_hs_bar` SET `code`=%s, `year`=%s, \
`open`=%s, `high`=%s, `low`=%s, `close`=%s, `vol`=%s, `adj_open`=%s, `adj_high`=%s, \
`adj_low`=%s, `adj_close`=%s, `adj_vol`=%s WHERE (`code`=%s) AND (`year`=%s);"

def worker(symbols, work_id):
    print('worker started ->', work_id)
    db = mysql_dao()
    for symbol in symbols:
        handle_a_stock(symbol, db, work_id)
    db.commit()
    db.close()
    print('calculator completed ! work_id ->', work_id)

def main():
    symbols = flush(AREA_KEY).get_db_symbols()
    print('start task calculate variance, length is', len(symbols))
    work_index = 0
    step = 10
    for index in range(0, len(symbols), step):
        work_index += 1
        work_sy =symbols[index : index + step]
        p = multiprocessing.Process(target = worker, args = (work_sy, work_index))
        p.start()    
    print('calculate variance task has', work_index, 'process.')


def handle_a_stock(symbol, db, work_id):
    # ''' 计算一只股票的方差，并直接保存到数据库中 '''
    variances = [symbol, '2017']
    condition = [symbol, '2017']
    
    for col_head in db_stock_col_grade:
        p_variance = 0        
        try:
            p_grades = db_grades(symbol, col_head, db)
            if len(p_grades) is not 0:
                p_average = grades_average(p_grades)
                p_average = round(p_average, 10)
                p_variance = grades_variance(p_grades, p_average)
                p_variance = round(p_variance, 10)
        except:
            pass
        variances.append(p_variance)

    db.safe_updata_value(SQL_INSERT, SQL_UPDATE, variances, condition, ['calculate floating variance, work id:', work_id] )

        

def db_abs_range(cur, code, average, col_head):
    # '''  È¡×î´ó²îÖµ  '''
    sql = 'SELECT MAX(u_stock_bar_data.%s) FROM u_stock_bar_data WHERE u_stock_bar_data.stock_code = \'%s\'' %(col_head, str(code))
    mmax = db_value_format(cur, sql)[0]
    max_rate = round((abs(mmax - average) / average), 4)
    sql = 'SELECT MIN(u_stock_bar_data.%s) FROM u_stock_bar_data WHERE u_stock_bar_data.stock_code = \'%s\'' %(col_head, str(code))
    mmin = db_value_format(cur, sql)[0]
    min_rate = round((abs(mmin - average) / average), 4)
    if max_rate > min_rate :
        return [mmax, max_rate]
    else:
        return [mmin, min_rate]


def db_grades(symbol, col_head, db):
    # ''' 计算单列方差 '''
    sql = SQL_SELECT % (col_head, symbol)
    values = db.fetchall_no_element(sql)
    return db_value_format(values, col_head)
    

def db_value_format(values, col_head):
    result = []
    for item in values:
        if item[col_head] is not None:
            result.append(float(item[col_head]))
    return result


def grades_sum(grades):
    ''' 求和 '''
    total = 0
    for grade in grades:
        total += grade
    return total


def grades_average(grades):
    '''  计算平均值  '''
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average


def grades_variance(scores, average=None):
    ''' 计算方差 '''
    if average == None:
        average=grades_average(scores)
    variance=0
    for score in scores:
        variance+=(average-score)**2
    return variance/len(scores)


if __name__ == '__main__':
    main()