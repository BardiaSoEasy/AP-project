import mysql.connector

# Database
def initializeDatabase():
    createDatabaseSQL = "CREATE DATABASE IF NOT EXISTS `clinic_db`"
    createUserTableSQL = """
        CREATE TABLE IF NOT EXISTS `clinic_db`.`user` (
            `UserName` varchar(50) NOT NULL,
            `Password` varchar(50) NOT NULL,
            `Name` varchar(50) NOT NULL,
            `EMail` varchar(50) DEFAULT NULL,
            `UserType` char(1) NOT NULL,
            PRIMARY KEY (`UserName`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    createClinicTableSQL = """
        CREATE TABLE IF NOT EXISTS `clinic_db`.`clinic` (
            `ClinicId` int NOT NULL AUTO_INCREMENT,
            `Name` varchar(50) NOT NULL,
            `Address` varchar(255) NOT NULL,
            `Contact` varchar(50) DEFAULT NULL,
            `Availability` char(1) NOT NULL,
            PRIMARY KEY (`ClinicId`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    createServiceTableSQL = """
        CREATE TABLE IF NOT EXISTS `clinic_db`.`service` (
            `ServiceId` INT NOT NULL AUTO_INCREMENT,
            `ClinicId` INT NOT NULL,
            `Name` VARCHAR(50) NOT NULL,
            `Price` INT NOT NULL,
            PRIMARY KEY (`ServiceId`),
            INDEX `ClinicId_Service_idx` (`ClinicId` ASC) VISIBLE,
            CONSTRAINT `ClinicId_Service`
                FOREIGN KEY (`ClinicId`)
                REFERENCES `clinic_db`.`clinic` (`ClinicId`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    createApointmentTableSQL = """
        CREATE TABLE IF NOT EXISTS `clinic_db`.`appointment` (
            `AppointmentId` INT NOT NULL AUTO_INCREMENT,
            `ClinicId` INT NOT NULL,
            `UserName` VARCHAR(50) NOT NULL,
            `ServiceId` INT NOT NULL,
            `DateTime` VARCHAR(50) NOT NULL,
            `Status` CHAR(1) NOT NULL,
            PRIMARY KEY (`AppointmentId`),
            INDEX `ClinicId_Appointment_idx` (`ClinicId` ASC) VISIBLE,
            INDEX `UserName_Appointment_idx` (`UserName` ASC) VISIBLE,
            INDEX `ServiceId_Appointment_idx` (`ServiceId` ASC) VISIBLE,
            CONSTRAINT `ClinicId_Appointment`
                FOREIGN KEY (`ClinicId`)
                REFERENCES `clinic_db`.`clinic` (`ClinicId`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `UserName_Appointment`
                FOREIGN KEY (`UserName`)
                REFERENCES `clinic_db`.`user` (`UserName`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `ServiceId_Appointment`
                FOREIGN KEY (`ServiceId`)
                REFERENCES `clinic_db`.`service` (`ServiceId`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    createNotificationTableSQL = """
        CREATE TABLE IF NOT EXISTS `clinic_db`.`notification` (
            `NotificationId` INT NOT NULL AUTO_INCREMENT,
            `UserName` VARCHAR(50) NOT NULL,
            `DateTime` VARCHAR(50) NOT NULL,
            `Message` TEXT NOT NULL,
            PRIMARY KEY (`NotificationId`),
            INDEX `UserName_Notification_idx` (`UserName` ASC) VISIBLE,
            CONSTRAINT `UserName_Notification`
                FOREIGN KEY (`UserName`)
                REFERENCES `clinic_db`.`user` (`UserName`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    createPaymentTableSQL = """
        CREATE TABLE IF NOT EXISTS `clinic_db`.`payment` (
            `PaymentId` INT NOT NULL AUTO_INCREMENT,
            `AppointmentId` INT NOT NULL,
            `DateTime` VARCHAR(50) NOT NULL,
            `Amount` INT NOT NULL,
            PRIMARY KEY (`PaymentId`),
            INDEX `AppointmentId_Payment_idx` (`AppointmentId` ASC) VISIBLE,
            CONSTRAINT `AppointmentId_Payment`
                FOREIGN KEY (`AppointmentId`)
                REFERENCES `clinic_db`.`appointment` (`AppointmentId`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """

    serverName = ""
    databaseUserName = ""
    databaseUserPassword = ""
    databaseName = "clinic_db"
    try:
        dbFile = open("file.db", "r")
        serverName = dbFile.readline().replace("\n", "")
        databaseUserName = dbFile.readline().replace("\n", "")
        databaseUserPassword = dbFile.readline().replace("\n", "")
    except:
        dbFile = open("file.db", "w")
    
    if serverName == "":
        serverName = input(" Server Name (localhost) : ")
        if serverName == "":
            serverName = "localhost"
        databaseUserName = input(" Database User Name (root) : ")
        if databaseUserName == "":
            databaseUserName = "root"
        databaseUserPassword = input(" Database User Password : ")
        dbFile.writelines([serverName, "\n", databaseUserName, "\n", databaseUserPassword])
    dbFile.close()
    
    try:  
        db = mysql.connector.connect(host=serverName, user=databaseUserName, password=databaseUserPassword, database=databaseName)
        db.close()
    except:  
        db = mysql.connector.connect(host=serverName, user=databaseUserName, password=databaseUserPassword)
        cursor = db.cursor()  
        cursor.execute(createDatabaseSQL)
        cursor.close()
        db.close()

    db = mysql.connector.connect(host=serverName, user=databaseUserName, password=databaseUserPassword, database=databaseName)
    cursor = db.cursor()  
    cursor.execute(createUserTableSQL)
    cursor.execute(createClinicTableSQL)
    cursor.execute(createServiceTableSQL)
    cursor.execute(createApointmentTableSQL)
    cursor.execute(createNotificationTableSQL)
    cursor.execute(createPaymentTableSQL)
    cursor.close()
    db.close()
    admin = selectUserByUserNamePassword(username="Admin", password="Pass@word1")
    if len(admin) <= 0:
        insertUser(username="Admin", password="Pass@word1", name="Administrator", email="admin@gmail.com", usertype="A")
    return True

def openDatabase():
    dbFile = open("file.db", "r")
    serverName = dbFile.readline().replace("\n", "")
    databaseUserName = dbFile.readline().replace("\n", "")
    databaseUserPassword = dbFile.readline().replace("\n", "")
    return mysql.connector.connect(host=serverName, user=databaseUserName, password=databaseUserPassword, database="clinic_db")


# User Table
def insertUser(username, name, password, email, usertype):
    try:
        db = openDatabase()
        cursor = db.cursor()
        sql = "INSERT INTO `user` (`UserName`, `Name`, `Password`, `EMail`, `UserType`) Values (%s, %s, %s, %s, %s);"
        cursor.execute(sql, (username, name, password, email, usertype))
        db.commit()
        db.close()
    except mysql.connector.Error as err:
        print(err)
        return 0
    return cursor.rowcount

def selectUsers():
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `UserName`, `Password`, `Name`, `Email`, `UserType` FROM `user`;"
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result

def selectUserByUserNamePassword(username, password):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `UserName`, `Password`, `Name`, `EMail`, `UserType` FROM `user` WHERE `UserName` = %s AND `Password` = %s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchall()
    db.close()
    return result

def selectUserByUserName(username):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `UserName`, `Password`, `Name`, `EMail`, `UserType` FROM `user` WHERE `UserName` = %s"
    cursor.execute(sql, [username])
    result = cursor.fetchall()
    db.close()
    return result

def getUserPassword(username):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `Password` FROM `user` WHERE `UserName` = %s"
    cursor.execute(sql, (username))
    result = cursor.fetchall()
    db.close()
    return result[0][1]

def updateUser(username, currentPassword, newPassword, name, email):
    db = openDatabase()
    cursor = db.cursor()
    sql = "UPDATE `user` SET `Password` = %s, `Name` = %s, `EMail` = %s WHERE `UserName` = %s AND `Password` = %s"
    cursor.execute(sql, (newPassword, name, email, username, currentPassword))
    db.commit()
    db.close()
    return cursor.rowcount

def deleteUser(username):
    db = openDatabase()
    cursor = db.cursor()
    sql = "DELETE FROM `user` WHERE `UserName` = %s"
    cursor.execute(sql, [username])
    db.commit()
    db.close()
    return cursor.rowcount


# Clinic Table
def insertClinic(name, address, contact):
    try:
        db = openDatabase()
        cursor = db.cursor()
        sql = "INSERT INTO `clinic` (`Name`, `Address`, `Contact`, `Availability`) Values (%s, %s, %s, %s);"
        cursor.execute(sql, (name, address, contact, '0'))
        db.commit()
        db.close()
    except mysql.connector.Error as err:
        print(err)
        return 0
    return cursor.rowcount

def selectClinicById(clinicId):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `ClinicId`, `Name`, `Address`, `Contact`, `Availability` FROM `clinic` WHERE `ClinicId` = %s"
    cursor.execute(sql, [clinicId])
    result = cursor.fetchall()
    db.close()
    return result

def updateClinic(clinicid, name, address, contact):
    db = openDatabase()
    cursor = db.cursor()
    sql = "UPDATE `clinic` SET `Name` = %s, `Address` = %s, `Contact` = %s WHERE `ClinicId` = %s"
    cursor.execute(sql, (name, address, contact, clinicid))
    db.commit()
    db.close()
    return cursor.rowcount

def updateClinicAvailability(clinicid, availability):
    db = openDatabase()
    cursor = db.cursor()
    sql = "UPDATE `clinic` SET `Availability` = %s WHERE `ClinicId` = %s"
    cursor.execute(sql, (clinicid, availability))
    db.commit()
    db.close()
    return cursor.rowcount

def deleteClinic(clinicid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "DELETE FROM `clinic` WHERE `ClinicId` = %s"
    cursor.execute(sql, [clinicid])
    db.commit()
    db.close()
    return cursor.rowcount

def selectClinics():
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `ClinicId`, `Name`, `Address`, `Contact`, `Availability` FROM `clinic`"
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result


# Appointment Table
def insertAppointment(clinicid, username, serviceid, datetime, status):
    try:
        db = openDatabase()
        cursor = db.cursor()
        sql = "INSERT INTO `appointment` (`ClinicId`, `UserName`, `ServiceId`, `DateTime`, `Status`) Values (%s, %s, %s, %s, %s);"
        cursor.execute(sql, (clinicid, username, serviceid, datetime, status))
        db.commit()
        db.close()
    except mysql.connector.Error as err:
        print(err)
        return 0
    return cursor.rowcount

def selectCurrentAppointmentsByUser(username):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `AppointmentId`, `ClinicId`, `UserName`, `DateTime`, `Status`, `ServiceId` FROM `appointment` WHERE `UserName` = %s AND `DateTime` >= CURDATE() AND `Status` != 'C' AND `Status` != 'P'"
    cursor.execute(sql, [username])
    result = cursor.fetchall()
    db.close()
    return result

def updateAppointmentToPayment(appointmentid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "UPDATE `appointment` SET `Status` = 'P' WHERE `AppointmentId` = %s"
    cursor.execute(sql, [appointmentid])
    db.commit()
    db.close()
    return cursor.rowcount

def selectAppointmentsHistory(username):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `AppointmentId`, `ClinicId`, `UserName`, `DateTime`, `Status`, `ServiceId` FROM `appointment` WHERE `UserName` = %s AND (`DateTime` < CURDATE() OR `Status` = 'C' OR `Status` = 'P')"
    cursor.execute(sql, [username])
    result = cursor.fetchall()
    db.close()
    return result

def selectAppointments():
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `AppointmentId`, `ClinicId`, `UserName`, `DateTime`, `Status`, `ServiceId` FROM `appointment` WHERE `DateTime` >= CURDATE() AND `Status` != 'C'"
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result

def selectAppointmentServiceId(appointmentid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `ServiceId` FROM `appointment` WHERE `DateTime` >= CURDATE() AND `Status` != 'C' AND `AppointmentId` = %s"
    cursor.execute(sql, [appointmentid])
    result = cursor.fetchall()[0][0]
    db.close()
    return result

def updateAppointment(appointmentid, clinicid, username, status):
    db = openDatabase()
    cursor = db.cursor()
    sql = "UPDATE `appointment` SET `Status` = %s WHERE `AppointmentId` = %s AND `ClinicId` = %s AND `UserName` = %s"
    cursor.execute(sql, (status, appointmentid, clinicid, username))
    db.commit()
    db.close()
    return cursor.rowcount

def isClinicExists(clinicid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `ClinicId` FROM `clinic` WHERE `ClinicId` = %s"
    cursor.execute(sql, [clinicid])
    result = cursor.fetchall()
    db.close()
    return len(result)

def isAppointmentExists(appointmentid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `AppointmentId` FROM `appointment` WHERE `AppointmentId` = %s AND `DateTime` >= CURDATE() AND `Status` != 'C'"
    cursor.execute(sql, [appointmentid])
    result = cursor.fetchall()
    db.close()
    return len(result)

def isUserExists(username):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `UserName` FROM `user` WHERE `UserName` = %s"
    cursor.execute(sql, [username])
    result = cursor.fetchall()
    db.close()
    return len(result)


# Notification
def insertNotification(username, message, datetime):
    try:
        db = openDatabase()
        cursor = db.cursor()
        sql = "INSERT INTO `notification` (`UserName`, `Message`, `DateTime`) Values (%s, %s, %s);"
        cursor.execute(sql, (username, message, datetime))
        db.commit()
        db.close()
    except mysql.connector.Error as err:
        print(err)
        return 0
    return cursor.rowcount


# Service Table
def insertService(clinicid, name, price):
    try:
        db = openDatabase()
        cursor = db.cursor()
        sql = "INSERT INTO `service` (`ClinicId`, `Name`, `Price`) Values (%s, %s, %s);"
        cursor.execute(sql, (clinicid, name, price))
        db.commit()
        db.close()
    except mysql.connector.Error as err:
        print(err)
        return 0
    return cursor.rowcount

def updateService(serviceid, clinicid, name, price):
    db = openDatabase()
    cursor = db.cursor()
    sql = "UPDATE `service` SET `ClinicId` = %s, `Name` = %s, `Price` = %s WHERE `ServiceId` = %s"
    cursor.execute(sql, (clinicid, name, price, serviceid))
    db.commit()
    db.close()
    return cursor.rowcount

def deleteService(serviceid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "DELETE FROM `service` WHERE `ServiceId` = %s"
    cursor.execute(sql, [serviceid])
    db.commit()
    db.close()
    return cursor.rowcount

def selectServiceById(serviceid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `ServiceId`, `ClinicId`, `Name`, `Price` FROM `service` WHERE `ServiceId` = %s"
    cursor.execute(sql, [serviceid])
    result = cursor.fetchall()
    db.close()
    return result

def selectClinicServices(clinicid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `ServiceId`, `ClinicId`, `Name`, `Price` FROM `service` WHERE `ClinicId` = %s"
    cursor.execute(sql, [clinicid])
    result = cursor.fetchall()
    db.close()
    return result

def selectServicePrice(serviceid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `Price` FROM `service` WHERE `ServiceId` = %s"
    cursor.execute(sql, [serviceid])
    result = cursor.fetchall()[0][0]
    db.close()
    return result    

# Payment Table
def insertPayment(appointmentid, datetime, amount):
    try:
        db = openDatabase()
        cursor = db.cursor()
        sql = "INSERT INTO `payment` (`AppointmentId`, `DateTime`, `Amount`) Values (%s, %s, %s);"
        cursor.execute(sql, (appointmentid, datetime, amount))
        db.commit()
        db.close()
    except mysql.connector.Error as err:
        print(err)
        return 0
    return cursor.rowcount

def updatePayment(paymentid, appointmentid, datetime, amount):
    db = openDatabase()
    cursor = db.cursor()
    sql = "UPDATE `payment` SET `AppointmentId` = %s, `DateTime` = %s, `Amount` = %s WHERE `PaymentId` = %s"
    cursor.execute(sql, (appointmentid, datetime, amount, paymentid))
    db.commit()
    db.close()
    return cursor.rowcount

def deletePayment(paymentid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "DELETE FROM `payment` WHERE `PaymentId` = %s"
    cursor.execute(sql, [paymentid])
    db.commit()
    db.close()
    return cursor.rowcount

def selectPaymentByAppointmentId(appointmentid):
    db = openDatabase()
    cursor = db.cursor()
    sql = "SELECT `PaymentId`, `AppointmentId`, `DateTime`, `Amount` FROM `payment` WHERE `AppointmentId` = %s"
    cursor.execute(sql, [appointmentid])
    result = cursor.fetchall()
    db.close()
    return result
