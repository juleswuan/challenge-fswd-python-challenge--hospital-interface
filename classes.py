from colorama import Fore, Style, Back

class Hospital():
    def __init__(self, name):
        self.hospital_name = name
        self.employees_records = []
        self.patients_records = []

    def __repr__(self):
        return f"{self.hospital_name}"

    def hire_employee(self, employee):
        self.employees_records.append(employee)

    def fire_employee(self, employee):
        self.employees_records.remove(employee)

    def view_employee_records(self):
        print(Fore.LIGHTMAGENTA_EX + "Current Employees\n----------")
        for e in self.employees_records:
            print(e)
        print(Style.RESET_ALL)

    def admit_patient(self, patient):
        patient.status = "Admitted"
        self.patients_records.append(patient)

    def discharge_patient(self, patient):
        patient.status = "Discharged"

    def view_patient_records(self):
        print(Fore.CYAN + "Patients Records\n----------")
        for p in self.patients_records:
            print(p)
        print(Style.RESET_ALL)


class Employee(Hospital):
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.username = self.name
        self.password = 1111

    def __repr__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nPosition: {self.position}\nUsername: {self.username}\nPassword: {self.password}\n----------"


class Patient():
    diagnosis = ''

    def __init__(self, name, age, blood_type):
        self.name = name
        self.age = age
        self.blood_type = blood_type
        self.diagnosis = ""
        self.status = ""

    def __repr__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nBlood Type: {self.blood_type}\nStatus: {self.status}\nDiagnosis: {self.diagnosis}\n----------"

    def add_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis

