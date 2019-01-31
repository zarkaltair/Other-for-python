from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=1)
def timed_job():
	print('This job is run every one seconds.')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=9)
def scheduled_job():
	print('This job is run every weekday at 5pm.')


sched.start()

# print(dir(BlockingScheduler))