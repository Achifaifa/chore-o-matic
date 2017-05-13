#! /usr/bin/env/python

import datetime, os, time
from email.mime.text import MIMEText
# Import file with emails, names, etc
import data

def rotate():
  """
  Cycles through the persons and assigns different tasks to them
  """

  chores=[i["chore"] for i in data.people]
  newchores=chores[-1]+chores[:-1]

  #replace chores in data.py module and website
  for i in range(4):
    os.system("""awk '{if($2=="%s") {$2="%s"} print $0}' status.py"""%(chores[i], newchores[i]))
    os.system("""awk '{if($2=="%s") {$2="%s"} print $0}' index.html"""%(chores[i], newchores[i]))


def notify(who, chore):
  """
  sends an email to everyone with their assigned tasks
  """

  # Compose email
  txt="Hola %s!\nEsta semana te toca %s, recuerda hacerlo antes del lunes :)\n"%(who["name"],chore)
  mensaje=MIMEText(txt)
  mensaje['subject']="Tareas para esta semana"
  mensaje['from']="Chore-O-Matic"
  mensaje['to']=who["email"]

  # Connect to server and send email
  s=smtplib.SMTP(data.emailnode["smtp"], data.emailnode["port"])
  s.ehlo()
  s.starttls()
  s.login(data.emailnode["address"], data.emailnode["password"])
  try:
    s.sendmail(data.emailnode["address"], who["email"], mensaje.as_string())
  except: 
    pass #YOLO
  finally:
      s.close()

rotate()
updateweb()
notify()