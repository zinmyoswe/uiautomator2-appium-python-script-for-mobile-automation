from celery import Celery

# Create a Celery instance
app = Celery(
    'youtube_data_task',
    broker='redis://localhost:6379/0',  # Replace with your broker URL
    backend='redis://localhost:6379/0'  # Replace with your backend URL
)

# Configuration settings for Celery
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_annotations={
        'tasks.fetch_youtube_data': {'rate_limit': '10/m'}  # Limit task to 10 calls per minute
    },
)
