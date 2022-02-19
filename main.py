import mysql.connector
import tkinter as tk
from contents import menuKategori
import re

from datetime import datetime

font = ("Vertana", 25)
font2 = ("Vertana", 15)


def signUp():
    signUpPart = tk.Tk()

    def signUpButton():
        print("aaa")

    def logIn():
        signUpPart.destroy()
        loginRepeat()

    signUpPart.geometry("400x600")
    signUpPart.resizable(width=False, height=False)
    usernameText = tk.Label()
    usernameText.config(text="Username", font=font)
    usernameText.place(x=120, y=20)
    usernamePut = tk.Entry(signUpPart)
    usernamePut.config()
    usernamePut.place(x=120, y=80, width=150, height=50)
    passwordText = tk.Label(signUpPart)
    passwordText.config(text="Password", font=font)
    passwordText.place(x=120, y=160)
    passwordPut = tk.Entry(signUpPart)
    passwordPut.config()
    passwordPut.place(x=120, y=220, width=150, height=50)
    emailText = tk.Label(signUpPart)
    emailText.config(text="Email", font=font)
    emailText.place(x=140, y=290)
    emailPut = tk.Entry(signUpPart)
    emailPut.config()
    emailPut.place(x=120, y=340, width=150, height=50)
    buton = tk.Button(signUpPart)
    buton.config(text="Sign Up", font=font, command=signUpButton)
    buton.place(x=122, y=420)
    buton2 = tk.Button(signUpPart)
    buton2.config(text="Log In", font=font, command=logIn)
    buton2.place(x=10, y=520)


def login():
    def signUpButton():
        loginPart.destroy()
        signUp()

    def loginButton():
        username, password = usernamePut.get(), passwordPut.get()
        liste = tableList()
        print("Tables :", liste)
        if liste == []:
            print("Tablo Boş")
        elif str(username) == "admin":
            print("Admin Sifresi isteniyor")
            if replacePasswords(username, password) == True:
                print("Admin Girisi Tamamlandı")
                loginPart.destroy()
                admin()

        if str(username) in liste:
            print("{} adlı kullanıcının sifresi isteniyor".format(str(username)))
            if replacePasswords(username, password) == True:
                print("{} adlı hesaba giriş gerçekleşti".format(username))
            else:
                print("{} adlı hesaba giriş reddedildi".format(username))

    def tableList():
        liste = []
        db = openMysql()
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")
        for x in cursor:
            liste.append(x[0])
        liste.remove("userrecords")
        liste.remove("foodrecords")
        return liste

    def takePassword(username):
        db = openMysql()
        cursor = db.cursor()
        sql = "SELECT password FROM userrecords WHERE username = '{}'".format(str(username))
        cursor.execute(sql)
        for x in cursor:
            return x[0]

    def replacePasswords(username, password):
        if str(password) == str(takePassword(username)):
            return True
        else:
            return False

    loginPart.geometry("400x600")
    loginPart.resizable(width=False, height=False)
    usernameText = tk.Label(loginPart)
    usernameText.config(text="Username", font=font)
    usernameText.place(x=120, y=40)
    usernamePut = tk.Entry(loginPart)
    usernamePut.config()
    usernamePut.place(x=120, y=100, width=150, height=50)
    passwordText = tk.Label(loginPart)
    passwordText.config(text="Password", font=font)
    passwordText.place(x=120, y=180)
    passwordPut = tk.Entry(loginPart)
    passwordPut.config()
    passwordPut.place(x=120, y=240, width=150, height=50)
    buton = tk.Button(loginPart)
    buton.config(text="Log In", font=font, command=loginButton)
    buton.place(x=135, y=300)
    buton2 = tk.Button(loginPart)
    buton2.config(text="Sing Up", font=font, command=signUpButton)
    buton2.place(x=30, y=500)


