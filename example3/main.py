import logging



# logging.basicConfig()
logger = logging.getLogger()

# formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# logger.addHandler(handler)


# file_formatter = logging.Formatter('t=%(created)f || line=%(lineno)d || func=%(funcName)s || lvl=%(levelname)s || msg=%(message)s')
# file_handler = logging.FileHandler("my_app.log")
# file_handler.setLevel(logging.WARNING)
# file_handler.setFormatter(file_formatter)

# logger.addHandler(file_handler)



def main():
  logger.debug('This is a debug message')
  logger.info('This is an info message')
  logger.warning('This is a warning message')
  logger.error('This is an error message')
  logger.critical('This is a critical message')


# print("logger.getEffectiveLevel(): " + str(logger.getEffectiveLevel()))
# print("logging.getLevelName(logger.getEffectiveLevel()): " + logging.getLevelName(logger.getEffectiveLevel()))



# https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://docs.python.org/3/library/logging.html#logging-levels




if __name__ == '__main__':
  main()
