# Python read command usage
#
#

employee_file = open("employees.txt", "r")
# open("employees.txt", "w") write
# open("employees.txt", "a") append
# open("employees.txt", "r+") read and write

# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines())
# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

