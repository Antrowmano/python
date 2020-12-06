#single inheritance
class Employee:
    def emp_id(self,id):
        print("employee id is",id)
    def emp_name(self,name):
        print("employee name is",name)
class company(Employee):
    def com_id(self,id):
        print("company id is",id)
    def com_name(self,name):
        print("company name is",name)
c=company()
c.emp_id(9999)
c.emp_name("antrow")
c.com_id(1)
c.com_name("google")

#multilevel inheritance


class Employee:
    def emp_id(self,id):
        print("employee id is",id)
    def emp_name(self,name):
        print("employee name is",name)
class company(Employee):
    def com_id(self,id):
        print("company id is",id)
    def com_name(self,name):
        print("company name is",name)
class client(company):
    def cl_name(self,name):
        print("client name is",name)
cl=client()
cl.emp_id(9999)
cl.emp_name("antrow")
cl.com_id(1)
cl.com_name("google")
cl.cl_name("mano")

#multiple inheritance

class Employee:
    def emp_id(self,id):
        print("employee id is",id)
    def emp_name(self,name):
        print("employee name is",name)
class company:
    def com_id(self,id):
        print("company id is",id)
    def com_name(self,name):
        print("company name is",name)
class client(Employee,company):
    def cl_name(self,name):
        print("client name is",name)
cl=client()
cl.emp_id(9999)
cl.emp_name("antrow")
cl.com_id(1)
cl.com_name("google")
cl.cl_name("mano")

#Hierarchical inheritance


class Employee:
    def emp_id(self,id):
        print("employee id is",id)
    def emp_name(self,name):
        print("employee name is",name)
class company(Employee):
    def com_id(self,id):
        print("company id is",id)
    def com_name(self,name):
        print("company name is",name)
c=company()
c.emp_id(999)
c.emp_name("antrow")
c.com_id(1)
c.com_name("google")

class client(Employee):
    def cl_name(self,name):
        print("client name is",name)


cl=client()
cl.emp_id(999)
cl.emp_name("antrow")

cl.cl_name("mano")

#hybrid inheritance


class A:
    def m1(self):
        print("hey")
class B:
    def m2(self):
        print("hi")
class C(A,B):
    def m3(self):
        print("antrow")

class D(C):
    def m4(self):
        print("mano")
b=D()
b.m1()
b.m2()
b.m3()
b.m4()
class E(C):
    def m5(self):
        print("python")
b=E()
b.m1()
b.m2()
b.m3()
b.m5()







