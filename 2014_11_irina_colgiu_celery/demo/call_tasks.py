from __future__ import absolute_import
from celery_exp.tasks import add, print_fct


for i in range(1,10):
	async_result = add.apply_async([i, i+1], link=print_fct.s())
	print "submitted task! This is the task id: "+str(async_result)
