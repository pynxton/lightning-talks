from __future__ import absolute_import
from celery import Celery


app = Celery('celery_exp', broker='amqp://', include=['celery_exp.tasks'])

if __name__ == '__main__':
	app.start()
