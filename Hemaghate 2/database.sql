CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Clinic (
    id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT
);

CREATE TABLE Service (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    clinic_id INTEGER,
    FOREIGN KEY(clinic_id) REFERENCES Clinic(id) ON DELETE CASCADE
);

CREATE TABLE Appointment (
    id INTEGER PRIMARY KEY,
    date TEXT,
    time TEXT,
    user_id INTEGER,
    clinic_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY(clinic_id) REFERENCES Clinic(id) ON DELETE CASCADE
);

CREATE TABLE Payment (
    id INTEGER PRIMARY KEY,
    amount REAL,
    user_id INTEGER,
    appointment_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY(appointment_id) REFERENCES Appointment(id)
);

CREATE TABLE Notification (
    id INTEGER PRIMARY KEY,
    message TEXT,
    user_id INTEGER,
    appointment_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(id),
    FOREIGN KEY(appointment_id) REFERENCES Appointment(id) ON DELETE CASCADE
);
