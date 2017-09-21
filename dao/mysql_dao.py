'''
Created on Aug 31, 2017

@author: Coder_J
'''
import pymysql.cursors
from configure.cn_setting import CN_MYSQL_HOST, CN_MYSQL_USER, CN_MYSQL_PASSWD,\
    CN_MYSQL_DB

from tools.format_print import jprint as print

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
    
    cursor = connection.cursor()
    
    def execute(self, sql, element):
        ''''  封装执行方法  '''
        try:            
            self.cursor.execute(sql, element)
        finally:
            pass
    
    def commit (self):
        self.connection.commit()
    
    def execute_old(self, sql, element):
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

    def fetchall(self, sql, element):
        '''  封装 获取所有数据，带参数  '''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, element)
                result = cursor.fetchall()
                return result 
        finally:
            pass

    def fetchall_one_column(self, sql, element, column):
        '''  获取一行数据  '''
        try:
            result = []
            with self.connection.cursor() as cursor:
                cursor.execute(sql, element)
                vals = cursor.fetchall()
                for item in vals:
                    result.append(item[column])
                return result
        finally:
            pass

    def close(self):
        '''  关闭数据库连接通道  '''
        self.cursor.close()
        self.connection.close()

    def insert_value_to_db(self, sql, element, code):
        return self.update_value_to_db(sql, element, code)
    
    def update_value_to_db(self, sql, element, code):
        msg = 'ok'
        try:
            self.update(sql, element)
            print('code', code,'updated ->', element)
              
        except pymysql.err.IntegrityError:
            msg = 'IntegrityError'
            pass
        except Exception as e:
            print('diff update', element[0], element[1], "Error !", end=' ')
            print(e, end=' ')
            print(element)
            pass
        return msg
    
    def safe_updata_value(self, insert_url, update_url, element, condition, task_name=None):
        try:
            self.insert(insert_url, element)
            print(task_name,'insert', element[0], element[1], "OK !")
        except pymysql.err.IntegrityError:
            for item in condition:
                element.append(item)
            self.update(update_url, element)
            print(task_name,'update', element[0], element[1], "OK !")
        except Exception as e:
            print(task_name,'safe update value', element[0], element[1], "Error !", e, 'element:', element)
            pass

