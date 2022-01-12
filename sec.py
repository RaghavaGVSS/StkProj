from flask import Blueprint,render_template
# import numpy as np
# import pandas as pd
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
#
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.ensemble import RandomForestClassifier
#
# import seaborn as sns


sec= Blueprint("sec",__name__,static_folder="static",template_folder="templates")

@sec.route("/stat1")
def sts():
    data = [
        ("01-01-2020", 198),
        ("02-02-2020", 356),
        ("03-03-2020", 508),
        ("04-04-2020", 496),
        ("05-05-2020", 955),
        ("06-06-2020", 1453),
        ("07-07-2020", 100),
        ("08-08-2020", 1135),
        ("09-09-2020", 2678),
        ("10-10-2020", 4130),
        ("11-11-2020", 140),
        ("12-12-2020", 310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("apex.html", labels=labels, values=values)

@sec.route("/tcs")
def sts1():
    data = [
        ("01-01-2020", 1980),
        ("02-02-2020", 1990),
        ("03-03-2020", 1745),
        ("04-04-2020", 1880),
        ("05-05-2020", 1955),
        ("06-06-2020", 1553),
        ("07-07-2020", 1800),
        ("08-08-2020", 1345),
        ("09-09-2020", 1878),
        ("10-10-2020", 1730),
        ("11-11-2020", 1940),
        ("12-12-2020", 1946),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("TCS.html", labels=labels, values=values)

@sec.route("/axis")
def sts2():
    data = [
        ("01-01-2020", 1980),
        ("02-02-2020", 1990),
        ("03-03-2020", 1745),
        ("04-04-2020", 1880),
        ("05-05-2020", 1955),
        ("06-06-2020", 1553),
        ("07-07-2020", 1800),
        ("08-08-2020", 1345),
        ("09-09-2020", 1878),
        ("10-10-2020", 1730),
        ("11-11-2020", 1940),
        ("12-12-2020", 1946),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("axis.html", labels=labels, values=values)

@sec.route("/bauto")
def sts3():
    data = [
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

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("bauto.html", labels=labels, values=values)

@sec.route("/tesla")
def sts4():
    data = [
        ("01-01-2020", 2097),
        ("02-02-2020", 2356),
        ("03-03-2020", 508),
        ("04-04-2020", 4096),
        ("05-05-2020", 655),
        ("06-06-2020", 3453),
        ("07-07-2020", 2100),
        ("08-08-2020", 1235),
        ("09-09-2020", 1678),
        ("10-10-2020", 130),
        ("11-11-2020", 140),
        ("12-12-2020", 1310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("tesla.html", labels=labels, values=values)

@sec.route("/bfin")
def sts5():
    data = [
        ("01-01-2020", 6097),
        ("02-02-2020", 1356),
        ("03-03-2020", 1508),
        ("04-04-2020", 7096),
        ("05-05-2020", 655),
        ("06-06-2020", 453),
        ("07-07-2020", 2100),
        ("08-08-2020", 235),
        ("09-09-2020", 1678),
        ("10-10-2020", 1130),
        ("11-11-2020", 140),
        ("12-12-2020", 1910),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("bfin.html", labels=labels, values=values)

@sec.route("/bfser")
def sts6():
    data = [
        ("01-01-2020", 2097),
        ("02-02-2020", 1356),
        ("03-03-2020", 8508),
        ("04-04-2020", 7796),
        ("05-05-2020", 1655),
        ("06-06-2020", 1453),
        ("07-07-2020", 2100),
        ("08-08-2020", 3235),
        ("09-09-2020", 1678),
        ("10-10-2020", 130),
        ("11-11-2020", 140),
        ("12-12-2020", 910),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("bfs.html", labels=labels, values=values)

@sec.route("/hcl")
def sts7():
    data = [
        ("01-01-2020", 1497),
        ("02-02-2020", 1356),
        ("03-03-2020", 1608),
        ("04-04-2020", 8296),
        ("05-05-2020", 455),
        ("06-06-2020", 1453),
        ("07-07-2020", 3100),
        ("08-08-2020", 2235),
        ("09-09-2020", 1678),
        ("10-10-2020", 1130),
        ("11-11-2020", 1240),
        ("12-12-2020", 1910),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("hcl.html", labels=labels, values=values)

@sec.route("/hdfc")
def sts8():
    data = [
        ("01-01-2020", 1597),
        ("02-02-2020", 456),
        ("03-03-2020", 1708),
        ("04-04-2020", 796),
        ("05-05-2020", 55),
        ("06-06-2020", 453),
        ("07-07-2020", 6100),
        ("08-08-2020", 8235),
        ("09-09-2020", 478),
        ("10-10-2020", 1730),
        ("11-11-2020", 1240),
        ("12-12-2020", 110),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("hdfc.html", labels=labels, values=values)

@sec.route("/apple")
def sts9():
    data = [
        ("01-01-2020", 2198),
        ("02-02-2020", 235),
        ("03-03-2020", 508),
        ("04-04-2020", 1496),
        ("05-05-2020", 3955),
        ("06-06-2020", 153),
        ("07-07-2020", 1100),
        ("08-08-2020", 135),
        ("09-09-2020", 2678),
        ("10-10-2020", 14130),
        ("11-11-2020", 140),
        ("12-12-2020", 210),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("apple.html", labels=labels, values=values)

@sec.route("/icici")
def sts10():
    data = [
        ("01-01-2020", 2198),
        ("02-02-2020", 235),
        ("03-03-2020", 508),
        ("04-04-2020", 1296),
        ("05-05-2020", 3955),
        ("06-06-2020", 153),
        ("07-07-2020", 3100),
        ("08-08-2020", 135),
        ("09-09-2020", 678),
        ("10-10-2020", 4130),
        ("11-11-2020", 2140),
        ("12-12-2020", 3210),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("icici.html", labels=labels, values=values)

@sec.route("/ind")
def sts11():
    data = [
        ("01-01-2020", 218),
        ("02-02-2020", 235),
        ("03-03-2020", 1508),
        ("04-04-2020", 796),
        ("05-05-2020", 3955),
        ("06-06-2020", 1153),
        ("07-07-2020", 3200),
        ("08-08-2020", 135),
        ("09-09-2020", 1678),
        ("10-10-2020", 4130),
        ("11-11-2020", 2140),
        ("12-12-2020", 310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("IndusInd.html", labels=labels, values=values)

@sec.route("/info")
def sts12():
    data = [
        ("01-01-2020", 6218),
        ("02-02-2020", 2235),
        ("03-03-2020", 1508),
        ("04-04-2020", 1796),
        ("05-05-2020", 355),
        ("06-06-2020", 153),
        ("07-07-2020", 3200),
        ("08-08-2020", 4135),
        ("09-09-2020", 1678),
        ("10-10-2020", 130),
        ("11-11-2020", 140),
        ("12-12-2020", 310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("info.html", labels=labels, values=values)

@sec.route("/tech")
def sts13():
    data = [
        ("01-01-2020", 441),
        ("02-02-2020", 2235),
        ("03-03-2020", 1508),
        ("04-04-2020", 796),
        ("05-05-2020", 3255),
        ("06-06-2020", 6153),
        ("07-07-2020", 300),
        ("08-08-2020", 1315),
        ("09-09-2020", 178),
        ("10-10-2020", 1130),
        ("11-11-2020", 140),
        ("12-12-2020", 9310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("tech.html", labels=labels, values=values)

@sec.route("/air")
def sts14():
    data = [
        ("01-01-2020", 441),
        ("02-02-2020", 2235),
        ("03-03-2020", 1508),
        ("04-04-2020", 796),
        ("05-05-2020", 3255),
        ("06-06-2020", 6153),
        ("07-07-2020", 300),
        ("08-08-2020", 1315),
        ("09-09-2020", 178),
        ("10-10-2020", 1130),
        ("11-11-2020", 140),
        ("12-12-2020", 9310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("airtel.html", labels=labels, values=values)

@sec.route("/dr")
def sts15():
    data = [
        ("01-01-2020", 4418),
        ("02-02-2020", 2235),
        ("03-03-2020", 1508),
        ("04-04-2020", 1796),
        ("05-05-2020", 3255),
        ("06-06-2020", 6153),
        ("07-07-2020", 3200),
        ("08-08-2020", 1315),
        ("09-09-2020", 1780),
        ("10-10-2020", 2130),
        ("11-11-2020", 1240),
        ("12-12-2020", 2310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("dr.html", labels=labels, values=values)

@sec.route("/itc")
def sts16():
    data = [
        ("01-01-2020", 6218),
        ("02-02-2020", 2235),
        ("03-03-2020", 1508),
        ("04-04-2020", 1796),
        ("05-05-2020", 3555),
        ("06-06-2020", 1543),
        ("07-07-2020", 3200),
        ("08-08-2020", 4135),
        ("09-09-2020", 1678),
        ("10-10-2020", 1380),
        ("11-11-2020", 1240),
        ("12-12-2020", 1310),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("airtel.html", labels=labels, values=values)

# @sec.route("/kag")
# def kag():
#     df = pd.read_csv('Combined_News_DJIA.csv')
#     m=[];m=df.head()
#     return render_template("kag.html")
