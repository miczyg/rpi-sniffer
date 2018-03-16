INTERFACE = "eth0"
PROMISCOUS_ON = "sudo ifconfig {interface} promisc".format(interface=INTERFACE)
PROMISCOUS_OFF = "sudo ifconfig {interface} -promisc".format(interface=INTERFACE)

DUMP_FOLDER = "/home/pi/shared/rpi-sniffer/dumps"
LOG_FOLDER = "/home/pi/shared/logs"