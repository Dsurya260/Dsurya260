import logging
from abc import ABC, abstractmethod
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("hospital_management.log"),
        logging.StreamHandler()
    ]
)

# Custom Exception for Invalid Age
class InvalidAgeError(Exception):
    """Raised when an invalid age is provided."""
    pass


# Abstract Base Class
class Person(ABC):
    def __init__(self, name, age):
        if not self.is_valid_age(age):
            raise InvalidAgeError("Age must be a positive integer.")
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and age > 0

    @abstractmethod
    def get_details(self):
        pass


class Doctor(Person):
    def __init__(self, doctor_id, name, age, specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.schedule = []

    def display_schedule(self):
        logging.info(f"Displaying schedule for Dr. {self.name}.")
        if not self.schedule:
            logging.info(f"No appointments scheduled for Dr. {self.name}.")
        else:
            for appointment in self.schedule:
                logging.info(f"  {appointment}")

    def get_details(self):
        return f"Doctor[ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}]"

    def __str__(self):
        return self.get_details()


class Patient(Person):
    def __init__(self, patient_id, name, age, ailment):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.ailment = ailment

    def get_details(self):
        return f"Patient[ID: {self.patient_id}, Name: {self.name}, Ailment: {self.ailment}]"

    def __str__(self):
        return self.get_details()


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        return f"Appointment[ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Time: {self.date_time}]"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def add_doctor(self, doctor):
        if doctor.doctor_id not in self.doctors:
            self.doctors[doctor.doctor_id] = doctor
            logging.info(f"Added Doctor: {doctor.name} ({doctor.specialization}).")
        else:
            logging.error(f"Doctor {doctor.name} is already registered.")
            raise ValueError(f"Doctor {doctor.name} is already registered.")

    def add_patient(self, patient):
        if patient.patient_id not in self.patients:
            self.patients[patient.patient_id] = patient
            logging.info(f"Added Patient: {patient.name} (Ailment: {patient.ailment}).")
        else:
            logging.error(f"Patient {patient.name} is already registered.")
            raise ValueError(f"Patient {patient.name} is already registered.")

    def book_appointment(self, appointment_id, patient_id, doctor_id, date_time):
        if doctor_id not in self.doctors:
            logging.error("Doctor not found.")
            raise ValueError("Doctor not found.")
        if patient_id not in self.patients:
            logging.error("Patient not found.")
            raise ValueError("Patient not found.")
        
        doctor = self.doctors[doctor_id]
        patient = self.patients[patient_id]
        appointment = Appointment(appointment_id, patient, doctor, date_time)

        self.appointments[appointment_id] = appointment
        doctor.schedule.append(appointment)

        logging.info(f"Appointment booked: {appointment}")

    def display_patients(self):
        logging.info("Displaying all patients in the hospital.")
        for patient in self.patients.values():
            logging.info(patient)

    def display_doctors(self):
        logging.info("Displaying all doctors in the hospital.")
        for doctor in self.doctors.values():
            logging.info(doctor)

    def display_appointments(self):
        logging.info("Displaying all appointments in the hospital.")
        if not self.appointments:
            logging.info("No appointments scheduled.")
        else:
            for appointment in self.appointments.values():
                logging.info(appointment)

    def __str__(self):
        return f"Hospital[{self.name}]: {len(self.doctors)} doctors, {len(self.patients)} patients."


# Main Program
if __name__ == "__main__":
    hospital = Hospital("City Hospital")

    try:
        # Add Doctors
        doctor1 = Doctor(1, "Dr. Doctor1", 45, "Cardiology")
        doctor2 = Doctor(2, "Dr. Doctor2", 50, "Neurology")
        hospital.add_doctor(doctor1)
        hospital.add_doctor(doctor2)

        # Add Patients
        patient1 = Patient(101, "Patient_y", 30, "Chest Pain")
        patient2 = Patient(102, "Patient_z", 45, "Headache")
        hospital.add_patient(patient1)
        hospital.add_patient(patient2)

        # Book Appointments
        hospital.book_appointment(1, 101, 1, datetime(2024, 11, 26, 10, 0))
        hospital.book_appointment(2, 102, 2, datetime(2024, 11, 26, 14, 0))

        # Display Information
        hospital.display_doctors()
        hospital.display_patients()
        hospital.display_appointments()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
