from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Base Class
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_details(self):
        pass


# Doctor Class inheriting from Person
class Doctor(Person):
    def __init__(self, doctor_id, name, age, specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.schedule = []  # Public schedule (no encapsulation)

    def display_schedule(self):
        print(f"Schedule for Dr. {self.name} ({self.specialization}):")
        if not self.schedule:
            print("  No appointments scheduled.")
        else:
            for appointment in self.schedule:
                print(f"  {appointment}")

    def get_details(self):
        return f"Doctor[ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}]"

    def __str__(self):
        return self.get_details()


# Patient Class inheriting from Person
class Patient(Person):
    def __init__(self, patient_id, name, age, ailment):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.ailment = ailment

    def get_details(self):
        return f"Patient[ID: {self.patient_id}, Name: {self.name}, Ailment: {self.ailment}]"

    def __str__(self):
        return self.get_details()


# Appointment Class
class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        return f"Appointment[ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Time: {self.date_time}]" 


# Hospital Class
class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def add_doctor(self, doctor):
        if doctor.doctor_id not in self.doctors:
            self.doctors[doctor.doctor_id] = doctor
            print(f"Added Doctor: {doctor.name} ({doctor.specialization}).")
        else:
            print(f"Doctor {doctor.name} is already registered.")

    def add_patient(self, patient):
        if patient.patient_id not in self.patients:
            self.patients[patient.patient_id] = patient
            print(f"Added Patient: {patient.name} (Ailment: {patient.ailment}).")
        else:
            print(f"Patient {patient.name} is already registered.")

    def book_appointment(self, appointment_id, patient_id, doctor_id, date_time):
        if doctor_id not in self.doctors:
            print("Doctor not found.")
            return

        if patient_id not in self.patients:
            print("Patient not found.")
            return

        doctor = self.doctors[doctor_id]
        patient = self.patients[patient_id]
        appointment = Appointment(appointment_id, patient, doctor, date_time)

        self.appointments[appointment_id] = appointment
        doctor.schedule.append(appointment)  # Direct access to `schedule`

        print(f"Appointment booked: {appointment}")

    def display_patients(self):
        print("\nPatients in the hospital:")
        for patient in self.patients.values():
            print(patient)

    def display_doctors(self):
        print("\nDoctors in the hospital:")
        for doctor in self.doctors.values():
            print(doctor)

    def display_appointments(self):
        print("\nAppointments in the hospital:")
        if not self.appointments:
            print("  No appointments scheduled.")
        else:
            for appointment in self.appointments.values():
                print(appointment)

    def __str__(self):
        return f"Hospital[{self.name}]: {len(self.doctors)} doctors, {len(self.patients)} patients."


# Main Program
if __name__ == "__main__":
    # Create Hospital
    hospital = Hospital("City Hospital")

    # Add Doctors
    doctor1 = Doctor(1, "Dr. Smith", 45, "Cardiology")
    doctor2 = Doctor(2, "Dr. Johnson", 50, "Neurology")
    

    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    

    # Add Patients
    patient1 = Patient(101, "Alice", 30, "Chest Pain")
    patient2 = Patient(102, "Bob", 45, "Headache")
    

    hospital.add_patient(patient1)
    hospital.add_patient(patient2)
    
    # Book Appointments
    hospital.book_appointment(1, 101, 1, datetime(2024, 11, 23, 10, 0))
    hospital.book_appointment(2, 102, 2, datetime(2024, 11, 23, 11, 0))
    

    # Display Data
    hospital.display_patients()
    hospital.display_doctors()
    

    # Doctor's Schedule
    doctor1.display_schedule()
    doctor2.display_schedule()
    
