import os
import constants

tshark_command = "tshark -i {interface} -w {out_file} "
out_file = "test1.pcap"

#timeout stop condition in seconds
timeout = 30
timeout_formatter = "-a duration:{timeout} ".format(timeout=timeout)

#stop condition on filesize in KB
max_filesize = 20000
filesize_formatter = "-a filesize:{max_size} ".format(max_size=max_filesize)

output_formatter = "-F pcap "

#set promiscous mode for capture
ret =  os.system(constants.PROMISCOUS_ON)
print ret
if ret == 0:
    command = tshark_command.format(
        interface=constants.INTERFACE, 
        out_file=out_file)

    #save to pcap no pcap-ng
    command += output_formatter
    command += timeout_formatter
    command += "-P" # print summarry when writing to file

    print command
    # ret = os.system(command)
    ret =  os.system(constants.PROMISCOUS_OFF)
    print ret
    
    