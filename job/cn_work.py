'''
Created on Sep 14, 2017

@author: Coder_J
'''
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)



from crawl_to_cassandra import basic_10jqka as basic_from_10jqka_to_cassandra
from crawl_to_mysql import basic_10jqka as basic_from_10jqka_to_mysql
from crawl_to_mysql import daily_10jqka as daily_from_10jqka_to_mysql


# do work
basic_from_10jqka_to_cassandra.main()
basic_from_10jqka_to_mysql.main()
daily_from_10jqka_to_mysql.main()