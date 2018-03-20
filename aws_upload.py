import os
import datetime
import logging

bucket_name = "rpi-sniffer-dumps"

def move_dumps(dumps_dir):
    remote_dir = "dumps/"
    remote_dir += datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    command = "aws s3 --region eu-central-1 mv {local_dir} s3://{bucket}/{folder_name} --recursive --debug".format(
        local_dir=dumps_dir,
        bucket = bucket_name, 
        folder_name=remote_dir)
    print command
    return os.system(command)

def move_logs(logs_dir):
    remote_folder = "logs/"
    remote_folder += datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    command = "aws s3 --region eu-central-1 mv {local_dir} s3://{bucket}/{folder_name} --recursive".format(
        local_dir=logs_dir,
        bucket = bucket_name, 
        folder_name=remote_folder)
    print command
    return os.system(command)
        


