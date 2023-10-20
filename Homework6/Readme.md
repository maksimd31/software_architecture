Архитектура ПО (семинары)
Урок 6. Принципы построения приложений «чистая архитектура»
Разработать полную ERD домена в https://www.dbdesigner.net/.
Как вы понимаете гексагональную архитектуру
Я не понимаю вашу фурмолировку домашнего задания! 
В 6 домашнем задание нужно делать ERD про поликлинику ? Или про домен ? Или про домен к поликлинике ? Или про домен создания доменов? Решил сделать про поликлинику, посколько не понял что требуется в домашней работе!

## Убедительная просьба на странице с д/з формулируйте более развернуто задание, а то приходится гадать что нужно сделать. Какая цель домашнего задания какие инструменты использовать и тд.. очень прошу четко формулировать ТЗ 

Высылаю ссылку на готовую ERD диаграмму в https://www.dbdesigner.net/

## [ссылка](https://dbdesigner.page.link/FA5r1TfpUPyy3C7bA) 

![Снимок экрана 2023-10-20 в 16.38.03.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2F1d%2F7byy1tjj5p36r6btnpzyg4s80000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_4xbqbz%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-10-20%20%D0%B2%2016.38.03.png)

## код markup
```mysql-sql

patient {
	id int pk increments
	name varchar(255)
	address varchar(255)
	phone varchar(20)
	email varchar(255)
	birthdate date
}

doctor {
	id int pk increments
	name varchar(255)
	specialization varchar(255)
	phone varchar(20)
	email varchar(255)
}

appointment {
	id int pk increments
	date datetime
	duration int
	patient_id int > patient.id
	doctor_id int > doctor.id
	room_id int > room.id
}

prescription {
	id int pk increments
	medication varchar(255)
	dosage varchar(255)
	patient_id int > patient.id
	doctor_id int
}

medicalrecord {
	id int pk increments
	symptoms varchar(255)
	diagnosis varchar(255)
	treatment varchar(255)
	patient_id int > patient.id
	doctor_id int
}

invoice {
	id int pk increments
	amount decimal(10,2)
	duedate datetime
	paid boolean
	patient_id int > patient.id
}

therapy {
	id int pk increments
	name varchar(255)
	description varchar(255)
	duration int
	medicalrecord_id int > medicalrecord.id
}

diagnosis {
	id int pk increments
	name varchar(255)
	description varchar(255)
	medicalrecord_id int > medicalrecord.id
}

room {
	id int pk increments
	number varchar(20)
	type varchar(255)
}

service {
	id int pk increments
	name varchar(255)
	description varchar(255)
	price decimal(10,2)
	doctor_id int > doctor.id
}


```
## код mysql
```mysql-sql
CREATE TABLE Patient (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255),
  phone VARCHAR(20),
  email VARCHAR(255),
  birthDate DATE
);

CREATE TABLE Doctor (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  specialization VARCHAR(255),
  phone VARCHAR(20),
  email VARCHAR(255)
);

CREATE TABLE Appointment (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date DATETIME,
  duration INT,
  patient_id INT,
  doctor_id INT,
  room_id INT,
  FOREIGN KEY (patient_id) REFERENCES Patient(id),
  FOREIGN KEY (doctor_id) REFERENCES Doctor(id),
  FOREIGN KEY (room_id) REFERENCES Room(id)
);

CREATE TABLE Prescription (
  id INT AUTO_INCREMENT PRIMARY KEY,
  medication VARCHAR(255),
  dosage VARCHAR(255),
  patient_id INT,
  doctor_id INT,
  FOREIGN KEY (patient_id) REFERENCES Patient(id),
  FOREIGN KEY (doctor_id) REFERENCES Doctor(id)
);

CREATE TABLE MedicalRecord (
  id INT AUTO_INCREMENT PRIMARY KEY,
  symptoms VARCHAR(255),
  diagnosis VARCHAR(255),
  treatment VARCHAR(255),
  patient_id INT,
  doctor_id INT,
  FOREIGN KEY (patient_id) REFERENCES Patient(id),
  FOREIGN KEY (doctor_id) REFERENCES Doctor(id)
);

CREATE TABLE Invoice (
  id INT AUTO_INCREMENT PRIMARY KEY,
  amount DECIMAL(10,2),
  dueDate DATETIME,
  paid BOOLEAN,
  patient_id INT,
  FOREIGN KEY (patient_id) REFERENCES Patient(id)
);

CREATE TABLE Therapy (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  duration INT,
  medicalRecord_id INT,
  FOREIGN KEY (medicalRecord_id) REFERENCES MedicalRecord(id)
);

CREATE TABLE Diagnosis (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  medicalRecord_id INT,
  FOREIGN KEY (medicalRecord_id) REFERENCES MedicalRecord(id)
);

CREATE TABLE Room (
  id INT AUTO_INCREMENT PRIMARY KEY,
  number VARCHAR(20),
  type VARCHAR(255)
);

CREATE TABLE Service (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  price DECIMAL(10,2),
  doctor_id INT,
  FOREIGN KEY (doctor_id) REFERENCES Doctor(id)
);

ALTER TABLE Appointment ADD FOREIGN KEY (patient_id) REFERENCES Patient(id);
ALTER TABLE Appointment ADD FOREIGN KEY (doctor_id) REFERENCES Doctor(id);
ALTER TABLE Appointment ADD FOREIGN KEY (room_id) REFERENCES Room(id);
ALTER TABLE Service ADD FOREIGN KEY (doctor_id) REFERENCES Doctor(id);
```

