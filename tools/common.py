'''
Created on Sep 1, 2017

@author: Coder_J
'''
    
#     def get_codes(self, area):
#         codes = []
#         sql = 'use stock_kompor; SELECT `symbol` FROM ` ' + CN_MYSQL_TABLES_STOCK_BASIC_FROM_10JQKA + ' ` WHERE type = %s ;'
#         try:
#             codes = db.fetchall_one_column(sql, (area), column='code')
#         except:
#             print("There was an error in the query the stock code!" )
#         return codes

def filt_codes(codes, start):
    result = []
    for code in codes:
        if str(code).startswith(start):
            result.append(code)
    
    return result
    
    
        