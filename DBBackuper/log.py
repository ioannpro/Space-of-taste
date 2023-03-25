from config import log_dir
import logging 


# Setup

name = 'DBBackuper'
logging.basicConfig(level=logging.INFO )

# Create Handler

terminal = logging.StreamHandler()
debug_handler = logging.FileHandler(filename=f'{log_dir}/debug.log', mode='w')
warning_handler = logging.FileHandler(filename=f'{log_dir}/warning.log', mode='w')
error_handler = logging.FileHandler(filename=f'{log_dir}/error.log', mode='w')
format = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')

# Set Format to Handler

terminal.setFormatter(format)
debug_handler.setFormatter(format)
warning_handler.setFormatter(format)
error_handler.setFormatter(format)

# Create Logging Object

logger = logging.getLogger(name)


logger.addHandler(terminal)




logger.warning('Protocol problem: %s', 'connection reset')

def main():
    
    logger.info('Started')
    logger.info('Finished')

if __name__ == '__main__':
    main()