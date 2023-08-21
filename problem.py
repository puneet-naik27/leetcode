input = 2314


while input >=9:
    input = sum([int(i) for i in str(input)])


print(input)
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@logger
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)
