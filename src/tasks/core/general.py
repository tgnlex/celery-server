from celery import shared_task 
import datetime


##################################
@shared_task
def get_date():
  date = datetime.datetime.now()
  print(date)
  return date