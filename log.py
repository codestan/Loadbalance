import sys, os, subprocess, get
import socket, struct
import datetime
hours = "hours = 1"
weekday = 7

def client(APdata,users):
    header = []
    now = datetime.datetime.now()
    header.append(now.strftime("%d-%m-%Y-%H-%M"))
    header.append(get.Group(APdata[0]))
    header.append(APdata[0])
    #for u in user :
    #    db.append(u)

    sevendays(header,users)
    onehour(header,users)
#/var/www/html/loadbalance/loadbalance/text/ap_log_7d.txt
def sevendays(header,users):
    fileR = open("/var/www/html/loadbalance/text/ap_log_7d.txt","r")
    lines = fileR.readlines()
    fileR.close()
    now = datetime.datetime.now()
    sevenday = now - datetime.timedelta(days = 1)
    sevenday = sevenday.strftime('%d-%m-%Y')
    fileW = open("/var/www/html/loadbalance/text/ap_log_7d.txt","w")
    print (sevenday)
    for line in lines:
        if not sevenday in line:
            fileW.write(line)
    fileW.close()
    file = open("/var/www/html/loadbalance/text/ap_log_7d.txt","a")
    for user in users:
        for h in header:
            file.write(h)
            file.write("|")
        for u in user:
            file.write(u)
            file.write("|")
        file.write("\n")
    file.close()

def onehour(header,users):
    fileR = open("/var/www/html/loadbalance/text/ap_log_1hr.txt","r")
    lines = fileR.readlines()
    fileR.close()
    now = datetime.datetime.now()
    hour = now - datetime.timedelta(hours = 1)
    hour = hour.strftime('%H-%M')
    print (hour)

    fileW = open("/var/www/html/loadbalance/text/ap_log_1hr.txt","w")
    for line in lines:
        if not hour in line:
            fileW.write(line)
    fileW.close()

    file = open("/var/www/html/loadbalance/text/ap_log_1hr.txt","a")
    for user in users:
        for h in header:
            file.write(h)
            file.write("|")
        for u in user:
            file.write(u)
            file.write("|")
        file.write("\n")
    file.close()
