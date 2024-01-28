from django.db import models
from django.core.exceptions import ValidationError
from .validators import username_validation , email_validation , password_validation
from datetime import datetime
import database
import system 

class User:
  def __init__(self):
    self.username: str = ""
    self.name: str = ""
    self.email: str = ""
    self.password: str = ""
    self.usertype: str = ""

  def register(self, username, password, name, email, usertype):
    return database.insertUser(username=username, password=password, name=name, email=email, usertype=usertype)
  
  def login(self, username, password):
    userList = database.selectUserByUserNamePassword(username, password)
    if len(userList) > 0:
      self.username = userList[0][0]
      self.password = userList[0][1]
      self.name = userList[0][2]
      self.email = userList[0][3]
      self.usertype = userList[0][4]
    return self

  def loginByUserName(self, username):
    userList = database.selectUserByUserNamePassword(username, database.getUserPassword(username=username))
    if len(userList) > 0:
      self.username = userList[0][0]
      self.password = userList[0][1]
      self.name = userList[0][2]
      self.email = userList[0][3]
      self.usertype = userList[0][4]
    return self

  def getUser(self, username):
    userList = database.selectUserByUserName(username)
    if len(userList) > 0:
      self.username = userList[0][0]
      self.password = userList[0][1]
      self.name = userList[0][2]
      self.email = userList[0][3]
      self.usertype = userList[0][4]
    return self
  
  def updateProfile(self, password, name, email):
    return database.updateUser(username=self.username, currentPassword=self.password, newPassword=password, name=name, email=email)

  def viewAppointments(self):
    # This method returns a list of appointments that the user has booked or assigned
    pass

  def removeUser(self, username):
    database.deleteUser(username=username)
  
  def isUserExists(self, username):
    return database.isUserExists(username=username)
  
class Clinic:
  def __init__(self):
    self.clinicid: int = 0
    self.name: str = ""
    self.address: str = ""
    self.contact: str = ""
    self.availability: str = "0"

  def addClinic(self, name, address, contact):
    return database.insertClinic(name=name, address=address, contact=contact)

  def updateClinicInfo(self, clinicid, name, address, contact):
    return database.updateClinic(clinicid=clinicid, name=name, address=address, contact=contact)
  
  def setAvailability(self, clinicid, availability):
    return database.updateClinicAvailability(clinicid=clinicid, availability=availability)
    
  def viewAppointments(self):
    apointmentList = database.selectAppointments()
    return apointmentList
    
  def getClinicById(self, clinicId):
    clinicList = database.selectClinicById(clinicId)
    if len(clinicList) > 0:
      self.clinicid = clinicList[0][0]
      self.name = clinicList[0][1]
      self.address = clinicList[0][2]
      self.contact = clinicList[0][3]
      self.availability = clinicList[0][4]
    return self    

  def removeClinic(self, clinicId):
    database.deleteClinic(clinicId=clinicId)
    
  def getClinics(self):
    clinicList = database.selectClinics()
    return clinicList
  
  def isClinicExists(self, clinicid):
    return database.isClinicExists(clinicid=clinicid)
    
class Appointment:
  def __init__(self):
    self.appointmentid: int = 0
    self.clinicid: int = 0
    self.serviceid: int = 0
    self.username: int = ""
    self.datetime: str = ""
    self.status: str = ""


  def bookAppointment(self, clinidid, serviceid, username, datetime):
    return database.insertAppointment(clinicid=clinidid, serviceid=serviceid, username=username, datetime=datetime, status="B")

  def clinicExists(self, clinicId):
    return len(database.selectClinicById(clinicId=clinicId))

  def getCurrentAppointments(self, username):
    return database.selectCurrentAppointmentsByUser(username)

  def getAppointmentsHistory(self, username):
    return database.selectAppointmentsHistory(username)

  def getAppointments(self):
    return database.selectAppointments()

  def cancelAnAppointment(self, appointmentid, clinicid, username):
    return database.updateAppointment(appointmentid=appointmentid, clinicid=clinicid, username=username, status="C")

  def isAppointmentExists(self, appointmentid):
    return database.isAppointmentExists(appointmentid=appointmentid)
  

class Notification:
  def __init__(self):
    self.notificationid: int = 0
    self.username: str = ""
    self.datetime: str = ""
    self.message: str = ""

  def sendMessage(self, username, email, message):
    user = User()
    self.username = username
    self.datetime = system.currentDateTime()
    self.message = message
    database.insertNotification(username=username, message=message, datetime=self.datetime)
    system.sendEmail(email=email, message=message)


class Service:
  def __init__(self):
    self.serviceid: int = 0
    self.clinicid: int = 0
    self.name: str = ""
    self.price: int = 0
  
  def addService(self, clinicid, name, price):
    return database.insertService(clinicid=clinicid, name=name, price=price)
    
  def updateService(self, serviceid, clinicid, name, price):
    return database.updateService(serviceid=serviceid, clinicid=clinicid, name=name, price=price)
  
  def viewServices(self, clinicid):
    serviceList = database.selectServiceByClinicId(clinicid=clinicid)
    return serviceList
  
  def getServiceById(self, serviceid):
    serviceList = database.selectServiceById(serviceid=serviceid)
    if len(serviceList) > 0:
      self.serviceid = serviceList[0][0]
      self.clinicid = serviceList[0][1]
      self.name = serviceList[0][2]
      self.price = serviceList[0][3]
    return self 
    
  def getServiceList(self, serviceid):
    serviceList = database.selectServiceById(serviceid=serviceid)
    services = ""
    for s in serviceList:
      services += f"({s[0]}) {s[2]})"
    return services

  def getClinicServiceList(self, clinicid):
    serviceList = database.selectClinicServices(clinicid=clinicid)
    services = "["
    for s in serviceList:
      services += f"{s[0]}) {s[2]}, "
    services += "]"
    return services

  def removeService(self, serviceid):
    database.deleteService(serviceid=serviceid)

  def getClinicServices(self, clinicid):
    serviceList = database.selectClinicServices(clinicid=clinicid)
    return serviceList
    
class Payment:
  def __init__(self):
    self.paymentid: int = 0
    self.appointmentid: int = 0
    self.datatime: str = ""
    self.amount: int = 0

  def addPayment(self, appointmentid):
    database.updateAppointmentToPayment(appointmentid=appointmentid)
    serviceid = database.selectAppointmentServiceId(appointmentid=appointmentid)
    datetime = system.currentDateTime()
    amount = database.selectServicePrice(serviceid=serviceid)
    return database.insertPayment(appointmentid=appointmentid, datetime=datetime, amount=amount)

  def updatePayment(self, paymentid, appointmentid, datetime, amount):
    return database.updatePayment(paymentid=paymentid, appointmentid=appointmentid, datetime=datetime, amount=amount)
  
  def viewPayments(self, appointmentid):
    paymentList = database.selectPaymentByAppointmentId(appointmentid=appointmentid)
    return paymentList
