'''
Created on Aug 31, 2017

@author: Coder_J
'''
import pymysql.cursors
from configure.cn_setting import CN_MYSQL_HOST, CN_MYSQL_USER, CN_MYSQL_PASSWD,\
    CN_MYSQL_DB
import sys

class mysql_dao(object):
    '''
    classdocs
    '''
    # 
    connection = pymysql.connect(host=CN_MYSQL_HOST,
                                 user=CN_MYSQL_USER,
                                 password=CN_MYSQL_PASSWD,
                                 db=CN_MYSQL_DB,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        
    def execute(self, sql, element):
        ''''  封装执行方法  '''
        try:            
            with self.connection.cursor() as cursor:
                cursor.execute(sql, element)
            self.connection.commit()
        finally:
            pass
        
    def insert(self, sql, element):
        ''''  封装插入方法  '''
        self.execute(sql, element)
        
    def update(self, sql, element):
        ''''  封装执行方法  '''
        self.execute(sql, element)

    def fetchall_no_element(self, sql):
        '''  封装 获取所有数据 ，不带参数 '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result 
        finally:
            pass

    def fetchall(self,  sql, element):
        '''  封装 获取所有数据，带参数  '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, element)
                result = cursor.fetchall()
                return result 
        finally:
            pass

    def fetchall_one_column(self,  sql, element, column):
        '''  获取一行数据  '''
        try:
            result = []
            with self.connection.cursor() as cursor:
                cursor.execute(sql, element)
                all = cursor.fetchall()  # @ReservedAssignment
                for item in all:
                    result.append(item[column])
                return result
        finally:
            pass

    def close(self):
        '''  关闭数据库连接通道  '''
        self.connection.close()

    def insert_value_to_db(self, sql, element, code):
        return self.update_value_to_db(sql, element, code)
    
    def update_value_to_db(self, sql, element, code):
        msg = 'ok'
        try:
            self.update(sql, element)
            print('code \t', code, '\t :Updated')
              
        except pymysql.err.IntegrityError:
#             print('code \t', code, '\t', code, '\t :already has')
            msg = 'IntegrityError'
            pass
        except pymysql.err.ProgrammingError as err:
            print('code \t', code, '\t', code, '\t :ProgrammingError')
            print(repr(err))
            print(element)
            pass
        except pymysql.err.InternalError as err:
            print('code \t', code, '\t\t :InternalError')
            print(repr(err))
            print(element)
            pass
        except KeyError:
            print('code \t', code, '\t\t :KeyError')
            print(element)
            pass
        except TimeoutError as err:
            print('code \t', code, '\t\t :TimeoutError')
            print(repr(err))
            print(element)
            pass
        except pymysql.err.DataError as err:
            print('code \t', code, '\t\t :pymysql.err.DataError')
            print(repr(err))
            print(element)
            pass
        except ValueError as err:
            print('code \t', code, '\t\t :ValueError')
            print(repr(err))
            print(element)
            pass
        except TypeError as err:
            print('code \t', code, '\t\t :TypeError')
            print(repr(err))
            print(element)
            pass
        except:
            print('\t\t', code, '\t\t :OtherError')
            print(sys.exc_info()[0])
            print(element)
            pass
        return msg