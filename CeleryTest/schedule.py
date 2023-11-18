from celery.schedules import crontab

tasks_schedule = {
    '10am_daily_mail_schedule': {
        'task': '10am_daily_mail',
        'schedule': crontab(minute="0", hour="10")
    },
}
