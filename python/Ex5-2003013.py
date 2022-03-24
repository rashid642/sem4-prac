# # Ex5-2003013.py
# class employee:
#     employecount = 0
#     def __init__(self, id):
#         self.id = id
#     def set_name(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
#     def get_id(self):
#         return self.id
#     @classmethod
#     def set_emp_count(cls):
#         cls.employecount = cls.employecount + 1

# emp = []
# n = int(input("enter number of employe:"))
# for i in range(0, n):
#     name = input("enter name of the employe:")
#     e = employee(i+1)
#     e.set_name(name)
#     emp.append(e)

# print("number of employees = ", employee.employecount)
# n = employee.employecount
# for e in emp:
#     print( e.id, e.name)



class student:
    def __init__(self, college):
        print("inside student init")
        self.college = college
    def getcollege(self):
        return self.college
        
class employee:
    print("inside employee init")
    def __init__(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_id(self):
        return self
        
class intern(student, employee):
    def __init__(self, id, college, period):
        employee.__init__(self,id)
        student.__init__(self,college)
        self.period = period
    def setdetails(self, name):
        self.name = name
    def getdetail(self):
        return self.name


it = intern(1, "Rajhans", "Sports")
it.setdetails("Rashid")
print(it.id, it.name, it.period)