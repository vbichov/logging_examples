import logging


logger = logging.getLogger(__name__)


def run():
  logger.info(f"this is an info message from {__name__}")
  logger.warning(f"this is an info message from {__name__}")