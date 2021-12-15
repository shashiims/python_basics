
a = 5
b = 6


# try:
#     result = a < b
#     print(result)

# except:
#     print("error comparing a and b")

# try:
#     print(a/0)

# except:
#     print("divide by zero error")

# try:
#     print(a<'')
# except ZeroDivisionError:
#     print("Divide by zero")
# except:
#     print("this will catch all types of errors")

try:
    print("hello")
except:
    print("error printing hello")
finally:
    print("after executing try and except")