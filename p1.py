while True:
    print("Welcome to the Pattern Generator and Number and Number Analyzer!")
    print()
    
    print("1 Generate a pattern")
    print("2 Analyse a range of number")
    print("3 Exit")
    print()
    
    choice = int(input("Enter your choice :"))
    
    if choice==1:
        for i in range (0,6):
            print("*"*i)
    elif choice==2:
        start = int(input("Enter the start of range:"))
        end = int(input("Enter the end of range:"))
        for i in range(10,15):
            if i%2==0:
                print("Number",i,"is Even")
            else:
                print("Number",i,"is Odd")
                
        sum = 0
        num = 10
        
        while num <=15:
            sum += num
            num += 1
        print("Sum of all numbers from 10 to 15 is:",sum)
        print()
    elif choice==3:
        print("Exiting the program, Goodbye!")
        break
    else:
        print()
        print("Exiting the program")