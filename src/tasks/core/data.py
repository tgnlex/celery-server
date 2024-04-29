from celery import shared_task 
import csv 
import json

@shared_task 
def jsonify(object):
  data = json.dumps(object)
  print(data)
  return data

@shared_task
def read_csv(filename):
  with open(filename, newline='') as csvfile: 
    reader = csv.reader(csvfile, delimiter= ' ', quotechar='|')
    for row in reader:
      data = []
      current_row = ', '.join(row)
      data.append(current_row)
      print(current_row)
    return data 
      
