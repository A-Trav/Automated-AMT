"""
The scheduler module: Application task scheduler.

Provides the applications task scheduler for running the AMT distribution
import task on a daily basis.
"""

from apscheduler.schedulers.background import BackgroundScheduler
import atexit, logging, datetime

from ScheduledTask.task import importer_task
from app_logging import log

scheduler = BackgroundScheduler(logger = logging.getLogger('root'))

def scheduler_init_app(app):
    start_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    scheduler.add_job(lambda: importer_task(app),'interval', minutes = 1, next_run_time = start_time)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=True))
