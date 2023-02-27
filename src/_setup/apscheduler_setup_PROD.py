"""
====================================================================================================
.DESCRIPTION
    APScheduler to launch jobs

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		18/02/2023  CWY Initial Version

.COMMENTS

    scheduler.add_job(job, 'cron', hour='6,10,12,16,20', minute=00)

    scheduler.add_job(job, 'interval', seconds=5)

    scheduler.add_job(job, 'cron', hour='9,13,18')

    scheduler.add_job(job, 'cron', hour='6,11,12,18', minute=30)

    # Schedule the job to run at multiple times
    job_times = [
        datetime(2023, 2, 20, 12, 0, 0),
        datetime(2023, 2, 21, 10, 30, 0),
        datetime(2023, 2, 22, 16, 15, 0),
    ]
    for time in job_times:
        scheduler.add_job(job, 'date', run_date=time)
====================================================================================================
"""
import os
# from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print('Start run_all_scripts')

    os.system("python run_all_scripts_REPRISE.py")

    print('Stop run_all_scripts')


scheduler = BlockingScheduler()

scheduler.add_job(job, 'cron', hour='6,10,12,16,20', minute=00)
# scheduler.add_job(job, 'cron', hour='14', minute=50)

scheduler.start()
