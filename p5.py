print(" --- python OOP: employee Management System --- \n")

class Employee:
    
    def __init__(self,Employee_id,name,age,salary):
        self.Employee_id=Employee_id
        self.name=name
        self.age=age
        self.salary=salary
        
    def getter(self):
        print(f"\nemployee craeted with name :{self.name},age :{self.age},employee ID :{self.Employee_id},salary :{self.salary}\n")
        
    def showEmployeeinfo(self):
        print("\n Employee details")
        print("name :",self.name)
        print("age :",self.age)
        print("Employee ID :",self.Employee_id)
        print("salary :",self.salary)   
        
    def __del__(self):
        pass
        
class manager(Employee):
    
    def __init__(self,Employee_id,name,age,salary,department):
        super().__init__(Employee_id,name,age,salary)
        self.department=department
        
    def getter(self):
        print(f"\nManager created with name :{self.name},age :{self.age},Employee ID :{self.Employee_id},salary :{self.salary}\n")
        
    def showEmployeeinfo(self):
        print("\n Manager detail")
        print("name :",self.name)
        print("age :",self.age)
        print("employee ID :",self.Employee_id)
        print("salary :",self.salary)
        print("Department :",self.department)
        
    def __del__(self):
            pass
        
class devloper(Employee):
    
    def __init__(self,Employee_id,name,age,salary,programinglanguage):
        super().__init__(Employee_id,name,age,salary)
        self.programing_language=programinglanguage
        
    def getter(self):
        print(f"\ndevloper creted with name :{self.name},age :{self.age},Employee ID :{self.Employee_id},salary :{self.salary},programing language :{self.programing_language}\n")
        
        
    def showEmployeeinfo(self):
        print("\ndevloper details")
        print("name :",self.name)    
        print("age :",self.age)
        print("Employee ID :",self.Employee_id)
        print("salary :",self.salary)
        print("programing language :",self.programing_language)
        
        def __del__(self):
            pass
        
        
Elist = []
Mlist = []
Dlist = []

first = True
 
while True:
            if not first:
                print("choose another opration\n")
                
            first=False
            print("choose an opration")
            print("1. crate an Employee")
            print("2. create an Manager")
            print("3. create an devloper")
            print("4. show details")
            print("5. exit\n")
            
            choice = int(input("Enter your choice :"))
            
            if choice==1:
                name=input("Enter Employee name :")
                age=int(input("Enter Employee age :"))
                Employee_id=int(input("Enter employee ID :"))
                salary=int(input("Enter Employee salary :"))
                
                emobj=Employee(Employee_id,name,age,salary)
                Elist.append(emobj)
                emobj.getter()
                
            elif choice==2:
                name=input("Enter manager name :")
                age=int(input("Enter manager age :"))
                Employee_id=int(input("Enter manager ID :"))
                salary=int(input("Enter manager salary :"))
                department=input("Enter manager department :")
                
                maobj=manager(Employee_id,name,age,salary,department)
                Mlist.append(maobj)
                maobj.getter()
                
            elif choice==3:
                name=input("Enter devloper name :")
                age=int(input("Enter devloper age :"))
                Employee_id=int(input("Enter devloper ID :"))
                salary=int(input("Enter devloper salary :"))
                programinglanguage=input("Enter devloper programing language :")
                
                deobj=devloper(Employee_id,name,age,salary,programinglanguage)
                Dlist.append(deobj)
                deobj.getter()
                
            elif choice==4:
                print("\nchoose detail to show")
                print("1. all employee")        
                print("2. all manager")
                print("3. all devloper\n")
                
                vchoice=int(input("Enter your choice :"))
                
                if vchoice==1:
                    for e in Elist:
                        e.showEmployeeinfo()
                        
                elif vchoice==2:
                    for m in Mlist:
                        m.showEmployeeinfo()
                
                elif vchoice==3:
                    for d in Dlist:
                        d.showEmployeeinfo()
                        
                else:
                    print("\ninvalid chocie\n")
                    
            elif choice==5:
                print("\nExiting the system. all resoures have been freed.\n")
                break
            else :
                print("invalid choice")