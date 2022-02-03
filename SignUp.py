import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random,re
from mailandpass import MAIL, MAIL_SIFRE
from datetime import datetime


def Names():
    data = []
    username, password, email = input("Username ?"), input("Password ?"), input("Mail ?")
    print(checkUsername())
    if username in checkUsername():
        print("username kullanılıyor")
    else:
        if email in checkEmail():
            print("Email kullanılıyor")
        else:
            print("Hesap olusturuluyor")
            code = randomCode()
            sendMailCode(code, email)
            readCode = input("Code = ?")
            if len(re.findall("%D+", str(readCode))) != 0:
                print("Code Sadece sayılardan olusur.")
            else:
                if int(readCode) == int(code):
                    recordUser(username, password, email)
                    print("Kayıt tamamlandı.")
                else:
                    print("Kod yanlıs")


def timeSettings(now=datetime.today()):
    timeNow = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)
    return timeNow


def randomCode():
    return random.randint(1000, 9999)


def recordUser(username, password, email):
    db = connectMysql()
    cursor = db.cursor()
    sql = "INSERT INTO `userrecords`(`username`, `password`, `mail`, `time`) VALUES (%s,%s,%s,%s)"
    content = (username, password, email, timeSettings())
    cursor.execute(sql, content)
    db.commit()


def connectMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="menu")


def checkUsername():
    db = connectMysql()
    cursor = db.cursor()
    liste = []
    cursor.execute("SELECT username FROM userrecords")
    for x in cursor:
        liste.append(x[0])
    return liste


def checkEmail():
    db = connectMysql()
    cursor = db.cursor()
    liste = []
    cursor.execute("SELECT mail FROM userrecords")
    for x in cursor:
        liste.append(x[0])
    return liste


def sendMailCode(code, email):
    msj = MIMEMultipart()
    msj['from'] = str(MAIL)
    msj['to'] = str(email)
    msj['subject'] = "Deneme Maili"

    text = "Dogrulama Kodu:{}".format(code)

    msjBuilt = MIMEText(text, 'plain')
    msj.attach(msjBuilt)
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(msj['from'], str(MAIL_SIFRE))
        mail.sendmail(msj['from'], msj['to'], msj.as_string())
        print('Mail gönderildi')
        mail.close()
    except:
        print('hata oluştu')


if __name__ == "__main__":
    Names()
