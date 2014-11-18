This example shows briefly the functionality of celery using RabbitMQ as message broker.
In order to run it, you need to start one or more worker processes with:

	celery worker -A celery_exp

and you can submit tasks with:

	python call_tasks.py

Please note that you should be running the workers in an environment that has celery installed.
For instance, you can create a virtualenv environment where you can install all the python libraries your tasks use as part of their functionality plus celery and activate this environment before starting the workers processes, no matter if you run them locally or on the cluster.


The way I run the workers on the farm is:

# I activate my own Python environment, and then I bsub the workers - e.g.:
bsub -R"select[mem>4000] rusage[mem=4000]" -M4000 -G hgi -o worker1.out  "celery worker -A celery_exp --loglevel=info"



