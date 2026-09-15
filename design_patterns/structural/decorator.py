# Add behavior without modifying the original function.


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def greet(name):
    return f"Hello, {name}"


print(greet("Rashid"))
