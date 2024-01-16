import system
import forms

currentUser = None

def loginMenu():
  choice = 0
  while choice != 3:
    system.clearTerminal()
    print("───────────────────────────")
    print("         Login Menu        ")
    print(" Clinic Reservation System ")
    print("───────────────────────────")
    system.printBlankLine(1)
    print(" 1) Signin                 ")
    print(" 2) Signup                 ")
    print(" 3) Exit                   ")
    system.printBlankLine(1)
    print("───────────────────────────")
    choice = system.inputNumber(" Select a number : ")
    if choice == 1:
      currentUser = signinMenu()
      if currentUser != None:
        return currentUser
    elif choice == 2:
      forms.signupForm()
  return None
  
def signinMenu():
  choice = 0
  while choice != 3:
    system.clearTerminal()
    print("───────────────────────────────")
    print("          Signin Menu          ")
    print("   Clinic Reservation System   ")
    print("───────────────────────────────")
    system.printBlankLine(1)
    print("1) Username / Password")
    print("2) Username / One-Time Password")
    print("3) Return")
    system.printBlankLine(1)
    print("───────────────────────────────")
    choice = system.inputNumber(" Select a number : ")
    if choice == 1:
      currentUser = forms.usernamePasswordForm()
      if currentUser != None:
        return currentUser
    elif choice == 2:
      currentUser = forms.usernameOneTimePasswordForm()
      if currentUser != None:
        return currentUser
  return None

def staffMainMenu(currentUser):
  choice = 0
  while choice != 8:
    system.clearTerminal()
    print("───────────────────────────────────────────────")
    print("                 Staff Main Menu               ")
    print("          Clinic  Reservation  System          ")
    print("───────────────────────────────────────────────")
    system.printBlankLine(1)
    print(" 1) View Current Appointments")
    print(" 2) Cancel An Appointment")
    print(" 3) Increase Clinic Appointment Counter By API")
    print(" 4) View Clinic Slot")
    print(" 5) View Clinic Services")
    print(" 6) Pay Appointment")
    print("───────────────────────────────────────────────")
    print(" 7) Update Profile")
    print(" 8) Exit")
    system.printBlankLine(1)
    print("───────────────────────────────────────────────")
    choice = system.inputNumber(" Select a number : ")
    if choice == 1:
      forms.viewAppointments()
    elif choice == 2:
      forms.cancelAnAppointment()
    elif choice == 3:
      forms.increaseClinicAppointmentCounter()
    elif choice == 4:
      forms.viewClinicSlot()
    elif choice == 5:
      forms.viewClinicServices()
    elif choice == 6:
      forms.payAppointment()
    elif choice == 7:
      forms.updateProfileForm(currentUser)
  return

def patientMainMenu(currentUser):
  choice = 0
  while choice != 6:
    system.clearTerminal()
    print("──────────────────────────────────────")
    print("           Patient Main Menu          ")
    print("     Clinic  Reservation  System      ")
    print("──────────────────────────────────────")
    system.printBlankLine(1)
    print(" 1) View Current Appointments")
    print(" 2) View Appointments History")
    print(" 3) Reserve An Appointment")
    print(" 4) View Clinic Services")
    print("───────────────────────────────────────")
    print(" 5) Update Profile")
    print(" 6) Exit")
    system.printBlankLine(1)
    print("───────────────────────────────────────")
    choice = system.inputNumber(" Select a number : ")
    if choice == 1:
      forms.viewCurrentAppointments(currentUser)
    elif choice == 2:
      forms.viewAppointmentsHistory(currentUser)
    elif choice == 3:
      forms.reserveAnAppointment(currentUser)
    elif choice == 4:
      forms.viewClinicServices()
    elif choice == 5:
      forms.updateProfileForm(currentUser)
  return

def adminMainMenu(currentUser):
  choice = 0
  while choice != 11:
    system.clearTerminal()
    print("──────────────────────────────────────")
    print("            Admin Main Menu           ")
    print("     Clinic  Reservation  System      ")
    print("──────────────────────────────────────")
    system.printBlankLine(1)
    print("  1) Create A Clinic")
    print("  2) Update A Clinic")
    print("  3) Delete A Clinic")
    print("  4) Set A Clinic Availablity")
    print("  5) View Clinics")
    print("  6) Delete A User")
    print("  7) Create Clinic Service")
    print("  8) Update Clinic Service")
    print("  9) Delete Clinic Service")
    print("──────────────────────────────────────")
    print(" 10) Update Profile")
    print(" 11) Exit")
    system.printBlankLine(1)
    print("───────────────────────────────────────")
    choice = system.inputNumber(" Select a number : ")
    if choice == 1:
      forms.createClinic()
    elif choice == 2:
      forms.updateClinic()
    elif choice == 3:
      forms.deleteClinic()
    elif choice == 4:
      forms.setAvailabilityClinic()
    elif choice == 5:
      forms.viewClinics()
    elif choice == 6:
      forms.deleteUser()
    elif choice == 7:
      forms.createService()
    elif choice == 8:
      forms.updateService()
    elif choice == 9:
      forms.deleteService()
    elif choice == 10:
      forms.updateProfileForm(currentUser)
  return
