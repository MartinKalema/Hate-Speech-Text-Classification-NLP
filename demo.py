from hateSpeechClassifier.logger import logging
from hateSpeechClassifier.exception import CustomException
import sys as system

# logging.info("Testing Logger")

try:
    a = 7 / "0"
except Exception as e:
    raise CustomException(e, system) from e
