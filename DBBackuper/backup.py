from config import * 
from log import logger

import os
import datetime


def dump_database(CONTAINER_NAME, DB_HOSTNAME, DB_USER, DB_NAME):

    filename = f'/temp/DB_{DB_NAME}_dump_{datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'

    logger.info(f'Start dump {DB_NAME}')
    dump_status = os.WEXITSTATUS(os.system(f'docker exec -it {CONTAINER_NAME} pg_dump -h {DB_HOSTNAME} -U {DB_USER} {DB_NAME} | gzip -c --best | '))

    if dump_status != 0:
        logger.error('er')

    elif dump_status == 0:
        logger.info(f'Finish dump {DB_NAME}')
        return 


def p():
    pass
        


if __name__ == "__main__":
    

    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
