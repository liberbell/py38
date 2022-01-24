# print(10 * 2 / 0)
# print("hello" + 3)
# print(does_not_exit + 3)

# try:
#     user_input = input("Please input an integer: ")
#     result = 100 / int(user_input)
#     print("100 divided by the integer you input: ", result)
# except ValueError:
#     print("Oops an exception was thrown.")
# print("outside the try/except block")

# try:
#     user_input = input("Please input an integer: ")
#     result = 100 / int(user_input)
#     print("100 divided by the integer you input: ", result)
# except (ValueError, ZeroDivisionError):
#     print("Oops an exception was thrown.")
# print("outside the try/except block")

from logging import exception


# try:
#     user_input = input("Please input an integer: ")
#     result = 100 / int(user_input)
#     print("100 divided by the integer you input: ", result)
# except ValueError as ve:
#     print("Oops a Value error was thrown.")
#     print("Error type: ", type(ve))
# except ZeroDivisionError as zde:
#     print("Oops a zero divided was thrown.")
#     print("Error type: ", type(zde))
# print("outside the try/except block")

# print(issubclass(ValueError, Exception))

# try:
#     user_input = input("Please input an integer: ")
#     result = 100 / int(user_input)
#     print("100 divided by the integer you input: ", result)
# except Exception:
#     print("Oops an exception was thrown.")
# print("outside the try/except block")

# try:
#     user_input = input("Please input an integer: ")
#     result = 100 / int(user_input)
#     print("100 divided by the integer you input: ", result)
# except ValueError as ve:
#     print("Oops a Value error was thrown.")
#     print("Error type: ", type(ve))
# except ZeroDivisionError as zde:
#     print("Oops a zero divided was thrown.")
#     print("Error type: ", type(zde))
# else:
#     print("Successfully executed the code in the try block.")
# print("outside the try/except block")

try:
    raise Exception("green", "eggs", "and", "ham")

except Exception as exe:
    print("Exception: ", exe)
    print("Type: ", type(exe))
    print("Arguments: ", exe.args)