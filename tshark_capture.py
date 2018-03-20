import os
import constants
import aws_upload

tshark_command = "tshark -i {interface} -w {out_file} "
out_file = constants.DUMP_FOLDER + "/buffer_dump.pcap"

#ringbuffer for dividing files
max_one_file_size = 40*1000 #40MB = 20000 KB
num_files = 50
ring_buffer_formatter = "-b filesize:{s} -a files:{num_files}".format(s=max_one_file_size, 
                                                                    num_files=num_files) 

#timeout stop condition in seconds
timeout = 2*60*60
# timeout = 30
timeout_formatter = "-a duration:{timeout} ".format(timeout=timeout)

#stop condition on filesize in KB
max_filesize = 1*1000*1000 #set to 1GB for one dump overall
filesize_formatter = "-a filesize:{max_size} ".format(max_size=max_filesize)

output_formatter = "-F pcap "

#set promiscous mode for capture
ret =  os.system(constants.PROMISCOUS_ON)
print ret
if ret == 0:
    print "Promiscous ON"
    command = tshark_command.format(
        interface=constants.INTERFACE, 
        out_file=out_file)

    #save to pcap no pcap-ng
    command += output_formatter
    command += timeout_formatter
    # command += filesize_formatter
    command += ring_buffer_formatter
    # command += "-P" # print summarry when writing to file

    print command
    
    ret = os.system(command)
    print ret

    ret =  os.system(constants.PROMISCOUS_OFF)
    print ret
    print "Promiscous OFF"
else:
    print "Unable to set promiscous. Existing..."

# aws move files
print aws_upload.move_dumps(constants.DUMP_FOLDER)
print aws_upload.move_logs(constants.LOG_FOLDER)


    