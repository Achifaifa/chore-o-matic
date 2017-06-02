#! /usr/bin/env/python

import datetime, os, smtplib, time
from email.mime.text import MIMEText
# Import file with emails, names, etc
import data

def rotate():
  """
  Cycles through the persons and assigns different tasks to them
  """

  chores=[i["chore"] for i in data.people]
  newchores=chores[-1:]+chores[:-1]
  print chores, newchores

  #replace chores in data.py module and website

  with open("./data.py","r") as instatus:
    status=instatus.read()
  with open("./index.html","r") as inindex:
    index=inindex.read()

  for i in range(4):
    status=status[::-1].replace(chores[i][::-1],newchores[i][::-1],1)[::-1]
    index=index[::-1].replace(chores[i].split()[-1][::-1],newchores[i].split()[-1][::-1],1)[::-1]
    print "Swapping...\nPrevious: %s\nNew:%s\n"%(", ".join(chores[i]), ", ".join(newchores[i]))

  # Change date in index
  week=datetime.date.today().isocalendar()[1]
  t=week-1
  prevweek=t if t>0 else 52
  index=index.replace("Semana %i"%prevweek, "Semana %i"%week)

  with open("./data.py","w+") as outstatus:
    outstatus.write(status)
  with open("./index.html","w+") as outindex:
    outindex.write(index)


def notify(who):
  """
  sends an email to everyone with their assigned tasks
  """

  # Compose email
  txt="Hola %s!\n\nEsta semana te toca %s, recuerda hacerlo antes del lunes :)\n"%(who["name"],who["chore"])
  mensaje=MIMEText(txt)
  mensaje['subject']="Tareas para esta semana"
  mensaje['from']="Chore-O-Matic"
  mensaje['to']=who["email"]

  # Connect to server and send email
  s=smtplib.SMTP(data.emailnode["smtp"], data.emailnode["port"])
  s.ehlo()
  s.starttls()
  s.login(data.emailnode["address"], data.emailnode["password"])
  s.sendmail(data.emailnode["address"], who["email"], mensaje.as_string())
  s.close()


print "Rotating chores..."
try:
  rotate()
  reload(data) #Data is changed in the .py file, so we have to reload it
  print "done"
except Exception as e:
  print "failed, quitting"
  print e
  exit()
for person in data.people:
  try:
    print "Sending email to %s..."%person["name"],
    notify(person)
    print "done"
  except:
    print "failed"

#testing
#notify(data.people[0])