import logging
import requests

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

requests_logger = logging.getLogger("requests.packages.urllib3")
requests_logger.setLevel(logging.DEBUG)



requests.get('https://google.com')