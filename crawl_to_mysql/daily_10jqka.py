'''
Created on Aug 31, 2017

@author: Coder_J
'''
from dao.mysql_dao import mysql_dao as mysql_db
from crawl_lib.crawl import crawl
import multiprocessing
from configure.area_config import AREA_KEY
from configure.cn_setting import DAY, LINE, OFF_SHARE, ADJ_SHARE
from url_lib import url_cn
from crawl_to_cassandra.basic_10jqka import flush
from tools.common import filt_codes


db = mysql_db()
crawl = crawl()

def craw_quote_hs_2017(codes):
    '''
    获取A股数据
    
    http://d.10jqka.com.cn/v2/line/hs_600000/01/last.js
    '''
    type = LINE  # @ReservedAssignment
    area = AREA_KEY
    flag = OFF_SHARE + DAY
    year = '2017'
    db_name = '10jqka_hs_00_bar'
    
    for code in codes:    
        print('--------------------doing--------------------\t', code,)
        craw_10jqka(type, area, code, flag, year, db_name)
    
    flag = ADJ_SHARE + DAY
    db_name = '10jqka_hs_01_bar'
    for code in codes:
        craw_10jqka(type, area, code, flag, year, db_name)

def craw_quote_usa_2017(codes):
    '''
    获取美股数据
    
    http://d.10jqka.com.cn/v2/line/usa_AAPL/01/last.js
    '''
    type = LINE  # @ReservedAssignment
    area = 'usa'
    flag = '01'
    year = '2017'
    db_name = '10jqka_usa_01_bar'
    
    for code in codes:    
        print('--------------------doing--------------------\t', code,)
        craw_10jqka(type, area, code, flag, year, db_name)

def craw_10jqka(type, area, code, flag, year, db_name):  # @ReservedAssignment
    '''  获取单个股票的数据  '''
    
    inserl_sql = 'INSERT INTO `%s` (`code`, `date`, `type`, `open`, `high`, `low`, `close`, `vol`, `val_01`, `val_02`) VALUES (##, ##, ##, ##, ##, ##, ##, ##, ##, ##);' % (db_name)
    inserl_sql = inserl_sql.replace('##', '%s')
    update_sql = "UPDATE %s SET `code`=##, `date`=##, `type`=##, `open`=##, `high`=##, `low`=##, `close`=##, `vol`=##, `val_01`=##, `val_02`=## WHERE (`code`=##) AND (`date`=##);" %(db_name)
    update_sql = update_sql.replace('##', '%s')
    
#     url = jurl.get(type, area, code, flag, year)
    url = url_cn.get_share_url(LINE, AREA_KEY, code, OFF_SHARE, DAY, year)
    datas = crawl.craw_to_list(url)
    
    if datas == []:
        return
    
    for row in datas:
        row = str(row).split(',')
        date = row[0]
        date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
        
        elem = []
        for r in row:
            if len(r) == 0:
                r = None
            elem.append(r)
        row = elem
        
        element = [
            code,
            date,
            flag,
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            ]
        
#         db.insert_value_to_db(sql, element, code)
        flag = db.insert_value_to_db(inserl_sql, element, code)
        if flag == "IntegrityError":
            element.append(code)
            element.append(date)
            db.update_value_to_db(update_sql, element, code)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def worker_usa(codes, name):
    craw_quote_usa_2017(codes)
    print('\t\t\t\t\t', name, ' is completed !-------------------------------------------------!')

def worker_hs(codes, name):
    craw_quote_hs_2017(codes)
    print('\t\t\t\t\t', name, ' is completed !-------------------------------------------------!')

def main():
#     codes_usa = tool.get_codes("usa")
    codes_hs = flush(AREA_KEY).get_db_symbols()
    print(codes_hs)
    
#     for x in [chr(i) for i in range(65,91)]:
#         p = multiprocessing.Process(target = worker_usa, args = (tool.filt_codes(codes_usa, x), x, ))
#         p.start()
    
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