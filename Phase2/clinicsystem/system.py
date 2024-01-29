import os
import platform
import datetime
import requests
import smtplib

def clearTerminal():
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('reset')

def printBlankLine(n):
    for i in range(n):
        print("")

def generateGridHeader(columns, width):
    header = ""
    for i in range(len(columns)):
        header += columns[i].ljust(width)
    return header

def generateGridBody(data, width):
    body = ""
    for i in range(len(data)):
        row = ""
        for j in range(len(data[i])):
            row += str(data[i][j]).ljust(width)
        body += row + "\r\n"
    return body

def inputNumber(message):
  n = input(message)
  if not n.isdigit():
    return 0
  else:
    return int(n)

def currentDateTime():
    now = datetime.datetime.now()
    return f"{now.year}/{now.month}/{now.day} {now.hour}:{now.minute}:{now.second}"

def getAppointmentsCounterByAPI():
    url = 'http://localhost:5000/slots'
    resp = requests.get(url=url)
    data = resp.json()
    return data
    
def reserveClinicAppointmentCounterByAPI(clinicid, count):
    url = 'http://localhost:5000/reserve'
    json = dict(
        id=clinicid,
        reserved=count
    )
    headers = {'Accept': 'application/json'}
    resp = requests.post(url=url, json=json, headers=headers)
    data = resp.json()
    return data

def sendEmail(email, message):
    sender = "sahel.rajaie@gmail.com"
    receiver = email
    
    message = f"""\
    Subject: Clinic Reservation System
    To: {receiver}
    From: {sender}
    """ + message
    
    with smtplib.SMTP(host="sandbox.smtp.mailtrap.io", port=2525) as server:
        server.login("7820e36b182f23", "397d090b1ed496")
        server.sendmail(sender, receiver, message)

