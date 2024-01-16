import system
import models
import random

def signupForm():
  user = models.User()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                        Signup Form                        ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  username = input(" User Name                      : ")
  password = input(" Password                       : ")
  name =     input(" Name                           : ")
  email =    input(" E-Mail                         : ")
  usertype = input(" User Type (P=Patient, S=Staff) : ")
  print("───────────────────────────────────────────────────────────")
  rowcount = user.register(username=username, password=password, name=name, email=email, usertype=usertype)
  if rowcount > 0:
    print("User created successfully.")
  else:
    print("Error on creating user.")
  print("───────────────────────────────────────────────────────────")
  input("Press Enter key to continue...")    
  return True

def usernamePasswordForm():
  currentUser = models.User()
  system.clearTerminal()
  print("───────────────────────────────")
  print("          Signin Form          ")
  print("   Clinic Reservation System   ")
  print("───────────────────────────────")
  username = input(" User Name : ")
  password = input(" Password  : ")
  currentUser.login(username=username, password=password)
  if username != "" and currentUser.username == username and currentUser.password == password:
    return currentUser
  else:
    print("───────────────────────────────")
    print(" Invalid username or password.")
    print("───────────────────────────────")
    input("Press Enter key to continue...")
    return None  

def usernameOneTimePasswordForm():
  currentUser = models.User()
  notification = models.Notification()
  OneTimePassword = random.randrange(1000, 9999)
  system.clearTerminal()
  print("───────────────────────────────────────────────")
  print("                  Signin Form                  ")
  print("           Clinic Reservation System           ")
  print("───────────────────────────────────────────────")
  username = input(" User Name : ")
  currentUser.getUser(username=username)
  if username != "" and currentUser.username == username:
    notification.sendMessage(username=username, email=currentUser.email, message=f"Clinic Reservation System (On-Time Password) : {OneTimePassword}")
    print("───────────────────────────────────────────────")
    print("    Check your e-mail for one-time password    ")
    print("───────────────────────────────────────────────")
    password = input(" One-Time Password  : ")
    if OneTimePassword == password:
      currentUser.loginByUserName(username=username)
      if currentUser.username == username:
        return currentUser
    else:
      print("───────────────────────────────────────────────")
      print(" Invalid one-time password.")
      print("───────────────────────────────────────────────")
      input(" Press Enter key to continue...")
      return None
  else:
    print("───────────────────────────────")
    print(" Invalid username.")
    print("───────────────────────────────")
    input("Press Enter key to continue...")
    return None  
    
def updateProfileForm(currentUser):
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                    Update Profile Form                    ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  print(f" UserName = {currentUser.username}")
  print(f" Password = {currentUser.password}")
  print(f" Name = {currentUser.name}")
  print(f" EMail = {currentUser.email}")
  print(f" UserType (P=Patient, S=Staff) = {currentUser.usertype}")
  print("───────────────────────────────────────────────────────────")
  password = input(" Password                       : ")
  name =     input(" Name                           : ")
  email =    input(" E-Mail                         : ")
  if password == '': password = currentUser.password
  if name == '': name = currentUser.name
  if email == '': email = currentUser.email
  print("───────────────────────────────────────────────────────────")
  rowcount = currentUser.updateProfile(password=password, name=name, email=email)
  if rowcount > 0:
    print("Profile updated successfully.")
  else:
    print("Error on updating profile.")
  print("───────────────────────────────────────────────────────────")
  input("Press Enter key to continue...")    
  return True

