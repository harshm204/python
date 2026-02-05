print("Welcome to student Data Organizer")

students = []

while True:
    print("\nMenu")
    print("Enter 1 to Add Student")
    print("Enter 2 to Display Student")
    print("Enter 3 to Update Student")
    print("Enter 4 to Delete Student")
    print("Enter 5 to Show Student")
    print("Enter 6 to Exit")
    
    choice = input("Enter Choice: ")
    if choice == "1":
        studentId = int(input("Enter student id:"))
        name = input("Enter Name:")
        age = int(input("Enter age:"))
        grade = input("Enter grade:")
        dob = input("Enter Date Of Birth")
        
        sub = input("Enter subjects:")
        subject_list = sub.split(",")
        subject_set = set()
        
        for sub in subject_list:
            subject_set.add(sub.strip())
        
        id_dob = (studentId, dob)
        
        student = {}
        student["id_dob"] = id_dob
        student["name"] = name
        student["age"] = age
        student["grade"] = grade
        student["subjects"] = subject_set
        
        students.append(student)
        print("Student added")
        
    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            for student in students:
                print("-----------------")
                print("ID:", student["id_dob"][0])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                print("Subjects:", student["subjects"])
                
    elif choice == "3":
        studentId = int(input("Enter student id to update:"))
        found = False
        
        for student in students:
            if student["id_dob"][0] == studentId:
                found = True
                print("1. Update age")
                print("2. Update subjects")
                opt = input("Enter option:")
                
                if opt == "1":
                    student["age"] = int(input("Enter new age: "))
                    print("Age Updated")
                
                elif opt == "2":
                    new_sub = input("Enter new subjects: ")
                    new_list = new_sub.split(",")
                    new_set = set()
                    
                    for s in new_list:
                        new_set.add(s.strip())
                        subject_set.add(s.strip())
                        
                    student["subjects"] = new_set
                    print("Subjects Updated")
                    
                break
            if found == False:
                print("Student Not Found")
                
    elif choice == "4":
        studentId = int(input("Enter student id to delete: "))
        deleted = False
        
        for i in range(len(student)):
            if studentId == studentId:
                del student
                deleted = True
                print("Student deleted")
                break
            
            if deleted == False:
                print("Student not found")
                
    elif choice == "5":
        print("Subjects offered:")
        for sub in subject_set:
            print(sub)
            
    elif choice == "6":
        print("Thank you for using the program")
        break
    
    else:

        print("Invalid choice")
