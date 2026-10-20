# Task 1: Writing and Testing a Decorator
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional = args if args else "none"
        keyword = kwargs if kwargs else "none"

        logger.log(
            logging.INFO,
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keyword}\n"
            f"return: {result}\n"
        )
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def accept_arguments(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()

    accept_arguments(12, "hello", True)

    return_decorator(name="Jess", count=5)