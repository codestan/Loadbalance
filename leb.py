#static ip_address=192.168.1.21/24
#static routers=192.168.1.1
#static domain_name_servers=8.8.8.8
import sys, os, subprocess, get
import fcntl, socket, struct
#https://danielmiessler.com/study/set_ip/
def getMAC(ifname):
    s = socket.socket(socket.AF_IET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

def format_ip(addr):
    return str(ord(addr[0])) + '.' + \
           str(ord(addr[1])) + '.' + \
           str(ord(addr[2])) + '.' + \
           str(ord(addr[3]))

gw = '192.168.1.1'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw, 0))
ipaddr = s.getsockname()[0]
gateway = gw
host = socket.gethostname()
print ("IP:", ipaddr, " GW:", gateway, " Host:", host)
f = os.popen('cat /etc/resolv.conf ')
#f = os.popen('ifconfig eth0')
your_ip=f.read()
print your_ip
print getMAC('eth0')

print "get.ipadmin"
