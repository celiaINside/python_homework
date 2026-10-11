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