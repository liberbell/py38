from ast import If
import sys

if __name__ == "__main__":
    print("Number of command line arguments: ", len(sys.argv))
    print("Script name: ", sys.argv[0])
    print("All arguments: ", sys.argv)