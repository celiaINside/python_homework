# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)
task1_data_frame = df
print(task1_data_frame)

# Add a column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

# Modify a column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

# Save the DataFrame as a CSV file
task1_older.to_csv("employees.csv", index=False)

# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

json_employees = pd.read_json('additional_employees.json')
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
first_three = (more_employees.head(3))
print(first_three)

last_two = (more_employees.tail(2))
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

# Task 4: Data Cleaning
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)
clean_data = dirty_data.copy()

clean_data = clean_data.drop_duplicates()
print(clean_data)

clean_data["Age"] = clean_data["Age"].replace("unknown", pd.NA)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data) 

clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

mean_age = clean_data["Age"].mean()  
clean_data["Age_filled_mean"] = clean_data["Age"].fillna(mean_age)

median_salary = clean_data["Salary"].median()  
clean_data["Salary_filled_median"] = clean_data["Salary"].fillna(median_salary)
