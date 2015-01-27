from django.db import models
import pymysql

# Create your models here.

def testConnexion(login,password):
    connection = pymysql.connect(db='ROM',user='root',passwd='root',host='localhost',port=3306)
    cur = connection.cursor()
    result = cur.execute("select * from utilisateurs where login = '"+login+"' and password = md5('"+password+"')")        
    resultats = cur.fetchall()
    if len(resultats) != 0:
        return resultats
    return {}