## код на python 

```python
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
cursor.execute("CREATE TABLE Patient (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), phone VARCHAR(20), email VARCHAR(255), birthDate DATE)")

# Создание таблицы Doctor
cursor.execute("CREATE TABLE Doctor (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), specialization VARCHAR(255), phone VARCHAR(20), email VARCHAR(255))")

# Создание таблицы Appointment
cursor.execute("CREATE TABLE Appointment (id INT AUTO_INCREMENT PRIMARY KEY, date DATETIME, duration INT, patient_id INT, doctor_id INT, room_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id), FOREIGN KEY (doctor_id) REFERENCES Doctor(id), FOREIGN KEY (room_id) REFERENCES Room(id))")

# Создание таблицы Prescription
cursor.execute("CREATE TABLE Prescription (id INT AUTO_INCREMENT PRIMARY KEY, medication VARCHAR(255), dosage VARCHAR(255), patient_id INT, doctor_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id), FOREIGN KEY (doctor_id) REFERENCES Doctor(id))")

# Создание таблицы MedicalRecord
cursor.execute("CREATE TABLE MedicalRecord (id INT AUTO_INCREMENT PRIMARY KEY, symptoms VARCHAR(255), diagnosis VARCHAR(255), treatment VARCHAR(255), patient_id INT, doctor_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id), FOREIGN KEY (doctor_id) REFERENCES Doctor(id))")

# Создание таблицы Invoice
cursor.execute("CREATE TABLE Invoice (id INT AUTO_INCREMENT PRIMARY KEY, amount DECIMAL(10,2), dueDate DATETIME, paid BOOLEAN, patient_id INT, FOREIGN KEY (patient_id) REFERENCES Patient(id))")

# Создание таблицы Therapy
cursor.execute("CREATE TABLE Therapy (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), duration INT, medicalRecord_id INT, FOREIGN KEY (medicalRecord_id) REFERENCES MedicalRecord(id))")

# Создание таблицы Diagnosis
cursor.execute("CREATE TABLE Diagnosis (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), medicalRecord_id INT, FOREIGN KEY (medicalRecord_id) REFERENCES MedicalRecord(id))")

# Создание таблицы Room
cursor.execute("CREATE TABLE Room (id INT AUTO_INCREMENT PRIMARY KEY, number VARCHAR(20), type VARCHAR(255))")

# Создание таблицы Service
cursor.execute("CREATE TABLE Service (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), price DECIMAL(10,2), doctor_id INT, FOREIGN KEY (doctor_id) REFERENCES Doctor(id))")

# Применение изменений
mydb.commit()

# Закрытие соединения
mydb.close()

```
## Как вы понимаете гексагональную архитектуру

В гексагональной архитектуре основное внимание уделяется двум аспектам:
1. Внешним интерфейсам: Гексагональная архитектура рассматривает внешние интерфейсы как "входные" и "выходные" точки системы. Входные точки представляются в области, где приложение принимает внешние входные данные, а выходные точки представляют область, где приложение генерирует выходные данные для внешних систем или пользователей.
2. Бизнес-логике: Бизнес-логика представлена внутренними компонентами системы, которые обрабатывают входные данные из внешних интерфейсов и выполняют операции в соответствии с бизнес-правилами и логикой приложения.
Гексагональная архитектура включает различные слои: внешний слой (где находятся внешние интерфейсы), внутренний слой (где расположена бизнес-логика), а также слой хранения данных, слой инфраструктуры и т. д. Она также поддерживает принципы чистой архитектуры (clean architecture), такие как разделение концепций, инверсия зависимостей и тестируемость.