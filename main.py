from utils import init_csv
import logger
import time 
from sensor import get_temp

path = init_csv()

if __name__ == "__main__":
    for _ in range(10):
        logger.log(get_temp(), path)
        time.sleep(1)
    # logger.show_log(path)
