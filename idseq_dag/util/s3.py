import os
import threading
import subprocess
import time
def check_s3_presence(s3_path):
    ''' True if s3_path exists. False otherwise. '''
    try:
        o = subprocess.check_output("aws s3 ls %s" % s3_path, shell=True)
        if o:
            return True
    except:
        pass
    return False

def check_s3_presnce_for_file_list(s3_dir, file_list):
    for f in file_list:
        if not check_s3_presence(os.path.join(s3_dir, f)):
            return False
    return True

def touch_s3_file(s3_file_path):
    try:
        subprocess.check_call("aws s3 cp --metadata '{\"touched\":\"now\"}' %s %s" % (s3_file_path, s3_file_path), shell=True)
        return True
    except:
        return False

def touch_s3_file_list(s3_dir, file_list):
    for f in file_list:
        touch_s3_file(os.path.join(s3_dir, f))
