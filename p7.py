import datetime
import time
import random
import math
import uuid
import os


# -------- Date & Time --------
class DateStuff:
    def show_now(self):
        now = datetime.datetime.now()
        print("Current Date and Time : ", now.strftime("%Y-%m-%d %H:%M:%S"))

    def date_diff(self):
        try:
            d1 = input("Enter the First Date and Time (YYYY-MM-DD HH:MM:SS) : ")
            d2 = input("Enter the Second Date and Time (YYYY-MM-DD HH:MM:SS) : ")
            dt1 = datetime.datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
            dt2 = datetime.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
            print("Difference : ", dt1 - dt2)
        except:
            print("Invalid Format ! Use YYYY-MM-DD HH:MM:SS.")

    def change_format(self):
        try:
            d = input("Enter a Date (YYYY-MM-DD) : ")
            f = input("Enter a Format (e.g., %d/%m/%Y) : ")
            dt = datetime.datetime.strptime(d, "%Y-%m-%d")
            print("Formated Date : ", dt.strftime(f))
        except:
            print("Invalid Format ! ")

    def run_stopwatch(self):
        input("Press Enter to start the stopwatch...")
        st = time.time()
        input("Press Enter to stop the stopwatch...")
        et = time.time()
        diff = et - st
        h, rem = divmod(int(diff), 3600)
        m, s = divmod(rem, 60)
        print(f"Time Taken : {h}h {m}m {s}s ({diff:.2f} seconds)")

    def run_countdown(self):
        try:
            sec = int(input("Enter CountDown Time In Seconds : "))
            for t in range(sec, 0, -1):
                print(f"Time Left : {t} seconds.")
                time.sleep(1)
            print("Time's Up!")
        except:
            print("Please Enter a valid number!")


# -------- Math --------
class Maths:
    def fact(self):
        try:
            n = int(input("Enter a Number : "))
            print("Factorial : ", math.factorial(n))
        except:
            print("Invalid input! Please enter an integer.")

    def comp_interest(self):
        try:
            p = float(input("Enter principal amount : "))
            r = float(input("Enter rate of Interest (%) : "))
            t = float(input("Enter time (in years) : "))
            amt = p * ((1 + r / 100) ** t)
            ci = amt - p
            print("Compound Interest : ", round(ci, 2))
            print("Total Amount : ", round(amt, 2))
        except:
            print("Invalid input! Please enter numeric values.")

    def trig(self):
        try:
            deg = float(input("Enter angle in degrees: "))
            rad = math.radians(deg)
            print(f"sin({deg}) = {math.sin(rad):.4f}")
            print(f"cos({deg}) = {math.cos(rad):.4f}")
            try:
                print(f"tan({deg}) = {math.tan(rad):.4f}")
            except:
                print(f"tan({deg}) is undefined.")
        except:
            print("Invalid input! Please enter a number.")

    def areas(self):
        print("\n1. Area of Circle")
        print("2. Area of Rectangle")
        print("3. Area of Triangle")
        try:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                r = float(input("Enter radius: "))
                print("Area of Circle:", round(math.pi * r * r, 2))
            elif ch == 2:
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                print("Area of Rectangle:", round(l * b, 2))
            elif ch == 3:
                b = float(input("Enter base: "))
                h = float(input("Enter height: "))
                print("Area of Triangle:", round(0.5 * b * h, 2))
            else:
                print("Invalid choice")
        except:
            print("Invalid input! Please enter numbers only.")


# -------- Random --------
class RandomGen:
    def number(self):
        try:
            a = int(input("Enter the start range : "))
            b = int(input("Enter the end range : "))
            print("Random Numbers : ", random.randint(a, b))
        except:
            print("Invalid Input! Please Enter Correct Numbers.")

    def list_(self):
        try:
            sz = int(input("Enter the size of list : "))
            a = int(input("Enter the start range : "))
            b = int(input("Enter the end range : "))
            print("random List : ", [random.randint(a, b) for _ in range(sz)])
        except:
            print("Invalid Input! Kindly Enter Valid Numbers!")

    def password(self):
        try:
            ln = int(input("Enter the length of password : "))
            if ln <= 0:
                print("Password Length Must be Greater than 0.")
                return
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
            pw = "".join(random.choice(chars) for _ in range(ln))
            print("Random Password :", pw)
        except:
            print("Invalid input! Please enter a valid number.")

    def otp(self):
        print("Random Otp : ", "".join(str(random.randint(0, 9)) for _ in range(6)))


