import sql, get, Sort
#user[0] mac
#user[1] inactive time
#user[2] signalAvg
#user[3] ?
def start():
    #return analysis()
    presetlevel = get.server_presetlevel()
    completeSendBack=[]
    dbUserNumber = get.UserNumber()
    maxuser = max(dbUserNumber)
    minuser = min(dbUserNumber)
    differ = (int(maxuser[0])-int(minuser[0]))
    if check(presetlevel,differ,int(maxuser[0])) == True:
        targetUser = analysis(maxuser,(differ/2))
        completeSendBack.append(minuser[1])
        completeSendBack.append(targetUser)
        return completeSendBack
    else :
        return 0
def check(presetlevel,differ,maxuser):
    different = get.server_different()
    if (differ >= different) and (maxuser > presetlevel) :
        return True
    else :
        return False

def analysis(maxuser,Target):
    #print "target is %d"%Target
    APdataMAX = get.APdata(maxuser[1])
    #APdataMIN = get.APdata(minuser[1])
    UserDatas=get.Users(APdataMAX[0])
    userToMIN = helpAnalysis(UserDatas,Target)
    i=0
    MACtarget=[]
    while i < len(userToMIN):
        MACtarget.append(userToMIN[i][0])
        i+=1
    return MACtarget
def helpAnalysis(UserDatas,Target):
    UserDatasTemp=findInactiveUser(UserDatas,Target)
    if len(UserDatasTemp) == Target :
        return UserDatasTemp
    if len(UserDatasTemp) > Target : # Over User
        UserDatasTemp=findSignalMAXUser(UserDatasTemp,Target)
    else : # none User
        UserDatasTemp=findSignalMAXUser(UserDatas,Target)
    if len(UserDatasTemp) > Target :
        UserDatasTemp=findTxPlusTp(UserDatasTemp,Target)
        #print '3helpAnalysis'
        return UserDatasTemp
    else :
        #print '2helpAnalysis'
        return UserDatasTemp
def findInactiveUser(UserDatas,Target):
    inactiveTime=get.inactiveTime()
    UserInactive=findInactive(UserDatas,inactiveTime)
    while len(UserInactive)<Target:
        inactiveTime=inactiveTime-500
        if inactiveTime < 15000:
            return UserDatas
        UserInactive=findInactive(UserDatas,inactiveTime)
    return UserInactive
def findInactive(UserDatas,inactiveTime):
    UserInactive = []
    for user in UserDatas:
        if inactiveTime < int(user[1]):
            UserInactive.append(user)
    return UserInactive

def findSignalMAXUser(UserDatas,Target):
    signalMAX=findSignalMAX(UserDatas)
    i=len(signalMAX)
    i-=1
    j=0
    temp = signalMAX[i]
    for Smax in signalMAX :
        if Smax == temp:
            j+=1
    #j=len(SignalMAXUser)
    SignalMAXUser = []
    temp = []
    for user in UserDatas :
        if str(signalMAX[i]) == str(user[4]):
            temp.append(user)
            i-=1
    i=0
    while len(SignalMAXUser) < j :
        SignalMAXUser.append(temp[i])
        i+=1

    return SignalMAXUser

def findSignalMAX(UserDatas):
    signalMAX = []
    for user in UserDatas:
        signalMAX.append(int(user[4]))
    Sort.quickSort(signalMAX)
    return signalMAX

def findTxPlusTp(UserDatas,Target):
    TxPlusTp = 9223372036854775807
    lastSelectUser=[]
    tempUser = []
    #print UserDatas
    while len(lastSelectUser) < Target :
        for user in UserDatas:
            if TxPlusTp > (int(user[2])+int(user[3])):
                TxPlusTp = (int(user[2])+int(user[3]))
                temp = user
        if len(lastSelectUser) < Target :
            lastSelectUser.append(temp)
            for user in UserDatas:
                if temp[0] != user[0]:
                    tempUser.append(user)
        UserDatas=tempUser
    return lastSelectUser
