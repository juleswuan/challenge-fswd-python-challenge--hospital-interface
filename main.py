import classes as cl
from colorama import Fore, Back, Style
import database as db
import stdiomask

# starting employees
db.hospital.hire_employee(db.director)
db.hospital.hire_employee(db.doctor)
db.hospital.hire_employee(db.janitor)


# starting patients
db.hospital.admit_patient(db.patient_1)
db.hospital.admit_patient(db.patient_2)
db.hospital.admit_patient(db.patient_3)
db.hospital.admit_patient(db.patient_4)


# print signboard
print(Fore.YELLOW + f"||------------------------------------||\n||------------------------------------||\n|| Welcome to {db.hospital} ||\n||------------------------------------||\n||------------------------------------||")

print(Style.RESET_ALL)


# authenticate login
username = input("Please enter your username: ")
password = stdiomask.getpass("Please enter your password: ")

found_employee = False

# iterate over list to check employee objects
for e in db.hospital.employees_records:
    if e.username == username and e.password == int(password):
        print(f"Hello, {e.username}. Your access level is: {e.position}")

    while True:
        # give options of accessible actions
        if e.position == "Director":
            found_employee = True
            print("------------------------------\nOptions:\n1 - View employee records\n2 - Hire new employee \n3 - Fire bad employee\n4 - View patient records \n5 - Admit new patient\n6 - Exit")
            dir_response = input(
                "What would you like to do? (Choose option between 1-6) ")

            # view employee records
            if dir_response == "1" or dir_response == "View employee records":
                db.hospital.view_employee_records()

            # hire new employee
            elif dir_response == "2" or dir_response == "Hire new employee":
                # get attributes via input
                # use input to create new employee (nurse)
                name = input("New name: ")
                age = input("Age: ")
                position = input ("New position: ")
                new_employee = cl.Employee(name, age, position)
                # call hire_employee()
                db.hospital.hire_employee(new_employee)
                print(f"Congratulations! You have 1 new {position}, {age} y o {name}")
                db.hospital.view_employee_records()

            # fire bad employee
            elif dir_response == "3" or dir_response == "Fire bad employee":
                # choose employee by id
                for id, emp in enumerate(db.hospital.employees_records):
                    print (id, emp)
                fire_id = int(input("Who would you like to fire: "))
                # call fire_employee()
                print(f"Bye, {db.hospital.employees_records[fire_id].name}! You're fired!")
                db.hospital.fire_employee(db.hospital.employees_records[fire_id])


            # view patient records
            elif dir_response == "4" or dir_response == "View patient records":
                db.hospital.view_patient_records()

            # admit new patient
            elif dir_response == "5" or dir_response == "Admit new patient":
                # get attributes via input
                # use input to create new patient
                name = input("Patient name: ")
                age = input("Patient age: ")
                blood_type = input("Patient blood type: ")
                new_patient = cl.Patient(name, age, blood_type)
                # call admit_patient()
                db.hospital.admit_patient(new_patient)
                print(f"Patient {name}, {age} y o, {blood_type} blood type has been admitted.")
                db.hospital.view_patient_records()

            elif dir_response == "6" or dir_response == "Exit":
                break

        elif e.position == "Doctor":
            found_employee = True
            print("------------------------------\nOptions:\n1 - View patient records\n2 - Diagnose patient\n3 - Discharge patient\n4 - Exit")
            doc_response = input(
                "What would you like to do? (Choose option between 1-4): ")

            # view patient records
            if doc_response == "1" or doc_response == "View patient records":
                db.hospital.view_patient_records()

            # diagnose patient
            elif doc_response == "2" or doc_response == "Diagnose patient":
                for id, patient in enumerate(db.hospital.patients_records):
                    print(id, patient)

                diagnose_id = int(
                    input("Who would you like to diagnose? (Choose a patient number): "))
                # select patient by id
                # get diagnosis via input and store as new diagnosis
                new_diagnosis = input("Patient is suffering from: ")
                db.hospital.patients_records[diagnose_id].add_diagnosis(
                    new_diagnosis)
                print(db.hospital.patients_records[diagnose_id])

            # discharge patient
            elif doc_response == "3" or doc_response == "Discharge patient":
                for id, patient in enumerate(db.hospital.patients_records):
                    print(id, patient)

                discharge_id = int(
                    input("Who would you like to discharge? (Choose a patient number): "))
                # select patient by id
                # call discharge_patient()
                db.hospital.discharge_patient(
                    db.hospital.patients_records[discharge_id])

                print(db.hospital.patients_records[discharge_id])

            elif dir_response == "4" or dir_response == "Exit":
                break

        elif e.position == "Janitor":
            found_employee = True
            print(f"------------------------------\nOptions:\n1 - Work report\n2 - Exit")
            jan_response = input(
                "What would you like to do? (Choose option between 1-2): ")
            
            if jan_response == "1" or jan_response == "Work report":
                print("Keep up the good work, {e.username}!")

            elif jan_response == "2" or jan_response == "Exit":
                break

if not found_employee:
    print("You shall not pass >:")


