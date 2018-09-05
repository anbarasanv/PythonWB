class Employee:
    '''This class stores employee details'''
    def __init__(self,e_name,e_id,e_sal):
        self.name = e_name
        self.e_id = e_id
        self.salary = e_sal

employees = []
no_emp = int(input("Enter the total number of employess: "))

#getting employee details and storing them into the list
for i in range(0,no_emp):
    print("Enter the details of employe id {} : ".format(i+1))
    name = input("Enter the employee name: ")
    sal = input("Enter the employee salary: ")
    obj = Employee(name,i+1,sal)
    employees.append(obj)

print("Employees Table:",end='\n')
print("Employee_ID Employee_name Employee_salary",end="\n")
#displaying the employee details:
for item in employees:
    print(item.e_id,item.name,item.salary,end="\n")
