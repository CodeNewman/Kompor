'''
Created on 2017年8月1日

python对cassandra的一些操作

@author: liqing
'''
from cassandra import ConsistencyLevel
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster, ResultSet
from cassandra.query import BatchStatement, SimpleStatement


class CassandraDao(object):
    """
    python对cassandra的一些操作
    """
    cluster = None
    def __init__(self, username, password, contact_points, port):
        """
        初始化连接
        """
        csd_auth = PlainTextAuthProvider(username, password)
        cluster = Cluster(contact_points, port=port, auth_provider=csd_auth)
        self.cluster = cluster
    
    def shutdown(self):
        if self.cluster:
            self.cluster.shutdown()
    
    def get_session(self, keyspace=None):
        """
        得到Session
        """
        return self.cluster.connect(keyspace, keyspace)
    
    def execute_sql(self, sql, keyspace=None):
        """
        普通的SQL执行
        """
        session = self.get_session(keyspace)
        return session.execute(sql)
        
    
    def execute_prepared_sql(self, sql, parameters, consistency_level=None, keyspace=None):
        """
        执行一条Sql
        :sql
            执行Prepared Statements 的Sql
        :parameters
            是一个List，元素是对应的参数
        """
        session = self.get_session(keyspace)
        prepared_statement = session.prepare(sql)
        if consistency_level:
            prepared_statement.consistency_level = consistency_level
        else:
            prepared_statement.consistency_level = ConsistencyLevel.LOCAL_QUORUM
        return session.execute(prepared_statement, parameters)
    
    def get_prepared_statement(self, sql, consistency_level=None, keyspace=None):
        """
        预处理SQL
        """
        session = self.get_session(keyspace)
        prepared_statement = session.prepare(sql)
        if consistency_level:
            prepared_statement.consistency_level = consistency_level
        else:
            prepared_statement.consistency_level = ConsistencyLevel.LOCAL_QUORUM
        return session, prepared_statement
        
        
    
    def batch_execute_prepared_one_sql(self, sql, parameters, consistency_level=None, keyspace=None, slice_length=200):
        """
        相同操作（语义）的SQL，批量执行，比如批量插入和更新等
        :sql
            执行Prepared Statements 的Sql
        :parameters
            是一个List，元素是也是一个list或者tuple
        """
        def slice_execute(session, prepared_statement, consistency_level, parameters):
            """
            分片执行
            """
            if consistency_level:
                batch = BatchStatement(consistency_level=consistency_level)
            else:
                batch = BatchStatement(consistency_level=ConsistencyLevel.LOCAL_QUORUM)
            
            for paras in parameters:
                batch.add(prepared_statement, paras)        
            return session.execute(batch)
        
        
        session = self.get_session(keyspace)
        prepared_statement = session.prepare(sql)
        step = slice_length
        start = 0
        length = len(parameters)
        while start < length:
            end = start + step
            if end >= length:
                end = length
            tmp = parameters[start:end]
            slice_execute(session, prepared_statement, consistency_level, tmp)
            start = end
        
        
        
        
    
    def batch_execute_prepared_sqls(self, sqls, parameters, consistency_level=None, keyspace=None):
        """
        不同同操作（语义）的SQL，批量执行，比如批量插入和更新等
        :sqls
            执行Prepared Statements 的Sql,是一个List,每个元素是一条SQL操作
        :parameters
            是一个List，元素是也是一个list或者tuple
        """
        if len(sqls) != len(parameters):
            return False
        
        session = self.get_session(keyspace)
        if consistency_level:
            batch = BatchStatement(consistency_level=consistency_level)
        else:
            batch = BatchStatement(consistency_level=ConsistencyLevel.LOCAL_QUORUM)
        
        for sql, paras in zip(sqls, parameters):
            batch.add(SimpleStatement(sql), paras)
        
        return session.execute(batch)
            
    
