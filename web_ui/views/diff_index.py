from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sqlite3
import os
from kompor.settings import BASE_DIR
from dao.mysql_dao import mysql_dao

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    sql = 'SELECT * FROM diff_count'
    db = mysql_dao()
    result = db.fetchall_no_element(sql)    
    return render(request, base_dir + '\\templates\\index.html', {'result': result})
#     return HttpResponse(result)


    