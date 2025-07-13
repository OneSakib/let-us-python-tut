# Decorator

def my_decorator(func):
    def wrapper():
        print("**************")
        func()
        print("--------------")
    return wrapper


@my_decorator
def display():
    print("I stand")

display()
