from celery import shared_task
from .email import *
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(bind=True, name='sending_review_email', max_retries=3, retry_backoff=10)
def sending_review_email_task(self, name, email, review):
    logger.info("Executing sending_review_email task")
    logger.info(f"Task {self.request.id}")
    logger.info("Task result: ")
    return review_mail_sender(name, email, review)


@shared_task(bind=True, name='10am_daily_mail', max_retries=2, retry_backoff=60)
def daily_10_mail_sender_task(self):
    logger.info("Executing sending_review_email task")
    logger.info(f"Task {self.request.id}")
    logger.info("Task result: ")
    return daily_10am_mail_sender()
