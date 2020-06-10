from apscheduler.schedulers.blocking import BlockingScheduler
from val import wastmes



sched = BlockingScheduler()

sched.add_job(wastmes,day_of_week='mon-sun', hour=11, minute=30, end_date='2020-12-30')

sched.start()