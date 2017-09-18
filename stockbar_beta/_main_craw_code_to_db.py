'''
Created on Aug 31, 2017

@author: Coder_J
'''
from stockbar_beta.beta_bar_query_us_lib import beta_bar_query_us
from stockbar_beta.beta_bar_query_hs_lib import beta_bar_query_hs
from sql_helper.mysql_helper_lib import mysql_helper

def insert_usa_stock_code():
    '''  获取所有美股的股票代码，并存入数据库  '''
    
    q = beta_bar_query_us()
    sql_exe = mysql_helper()
    
    codes = q.query_stock_symbols()
    print(codes)
    sql = "INSERT INTO `code` (`code`, `type`) VALUES (%s, %s);"
#     type = 'usa'
    
    for code in codes:
        try:
            sql_exe.insert(sql, (code, type))
        except:
            print( code, "has a error !" )
    print("Completed!")    
    
    sql_exe.close()

def insert_hs_stock_code():
    '''  获取所有A股的股票代码数据，并存入数据库  '''
    q = beta_bar_query_hs()
    sql_exe = mysql_helper()
    
    codes = q.query_stock_symbols()
    print(codes)
    sql = "INSERT INTO `code` (`code`, `type`) VALUES (%s, %s);"
#     type = 'hs'
    
    for code in codes:
        try:
            sql_exe.insert(sql, (code, type))
        except:
            print(code, "has a error !" )
            
    print("Completed!")    
    
    sql_exe.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__ == "__main__":
#     insert_usa_stock_code()
    insert_hs_stock_code()
    