def deleteUser():
  user = models.User()
  system.clearTerminal()
  print("─────────────────────────────────────────────────────────")
  print("                    Delete User Form                     ")
  print("                Clinic Reservation System                ")
  print("─────────────────────────────────────────────────────────")
  username = input(" User Name : ")
  user.getUser(username=username)
  if user.username != '' and user.username == username:
    user.removeUser(username=username)
    print("───────────────────────────────────────────────────────────")
    print("User deleted successfully.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  else:
    print("───────────────────────────────────────────────────────────")
    print(" User not found.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  return True

def createClinic():
  clinic = models.Clinic()
  system.clearTerminal()
  print("───────────────────────────────────────────────")
  print("              Create Clinic Form               ")
  print("           Clinic Reservation System           ")
  print("───────────────────────────────────────────────")
  name = input(" Name     : ")
  address = input(" Address  : ")
  contact = input(" Contact  : ")
  print("───────────────────────────────────────────────")
  rowcount = clinic.addClinic(name=name, address=address, contact=contact)
  if rowcount > 0:
    print("Clinic created successfully.")
  else:
    print("Error on creating clinic.")
  print("───────────────────────────────────────────────")
  input("Press Enter key to continue...")    
  return True

def updateClinic():
  clinic = models.Clinic()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                    Update Clinic Form                     ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  clinicid = system.inputNumber(" ClinicId : ")
  clinic.getClinicById(clinicId=clinicid)
  if clinicid != 0 and clinic.clinicid == clinicid:
    print(f" Name = {clinic.name}")
    print(f" Address = {clinic.address}")
    print(f" Contact = {clinic.contact}")
    print(f" Availability = {clinic.availability}")
    print("───────────────────────────────────────────────────────────")
    name = input(" Name     : ")
    address = input(" Address  : ")
    contact = input(" Contact  : ")
    if name == '': name = clinic.name
    if address == '': address = clinic.address
    if contact == '': contact = clinic.contact
    print("───────────────────────────────────────────────────────────")
    rowcount = clinic.updateClinicInfo(clinicid=clinicid, name=name, address=address, contact=contact)
    if rowcount > 0:
      print("Clinic updated successfully.")
    else:
      print("Error on updating clinic.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  else:
    print("───────────────────────────────────────────────────────────")
    print(" Clinic not found.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  return True

def deleteClinic():
  clinic = models.Clinic()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                    Delete Clinic Form                     ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  c = input(" ClinicId : ")
  if not c.isdigit():
    clinicId = 0
  else:
    clinicId = int(c)
  clinic.getClinicById(clinicId=clinicId)
  if clinic.clinicid > 0 and clinic.clinicid == clinicId:
    clinic.removeClinic(clinicId=clinicId)
    print("───────────────────────────────────────────────────────────")
    print("Clinic deleted successfully.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  else:
    print("───────────────────────────────────────────────────────────")
    print(" Clinic not found.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  return True

def viewClinics():
  clinic = models.Clinic()
  system.clearTerminal()
  print("".ljust(120, "─"))
  print("View Clinics Form".rjust(70))
  print("Clinic Reservation System".rjust(75))
  print("".ljust(120, "─"))
  clinicList = clinic.getClinics()
  print(system.generateGridHeader(['ClinicId', 'Name', 'Address', 'Contact', 'Availability'], 20))
  print("".ljust(120, "─"))
  print(system.generateGridBody(clinicList, 20))
  print("".ljust(120, "─"))
  input("Press Enter key to continue...")

def setAvailabilityClinic():
  clinic = models.Clinic()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("              Set Availability A Clinic Form               ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  clinicId = system.inputNumber(" ClinicId : ")
  clinic.getClinicById(clinicId=clinicId)
  if clinicId != 0 and clinic.clinicid == clinicId:
    print(f" Name = {clinic.name}")
    print(f" Address = {clinic.address}")
    print(f" Contact = {clinic.contact}")
    print(f" Availability = {clinic.availability}")
    print("───────────────────────────────────────────────────────────")
    rowcount = clinic.setAvailability(clinicid=clinicId, availability="1")
    if rowcount > 0:
      print("Clinic availability updated successfully.")
    else:
      print("Error on updating clinic availability.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  else:
    print("───────────────────────────────────────────────────────────")
    print(" Clinic not found.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  return True

def reserveAnAppointment(currentuser):
  appointment = models.Appointment()
  service = models.Service()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                Reserve An Appointment Form                ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  clinicid = system.inputNumber(" ClinicId : ")
  datetime = input("Date/Time : ")
  print(service.getClinicServiceList(clinicid=clinicid))
  serviceid = system.inputNumber(" Service Id : ")
  print("───────────────────────────────────────────────────────────")
  if appointment.clinicExists(clinicid) > 0:
    if datetime == '':
      datetime = system.currentDateTime()
    rowcount = appointment.bookAppointment(clinidid=clinicid, serviceid=serviceid, username=currentuser.username, datetime=datetime)
    if rowcount > 0:
      system.reserveClinicAppointmentCounterByAPI(clinicid=clinicid, count=1)
      print("Appointment booked successfully.")
    else:
      print("Error on bokking appointment.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
    return True
  else:
    print(" Clinic Id not found.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
    return True

def viewCurrentAppointments(currentuser):
  appointment = models.Appointment()
  system.clearTerminal()
  print("".ljust(120, "─"))
  print("View Current Appointm;ents Form".rjust(73))
  print("Clinic Reservation System".rjust(70))
  print("".ljust(120, "─"))
  appointmentList = appointment.getCurrentAppointments(currentuser.username)
  print(system.generateGridHeader(['AppointmentId', 'ClinicId', 'UserName', 'Date/Time', 'Status', 'ServiceId'], 20))
  print("".ljust(120, "─"))
  print(system.generateGridBody(appointmentList, 20))
  print("".ljust(120, "─"))
  input("Press Enter key to continue...")
  
def viewAppointmentsHistory(currentuser):
  appointment = models.Appointment()
  system.clearTerminal()
  print("".ljust(120, "─"))
  print("View Appointments History Form".rjust(73))
  print("Clinic Reservation System".rjust(70))
  print("".ljust(120, "─"))
  appointmentList = appointment.getAppointmentsHistory(currentuser.username)
  print(system.generateGridHeader(['AppointmentId', 'ClinicId', 'UserName', 'Date/Time', 'Status', 'ServiceId'], 20))
  print("".ljust(120, "─"))
  print(system.generateGridBody(appointmentList, 20))
  print("".ljust(120, "─"))
  input("Press Enter key to continue...")
  
def viewAppointments():
  appointment = models.Appointment()
  system.clearTerminal()
  print("".ljust(120, "─"))
  print("View Current Appointments Form".rjust(73))
  print("Clinic Reservation System".rjust(70))
  print("".ljust(120, "─"))
  appointmentList = appointment.getAppointments()
  print(system.generateGridHeader(['AppointmentId', 'ClinicId', 'UserName', 'Date/Time', 'Status', 'ServiceId'], 20))
  print("".ljust(120, "─"))
  print(system.generateGridBody(appointmentList, 20))
  print("".ljust(120, "─"))
  input("Press Enter key to continue...")

def increaseClinicAppointmentCounter():
  clinic = models.Clinic()
  system.clearTerminal()
  print("────────────────────────────────────────────────────────────")
  print("          Increase Clinic Appointment Counter Form          ")
  print("                  Clinic Reservation System                 ")
  print("────────────────────────────────────────────────────────────")
  clinicid = system.inputNumber(" Clinic Id : ")
  count = system.inputNumber(" Count : ")
  if clinic.isClinicExists(clinicid):
    print("────────────────────────────────────────────────────────────")
    data = system.reserveClinicAppointmentCounterByAPI(clinicid=clinicid, count=-count)
    if data["success"] == True:
      print(data)
    else:
      print(" Error on calling API.")
  else:
    print("────────────────────────────────────────────────────────────")
    print(" Clinic not found.")
  print("────────────────────────────────────────────────────────────")
  input(" Press Enter key to continue...")
  return True

def cancelAnAppointment():
  clinic = models.Clinic()
  appointment = models.Appointment()
  user = models.User()
  system.clearTerminal()
  print("──────────────────────────────────────────────")
  print("          Cancel An Appointment Form          ")
  print("           Clinic Reservation System          ")
  print("──────────────────────────────────────────────")
  appointmentid = system.inputNumber(" Appointment Id : ")
  clinicid = system.inputNumber(" Clinic Id : ")
  username = input(" User Name : ")
  if appointmentid > 0 and appointment.isAppointmentExists(appointmentid=appointmentid) > 0:
    if clinicid > 0 and  clinic.isClinicExists(clinicid=clinicid):
      if username != "" and user.isUserExists(username=username):
        print("────────────────────────────────────────────────────────────")
        appointment.cancelAnAppointment(appointmentid=appointmentid, clinicid=clinicid, username=username)
        data = system.reserveClinicAppointmentCounterByAPI(clinicid=clinicid, count=-1)
        if data["success"] == True:
          print(data)
          print(" Appointment cancelled successfully.")
        else:
          print("────────────────────────────────────────────────────────────")
          print(" Error on calling API.")
      else:
        print("────────────────────────────────────────────────────────────")
        print(" User not found.")
    else:
      print("────────────────────────────────────────────────────────────")
      print(" Clinic not found.")
  else:
    print("────────────────────────────────────────────────────────────")
    print(" Appointment not found.")
  print("────────────────────────────────────────────────────────────")
  input(" Press Enter key to continue...")
  return True

def viewClinicSlot():
  clinic = models.Clinic()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                     View Clinic Slot                      ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  clinicid = system.inputNumber(" ClinicId : ")
  clinic.getClinicById(clinicId=clinicid)
  if clinicid != 0 and clinic.clinicid == clinicid:
    print(f" Name = {clinic.name}")
    print(f" Address = {clinic.address}")
    print(f" Contact = {clinic.contact}")
    print(f" Availability = {clinic.availability}")
    print("───────────────────────────────────────────────────────────")
    clinics = system.getAppointmentsCounterByAPI()
    print(f" Clinic Slot = {clinics[str(clinicid)]}")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  return True

def viewClinicServices():
  service = models.Service()
  system.clearTerminal()
  print("".ljust(80, "─"))
  print("View Clinic Servies Form".rjust(54))
  print("Clinic Reservation System".rjust(54))
  clinicid = system.inputNumber(" Clinic Id : ")
  print("".ljust(80, "─"))
  serviceList = service.getClinicServices(clinicid=clinicid)
  print(system.generateGridHeader(['ServiceId', 'ClinicId', 'Name', 'Price'], 20))
  print("".ljust(80, "─"))
  print(system.generateGridBody(serviceList, 20))
  print("".ljust(80, "─"))
  input("Press Enter key to continue...")  

def createService():
  service = models.Service()
  system.clearTerminal()
  print("───────────────────────────────────────────────")
  print("              Create Service Form              ")
  print("           Clinic Reservation System           ")
  print("───────────────────────────────────────────────")
  clinicid = system.inputNumber(" Clinic Id : ")
  name = input(" Name : ")
  price = system.inputNumber(" Price : ")
  print("───────────────────────────────────────────────")
  rowcount = service.addService(clinicid=clinicid, name=name, price=price)
  if rowcount > 0:
    print("Service created successfully.")
  else:
    print("Error on creating service.")
  print("───────────────────────────────────────────────")
  input("Press Enter key to continue...")    
  return True

def updateService():
  service = models.Service()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                    Update Service Form                    ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  serviceid = system.inputNumber(" Service Id : ")
  service.getServiceById(serviceid=serviceid)
  if serviceid != 0 and service.serviceid == serviceid:
    print(f" Clinic Id = {service.clinicid}")
    print(f" Name = {service.name}")
    print(f" Price = {service.price}")
    print("───────────────────────────────────────────────────────────")
    clinicid = system.inputNumber(" Clinic Id : ")
    name = input(" Name : ")
    price = system.inputNumber(" Price : ")
    if clinicid == 0: clinicid = service.clinicid
    if name == '': name = service.name
    if price == 0: price = service.price
    print("───────────────────────────────────────────────────────────")
    rowcount = service.updateService(serviceid=serviceid, clinicid=clinicid, name=name, price=price)
    if rowcount > 0:
      print("Service updated successfully.")
    else:
      print("Error on updating service.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  else:
    print("───────────────────────────────────────────────────────────")
    print(" Service not found.")
    print("───────────────────────────────────────────────────────────")
    input("Press Enter key to continue...")    
  return True

def deleteService():
  service = models.Service()
  system.clearTerminal()
  print("───────────────────────────────────────────────────────────")
  print("                    Delete Service Form                    ")
  print("                 Clinic Reservation System                 ")
  print("───────────────────────────────────────────────────────────")
  serviceid = system.inputNumber(" Service Id : ")
  service.getServiceById(serviceid=serviceid)
  if serviceid > 0 and service.serviceid == serviceid:
    service.removeService(serviceid=serviceid)
    print("───────────────────────────────────────────────────────────")
    print(" Service deleted successfully.")
    print("───────────────────────────────────────────────────────────")
    input(" Press Enter key to continue...")    
  else:
    print("───────────────────────────────────────────────────────────")
    print(" Service not found.")
    print("───────────────────────────────────────────────────────────")
    input(" Press Enter key to continue...")    
  return True

def payAppointment():
  payment = models.Payment()
  appointment = models.Appointment()
  system.clearTerminal()
  print("───────────────────────────────────────────────")
  print("              Pay Appointment Form             ")
  print("           Clinic Reservation System           ")
  print("───────────────────────────────────────────────")
  appointmentid = input(" Appointment Id : ")
  if appointment.isAppointmentExists(appointmentid=appointmentid):
    print("───────────────────────────────────────────────")
    rowcount = payment.addPayment(appointmentid=appointmentid)
    if rowcount > 0:
      print("Payment created successfully.")
    else:
      print("Error on creating payment.")
  else:
    print("───────────────────────────────────────────────")
    print (" Appointment not found.")
  print("───────────────────────────────────────────────")
  input("Press Enter key to continue...")    
  return True
