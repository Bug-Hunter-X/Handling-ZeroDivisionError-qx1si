def my_function(a, b):
    if b == 0:
        return 0 #or raise exception
    else:
        return a / b

result = my_function(10, 0)
print(result) # Output: 0

#Alternative solution using try-except block
def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0 #or raise exception

result = my_function(10, 0)
print(result) # Output: 0