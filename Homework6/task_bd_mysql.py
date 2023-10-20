import mysql.connector

# Подключение к базе данных
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Создание курсора для выполнения операций SQL
cursor = mydb.cursor()

# Создание таблицы Patient
cursor.execute(
    "CREATE TABLE Patient (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), phone VARCHAR(20), email VARCHAR(255), birthDate DATE)")

# Создание таблицы Doctor
cursor.execute(
    "CREATE TABLE Doctor (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), specialization VARCHAR(255), phone VARCHAR(20), email VARCHAR(255))")

# Создание таблицы Appointment
cursor.execute(
    "CREATE TABLE Appointment (id INT AUTO_INCREMENT PRIMARY KEY, date DATETIME, duration INT, patient_id INT, doctor_id INT, room_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id), FOREIGN KEY (doctor_id) REFERENCES Doctor(id), FOREIGN KEY (room_id) REFERENCES Room(id))")

# Создание таблицы Prescription
cursor.execute(
    "CREATE TABLE Prescription (id INT AUTO_INCREMENT PRIMARY KEY, medication VARCHAR(255), dosage VARCHAR(255), patient_id INT, doctor_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id), FOREIGN KEY (doctor_id) REFERENCES Doctor(id))")

# Создание таблицы MedicalRecord
cursor.execute(
    "CREATE TABLE MedicalRecord (id INT AUTO_INCREMENT PRIMARY KEY, symptoms VARCHAR(255), diagnosis VARCHAR(255), treatment VARCHAR(255), patient_id INT, doctor_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id), FOREIGN KEY (doctor_id) REFERENCES Doctor(id))")

# Создание таблицы Invoice
cursor.execute(
    "CREATE TABLE Invoice (id INT AUTO_INCREMENT PRIMARY KEY, amount DECIMAL(10,2), dueDate DATETIME, paid BOOLEAN, patient_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id))")

# Создание таблицы Therapy
cursor.execute(
    "CREATE TABLE Therapy (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), duration INT, medicalRecord_id INT, FOREIGN KEY (medicalRecord_id) REFERENCES MedicalRecord(id))")

# Создание таблицы Diagnosis
cursor.execute(
    "CREATE TABLE Diagnosis (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), medicalRecord_id INT, FOREIGN KEY (medicalRecord_id) REFERENCES MedicalRecord(id))")

# Создание таблицы Room
cursor.execute("CREATE TABLE Room (id INT AUTO_INCREMENT PRIMARY KEY, number VARCHAR(20), type VARCHAR(255))")

# Создание таблицы Service
cursor.execute(
    "CREATE TABLE Service (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), price DECIMAL(10,2), doctor_id INT, FOREIGN KEY (doctor_id) REFERENCES Doctor(id))")

# Применение изменений
mydb.commit()

# Закрытие соединения
mydb.close()
