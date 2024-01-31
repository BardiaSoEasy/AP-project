import menus
import database
import system

currentUser = None

system.clearTerminal()
print("──────────────────────────────────────")
print(" Welcome to Clinic Reservation System ")
print("──────────────────────────────────────")
print("              Loading...              ")
print("──────────────────────────────────────")
if database.initializeDatabase():
  while currentUser == None:
    currentUser = menus.loginMenu()
    if currentUser == None:
      break
    elif currentUser != None and currentUser.usertype == 'S':
      menus.staffMainMenu(currentUser)
    elif currentUser != None and currentUser.usertype == 'P':
      menus.patientMainMenu(currentUser)
    elif currentUser != None and currentUser.usertype == 'A':
      menus.adminMainMenu(currentUser)
else:
  system.clearTerminal()
  system.printBlankLine(1)  
  print("*** Error on creating or openning database ***")
  system.printBlankLine(1)  
system.clearTerminal()
system.printBlankLine(1)
print(" Bye...")
system.printBlankLine(1)
