from celery import shared_task
from .email import send_review_mail
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(bind=True, name='sending_review_email', max_retries=3, retry_backoff=10)
def sending_review_email(self, name, email, review):
    logger.info("Executing sending_review_email task")
    logger.info(f"Task {self.request.id}")
    logger.info("Task result: ")
    return send_review_mail(name, email, review)
