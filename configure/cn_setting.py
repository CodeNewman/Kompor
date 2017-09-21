'''
Created on Sep 13, 2017

@author: Coder_J
'''
# cycle type
LINE = "line"
TIME = "time"

# share type
OFF_SHARE = "0"
ADJ_SHARE = "1"
POS_SHARE = "2"

# transaction cycle
DAY    = "0"
WEEK   = "1"
MONTH  = "2"

# cassandra tables
CN_TABLES_STOCK_RATIO_FROM_10JQKA     = "stock_ratio_from_10jqka"
CN_TABLES_STOCK_BASIC_FROM_10JQKA     = "stock_basic_from_10jqka"

# mysql tables
CN_MYSQL_TABLES_STOCK_BASIC_FROM_10JQKA   = "stock_basic_from_10jqka"

# AWS外网HTTPS地址
AWS_HOST_ADD = 'https://54.223.238.148:8443'

# 办公室 ES_A
CN_CASSANDRA_HOSTS             = ['192.168.199.136',]
CN_CASSANDRA_PORT              =  9042
CN_CASSANDRA_USER              = 'cassandra'
CN_CASSANDRA_PASSWD            = 'cassandra'
CN_CASSANDRA_KEYSPACE          = "cn_kavoutdata"

CN_MYSQL_HOST     = '192.168.199.136'
CN_MYSQL_USER     = 'root'
CN_MYSQL_PASSWD   = 'Kavout@2017'
CN_MYSQL_DB       = 'stock_kompor'

# house config
# CN_CASSANDRA_HOSTS             = ['192.168.199.10',]
# CN_CASSANDRA_PORT              =  9042
# CN_CASSANDRA_USER              = 'cassandra'
# CN_CASSANDRA_PASSWD            = 'cassandra'
# CN_CASSANDRA_KEYSPACE          = "cn_kavoutdata"
# 
# CN_MYSQL_HOST     = '192.168.199.10'
# CN_MYSQL_USER     = 'root'
# CN_MYSQL_PASSWD   = 'abc123'
# CN_MYSQL_DB       = 'stock_kompor'