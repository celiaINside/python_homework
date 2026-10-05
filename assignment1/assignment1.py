# Task 1: Hello
def hello():
    return "Hello!"

result = hello()
print (result)

# Task 2: Greet with a Formatted String
def greet(name):
    return(f"Hello, {name}!")
    
greet("Lucia")

# Task 3: Calculator
def calc(val1, val2, operation="multiply"):
    try:
        if operation == "multiply":
            return val1 * val2
        elif operation == "add":
            return val1 + val2
        elif operation == "subtract":
            return val1 - val2
        elif operation == "modulo":
            return val1 % val2
        elif operation == "int_divide":
            return val1 // val2
        elif operation == "power":
            return val1 ** val2
        elif operation == "divide":
                return val1 / val2
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError as e:
        return(f"You can't {operation} those values!")

    calc(val1, val2, operation)

# Task 4: Data Type Conversion
def data_type_conversion(value, data_type): 
    try: 
        if data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
    except ValueError as e:
        return (f"You can't convert {value} into a {data_type}.")

# Task 5: Grading System, Using *args
def grade_function(*args):
    try:
        avg = sum(args) / len(args) 
        if avg < 60:
            return (f"The average grade is: F.")
        elif 60 <= avg <= 69:
            return (f"The average grade is: D.")
        elif 70 <= avg <= 79:
                return (f"The average grade is: C.")
        elif 80 <= avg <= 89:
                return (f"The average grade is: B.")
        elif avg >= 90:
                return (f"The average grade is: A.")
    except (TypeError, ZeroDivisionError):
        return ("Invalid data was provided.")