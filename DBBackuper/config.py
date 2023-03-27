from environs import Env
import os

#                 Basic Settings File
# 
# This code extracts all necessary data from the environment
# and creates basic global settings files

env = Env() 
env.read_env()

# Recording data from environment variables

IP = env.str("ip") # IP Database

# Dir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_dir = f'{BASE_DIR}/DBBackuper'


if __name__ == '__main__':
    print()