# must be fixed
def loginRepeat():
    loginPart = tk.Tk()

    def signUpButton():
        loginPart.destroy()
        signUp()

    def loginButton():
        username, password = usernamePut.get(), passwordPut.get()
        liste = tableList()
        print("Tables :", liste)
        if liste == []:
            print("Tablo Boş")
        elif str(username) == "admin":
            print("Admin Sifresi isteniyor")
            if replacePasswords(username, password) == True:
                admin()
                loginPart.destroy()
                print("Giriş yapıldı")
            else:
                print("şifre yanlıs")
        if str(username) in liste:
            print("{} adlı kullanıcının sifresi isteniyor".format(str(username)))
            if replacePasswords(username, password) == True:
                print("{} adlı hesaba giriş gerçekleşti".format(username))
            else:
                print("{} adlı hesaba giriş reddedildi".format(username))

    def tableList():
        liste = []
        db = openMysql()
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")
        for x in cursor:
            liste.append(x[0])
        liste.remove("userrecords")
        liste.remove("foodrecords")
        return liste

    def takePassword(username):
        db = openMysql()
        cursor = db.cursor()
        sql = "SELECT password FROM userrecords WHERE username = '{}'".format(str(username))
        cursor.execute(sql)
        for x in cursor:
            return x[0]

    def replacePasswords(username, password):
        if str(password) == str(takePassword(username)):
            return True
        else:
            return False

    loginPart.geometry("400x600")
    loginPart.resizable(width=False, height=False)
    usernameText = tk.Label(loginPart)
    usernameText.config(text="Username", font=font)
    usernameText.place(x=120, y=40)
    usernamePut = tk.Entry(loginPart)
    usernamePut.config()
    usernamePut.place(x=120, y=100, width=150, height=50)
    passwordText = tk.Label(loginPart)
    passwordText.config(text="Password", font=font)
    passwordText.place(x=120, y=180)
    passwordPut = tk.Entry(loginPart)
    passwordPut.config()
    passwordPut.place(x=120, y=240, width=150, height=50)
    buton = tk.Button(loginPart)
    buton.config(text="Log In", font=font, command=loginButton)
    buton.place(x=135, y=300)
    buton2 = tk.Button(loginPart)
    buton2.config(text="Sing Up", font=font, command=signUpButton)
    buton2.place(x=30, y=500)


