"""
The scheduler module: Application task scheduler.

Provides the applications task scheduler for running the AMT distribution
import task on a daily basis.
"""

from apscheduler.schedulers.background import BackgroundScheduler
import atexit, logging, datetime
from ScheduledTask.task import importer_task
from Utils.app_logging import log

scheduler = BackgroundScheduler(logger = logging.getLogger('root'))
"""The background scheduler global"""

@log
def scheduler_init_app(app):
    """
    Integrates and runs the background scheduler global with the current Flask application.

    :param app: The current flask application to initialize the scheduler with
    :type app: Flask applicaton
    """
    start_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    scheduler.add_job(lambda: importer_task(app), 'interval', days = 1, next_run_time = start_time)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=True))
