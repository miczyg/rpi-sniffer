import os
import constants
import aws_upload
import logging
import time

logger = logging.getLogger('rpi-logger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

tshark_command = "tshark -i {interface} -w {out_file} "
out_file = constants.DUMP_FOLDER + "/buffer_dump_HEADER_ONLY.pcap"

#ringbuffer for dividing files
max_one_file_size = 10*1000 #10MB = 20000 KB
num_files = 200
ring_buffer_formatter = "-b filesize:{s} -a files:{num_files}".format(s=max_one_file_size, 
                                                                    num_files=num_files) 

#timeout stop condition in seconds
timeout = 2*60*60
# timeout = 30
timeout_formatter = "-a duration:{timeout} ".format(timeout=timeout)

#stop condition on filesize in KB
max_filesize = 1*1000*2000 #set to 1G.5GB for one dump overall
filesize_formatter = "-a filesize:{max_size} ".format(max_size=max_filesize)

output_formatter = "-F pcap "

#set promiscous mode for capture
ret =  os.system(constants.PROMISCOUS_ON)
if ret == 0:
    logger.info("Promiscous ON")
    command = tshark_command.format(
        interface=constants.INTERFACE, 
        out_file=out_file)
    #capture headers inly with max size 60bytes
    command += "-s 60 "
    #save to pcap no pcap-ng
    command += output_formatter
    command += timeout_formatter
    # command += filesize_formatter
    command += ring_buffer_formatter
    # command += "-P" # print summarry when writing to file

    print command
    
    ret = os.system(command)
    logger.info("Capture completed with status: {}".format(ret))

    ret =  os.system(constants.PROMISCOUS_OFF)
    logger.info("Promiscous OFF")
else:
    logger.error("Unable to set promiscous. Exiting...")
