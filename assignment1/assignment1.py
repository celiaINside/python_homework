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
def grade(*args):
    try:
        avg = sum(args) / len(args) 
        if avg < 60:
            return (f"F")
        elif 60 <= avg <= 69:
            return (f"D")
        elif 70 <= avg <= 79:
                return (f"C")
        elif 80 <= avg <= 89:
                return (f"B")
        elif avg >= 90:
                return (f"A")
    except (TypeError, ZeroDivisionError):
        return ("Invalid data was provided.")

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    new_string = ""
    for i in range (count):
        new_string += string
    return new_string

# Task 7: Student Scores, Using **kwargs
def student_scores(type, **kwargs): 
    if type == "best":
        best_score = 0
        best_student = ""
        for key, value in kwargs.items():
            if value > best_score:
                best_score = value
                best_student = key
        return best_student
            
    elif type == "mean":
        return sum(kwargs.values()) / len(kwargs)

# Take 8: Titleize, with String and List Operations
def titleize(string): 
    words = (string).split()
    lower_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    for i, word in enumerate(words):
        if i == 0:
            words[i] = word.capitalize()
        elif i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in lower_words:
            pass
        else:
            words[i] = word.capitalize()
    return " ".join(words)

# Task 9: Hangman with More String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result = result + letter
        else:
            result = result + "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    words = string.split()
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"
        else:
            i = 0
            while word[i] not in vowels:
                if word[i] == "q" and word[i + 1] == "u":
                    i += 2
                else:
                    i +=1
            new_word = word[i:] + word[:i] + "ay"
        result.append(new_word)
    return " ".join(result)
