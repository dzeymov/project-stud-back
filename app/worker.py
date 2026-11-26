from celery import Celery

from app.config import settings

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app.conf.task_routes = {"app.worker.*": {"queue": "default"}}


@celery_app.task(name="send_notification")
def send_notification(item_id: int, title: str):
    print(f"[CELERY] Уведомление: создана запись #{item_id} '{title}'")
    return {"item_id": item_id, "status": "sent"}