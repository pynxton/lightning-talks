from __future__ import absolute_import

from celery_exp.celery import app


@app.task
def print_fct(smth):
	print "This is a task to print something: "+str(smth)

@app.task
def add(x, y):
	# print "I received params: "+str(x)+' '+str(y)
	return x+y
