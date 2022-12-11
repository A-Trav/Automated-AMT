from apscheduler.schedulers.background import BackgroundScheduler
import atexit, logging, datetime

from ScheduledTask.task import importer_task
    
scheduler = BackgroundScheduler()

def scheduler_init_app(app):
    start_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    scheduler.add_job(lambda: importer_task(app),'interval', minutes = 1, next_run_time = start_time)
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=True))
