# writing to a file will OVERWRITE the original
# appending to a file will appeand to end of existing data
# can use write to CREATE a file that does not already exist

employee_file = open("employees.txt", "a")
# employee_file.write("\nKelly - Customer Service")


employee_file.close()