from celery import shared_task 
import json
@shared_task 
def jsonify(object):
  data = json.dumps(object)
  print(data)
  return data
