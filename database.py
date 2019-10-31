import classes as cl    

# create patients
patient_1 = cl.Patient("Jasmine", 25, "AB")
patient_2 = cl.Patient("Alice", 40, "O")
patient_3 = cl.Patient("Ivan", 61, "B-")
patient_4 = cl.Patient("Joshua", 18, "B+")


# create employees
director = cl.Employee("Jules", 30, "Director")
doctor = cl.Employee("House", 55, "Doctor")
janitor = cl.Employee("Carlos", 28, "Janitor")


# create hospital
hospital = cl.Hospital("Code Well Soon Hospital")

# possible actions
actions = ["View patient records"]