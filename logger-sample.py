import logging.config
import json

## logger.config
logging.config.dictConfig(json.loads(open("config/logger.conf.json", encoding='UTF-8').read()))
## get logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
##
logger.info("//-----------// start.")
logger.debug("debug print")
logger.info("//-----------// end...")
