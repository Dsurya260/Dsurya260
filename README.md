Hospital Management System: Simplifying Hospital Operations with Python

The Hospital Management System is a Python-based application designed
to streamline the daily operations of a hospital. This system focuses
on key aspects such as managing patients, doctors, and appointments,
making hospital administration more efficient.

Abstract Base Class Person:
Purpose: Person is an abstract base class, meaning it defines common attributes (name and age) and forces any subclass to implement the get_details() method.

Abstract Method (get_details): This method must be implemented by any subclass, ensuring that each subclass provides its own version of how to display the details of a person.

Doctor Class:
The Doctor class inherits from Person and represents a doctor. Displays the doctor's schedule (appointments), or indicates that no appointments are scheduled. Returns a string with the doctor's details (ID, name, and specialization).

Patient Class:
The Patient class, also inheriting from Person, represents a patient. Besides name and age, a patient has an ID and an ailment (condition). Returns a string with the patient's details (ID, name, and ailment).

Appointment Class:
Represents an appointment between a doctor and a patient. An appointment has a unique ID, references to the patient and doctor objects, and a date/time

Hospital Class
The Hospital class manages doctors, patients, and appointments.  Initializes the hospital with a name and empty dictionaries for doctors, patients, and appointments. 
Method add_doctor(): Adds a doctor to the hospital if not already registered.
Method add_patient(): Adds a patient to the hospital if not already registered.
Method book_appointment(): Books an appointment by verifying the existence of the doctor and patient, creating an Appointment object, and adding it to the doctor's schedule.
Method display_patients(): Displays all patients in the hospital.
Method display_doctors(): Displays all doctors in the hospital.
Method display_appointments(): Displays all appointments in the hospital.

Main Program:
Creates a hospital object.
Adds doctors and patients.
Books appointments for patients with doctors.
Displays details of patients, doctors, and appointments.
Shows each doctor's schedule.