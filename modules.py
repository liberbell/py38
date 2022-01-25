import imp
import math
import os
from os import path
import pwd

print("Pi: ", math.pi)
print("e: ", math.e)
print(math.pow(3, 4))

print(os.getcwd())
print(os.listdir())

# os.mkdir("./osmodule")

# print(path.isdir(cwd))
print(path.isdir("./osmodule"))