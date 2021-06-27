FROM python:3.7

COPY . /celery_tasks
WORKDIR /celery_tasks
RUN pip install -r /celery_tasks/requirements.txt


ENTRYPOINT celery -A tasks worker --loglevel=info