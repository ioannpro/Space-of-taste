from config import * 
from log import logger

import os
import datetime


def get_desired_file(dir, location): 
    # Function for retrieving the file path. 
    # If location == 'last' his return last created file on dir
    # If location == 'first' his return first created file on dir
    
    files = os.listdir(dir)
    f_r = ['.DS_Store'] # Unused files
    time_create = [] 

    for i in f_r:
        try:
            files.remove(i)
        except:
            continue

    files = [os.path.join(dir, file) for file in files]
    files = [file for file in files if os.path.isfile(file)]

    for i in files:
        time_create.append(os.path.getctime(i))

    if len(files) != 0:
        if location == 'last':
            i = time_create.index(max(time_create))
            return files[i]
        elif location == 'first':
            i = time_create.index(min(time_create))
            return files[i]
        else:
            logger.error('Location is incorrect')
    else:
        return 0

def upload_dump(CONTAINER_NAME, DB_HOSTNAME, DB_USER, DB_NAME, file):
    pass

def start(dir):
    
    file = get_desired_file(dir, 'last')

    if file != 0:
        logger.info(f'Loading the last dump from a file: {file[file.rfind("/") + 1:]} ')
    else:
        logger.info('No files to load dump')
        logger.info('Nothing has been loaded')

    print(file)

def clear(dir):

    file = get_desired_file(dir, 'first')

    if file != 0:
        s = os.path.getsize(file)
        dtype = 'B'
        os.remove(file)
        if s >= 1024:
            s = s/1024
            dtype = 'KB'
        elif s >= 1048576:
            s = s/1048576
            dtype = 'MB'
        s = round(s, 2)
        logger.info(f'Delete file: {file} {s}{dtype}')
    else:
        logger.info('No files to deleted')
        logger.info('Nothing has been removed')

def dump_database(CONTAINER_NAME, DB_HOSTNAME, DB_USER, DB_NAME):

    filename = f'/temp/DB_{DB_NAME}_dump_{datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'

    logger.info(f'Start dump {DB_NAME}')
    dump_status = os.WEXITSTATUS(os.system(f'docker exec -it {CONTAINER_NAME} pg_dump -h {DB_HOSTNAME} -U {DB_USER} {DB_NAME} | gzip -c --best | '))

    if dump_status != 0:
        logger.error('Dump failed')
        logger.error(f'Code error: {dump_status}')
        
        

    elif dump_status == 0:
        logger.info(f'Finish dump {DB_NAME}')
        return 


def p():
    pass
        


if __name__ == "__main__":
    start('/Users/ioann/Desktop/path/')
    clear('/Users/ioann/Desktop/path/')