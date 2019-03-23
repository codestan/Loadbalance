import sql, SSHRunCom
import sys, os, subprocess
import paramiko
def server_different():
    sqlCom = "SELECT server_different FROM server_data"
    db = sql.RunCom(sqlCom)
    #print db
    return int(db[0][0])
def server_presetlevel():
    sqlCom = "SELECT server_presetlevel FROM server_data"
    db = sql.RunCom(sqlCom)
    #print db
    return int(db[0][0])
def server_inactivetime():
    sqlCom = "SELECT server_inactivetime FROM server_data"
    db = sql.RunCom(sqlCom)
    #print db
    return int(db[0][0])
def Users(APdata):
    i=0
    dataU = SSHRunCom.Stdout(APdata,'iw dev wlan0 station dump')
    userDatas = []
    for line in dataU:
        if "Station" in line:
            userDatas.append([])
            userDatas[i].append(line[8:25])
        if "inactive time" in line:
            userDatas[i].append(line[16:-4])
        if "rx bytes" in line:
            userDatas[i].append(line[11:-1])
        if "tx bytes" in line:
            userDatas[i].append(line[11:-1])
        if "signal avg" in line:
            userDatas[i].append(line[13:16])

            i+=1
    return userDatas
def APdataStart(Group):
    sqlCom = "SELECT ap_ip,ap_username,ap_password FROM accesspoint_ip WHERE ap_group = '%s'" %(Group)
    db = sql.RunCom(sqlCom)
    #print db
    return db
def APdatas():
    sqlCom = "SELECT ap_ip,ap_username,ap_password FROM accesspoint_ip "
    db = sql.RunCom(sqlCom)
    #print db
    return db
def Groups():
    sqlCom = "SELECT ap_group FROM accesspoint_ip"
    db = sql.RunCom(sqlCom)
    return db
def Group(ip):
    sqlCom = "SELECT ap_group FROM accesspoint_ip WHERE ap_ip = '%s'" %(ip)
    db = sql.RunCom(sqlCom)
    db = db[0]
    db = db[0]
    return db
def APdata(ip):
    sqlCom = "SELECT ap_ip,ap_username,ap_password FROM accesspoint_ip WHERE ap_ip = '%s'" % (ip)
    db = sql.RunCom(sqlCom)
    return db
def UserNumber():
    i=0
    sqlCom = "SELECT ap_numclient,ap_ip FROM accesspoint_ip"
    db = sql.RunCom(sqlCom)
    dbUserNumber=[]
    for x in db :
        dbUserNumber.append([])
        dbUserNumber[i].append(x[0])
        dbUserNumber[i].append(x[1])
        i+=1
    return dbUserNumber

def check_ping(hostname):
    print('check_ping')
    print(hostname)
    try:
        output = subprocess.check_output("ping -c 1 "+hostname, shell=True)
    except:
        return False
    
    return True

def testAuthen(APdata):
    print('testAuthen')
    print(APdata)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn = client.connect(APdata[0],'22' , APdata[1], APdata[2])
        print(conn)
    except:
        client.close()
        print("False")
        return False
    if conn is None:
        client.close()
        print("true")
        return True

def Model(APdata):
    data = SSHRunCom.Stdout(APdata,'cat /proc/cpuinfo')
    Data =''
    for line in data:
        if "machine" in line:
            Data=line[12:-1]
    return Data

def Hostname(APdata):
    data = SSHRunCom.Stdout(APdata,'cat /etc/config/system')
    Data =''
    for line in data:
        if "hostname" in line:
            Data=line[18:-2]
    return Data

def wifiIface(APdata):
    data = SSHRunCom.Stdout(APdata,'cat /etc/config/wireless')
    Data =[]
    i=0
    for line in data:
        if "ssid" in line:
            Data.append(line[14:-2])
        if "channel" in line:
            Data.append(line[17:-2])
    return Data

def updateAPdata(APdata):
    Multicommand=[]
    userDatas = []

    i=0
    Multicommand.append('iw dev wlan0 station dump')
    Multicommand.append('cat /proc/cpuinfo')
    Multicommand.append('cat /etc/config/system')
    Multicommand.append('cat /etc/config/wireless')

    Data = SSHRunCom.MultiStdout(APdata,Multicommand)
    APdata = []
    for line in Data[1]:
        if "machine" in line:
            data=line[12:-1]
            APdata.append(data)

    for line in Data[2]:
        if "hostname" in line:
            data=line[18:-2]
            APdata.append(data)

    for line in Data[3]:
        if "ssid" in line:
            data=(line[14:-2])
            APdata.append(data)
        if "channel" in line:
            data=(line[17:-2])
            APdata.append(data)

    for line in Data[0]:
        if "Station" in line:
            userDatas.append([])
            userDatas[i].append(line[8:25])
        if "inactive time" in line:
            userDatas[i].append(line[16:-4])
        if "rx bytes" in line:
            userDatas[i].append(line[11:-1])
        if "tx bytes" in line:
            userDatas[i].append(line[11:-1])
        if "signal avg" in line:
            userDatas[i].append(line[13:16])
            i+=1

    APdata.append(userDatas)
    return APdata

def ipadmin():
    filename = "/etc/dhcpcd.conf"
    file = open(filename, "r")
    for line in file:
        print (line)
