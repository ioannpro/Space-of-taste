from environs import Env

#
#
#

env = Env() 
env.read_env()

IP = env.str("ip") # IP Database


if __name__ == '__main__':
    print(IP)