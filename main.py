# import requests
# from win32com.client import Dispatch
from flask import Flask, render_template, request, Blueprint
import mysql.connector as ms
# from wtforms.validators import DataRequired, Email, EqualTo, Length
from validate_email import validate_email
from sec import sec

app = Flask(__name__)
app.register_blueprint(sec, url_prefix="/stock")
# app.register_blueprint(sec, url_prefix="/stock")
# app.register_blueprint(sec, url_prefix="/stock")


@app.route("/home")
def home():
    data = [
        ("01-01-2020",1597),
        ("02-02-2020", 1456),
        ("03-03-2020", 1908),
        ("04-04-2020", 896),
        ("05-05-2020", 755),
        ("06-06-2020", 453),
        ("07-07-2020", 1100),
        ("08-08-2020", 1235),
        ("09-09-2020", 1478),
        ("10-10-2020", 1230),
        ("11-11-2020", 1540),
        ("12-12-2020", 1010),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("home.html",labels=labels,values=values)


@app.route("/login", methods=["GET", "POST"])
def log():
    if request.method == 'POST':
        email = request.form['email']
        pswd1 = request.form['passwd']
        # mydb=ms.connect(host="localhost", user="root", passwd="mysql@!@");cu=mydb.cursor()
        # cu.execute("create database grp");
        # cu.execute("use grp");cu.execute("create table loginfo(name varchar(45), passwd varchar(25))")
        # cu.execute("select loginfo.name from loginfo where email,passwd=(%s,%s)",(email,pswd))
        try:
            mydb = ms.connect(host="localhost", user="root", passwd="mysql@!@")
            cu = mydb.cursor()
            cu.execute("use max")
            l = cu.execute("select * from userx where email=%s", (email,))
            p=cu.execute("select * from userx where pswd=%s",(pswd1,))
            p1=cu.fetchall()
            # lst = cu.fetchall()
            if l is not None:
                if pswd1 in p1 :
                # if p is not None:
                    return render_template("home.html")
                else:
                    return "pswd error"
            else:
                return "user doesn\'t exists"
            mydb.commit();
            cu.close()
            return render_template("home.html")
        except Exception as e:
            return str(e)

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def sign():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        pswd = request.form['passwd']
        pswd2 = request.form['passwd1']
        ph = request.form['phone']
        try:
            mydb = ms.connect(host="localhost", user="root", passwd="mysql@!@");
            cu = mydb.cursor()
            # cu.execute("create database max");
            cu.execute("use max");
            # cu.execute("create table Signup(username varchar(50) ,email varchar(320) primary key,phone varchar(20),pswd varchar(20))")
            # cu.execute("create table userx(uname varchar(50),email varchar(320) primary key,phone varchar(20),pswd varchar(20))")
            lst = cu.fetchall()
            if (email,) in lst:
                return "Email already exists!!"
            else:
                if str(validate_email(email)) == "False":
                    return "invalid email address"
                cu.execute("insert into Signup values(%s,%s,%s,%s)", (user, email, ph, pswd,))
                # cu.execute("insert into userx values(%s,%s,%s,%s)", (user, email, ph, pswd,))
                mydb.commit();
                print(validate_email(email));
            cu.close();
            return render_template("login.html")
        except Exception as e:
            if "Duplicate entry" in str(e):
                return "Email already exists!!"
            else:
                return str(e)
    return render_template("signup.html")


@app.route("/")
@app.route("/wel")
def welc():
    return render_template("welcome.html")


@app.route("/status")
def stat():

    data1 = [
        ("01-01-2020", 3098),
        ("02-02-2020", 2356),
        ("03-03-2020", 508),
        ("04-04-2020", 4096),
        ("05-05-2020", 655),
        ("06-06-2020", 1453),
        ("07-07-2020", 100),
        ("08-08-2020", 1135),
        ("09-09-2020", 2678),
        ("10-10-2020", 4130),
        ("11-11-2020", 140),
        ("12-12-2020", 1310),
    ]

    labels1 = [row[0] for row in data1]
    values1= [row[1] for row in data1]
    return render_template("Stocks.html", labels=labels1, values=values1)


    # return render_template("Stocks.html")

@app.route("/cust")
def customer():
    return render_template("index.html")














@app.route("/news")
def NewsFromBBC():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = request.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    # to read the news out loud for us

    # speak = Dispatcher("SAPI.Spvoice")
    # speak.Speak(results)


# Driver Code
if __name__ == '__main__':
    # function call
    NewsFromBBC()


# Commented login:
#
# if request.method == 'POST':
#     mail = request.form['email']
#     pswd = request.form['passwd']
#     # mydb=ms.connect(host="localhost", user="root", passwd="mysql@!@");cu=mydb.cursor()
#     # cu.execute("create database grp");
#     # cu.execute("use grp");cu.execute("create table loginfo(name varchar(45), passwd varchar(25))")
#     # cu.execute("select loginfo.name from loginfo where email,passwd=(%s,%s)",(email,pswd))
#     # try:
#     mydb = ms.connect(host="localhost", user="root", passwd="mysql@!@");
#     cu = mydb.cursor()
#     cu.execute("use max");
#     # lst = cu.fetchall()
#     cu.execute("SELECT * FROM userx WHERE email =%s", [mail])
#     if cu is not None:
#         data = cu.fetchone()
#         try:
#             if pswd == data['pswd']:
#                 return render_template("home.html")
#             else:
#                 return "here"
#         except Exception:
#             error = 'Invalid Username or Password'
#             return render_template('login.html', error=error);
#     # except Exception:
# return render_template('login.html');
#
# #     if (email,pswd,) in lst:
# #         return render_template("home.html")
# #     else:
# #         return "user doesn\'t exists"
# #     mydb.commit();cu.close()
# # except Exception as e:
# #     return str(e)
#
# # return render_template("login.html")


#
# 2
# try:
#     mydb = ms.connect(host="localhost", user="root", passwd="mysql@!@");
#     cu = mydb.cursor()
#     cu.execute("use max");
#     # lst = cu.fetchall()
#     if cu is not None:
#         d = cu.fetchone();
#         pd = d['pswd']
#         if pd == pswd:
#             return render_template("home.html")
#     else:
#         return "user doesn\'t exists"
#     mydb.commit();
#     cu.close()
# except Exception as e:
#     return str(e)
#
# return render_template("login.html")
