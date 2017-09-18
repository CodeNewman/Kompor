'''
Created on Sep 14, 2017

@author: Coder_J
'''
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)
    
    
from crawl_stock import crawl_10jqka


crawl_10jqka.main()