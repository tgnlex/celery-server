from celery import shared_task

@shared_task
def reverse(text):
	return text[::-1]
