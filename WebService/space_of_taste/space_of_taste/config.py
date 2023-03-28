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
PORT = env.int("port")
DB_NAME = env.str("db_name")
DB_USER = env.str("db_user")
DB_PASSWORD = env.str("db_password")



if __name__ == '__main__':
    print(IP)