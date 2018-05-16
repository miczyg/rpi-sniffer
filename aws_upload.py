import os, os.path
import datetime
import logging
import time
import constants

bucket_name = "rpi-sniffer-dumps"



def move_dumps(dumps_dir, logger):
    remote_dir = "dumps/"
    remote_dir += datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    command = "aws s3 --region eu-central-1 mv {local_dir} s3://{bucket}/{folder_name} --recursive".format(
        local_dir=dumps_dir,
        bucket = bucket_name,
        folder_name=remote_dir)
    print command
    files_to_upload = len([name for name in os.listdir(dumps_dir) if os.path.isfile(os.path.join(dumps_dir, name))])
    timeout = time.time() + 60*60*4 # 4h max for sending files
    while time.time() < timeout:
    	os.system(command)
	files_to_upload = len([name for name in os.listdir(dumps_dir) if os.path.isfile(os.path.join(dumps_dir, name))])
	if files_to_upload <= 0:
	    logger.info("All files uploaded :)") 
	    break
        logger.info("Remaining {} files to upload. Retrying...".format(files_to_upload))

def move_logs(logs_dir):
    remote_folder = "logs/"
    remote_folder += datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    command = "aws s3 --region eu-central-1 mv {local_dir} s3://{bucket}/{folder_name} --recursive".format(
        local_dir=logs_dir,
        bucket = bucket_name, 
        folder_name=remote_folder)
    print command
    return os.system(command)
        

if __name__=="__main__":
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
    logger.info("Starting AWS upload...")
    
    # aws move files
    start = time.time()
    move_dumps(constants.DUMP_FOLDER, logger)
    end = time.time()
    logger.info("Upload ended in {} seconds".format(end - start))
    logger.info("Uploading logs...")
    print move_logs(constants.LOG_FOLDER)
    logger.info("Logs uploaded. Exiting.")
