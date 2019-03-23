#                            -
#                         _ooOoo_
#                        o8888888o
#                        88" . "88
#                        (| -_- |)
#                        O\  =  /O
#                     ____/'---'\____
#                   .'  \\|     |//  '.
#                  /  \\|||  :  |||//  \
#                 /  _||||| -:- |||||_  \
#                 |   | \\\  -  /'| |   |
#                 | \_|  '\'---'//  |_/ |
#                 \  .-\__ '-. -'__/-.  /
#               ___'. .'  /--.--\  '. .'___
#            ."" '<  '.___\_<|>_/___.' _> \"".
#           | | :  '- \'. ;'. _/; .'/ /  .' ; |
#           \  \ '-.   \_\_'. _.'_/_/  -' _.' /
#============'-.'___'-.__\ \___  /__.-'_.'_.-'============
#                         '=--=-'
import sys, os, string, threading
import Sort, sql, analysis, get, transfer,SSHRunCom , reloads
from random import randint

#outlock = threading.Lock()

def refresh(APdatas):
    threads = []
    for AP in APdatas:
        t = threading.Thread(target=reloads.refreshInformation, args=(AP,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def main():
    print("main...")
    Groups = get.Groups()
    #print Groups
    for Group in Groups:
        APdatas = get.APdataStart(Group)
        refresh(APdatas)
        trigger=analysis.start()
        if trigger != 0 :
            transfer.start(trigger)
        else:
            transfer.reset()



main()
