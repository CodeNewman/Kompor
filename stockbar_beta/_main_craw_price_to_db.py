'''
Created on Aug 31, 2017

@author: Coder_J
'''
import multiprocessing
import pymysql
from sql_helper.mysql_helper_lib import mysql_helper as db
from stockbar_beta.beta_bar_query_us_lib import beta_bar_query_us as us_quote_query
from stockbar_beta.beta_bar_query_hs_lib import beta_bar_query_hs as hs_quote_query
import sys


db = db()
us_quote_query = us_quote_query()
hs_quote_query = hs_quote_query()

def get_codes(area):
    codes = []
    sql = 'SELECT `code` FROM `code` WHERE `code`.type = %s ;'
    try:
        codes = db.fetchall_one_column(sql, (area), column='code')
    except:
        print("There was an error in the query the stock code!" )
    return codes

def craw_quote_usa(codes):
    for code in codes:
        sql = 'INSERT INTO `quote_usa_bar` (`code`, `date`, `open`, `high`, `low`, `close`, `vol`, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_vol`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        try:
#             print('doing\t', code,)
            prices_array = us_quote_query.query_stock_bar(code, days='150')[code]
            for stock in prices_array:
                try:
                    if str(stock['date']).startswith('2017'):
                        element = (
                            stock['symbol'],
                            stock['date'],
                            stock['open'],
                            stock['high'],
                            stock['low'],
                            stock['close'],
                            stock['volume'],
                            stock['adj_open'],
                            stock['adj_high'],
                            stock['adj_low'],
                            stock['adj_close'],
                            stock['adj_volume']
                            )
                        db.insert(sql, element)
                        print('code \t', code, '\t', stock['date'],'\t\t :Inserted')
                
                except pymysql.err.IntegrityError:
            #             print('code \t', code, '\t', stock['date'], '\t :already has')
                    pass
        except pymysql.err.InternalError as err:
#             print('code \t', code, '\t\t :InternalError')
#             print(repr(err))
            pass
        except KeyError:
#             print('code \t', code, '\t\t :KeyError')
            try:
                sql_update = 'UPDATE code SET effective = \'F\' WHERE code = %s;'
                db.insert(sql_update, (code,))
#                 print('F is inserted')
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

def craw_quote_hs(codes):
    for code in codes:
        sql = 'INSERT INTO `quote_hs_bar` (`code`, `date`, `open`, `high`, `low`, `close`, `vol`, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_vol`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        try:
#             print('doing\t', code,)
            prices_array = hs_quote_query.query_stock_bar(code, days='300')[code]
                        
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
                        print('code \t', code, '\t', date, '\t\t :Inserted')
                
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

def craw_quote_usa_2(codes):
    sql = 'INSERT INTO `quote_us_bar` (`code`, `date`, `open`, `high`, `low`, `close`, `vol`, `adj_open`, `adj_high`, `adj_low`, `adj_close`, `adj_vol`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
    para_codes = ','.join(codes)
    prices_array = us_quote_query.query_stock_bar(para_codes, days='7')
    print(prices_array)
    for code in codes:
        try:
            stock_prices = prices_array[code]
            
            for stock in stock_prices:
                if str(stock['date']).startswith('2017'):
                        element = (
                            stock['symbol'],
                            stock['date'],
                            stock['open'],
                            stock['high'],
                            stock['low'],
                            stock['close'],
                            stock['volume'],
                            stock['adj_open'],
                            stock['adj_high'],
                            stock['adj_low'],
                            stock['adj_close'],
                            stock['adj_volume']
                            )
                        db.insert(sql, element)
    #                 print('craw_quote_usa: Insert ', code)
        except :
            print('craw_quote_usa->', code, ' has a exception. ')
            pass

def worker_usa(codes, name):
    craw_quote_usa(codes)
    print('\t\t\t\t\t', name, ' is completed !-------------------------------------------------!')

def worker_hs(codes, name):
    craw_quote_hs(codes)
    print('\t\t\t\t\t', name, ' is completed !-------------------------------------------------!')

def filt_codes(codes, start):
    result = []
    for code in codes:
        if str(code).startswith(start):
            result.append(code)
    
    return result

if __name__ == '__main__':
    codes_usa = get_codes("usa")
    codes_hs = get_codes("hs")
    
    for x in [chr(i) for i in range(65,91)]:
        p = multiprocessing.Process(target = worker_usa, args = (filt_codes(codes_usa, x), x, ))
        p.start()
    
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
    
    print('Init Success')
    