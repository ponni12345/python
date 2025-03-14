import threading
import time

# Employee data (shared resource)
employee_data = {}
# Lock to ensure thread safety
lock = threading.Lock()

# Function to add employee information
def add_employee(employee_id, name, department):
    with lock:  # Acquire lock before accessing shared resource
        employee_data[employee_id] = {"name": name, "department": department}
    print(f"Added employee {name} ({employee_id}) to the data.")

# Function to retrieve employee information
def get_employee(employee_id):
    with lock:
        if employee_id in employee_data:
            print(f"Retrieved employee {employee_data[employee_id]['name']} ({employee_id})")
            return employee_data[employee_id]
        else:
            print(f"Employee {employee_id} not found.")
            return None

# Function to update employee information
def update_employee(employee_id, new_department):
    with lock:
        if employee_id in employee_data:
            employee_data[employee_id]["department"] = new_department
            print(f"Updated employee {employee_data[employee_id]['name']} ({employee_id})'s department to {new_department}")
        else:
            print(f"Employee {employee_id} not found.")


# Thread functions (each thread will perform a specific task)
def thread_add_employees():
    add_employee("1", "ARUN", "HR")
    add_employee("2", "DEEPAK", "IT")
    add_employee("3", "RAJ", "Sales")

def thread_get_employees():
    get_employee("1")
    get_employee("2")
    get_employee("3")

def thread_update_employees():
    update_employee("2", "Marketing")
    update_employee("1", "HR")

# Create threads
thread1 = threading.Thread(target=thread_add_employees)
thread2 = threading.Thread(target=thread_get_employees)
thread3 = threading.Thread(target=thread_update_employees)

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for threads to complete
thread1.join()
thread2.join()
thread3.join()

print("All threads completed.")
