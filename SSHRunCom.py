import paramiko
def Stdout(APdata ,command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print (command)
    client.connect(APdata[0],'22' , APdata[1], APdata[2])
    stdin, stdout, stderr = client.exec_command(command)
    results = stdout.readlines()
    client.close()
    return results
def MultiStdout(APdata ,command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(APdata[0],'22' , APdata[1], APdata[2])
    results = []
    for com in command:
        stdin, stdout, stderr = client.exec_command(com)
        results.append(stdout.readlines())
    client.close()
    return results

def removeMAC(APdata,MACtarget):
    port=22
    t = paramiko.Transport(APdata[0],port)
    t.connect(username=APdata[1], password=APdata[2])
    sftp = paramiko.SFTPClient.from_transport(t)
    lines = readFile(sftp)
    if checkMAC(lines,MACtarget) == True:
        helpRemoveMAC(sftp,lines,MACtarget)
        Stdout(APdata,'wifi')
    t.close()

def resetMAC(APdata):
    port=22
    x = "maclist"
    i=0
    t = paramiko.Transport(APdata[0],port)
    t.connect(username=APdata[1], password=APdata[2])
    sftp = paramiko.SFTPClient.from_transport(t)
    lines = readFile(sftp)
    f = sftp.open("/etc/config/wireless", "w")
    for line in lines:
        if not x in line:
            f.write(line)
        else :
            i+=1
    f.close()
    if i >0:
        Stdout(APdata,'wifi')
    t.close()

def Transports(APdata,MACtarget):
    port=22
    t = paramiko.Transport(APdata[0],port)
    t.connect(username=APdata[1], password=APdata[2])
    sftp = paramiko.SFTPClient.from_transport(t)
    lines = readFile(sftp)
    lines = lines[:(len(lines))]
    if checkOption(lines) == True:
        if checkMAC(lines,MACtarget) == False:
            addMAC(sftp,lines,MACtarget)
            Stdout(APdata,'wifi')
    else:
        lines=addOption(lines)
        addMAC(sftp,lines,MACtarget)
        Stdout(APdata,'wifi')
    sftp.close()
    t.close()
def helpRemoveMAC(sftp,lines,MACtarget):
    f = sftp.open("/etc/config/wireless", "w")
    #print "helpRemoveMAC"
    for MAC in MACtarget :
        for line in lines:
            if not MAC in line:
                f.write(line)

    f.close()
def addMAC(sftp,lines,MACtarget):
    #print "addMAC"
    f = sftp.open("/etc/config/wireless", "w")
    for line in lines:
        f.write(line)
    for MAC in MACtarget :
        #print MAC
        f.write("\n\tlist maclist '%s'\n"%MAC)
    #f.write("\n")
    f.close()

def checkMAC(lines,MACtarget):
    #print "checkMAC"
    for MAC in MACtarget:
        for line in lines:
            if MAC in line:
                #print "True"
                return True
    #print "False"
    return False

def checkOption(lines):
    #print "checkOption"
    for line in lines:
        if "option macfilter" in line:
            return True
    return False
        #option macfilter 'deny'
def addOption(lines):
    lines.append("\toption macfilter \'deny\'\n")
    return lines
def readFile(sftp):
    f = sftp.open("/etc/config/wireless", "r")
    lines = f.readlines()
    f.close()
    return lines
