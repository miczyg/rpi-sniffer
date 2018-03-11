INTERFACE = "eth0"
PROMISCOUS_ON = "ifconfig {interface} promisc".format(interface=INTERFACE)
PROMISCOUS_OFF = "ifconfig {interface} -promisc".format(interface=INTERFACE)