# -------- Files --------
class Files:
    def create(self):
        try:
            name = input("Enter the file name : ")
            open(name, "w").close()
            print("File Created Successfully!")
        except:
            print("Error Occured!")

    def write(self):
        try:
            name = input("Enter the file name : ")
            data = input("Enter the data to write : ")
            with open(name, "w") as f:
                f.write(data)
            print("Data Written Successfully!")
        except:
            print("Error occured!")

    def read(self):
        try:
            name = input("Enter file name : ")
            if os.path.exists(name):
                with open(name, "r") as f:
                    print("File Data : \n", f.read(), "\n")
            else:
                print("File Not Found!")
        except:
            print("Error Occured!")

    def append(self):
        try:
            name = input("Enter file name: ")
            data = input("Enter data to append: ")
            with open(name, "a") as f:
                f.write("\n" + data)
            print("Data appended successfully!\n")
        except:
            print("Something went wrong while appending to the file.")


# -------- Main Menu --------
d = DateStuff()

while True:
    print("\n==============================")
    print("Welcom To Multi-Utility ToolKit")
    print("==============================")
    print("Choose an option : ")
    print("1. Datetime and Time Operations.")
    print("2. Mathematical Operations.")
    print("3. Random Data Generation.")
    print("4. Generate Unique Identifiers.")
    print("5. File Operations Custom Module.")
    print("6. Explore Module Attributes (dir()).")
    print("7. Exit.")
    print("==============================")

    ch = int(input("Enter Your Choice : "))

    if ch == 1:
        print("\nDateTime and Time Operations : ")
        print("1. Display current date and time.")
        print("2. Calculate difference between two dates and time.")
        print("3. Formate date into custom format.")
        print("4. Stopwatch.")
        print("5. Countdown timer.")
        print("6. Back To Main Menu.")

        sub = int(input("\nEnter Your Choice : "))
        if sub == 1:
            d.show_now()
        elif sub == 2:
            d.date_diff()
        elif sub == 3:
            d.change_format()
        elif sub == 4:
            d.run_stopwatch()
        elif sub == 5:
            d.run_countdown()
        elif sub == 6:
            continue

    elif ch == 2:
        m = Maths()
        print("\nMathematical Operations : ")
        print("1. Calculate Factorial.")
        print("2. Solve Compound Interest.")
        print("3. Trigonometric Calculations.")
        print("4. Area of Geometric Shapes.")
        print("5. Back to Main Menu.")
        sub = int(input("\nEnter Your Choice : "))
        if sub == 1:
            m.fact()
        elif sub == 2:
            m.comp_interest()
        elif sub == 3:
            m.trig()
        elif sub == 4:
            m.areas()
        elif sub == 5:
            continue

    elif ch == 3:
        r = RandomGen()
        while True:
            print("\nRandom Data Generation : ")
            print("1. Generate Random Number.")
            print("2. Generate Random List.")
            print("3. Generate Random Password.")
            print("4. generate Random Otp.")
            print("5. Back To Main Menu.")
            sub = int(input("\nEnter Your Choice : "))
            if sub == 1:
                r.number()
            elif sub == 2:
                r.list_()
            elif sub == 3:
                r.password()
            elif sub == 4:
                r.otp()
            elif sub == 5:
                break

    elif ch == 4:
        print("\nGenerate Unique Identifier (UUID):")
        print("Generated UUID:", uuid.uuid4(), "\n")

    elif ch == 5:
        f = Files()
        while True:
            print("\nFile Operations Custom Module:")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to Main Menu")
            sub = int(input("Enter Your Choice : "))
            if sub == 1:
                f.create()
            elif sub == 2:
                f.write()
            elif sub == 3:
                f.read()
            elif sub == 4:
                f.append()
            elif sub == 5:
                break

    elif ch == 6:
        mod = input("Enter module name to explore: ")
        try:
            m = __import__(mod)
            print(f"\nAttributes of {mod}:")
            print(dir(m))
        except:
            print("Module not found!")

    elif ch == 7:
        print("Exiting... Thank you for using Multi-Utility Toolkit!")
        break
    else:
        print("Invalid Choice! Please try again.")