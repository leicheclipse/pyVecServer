import yaml 
import logging 
import logging.config
import os 
import sys


def init_logging(conf='conf/logger.yaml', level=logging.INFO):
    if not os.path.exists(conf):
        print('logging conf not exists')
        sys.exit(1)
    with open(conf, 'r') as f:
        config = yaml.load(f)
        logging.config.dictConfig(config)


def test():
    logging.info("test info")
    logging.warning("test warning")
    logging.error("test error")


if __name__ == '__main__':
    init_logging()
    test()
