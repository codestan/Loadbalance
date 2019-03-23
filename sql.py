import pymysql
pymysql.install_as_MySQLdb()

# import MySQLdb
def RunCom(sqlcommand):
    db = Connect()
    cursor = db.cursor()
    try:
        cursor.execute(sqlcommand)
        results = cursor.fetchall()
        return results

    except:
        print ("Error: unable to fecth data %s" % (sqlcommand))
        # disconnect from server
    db.close()
    return
def Connect():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password=None,
                         db='loadbalance_database' )
    return db
