EMPNAME = []

def add_employee(name):
    EMPNAME.append(name)
    print(f"Employee {name} added successfully!")

def remove_employee(name):
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"Employee {name} removed successfully!")
    else:
        print(f"Employee {name} not found in the list.")

def append_employee(name):
    EMPNAME.append(name)
    print(f"Employee {name} appended successfully!")

EMPNAME.extend(["John", "Jane", "Doe"])

print("Initial List of Employees:", EMPNAME)
add_employee("Alice")
remove_employee("John")
append_employee("Bob")
print("Updated List of Employees:", EMPNAME)
