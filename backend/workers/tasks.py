from celery import Celery
from backend.core.email import send_email  # заглушка

celery = Celery(
    'tasks',
    broker='pyamqp://guest@rabbitmq//',
    backend='redis://redis:6379/0'
)

@celery.task
def send_vote_notification(vote_data):
    send_email(
        to=vote_data["email"],
        subject="Спасибо за голос!",
        body=f"Вы проголосовали за: {vote_data['option']}"
    )
