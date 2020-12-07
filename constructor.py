#constructor
class Employee:
    def __init__(self,id,name,mobile_num,car):
        self.id=id
        self.emp_name=name
        self.contact_num=mobile_num
        self.car=car
    def employee_name(self):
        print(self.emp_name)
    def employee_details(self):
        print(self.id)
        print(self.contact_num)
    def employee_car(self):
        print(self.car)
e=Employee(23,"antrow",8200692,"polo")
e.employee_name()
e.employee_details()
e.employee_car()


