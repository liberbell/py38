# print(10 * 2 / 0)
# print("hello" + 3)
# print(does_not_exit + 3)

try:
    user_input = input("Please input an integer: ")
    result = 100 / int(user_input)
    print("100 divided by the integer you input: ", result)
except ValueError:
    print("Oops an exception was thrown.")
print("outside the try/except block")