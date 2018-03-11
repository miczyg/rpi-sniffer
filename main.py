import pyshark
import os

# any OS calls on ifconfig must be with sudo
INTERFACE = "eth0"
PROMISCOUS_ON = "ifconfig {interface} promisc".format(interface=INTERFACE)
PROMISCOUS_OFF = "ifconfig {interface} -promisc".format(interface=INTERFACE)

capture = pyshark.LiveCapture(interface=INTERFACE)
capture.sniff(timeout=50)

print len(capture)
print capture[0]

# remeber always at the end
ret =  os.system(PROMISCOUS_OFF)
print ret