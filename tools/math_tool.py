'''
Created on Sep 4, 2017

@author: Coder_J
'''
import math

class math_tool(object):
    '''
    classdocs
    '''
    def grades_sum(self, grades):
        '''  sum  '''
        total = 0
        for grade in grades:
            total += grade
        return total
    
    def grades_average(self, grades):
        '''  averaging  '''
        sum_of_grades = self.grades_sum(grades)
        average = sum_of_grades / float(len(grades))
        return average
    
    def grades_variance(self, scores, average=None):
        '''  Strives for the variance  '''
        if average == None:
            average=self.grades_average(scores)
        variance=0
        for score in scores:
            variance+=(average-score)**2
        var=variance/len(scores)
        return math.sqrt(var)