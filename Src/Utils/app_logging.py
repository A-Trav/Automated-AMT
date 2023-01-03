"""
The Utils.app_logging module: Application logging.

Provides functionality to support logging throughout the application runtime.
"""

import logging
from logging.config import dictConfig
from functools import wraps

def prod_logging():
    """
    Configures the Flask applications logger to write logs to files found within the applications Log directory.
    """
    dictConfig(
        {
            'version': 1,
            'formatters': {
                'default': {
                    'format': '%(asctime)s - %(levelname)s - %(module)s - %(thread)d - %(message)s', 
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                }
            },
            'handlers': {
                'size-rotate': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': './Logs/app.log',
                    'maxBytes': 1024 * 1024 * 5,
                    'backupCount': 5,
                    'formatter': 'default',
                },
            },
            'root': {
                'level': 'INFO', 
                'handlers': ['size-rotate']
            }
        }
    )

def log(func):
    """
    A logging decorator function, used to log entry and exit of a given function.

    :param func: The callback function to log against.
    :type func: Function
    :return: The return value of the decorated function.
    :rtype: Any
    """    
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Entering function: {func.__name__} with {args, kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Exiting function: {func.__name__}')
        return result
    
    return wrapper
