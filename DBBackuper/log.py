from config import log_dir
import logging 


# Setup

FORMAT = '[%(asctime)s] %(name)s %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

# Create Handler

debug_handler = logging.FileHandler(filename=f'{log_dir}/debug.log', mode='a')
warning_handler = logging.FileHandler(filename=f'{log_dir}/warning.log', mode='a')
error_handler = logging.FileHandler(filename=f'{log_dir}/error.log', mode='a')

# Creater Formatter

formatter_a = logging.Formatter(FORMAT)

# Create Filter

class DebugFilter(logging.Filter):
    def filter(self, record):
        if record.levelname == "DEBUG":
            return True
        
class WarningFilter(logging.Filter):
    def filter(self, record):
        if record.levelname == "WARNING":
            return True
        
class ErrorFilter(logging.Filter):
    def filter(self, record):
        if record.levelname == "ERROR":
            return True
    
# Set Formatter

debug_handler.setFormatter(formatter_a)
warning_handler.setFormatter(formatter_a)
error_handler.setFormatter(formatter_a)

# Add Filter

debug_handler.addFilter(DebugFilter())
warning_handler.addFilter(WarningFilter())
error_handler.addFilter(ErrorFilter())

# Create Logging Object

logger = logging.getLogger(__name__)

# Add Handler

logger.addHandler(debug_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)




def main():
    logger.debug('BuuuuuuuuuG')
    logger.warning('Protocol problem: %s', 'connection reset')

    logger.info('Started')
    logger.info('Finished')

if __name__ == '__main__':
    main()