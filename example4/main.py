import logging



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# def custom_filter(event: logging.LogRecord):
#   # event.msg = event.getMessage() + " foo"
#   return event.levelname == 'INFO' && 'another' in event.msg 


# logger.addFilter(custom_filter)

logger.setLevel(logging.DEBUG)


def main():
  logger.debug('This is a debug message')
  logger.info('This is an info message')
  logger.info('This is another info message')
  logger.warning('This is a warning message')
  logger.error('This is an error message')
  logger.critical('This is a critical message')


print("logger.getEffectiveLevel(): " + str(logger.getEffectiveLevel()))
print("logging.getLevelName(logger.getEffectiveLevel()): " + logging.getLevelName(logger.getEffectiveLevel()))


# https://docs.python.org/3/library/logging.html#logging-levels
# https://docs.python.org/3/library/logging.html#logrecord-attributes





if __name__ == '__main__':
  main()
