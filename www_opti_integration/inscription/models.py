from django.db import models
import pymysql

# Create your models here.

def connexion():
    return pymysql.connect(db='ROM',user='root',passwd='root',host='localhost',port=3306)


def verifie_login_existe(login):
    connection = connexion()
    cur = connection.cursor()
    result = cur.execute("select * from utilisateurs where login = '"+login+"' ")        
    if len(cur.fetchall()) != 0:
        return True
    return False


def creer_utilisateur(login,password,name,firstname,profil,chemin_espace_perso):
    connection = connexion()
    try:
        cur = connection.cursor()
        request = ("INSERT INTO `ROM`.`utilisateurs`(`login`,`password`,`nom`,`prenom`,`profil`,`chemin_espace`)VALUES('%s',md5('%s'),'%s','%s','%s','%s')" %(login,password,name,firstname,profil,chemin_espace_perso)) 
        print(request)
        cur.execute(request)        
        connection.commit()
        return "OK"
    except Exception as err:
        print(err)
        return "ERROR"
    