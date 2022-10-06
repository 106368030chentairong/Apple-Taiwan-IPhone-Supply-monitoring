import os
import urllib.request
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from main import *

sched = BlockingScheduler(timezone="Asia/Taipei")
url_name = os.environ.get("CLOCK_NAME")

@sched.scheduled_job('cron', minute='*/1')
def scheduled_job():
    print('========== APScheduler CRON RUN =========')
    print('This job runs every day */1 min.')
    print(f'{datetime.datetime.now().ctime()}')
    url = "https://"+url_name+".herokuapp.com/"
    try:
        onn = urllib.request.urlopen(url)
    except Exception :
        pass
    try:
        get_order()
    except Exception:
        pass
    print('========== APScheduler CRON STOP =========')

sched.start()