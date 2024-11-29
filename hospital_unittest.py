import logging
from abc import ABC, abstractmethod
from datetime import datetime
import unittest

# Configure logging to display logs on the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidAgeError(Exception):
    """Custom exception to handle invalid age."""
    pass

class Person(ABC):
    """Abstract class representing a person."""
    def __init__(self, name, age):
        self.name = name
        if not self.is_valid_age(age):
            raise InvalidAgeError(f"Invalid age for {name}. Age must be a positive integer.")
        self.age = age
    
    @abstractmethod
    def get_details(self):
        """Abstract method to get details of the person."""
        pass

    @staticmethod
    def is_valid_age(age):
        """Static method to validate age."""
        return isinstance(age, int) and age > 0

class Doctor(Person):
    """Class representing a Doctor, inheriting from Person."""
    def __init__(self, doctor_id, name, age, specialty):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialty = specialty

    def get_details(self):
        """Return a string representation of the doctor's details."""
        return f"Doctor[ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}]"

class Patient(Person):
    """Class representing a Patient, inheriting from Person."""
    def __init__(self, patient_id, name, age, condition):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.condition = condition

    def get_details(self):
        """Return a string representation of the patient's details."""
        return f"Patient[ID: {self.patient_id}, Name: {self.name}, Condition: {self.condition}]"

class Appointment:
    """Class representing an appointment between a doctor and a patient."""
    def __init__(self, appointment_id, doctor, patient, date_time):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time

    def __str__(self):
        """Return a string representation of the appointment."""
        return f"Appointment[ID: {self.appointment_id}, Doctor: {self.doctor.name}, Patient: {self.patient.name}, DateTime: {self.date_time}]"

class Hospital:
    """Class to manage the hospital system."""
    def __init__(self, name):
        self.name = name
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def add_doctor(self, doctor):
        """Add a doctor to the hospital."""
        if doctor.doctor_id in self.doctors:
            logging.warning(f"Doctor with ID {doctor.doctor_id} already exists.")
            return
        self.doctors[doctor.doctor_id] = doctor
        logging.info(f"Added Doctor: {doctor.name} ({doctor.specialty}).")

    def add_patient(self, patient):
        """Add a patient to the hospital."""
        if patient.patient_id in self.patients:
            logging.warning(f"Patient with ID {patient.patient_id} already exists.")
            return
        self.patients[patient.patient_id] = patient
        logging.info(f"Added Patient: {patient.name} (Condition: {patient.condition}).")

    def book_appointment(self, appointment_id, doctor_id, patient_id, date_time):
        """Book an appointment for a patient with a doctor."""
        doctor = self.doctors.get(doctor_id)
        patient = self.patients.get(patient_id)

        if not doctor or not patient:
            logging.error("Error: Doctor or Patient not found.")
            return

        appointment = Appointment(appointment_id, doctor, patient, date_time)
        self.appointments[appointment_id] = appointment
        logging.info(f"Booked Appointment: {appointment}")

    def display_doctors(self):
        """Display all doctors in the hospital."""
        logging.info("Displaying all doctors in the hospital.")
        for doctor in self.doctors.values():
            print(doctor.get_details())
    
    def display_patients(self):
        """Display all patients in the hospital."""
        logging.info("Displaying all patients in the hospital.")
        for patient in self.patients.values():
            print(patient.get_details())
    
    def display_appointments(self):
        """Display all appointments in the hospital."""
        logging.info("Displaying all appointments in the hospital.")
        for appointment in self.appointments.values():
            print(appointment)

# Unit tests for the hospital system



class TestHospitalSystem(unittest.TestCase):

    def test_valid_age(self):
        """Test static method for valid age check."""
        self.assertTrue(Person.is_valid_age(25))
        self.assertFalse(Person.is_valid_age(-3))
        self.assertFalse(Person.is_valid_age("30"))

    def test_invalid_age_error(self):
        """Test the invalid age exception."""
        with self.assertRaises(InvalidAgeError):
            doctor = Doctor(1, "patient_1", -5, "Cardiology")

    def test_doctor_creation(self):
        """Test the creation of a doctor."""
        doctor = Doctor(1, "Dr. Doctor1", 40, "Cardiology")
        self.assertEqual(doctor.get_details(), "Doctor[ID: 1, Name: Dr. Doctor1, Specialty: Cardiology]")

    def test_patient_creation(self):
        """Test the creation of a patient."""
        patient = Patient(101, "Patient_1", 30, "Flu")
        self.assertEqual(patient.get_details(), "Patient[ID: 101, Name: Patient_1, Condition: Flu]")

    def test_appointment_booking(self):
        """Test the booking of an appointment."""
        hospital = Hospital("City Hospital")
        doctor = Doctor(1, "Dr. Doctor_1", 40, "Cardiology")
        patient = Patient(101, "Patient_1", 30, "Flu")
        hospital.add_doctor(doctor)
        hospital.add_patient(patient)

        appointment_time = datetime(2024, 11, 30, 9, 0)
        hospital.book_appointment(1, 1, 101, appointment_time)

        self.assertEqual(len(hospital.appointments), 1)
        self.assertEqual(hospital.appointments[1].doctor.name, "Dr. Doctor_1")
        self.assertEqual(hospital.appointments[1].patient.name, "Patient_1")
        self.assertEqual(hospital.appointments[1].date_time, appointment_time)

    def test_duplicate_doctor(self):
        """Test error handling when adding a duplicate doctor."""
        hospital = Hospital("City Hospital")
        doctor = Doctor(1, "Dr. Dcotor_1", 40, "Cardiology")
        hospital.add_doctor(doctor)
        hospital.add_doctor(doctor)  

    def test_duplicate_patient(self):
        """Test error handling when adding a duplicate patient."""
        hospital = Hospital("City Hospital")
        patient = Patient(101, "Patient_1", 30, "Flu")
        hospital.add_patient(patient)
        hospital.add_patient(patient) 

if __name__ == "__main__":
    unittest.main()
