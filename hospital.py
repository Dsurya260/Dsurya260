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
    """
    Abstract base class representing a person in the hospital system.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.

    Methods:
        is_valid_age(age): Validates if the age is a positive integer.
        get_details(): Abstract method to get details of the person.
    """
    def __init__(self, name, age):
        """
        Initializes a Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.

        Raises:
            InvalidAgeError: If the age is invalid.
        """
        if not self.is_valid_age(age):
            raise InvalidAgeError("Age must be a positive integer.")
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        """
        Checks if the provided age is a positive integer.

        Args:
            age (int): The age to check.

        Returns:
            bool: True if the age is valid, False otherwise.
        """
        return isinstance(age, int) and age > 0

    @abstractmethod
    def get_details(self):
        """Abstract method to get details of the person."""
        pass


class Doctor(Person):
    """
    Class representing a doctor in the hospital system, inheriting from Person.

    Attributes:
        doctor_id (int): The ID of the doctor.
        specialization (str): The specialization of the doctor.
        schedule (list): A list of appointments for the doctor.

    Methods:
        display_schedule(): Displays the doctor's schedule.
        get_details(): Returns a string with the doctor's details.
    """
    def __init__(self, doctor_id, name, age, specialization):
        """
        Initializes a Doctor object.

        Args:
            doctor_id (int): The unique ID of the doctor.
            name (str): The name of the doctor.
            age (int): The age of the doctor.
            specialization (str): The specialization of the doctor.
        """
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.schedule = []

    def display_schedule(self):
        """
        Displays the doctor's appointment schedule.
        Logs each scheduled appointment.
        """
        logging.info(f"Displaying schedule for Dr. {self.name}.")
        if not self.schedule:
            logging.info(f"No appointments scheduled for Dr. {self.name}.")
        else:
            for appointment in self.schedule:
                logging.info(f"  {appointment}")

    def get_details(self):
        """
        Returns a string with the doctor's details.

        Returns:
            str: A string representation of the doctor's details.
        """
        return f"Doctor[ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}]"

    def __str__(self):
        """Returns the string representation of the doctor's details."""
        return self.get_details()


class Patient(Person):
    """
    Class representing a patient in the hospital system, inheriting from Person.

    Attributes:
        patient_id (int): The ID of the patient.
        ailment (str): The ailment or illness the patient is suffering from.

    Methods:
        get_details(): Returns a string with the patient's details.
    """
    def __init__(self, patient_id, name, age, ailment):
        """
        Initializes a Patient object.

        Args:
            patient_id (int): The unique ID of the patient.
            name (str): The name of the patient.
            age (int): The age of the patient.
            ailment (str): The ailment the patient is suffering from.
        """
        super().__init__(name, age)
        self.patient_id = patient_id
        self.ailment = ailment

    def get_details(self):
        """
        Returns a string with the patient's details.

        Returns:
            str: A string representation of the patient's details.
        """
        return f"Patient[ID: {self.patient_id}, Name: {self.name}, Ailment: {self.ailment}]"

    def __str__(self):
        """Returns the string representation of the patient's details."""
        return self.get_details()


class Appointment:
    """
    Class representing an appointment between a doctor and a patient.

    Attributes:
        appointment_id (int): The unique ID of the appointment.
        patient (Patient): The patient for the appointment.
        doctor (Doctor): The doctor for the appointment.
        date_time (datetime): The date and time of the appointment.

    Methods:
        __str__(): Returns a string representation of the appointment.
    """
    def __init__(self, appointment_id, patient, doctor, date_time):
        """
        Initializes an Appointment object.

        Args:
            appointment_id (int): The unique ID of the appointment.
            patient (Patient): The patient for the appointment.
            doctor (Doctor): The doctor for the appointment.
            date_time (datetime): The date and time of the appointment.
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        """Returns a string representation of the appointment."""
        return f"Appointment[ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Time: {self.date_time}]"


class Hospital:
    """
    Class representing a hospital that manages doctors, patients, and appointments.

    Attributes:
        name (str): The name of the hospital.
        doctors (dict): A dictionary of doctors indexed by their doctor_id.
        patients (dict): A dictionary of patients indexed by their patient_id.
        appointments (dict): A dictionary of appointments indexed by appointment_id.

    Methods:
        add_doctor(doctor): Adds a doctor to the hospital.
        add_patient(patient): Adds a patient to the hospital.
        book_appointment(appointment_id, patient_id, doctor_id, date_time): Books an appointment for a patient with a doctor.
        display_patients(): Displays all registered patients.
        display_doctors(): Displays all registered doctors.
        display_appointments(): Displays all scheduled appointments.
    """
    def __init__(self, name):
        """
        Initializes a Hospital object.

        Args:
            name (str): The name of the hospital.
        """
        self.name = name
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def add_doctor(self, doctor):
        """
        Adds a doctor to the hospital.

        Args:
            doctor (Doctor): The doctor to add to the hospital.

        Raises:
            ValueError: If the doctor is already registered.
        """
        if doctor.doctor_id not in self.doctors:
            self.doctors[doctor.doctor_id] = doctor
            logging.info(f"Added Doctor: {doctor.name} ({doctor.specialization}).")
        else:
            logging.error(f"Doctor {doctor.name} is already registered.")
            raise ValueError(f"Doctor {doctor.name} is already registered.")

    def add_patient(self, patient):
        """
        Adds a patient to the hospital.

        Args:
            patient (Patient): The patient to add to the hospital.

        Raises:
            ValueError: If the patient is already registered.
        """
        if patient.patient_id not in self.patients:
            self.patients[patient.patient_id] = patient
            logging.info(f"Added Patient: {patient.name} (Ailment: {patient.ailment}).")
        else:
            logging.error(f"Patient {patient.name} is already registered.")
            raise ValueError(f"Patient {patient.name} is already registered.")

    def book_appointment(self, appointment_id, patient_id, doctor_id, date_time):
        """
        Books an appointment for a patient with a doctor.

        Args:
            appointment_id (int): The unique ID of the appointment.
            patient_id (int): The ID of the patient.
            doctor_id (int): The ID of the doctor.
            date_time (datetime): The date and time of the appointment.

        Raises:
            ValueError: If the doctor or patient is not found.
        """
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
        """Displays all registered patients in the hospital."""
        logging.info("Displaying all patients in the hospital.")
        for patient in self.patients.values():
            logging.info(patient)

    def display_doctors(self):
        """Displays all registered doctors in the hospital."""
        logging.info("Displaying all doctors in the hospital.")
        for doctor in self.doctors.values():
            logging.info(doctor)

    def display_appointments(self):
        """Displays all scheduled appointments in the hospital."""
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
