import logging
import os

from dotenv import load_dotenv
from jsonschema import validate

from exceptions.exception_validation_error import ValidationError


class Helper():

    def validateJson(request, schema):
        try:
            validate(instance=request, schema=schema)
        except Exception as error:
            raise ValidationError(error)
        return request

    def Log(message):
        logger = logging.getLogger('app')
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler('app.log')
        fh.setLevel(logging.INFO)
        logger.addHandler(fh)
        logger.debug(message)

    def loadEnv():
        load_dotenv(".env")
        config = {
            'JWT_SECRET': os.environ.get("JWT_SECRET"),
            'JWT_ALGORITHM': os.environ.get("JWT_ALGORITHM"),
            'JWT_EXP_DELTA_SECONDS': os.environ.get("JWT_EXP_DELTA_SECONDS"),
            'ENVIRONMENT': os.environ.get("ENVIRONMENT"),
            'MAIL_SERVER': os.environ.get('MAIL_SERVER'),
            'MAIL_PORT': os.environ.get('MAIL_PORT'),
            'MAIL_USE_TLS': os.environ.get('MAIL_USE_TLS'),
            'MAIL_USE_SSL': os.environ.get('MAIL_USE_SSL'),
            'MAIL_USERNAME': os.environ.get('MAIL_USERNAME'),
            'MAIL_PASSWORD': os.environ.get('MAIL_PASSWORD'),
            'URL_BASE':os.environ.get('URL_BASE'),
            'URL_FRONT_ADMIN':os.environ.get('URL_FRONT_ADMIN'),
            'URL_FRONT_DOCTOR':os.environ.get('URL_FRONT_DOCTOR'),
        }
        return config
