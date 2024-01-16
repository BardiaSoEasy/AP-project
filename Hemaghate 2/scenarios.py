import sqlite3
import requests
import re 

while True:
    print("1. Login")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        conn = sqlite3.connect('.database.sql')
        c = conn.cursor()

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Query the database
        c.execute("SELECT * FROM User WHERE name=? AND password=?", (username, password))

        # Fetch one record
        user = c.fetchone()

        if user is None:
            print("Invalid username or password.")
        else:
            print("Login successful.")

            while True:
                print("1. View Appointments")
                print("2. New Appointment")
                print("3. Logout")
                choice = input("Enter your choice: ")

                if choice == '1':
                    # Get appointments from the API
                    response = requests.get('http://localhost/slots')

                    if response.status_code == 200:
                        appointments = response.json()

                        for clinic_id, slots in appointments.items():
                            print(f"Clinic ID: {clinic_id}, Available Slots: {slots}")
                elif choice == '2':
                    # Search for a clinic/service
                    search = input("Enter clinic or doctor name: ")

                    # Use regex to match the search term
                    pattern = re.compile(search, re.IGNORECASE)

                    # Query the database for clinics
                    c.execute("SELECT * FROM Clinic")

                    # Fetch all records
                    clinics = c.fetchall()

                    if clinics:
                        for clinic in clinics:
                            if pattern.search(clinic[1]):
                                print(f"Match found: {clinic[1]}")
                                reserved = int(input("Enter number of slots to reserve: "))

                                # Send a POST request to the API
                                response = requests.post('http://localhost/reserve', json={'id': clinic[0], 'reserved': reserved})

                                if response.status_code == 200:
                                    result = response.json()

                                    if result['success']:
                                        print(f"Appointment reserved successfully. Remaining slots: {result['remaining_slots']}")
                                    else:
                                        print("Error reserving appointment.")
                                else:
                                    print("Error reserving appointment.")   
                    else:
                        print("No clinics found.")
                elif choice == '3':
                    break
       
    elif choice == '2':
        break
