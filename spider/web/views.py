from django.shortcuts import render
from django.http import JsonResponse
import pymysql
# Create your views here.

def showPosition(request):

    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        database='lagou',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from jobs order by formatCreateTime desc;"
    all = cursor.execute(sql)
    obj = cursor.fetchall()
    return  render(request,'position.html',{"obj":obj})

def showCompany(request):
    id = request.GET.get('id','')
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        database='lagou',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from jobs where order_id='{}' order by formatCreateTime desc;".format(id)
    all = cursor.execute(sql)
    obj = cursor.fetchone()
    return JsonResponse(obj)




