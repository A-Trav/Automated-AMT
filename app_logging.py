"""
The app_logging module: Application logging.

Provides functionality to support logging throughout the application runtime.
"""

import logging
from logging.config import dictConfig
from flask import current_app, request

def prod_logging():
    
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
    
    def wrapper(*args, **kwargs):
        logging.info(f'Entering function: {func.__name__} with {args, kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Exiting function: {func.__name__}')
        return result
    
    return wrapper
