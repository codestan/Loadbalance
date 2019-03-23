import get ,SSHRunCom
import threading

def start(trigger):
    destination=trigger[0]
    MACtarget=trigger[1]
    transfer(destination,MACtarget)

def transfer(destination,MACtarget):
    APdatas = transferHelp(destination,MACtarget)
    addMAC(APdatas,MACtarget)

def transferHelp(destination,MACtarget):
    APdatas = get.APdatas()
    APdatasNotdestination = []
    for data in APdatas:
        print (data)
        if not destination in data:
            APdatasNotdestination.append(data)
        else:
            SSHRunCom.removeMAC(data,MACtarget)
    return APdatasNotdestination

def addMAC(APdatas,MACtarget):
    threads = []
    for AP in APdatas:
        t = threading.Thread(target=SSHRunCom.Transports, args=(AP,MACtarget,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def reset():
    threads = []
    APdatas = get.APdatas()
    for APdata in APdatas:
        t = threading.Thread(target=SSHRunCom.resetMAC, args=(APdata,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
