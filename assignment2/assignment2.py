# Task 2: Read a CSV File

import csv
import traceback
import sys

def read_employees():
    employee_data = {}
    rows = []
    try:
        counter = 0
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if counter == 0:
                    employee_data["fields"] = row
                    counter += 1
                else:
                   rows.append(row)
            employee_data["rows"] = rows

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit()
    return employee_data

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id") 
print(employee_id_column)

# Task 4: Find the Employee First Name
def column_index(column_name):
    return employees["fields"].index(column_name)

first_name_column = column_index("first_name")
print(first_name_column)

def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches 

# Task 6: Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    column_index("last_name")
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees ["rows"]

sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    keys = employees["fields"]
    employee_data = {}
    for key, value in zip(keys, row):
        if key == "employee_id":
            pass
        else:
            employee_data[key] = value
    return employee_data
