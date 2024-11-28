from abc import ABC, abstractmethod
from datetime import datetime


# Custom Exception for Invalid Age
class InvalidAgeError(Exception):
    """Raised when an invalid age is provided."""
    pass


# Abstract Base Class
class Person(ABC):
    """
    Abstract base class representing a person.
    Provides common attributes like name and age for its subclasses.
    """
    def __init__(self, name, age):
        """
        Initializes a person with a name and age.
        
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        
        Raises:
            InvalidAgeError: If the provided age is invalid (non-positive integer).
        """
        if not self.is_valid_age(age):
            raise InvalidAgeError("Age must be a positive integer.")
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        """
        Validates the age to ensure it's a positive integer.
        
        Args:
            age (int): The age to validate.
        
        Returns:
            bool: True if the age is valid, False otherwise.
        """
        return isinstance(age, int) and age > 0

    @abstractmethod
    def get_details(self):
        """
        Abstract method to get details of the person.
        Must be implemented by subclasses.
        """
        pass


# Doctor Class inheriting from Person
class Doctor(Person):
    """
    Class representing a Doctor, inheriting from Person.
    Includes details such as doctor ID, specialization, and schedule.
    """
    def __init__(self, doctor_id, name, age, specialization):
        """
        Initializes a doctor with an ID, name, age, and specialization.
        
        Args:
            doctor_id (int): The doctor's unique ID.
            name (str): The doctor's name.
            age (int): The doctor's age.
            specialization (str): The doctor's area of specialization.
        
        Raises:
            InvalidAgeError: If the provided age is invalid.
        """
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.schedule = []

    def display_schedule(self):
        """
        Displays the doctor's schedule.
        """
        print(f"Schedule for Dr. {self.name} ({self.specialization}):")
        if not self.schedule:
            print("  No appointments scheduled.")
        else:
            for appointment in self.schedule:
                print(f"  {appointment}")

    def get_details(self):
        """
        Returns a string containing details about the doctor.
        
        Returns:
            str: A string with doctor details.
        """
        return f"Doctor[ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}]"

    def __str__(self):
        """
        Returns a string representation of the doctor's details.
        
        Returns:
            str: A string with doctor details.
        """
        return self.get_details()


# Patient Class inheriting from Person
class Patient(Person):
    """
    Class representing a Patient, inheriting from Person.
    Includes details such as patient ID and ailment.
    """
    def __init__(self, patient_id, name, age, ailment):
        """
        Initializes a patient with an ID, name, age, and ailment.
        
        Args:
            patient_id (int): The patient's unique ID.
            name (str): The patient's name.
            age (int): The patient's age.
            ailment (str): The patient's ailment.
        
        Raises:
            InvalidAgeError: If the provided age is invalid.
        """
        super().__init__(name, age)
        self.patient_id = patient_id
        self.ailment = ailment

    def get_details(self):
        """
        Returns a string containing details about the patient.
        
        Returns:
            str: A string with patient details.
        """
        return f"Patient[ID: {self.patient_id}, Name: {self.name}, Ailment: {self.ailment}]"

    def __str__(self):
        """
        Returns a string representation of the patient's details.
        
        Returns:
            str: A string with patient details.
        """
        return self.get_details()


# Appointment Class
class Appointment:
    """
    Class representing an Appointment.
    Includes details such as appointment ID, patient, doctor, and date/time.
    """
    def __init__(self, appointment_id, patient, doctor, date_time):
        """
        Initializes an appointment with an ID, patient, doctor, and date/time.
        
        Args:
            appointment_id (int): The appointment's unique ID.
            patient (Patient): The patient associated with the appointment.
            doctor (Doctor): The doctor associated with the appointment.
            date_time (datetime): The scheduled date and time of the appointment.
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        """
        Returns a string representation of the appointment details.
        
        Returns:
            str: A string with appointment details.
        """
        return f"Appointment[ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Time: {self.date_time}]"


# Hospital Class
class Hospital:
    """
    Class representing a Hospital, managing doctors, patients, and appointments.
    """
    def __init__(self, name):
        """
        Initializes a hospital with a name and empty records for doctors, patients, and appointments.
        
        Args:
            name (str): The name of the hospital.
        """
        self.name = name
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def add_doctor(self, doctor):
        """
        Adds a doctor to the hospital's records.
        
        Args:
            doctor (Doctor): The doctor to add.
        
        Raises:
            ValueError: If the doctor is already registered.
        """
        if doctor.doctor_id not in self.doctors:
            self.doctors[doctor.doctor_id] = doctor
            print(f"Added Doctor: {doctor.name} ({doctor.specialization}).")
        else:
            raise ValueError(f"Doctor {doctor.name} is already registered.")

    def add_patient(self, patient):
        """
        Adds a patient to the hospital's records.
        
        Args:
            patient (Patient): The patient to add.
        
        Raises:
            ValueError: If the patient is already registered.
        """
        if patient.patient_id not in self.patients:
            self.patients[patient.patient_id] = patient
            print(f"Added Patient: {patient.name} (Ailment: {patient.ailment}).")
        else:
            raise ValueError(f"Patient {patient.name} is already registered.")

    def book_appointment(self, appointment_id, patient_id, doctor_id, date_time):
        """
        Books an appointment for a patient with a doctor at a specified date and time.
        
        Args:
            appointment_id (int): The unique ID for the appointment.
            patient_id (int): The ID of the patient.
            doctor_id (int): The ID of the doctor.
            date_time (datetime): The date and time of the appointment.
        
        Raises:
            ValueError: If the doctor or patient is not found.
        """
        if doctor_id not in self.doctors:
            raise ValueError("Doctor not found.")
        
        if patient_id not in self.patients:
            raise ValueError("Patient not found.")
        
        doctor = self.doctors[doctor_id]
        patient = self.patients[patient_id]
        appointment = Appointment(appointment_id, patient, doctor, date_time)

        self.appointments[appointment_id] = appointment
        doctor.schedule.append(appointment)  # Direct access to `schedule`

        print(f"Appointment booked: {appointment}")

    def display_patients(self):
        """Displays all patients in the hospital."""
        print("\nPatients in the hospital:")
        for patient in self.patients.values():
            print(patient)

    def display_doctors(self):
        """Displays all doctors in the hospital."""
        print("\nDoctors in the hospital:")
        for doctor in self.doctors.values():
            print(doctor)

    def display_appointments(self):
        """Displays all appointments in the hospital."""
        print("\nAppointments in the hospital:")
        if not self.appointments:
            print("  No appointments scheduled.")
        else:
            for appointment in self.appointments.values():
                print(appointment)

    def __str__(self):
        """
        Returns a string representation of the hospital's details.
        
        Returns:
            str: A string with hospital details.
        """
        return f"Hospital[{self.name}]: {len(self.doctors)} doctors, {len(self.patients)} patients."


# Main Program
if __name__ == "__main__":
    # Create Hospital
    hospital = Hospital("City Hospital")

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
    hospital.book_appointment(1, 101, 1, datetime(2024, 11, 26, 10, 0))  # Patient1 with Doctor1 at 10:00 AM
    hospital.book_appointment(2, 102, 2, datetime(2024, 11, 26, 14, 0))  # Patient2 with Doctor2 at 2:00 PM

    # Display Information
    hospital.display_doctors()
    hospital.display_patients()
    hospital.display_appointments()
