'''
Created on 6 juin 2014

@author: georges
'''
import pymysql


#!/usr/bin/python



def testConnexion(login,password):
    connection = pymysql.connect(db='ROM',user='root',passwd='root',host='localhost',port=3306)
    cur = connection.cursor()
    result = cur.execute("select * from utilisateurs where login = '"+login+"' and password = md5('"+password+"')")        
    if len(cur.fetchall()) != 0:
        return True
    return False