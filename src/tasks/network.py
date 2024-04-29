from celery import shared_task 
import os
@shared_task
def ip_sweep():
  ip = input("[CELERY] Enter the Host IP Address:\t") 
  print("[CELERY] Starting ping sweet on host: " + ip)
  dot = ip.rfind(".")
  ip = ip[0:dot + 1]
  for i in range(1, 255): 
    list = []
    host = ip + str(i)
    response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
    if response == 0: 
      print("[CELERY]"+host + " is up")
      list.append(host)
    else: 
      print("[CELERY]" +host + " is down")
    return list
  print("[CELERY] Available hosts on this ip: " + list)
  return list