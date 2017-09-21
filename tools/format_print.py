'''
Created on Sep 19, 2017

@author: Coder_J
'''

import time

def jprint(*args, end='\n'):  # @ReservedAssignment
    sys_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print('[' + sys_time + ']',end=' ')
    print(*args, end=end)