import logging

logging.basicConfig(level=logging.DEBUG)
# logging.addLevelName(45, "ALMOST_CRITICAL")

def main():
  logging.debug('This is a debug message')
  logging.info('This is an info message')
  logging.warning('This is a warning message')
  logging.error('This is an error message')
  logging.critical('This is a critical message')
  
  # logging.log(45, "someththig almost critical happened")


# https://docs.python.org/3/library/logging.html#logging.basicConfig


# write to file with the following format:
# t=<time> || line=<lineNo> || func=<function name> || lvl=<log level> || msg=<message>




# https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://docs.python.org/3/library/logging.html#logging-levels



if __name__ == '__main__':
  main()















# 't=%(created)f || line=%(lineno)d || func=%(funcName)s || lvl=%(levelname)s || msg=%(message)s'