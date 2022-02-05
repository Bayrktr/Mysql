import mysql.connector
from datetime import datetime
import random, string

menu = ["kahve", "cay", "latte", "sut", "ekspresso", "americano", "meyvesuyu", "islakkek", "kurupasta", "cikolata"]


def randomList(number=string.digits):
    a = 0
    sayilari = []
    number = list(number)
    while a < 10:
        a += 1
        sayilari.append(random.choice(number))
    return sayilari


def main():
    username = input("username ? ")
    if personControl(username) == True:
        sayilari = randomList()
        insert(username, sayilari)
        print("Islem Bitti")


def personControl(username):
    liste = []
    db = openMysql()
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    for x in cursor:
        liste.append(x[0])
    print(liste)
    if liste == []:
        print("Tablo boş")
        return False
    else:
        if str(username) in liste:
            print("Username mevcut")
            return True
        else:
            print("Username mevcut değil")
            return False


def insert(username, sayilari):
    db = openMysql()
    cursor = db.cursor()
    sql = "INSERT INTO {} ({},{},{},{},{},{},{},{},{},{},time) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        username, menu[0], menu[1], menu[2], menu[3], menu[4], menu[5], menu[6], menu[7], menu[8], menu[9], sayilari[0],
        sayilari[1], sayilari[2], sayilari[3], sayilari[4], sayilari[5], sayilari[6], sayilari[7], sayilari[8],
        sayilari[9], timeSettings())
    cursor.execute(sql)
    db.commit()


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="menu")


def timeSettings(now=datetime.today()):
    timeNow = []
    timeNow.append(str(now.year)), timeNow.append(str(now.month)), timeNow.append(str(now.day)), timeNow.append(
        str(now.hour)), timeNow.append(str(now.minute))
    return ".".join(timeNow)


if __name__ == "__main__":
    main()
