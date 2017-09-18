'''
Created on Sep 18, 2017

@author: Coder_J
'''
import enum

CRAWL_PAGE_TYPE = enum.Enum("CRAWL_PAGE_TYPE", (
    'json',
    'text',
    'html',
    ))