# Must be fixed
def admin():
    def foodList():
        liste = []
        db = openMysql()
        cursor = db.cursor()
        sql = "SELECT food FROM foodrecords"
        cursor.execute(sql)
        for x in cursor.fetchall():
            liste.append(x[0])
        return liste

    def usernames():
        liste = []
        db = openMysql()
        cursor = db.cursor()
        sql = "SELECT username FROM userrecords"
        cursor.execute(sql)
        for x in cursor.fetchall():
            liste.append(x[0])
        return liste



    def updateUsers():
        def update():
            try:
                selectUser, password, mail = usernameList.selection_get(), newpassword.get(), newMail.get()
                if password == "" or mail == "":
                    print("Bos deger")
                else:
                    contentName = ["password", "mail"]
                    contents = [password, mail]
                    db = openMysql()
                    cursor = db.cursor()
                    for x, y in zip(contentName, contents):
                        sql = f"UPDATE userrecords SET {x} = '{y}' WHERE username = '{selectUser}'"
                        cursor.execute(sql)
                        db.commit()
                    print("{} adlı kullanıcının bilgileri güncellendi".format(selectUser))
            except:
                print("Bos deger hatası")

        updateUsersPart = tk.Tk()
        updateUsersPart.geometry("300x500")
        updateUsersPart.resizable(width=False, height=False)
        usernameList = tk.Listbox(updateUsersPart)
        liste = usernames().copy()
        liste.remove("admin")
        a = 0
        for x in liste:
            a += 1
            usernameList.insert(int(a), "{}".format(x))
        usernameList.grid(padx=90, pady=20)
        newpassword = tk.Entry(updateUsersPart)
        newpassword.config()
        newpassword.place(x=85, y=200, width=140, height=50)
        newMail = tk.Entry(updateUsersPart)
        newMail.config()
        newMail.place(x=85, y=270, width=140, height=50)
        updateButton = tk.Button(updateUsersPart)
        updateButton.config(text="Update", font=font2, command=update)
        updateButton.place(x=85, y=340, width=140, height=50)

    def deleteUsers():
        def deleteUser():
            try:
                db = openMysql()
                cursor = db.cursor()
                sql = "DELETE FROM userrecords WHERE username = '{}'".format(usernameList.selection_get())
                cursor.execute(sql)
                db.commit()
                sql = "DROP TABLE {}".format(usernameList.selection_get())
                cursor.execute(sql)
                db.commit()
                print("{} adlı kullanıcı silindi".format(usernameList.selection_get()))
                reflesh()
            except:
                print("Bos deger hatası")

        def reflesh():
            deleteUserPart.destroy()
            deleteUsers()

        deleteUserPart = tk.Tk()
        deleteUserPart.geometry("300x500")
        deleteUserPart.resizable(width=False, height=False)
        usernameList = tk.Listbox(deleteUserPart)
        a = 0
        liste = usernames().copy()
        liste.remove("admin")
        for x in liste:
            a += 1
            usernameList.insert(int(a), "{}".format(x))
        usernameList.grid(padx=90, pady=20)
        deleteButton = tk.Button(deleteUserPart)
        deleteButton.config(text="Delete", font=font2, command=deleteUser)
        deleteButton.place(x=80, y=240, width=150, height=50)

    def addUsers():
        def record():
            def names():
                contents = []
                for x in foodList():
                    contents.append(f"{x} VARCHAR(255)")
                print(",".join(contents))
                return ",".join(contents)

            def namesTwo():
                contents = []
                print(foodList())
                for x in foodList():
                    contents.append(f"{x}")
                print(",".join(contents))
                return ",".join(contents)

            def createZero():
                a = 0
                name = []
                while a < len(foodList()):
                    name.append("'0'")
                    a += 1
                print(",".join(name))
                return ",".join(name)

            def specialTable():
                db = openMysql()
                cursor = db.cursor()
                sql = f"CREATE TABLE {usernameText.get()} ({names()})"
                sqltwo = f"INSERT INTO {usernameText.get()} ({namesTwo()}) VALUES ({createZero()})"
                cursor.execute(sql)
                db.commit()
                cursor.execute(sqltwo)
                db.commit()

            def mails():
                liste = []
                db = openMysql()
                cursor = db.cursor()
                sql = "SELECT mail FROM userrecords"
                cursor.execute(sql)
                for x in cursor.fetchall():
                    liste.append(x[0])
                return liste

            if usernameText.get() == "" or passwordText.get() == "" or emailText == "":
                print("Bos eleman")
            else:
                if usernameText.get() in usernames() or emailText.get() in mails():
                    print("username veya mail zaten kullanılıyor")
                else:
                    if len(foodList()) == 0:
                        print("Menu yok")
                    else:
                        db = openMysql()
                        cursor = db.cursor()
                        sql = f"INSERT INTO userrecords (username,password,mail,time) VALUES ('{usernameText.get()}','{passwordText.get()}','{emailText.get()}','{timeSettings()}')"
                        cursor.execute(sql)
                        db.commit()
                        specialTable()
                        print("{} adlı kullanıcı kaydedildi".format(usernameText.get()))

        addUsersPart = tk.Tk()
        addUsersPart.geometry("300x500")
        addUsersPart.resizable(width=False, height=False)
        usernameText = tk.Entry(addUsersPart)
        usernameText.config()
        usernameText.place(x=70, y=50, width=150, height=50)
        passwordText = tk.Entry(addUsersPart)
        passwordText.config()
        passwordText.place(x=70, y=120, width=150, height=50)
        emailText = tk.Entry(addUsersPart)
        emailText.config()
        emailText.place(x=70, y=190, width=150, height=50)
        recordButton = tk.Button(addUsersPart)
        recordButton.config(text="Record", font=font2, command=record)
        recordButton.place(x=80, y=260, width=140, height=40)

    def deleteFood():
        def delete():
            try:
                if selectFood.selection_get() == "":
                    print("deger boş")
                else:
                    db = openMysql()
                    cursor = db.cursor()
                    cursor.execute("DELETE FROM foodrecords WHERE food = '{}'".format(selectFood.selection_get()))
                    db.commit()
                    print("{} basarıyla silindi".format(selectFood.selection_get()))
                    deleteFoodPart.destroy()
                    deleteFood()
            except:
                print("Bos deger hatası")

        deleteFoodPart = tk.Tk()
        deleteFoodPart.geometry("300x500")
        deleteFoodPart.resizable(width=False, height=True)
        a = 0
        selectFood = tk.Listbox(deleteFoodPart)
        for x in foodList():
            a += 1
            selectFood.insert(int(a), "{}".format(x))
        selectFood.grid(padx=90, pady=20)
        deletebutton = tk.Button(deleteFoodPart)
        deletebutton.config(text="Delete", font=font2, command=delete)
        deletebutton.place(x=80, y=240, width=140, height=40)

    def updateFood():
        def recordUpdate():
            try:
                food = selectFood.selection_get()
                print(food)
                if food == "" or newPrice.get() == "":
                    print("Boş deger girildi")
                else:
                    # print(len(re.findall("\D+", newPrice.get())))
                    if len(re.findall("\D+", newPrice.get())) != 0:
                        print("Sayi dısında bir deger girildi")
                    else:
                        db = openMysql()
                        cursor = db.cursor()
                        cursor.execute(
                            "UPDATE foodrecords SET price = '{}' WHERE food = '{}'".format(newPrice.get(), food))
                        db.commit()
                        print("Food : {}  Price : {} islem basarılı.".format(food, newPrice.get()))
            except:
                print("bos deger hatası")

        def priceList():
            liste = []
            db = openMysql()
            cursor = db.cursor()
            sql = "SELECT price FROM foodrecords"
            cursor.execute(sql)
            for x in cursor.fetchall():
                liste.append(x[0])
            return liste

        def foodList():
            liste = []
            db = openMysql()
            cursor = db.cursor()
            sql = "SELECT food FROM foodrecords"
            cursor.execute(sql)
            for x in cursor.fetchall():
                liste.append(x[0])
            return liste

        a = 0
        updateFoodPart = tk.Tk()
        updateFoodPart.geometry("300x500")
        updateFoodPart.resizable(width=False, height=False)
        selectFood = tk.Listbox(updateFoodPart)
        for x in foodList():
            a += 1
            selectFood.insert(int(a), "{}".format(x))
        selectFood.grid(padx=90, pady=20)
        newPrice = tk.Entry(updateFoodPart)
        newPrice.config()
        newPrice.place(x=75, y=220, width=150, height=50)
        recordButton = tk.Button(updateFoodPart)
        recordButton.config(text="Record", font=font2, command=recordUpdate)
        recordButton.place(x=75, y=300, width=150, height=50)

    def addFood():
        def record():
            try:
                food, price, category = foodtext.get(), pricetext.get(), selectCategory.selection_get()
                if food == "" or price == "" or len(list(category)) == 0:
                    print("Bos deger girildi")
                else:
                    if len(re.findall("\D+", str(price))) != 0:
                        print("Price degeri sadece sayi olabilir")
                    else:
                        if str(food) in foodList():
                            print("Zaten {} mevcut".format(food))
                        else:
                            print(f"Food :{food} Price :{price} Category:{category}")
                            db = openMysql()
                            cursor = db.cursor()
                            sql = "INSERT INTO foodrecords (food,price,category,time) VALUES ('{}','{}','{}','{}')".format(
                                food,
                                price,
                                category,
                                timeSettings())
                            cursor.execute(sql)
                            db.commit()
            except:
                print("boş deger hatası")

        a = 0
        addFoodPart = tk.Tk()
        addFoodPart.geometry("300x500")
        addFoodPart.resizable(width=False, height=False)
        foodtext = tk.Entry(addFoodPart)
        foodtext.config()
        foodtext.place(x=70, y=30, width=150, height=50)
        pricetext = tk.Entry(addFoodPart)
        pricetext.config()
        pricetext.place(x=70, y=120, width=150, height=50)
        selectCategory = tk.Listbox(addFoodPart)
        for x in menuKategori:
            a += 1
            selectCategory.insert(int(a), "{}".format(x))
        selectCategory.grid(padx=80, pady=200)
        recordButton = tk.Button(addFoodPart)
        recordButton.config(text="Record", font=font2, command=record)
        recordButton.place(x=80, y=400, width=120, height=40)

    adminPart = tk.Tk()
    adminPart.geometry("400x600")
    adminPart.resizable(width=False, height=False)
    foodaddButton = tk.Button(adminPart)
    foodaddButton.config(text="Add Food", font=font2, command=addFood)
    foodaddButton.place(x=50, y=50, width=140, height=60)
    foodUpdate = tk.Button(adminPart)
    foodUpdate.config(text="Update Food", font=font2, command=updateFood)
    foodUpdate.place(x=200, y=50, width=140, height=60)
    foodDeleteButton = tk.Button(adminPart)
    foodDeleteButton.config(text="Delete Food", font=font2, command=deleteFood)
    foodDeleteButton.place(x=50, y=120, width=140, height=60)
    usersAddbutton = tk.Button(adminPart)
    usersAddbutton.config(text="Add Users", font=font2, command=addUsers)
    usersAddbutton.place(x=200, y=120, width=140, height=60)
    deleteUserButton = tk.Button(adminPart)
    deleteUserButton.config(text="Delete User", font=font2, command=deleteUsers)
    deleteUserButton.place(x=50, y=190, width=140, height=60)
    updateUserButton = tk.Button(adminPart)
    updateUserButton.config(text="Update User", font=font2, command=updateUsers)
    updateUserButton.place(x=200, y=190, width=140, height=60)


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="menu")


def timeSettings(now=datetime.today()):
    timeNow = []
    timeNow.append(str(now.year)), timeNow.append(str(now.month)), timeNow.append(str(now.day)), timeNow.append(
        str(now.hour)), timeNow.append(str(now.minute))
    return ".".join(timeNow)


if __name__ == "__main__":
    loginPart = tk.Tk()
    login()
    loginPart.mainloop()
