# import sys
# from employee import create_employee

# if __name__ == "__main__":
#     # print("Number of command line arguments: ", len(sys.argv))
#     # print("Script name: ", sys.argv[0])
#     # print("All arguments: ", sys.argv)
#     print("All argument: ", sys.argv)

#     name = sys.argv[1]
#     deparmain10
# tment = sys.argv[2]
#     salary = int(sys.argv[3])

#     emplo = create_employee(name, department, salary)
#     emplo.display_detail()

import argparse
from employee import create_employee

parser = argparse.ArgumentParser(description="Parsing employee details.")

parser.add_argument("--name", help="Please specify the employee's name.", type=str)
parser.add_argument("--department", help="Please specify the employee's department.", type=str)
parser.add_argument("--salary", help="Please specify the employee's salary.", type=int)

if __name__ == "__main__":
    args = parser.parse_args()
    emplo = create_employee(args.name, args.department, args.salary)
    emplo.display_detail()