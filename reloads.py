#!/usr/bin/env python
import sys, os, subprocess, get, log
import paramiko, SSHRunCom, sql

def updateUser(APdata):
    #ap_numclientUpdate
    updateAPdata = get.updateAPdata(APdata)
    ap_model = updateAPdata[0]
    ap_hostname = updateAPdata[1]
    ap_ssid = updateAPdata[2]
    ap_channel = updateAPdata[3]
    userDatas = updateAPdata[4]

    db = sql.Connect()
    cursor = db.cursor()
    sqlCom = "UPDATE accesspoint_ip SET ap_numclient = '%s', ap_model = '%s', ap_hostname = '%s', ap_ssid = '%s', ap_channel = '%s', ap_status = 'Online', ap_authen = 'Success' WHERE ap_ip = '%s'" % (len(userDatas),Model,Hostname,channel,ssid, APdata[0])
    try:
        cursor.execute(sqlCom)
        db.commit()
    except:
        db.rollback()

    sqlCom = "DELETE FROM client_data WHERE client_ip = '%s' " % (APdata[0])
    try:
        cursor.execute(sqlCom)
        db.commit()
    except:
        db.rollback()
    db.close()

    #for user in userDatas :
    i=0
    userData = []
    log.client(APdata,userDatas)
    for user in userDatas :
        #log.client(APdata,user)
        userData.append([])
        userData[i].append(APdata[0])
        userData[i].append(user[0])
        userData[i].append(user[1])
        userData[i].append(user[2])
        userData[i].append(user[3])
        userData[i].append(user[4])
        i+=1
    sqlCom = "INSERT INTO client_data (APip, Station, inactive_time, rx_bytes, tx_bytes, signal_avg) VALUES (%s, %s, %s, %s, %s, %s) "
        #% (APdata[0],user[0],user[1],user[2],user[3],user[4])
    db = sql.Connect()
    cursor = db.cursor()
    try:
        cursor.executemany(sqlCom, userData)
        db.commit()
    except:
        db.rollback()
    db.close()

def refreshInformation(APdata):
    StatusOF = get.check_ping(APdata[0])
    if StatusOF != False:
        StatusAT = get.testAuthen(APdata)
        if StatusAT != False:
            updateUser(APdata)
        else :
            OFFline(APdata,1)
    else :
        OFFline(APdata,0)

def OFFline(APdata,stat):
    db = sql.Connect()
    cursor = db.cursor()
    if stat == 0:
        sqlCom = "UPDATE accesspoint_ip SET ap_numclient = '00', ap_model = 'NA', ap_hostname = 'NA', ap_ssid = 'NA', ap_channel = '00', ap_status = 'Offline', ap_authen = 'NA' WHERE ap_ip = '%s'" % (APdata[0])
    else :
        sqlCom = "UPDATE accesspoint_ip SET ap_numclient = '00', ap_model = 'NA', ap_hostname = 'NA', ap_ssid = 'NA', ap_channel = '00', ap_status = 'Online', ap_authen = 'Failed' WHERE ap_ip = '%s'" % (APdata[0])
    try:
        cursor.execute(sqlCom)
        db.commit()
    except:
        db.rollback()

    sqlCom = "DELETE FROM client_data WHERE client_ip = '%s' " % (APdata[0])
    try:
        cursor.execute(sqlCom)
        db.commit()
    except:
        db.rollback()
    db.close()
