import numpy as np

print("Welcome to the Numpy Analyzer!")
print("="*25)

class data_analytics:

    def __init__(self,arr=np.array([[10,20,30],[40,50,60],[70,80,90]]),row=3,col=3):
        self.arr=arr
        self.row=row
        self.col=col

    #-------------------- Create Array --------------------
    def array(self):
        num=input("\nEnter elements of 1D Array: ")
        num=list(map(int,num.split()))
        self.arr=np.array(num)
        print("\nArray created successfully:")
        print(self.arr,"\n")

    def array_2d(self):
        self.row=int(input("Enter the number of rows: "))
        self.col=int(input("Enter the number of columns: "))
        arr_l=input(f"Enter {self.row*self.col} elements for the array separated by space: ")
        arr_l=list(map(int,arr_l.split()))
        self.arr=np.array(arr_l).reshape(self.row,self.col)
        print("\nArray created successfully:")
        print(self.arr,"\n")

    def array_3d(self):
        block=int((input("Enter number of Blocks: ")))
        self.row=int(input("Enter number of Row: "))
        self.col=int(input("Enter number of columns: "))
        l1=input(f"Enter {block*self.row*self.col} elements separated by space: ")
        l1=list(map(int,l1.split()))
        self.arr=np.array(l1).reshape(block,self.row,self.col)
        print("\nArray created successfully:")
        print(self.arr,"\n")
    
    def indexing(self):
        try:
            ind_r=int(input("\nEnter a index for row: "))
            ind_c=int(input("Enter a index for colum: "))
            new=self.arr[ind_r][ind_c]
            print(f"\nSearch index is :{new}\n")
        except ValueError:
            print("\nInvalid Input!")

    def slicing(self):
        try:
            slice_r=input("Enter the row range (Start:End): ")
            slice_c=input("Enter the colume range (Start:End): ")
            slice_r=list(map(int,slice_r.split(":")))
            slice_c=list(map(int,slice_c.split(":")))
            new_arr=self.arr[slice_r[0]:slice_r[1],slice_c[0]:slice_c[1]]
            print("\nSliced Array:")
            print(new_arr,"\n")
        except ValueError:
            print("\nInvalid Input!")

    #-------------------- Mathematical opp --------------------
    def add(self):
        try:
            add_arr=input(f"Enter the same-size array elements ({self.row*self.col} elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(self.row,self.col)
            print("\nOriginal Array:")
            print(self.arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=self.arr+sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except TypeError:
            print("\nInvalid Input!")

    def sub(self):
        try:
            add_arr=input(f"Enter the same-size array elements ({self.row*self.col} elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(2,3)
            print("\nOriginal Array:")
            print(self.arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=self.arr-sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except ValueError:
            print("\nInvalid Input!")

    def mul(self):
        try:
            add_arr=input(f"Enter the same-size array elements ({self.row*self.col} elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(self.row,self.col)
            print("\nOriginal Array:")
            print(self.arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=self.arr*sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except ValueError:
            print("\nInvalided Input!")

    def div(self):
        try:
            add_arr=input(f"Enter the same-size array elements ({self.row*self.col} elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(self.row,self.col)
            print("\nOriginal Array:")
            print(self.arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=self.arr/sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except ValueError:
            print("\nInvalided Input!")

    #-------------------- Combine or split --------------------
    def combine(self):
        try:
            stack=input("Enter the array combine Vertically or Horizontally (V / H): ")
            stack_upper=stack.upper()
            add_arr=input(f"Enter the element of another array to combine ({self.row*self.col} elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(self.row,self.col)
            print("\nOriginal Array:")
            print(self.arr,"\n")
            print("Second Array:")
            print(sec_arr)
            if stack_upper=="V":
                new_arr=np.vstack((self.arr,sec_arr))
                print("\nCombine Array (Vertically Stack):")
                print(new_arr,"\n")
            elif stack_upper=="H":
                new_arr=np.hstack((self.arr,sec_arr))
                print("\nCombine Array (Horizontally Stack):")
                print(new_arr,"\n")
            else:
                print("\nInvalided Choice\n")
        except ValueError:
            print("\nInvalided Input!")

    def split(self):
        try:
            split=input("Enter the Split array Vertically or Horizontally (V / H): ")
            split_upper=split.upper()
            print("\nOriginal Array:")
            print(self.arr)
            if split_upper=="V":
                new_arr=np.vsplit(self.arr,self.row)
                print("\nSplit Array (Vertically Stack):")
                print(new_arr,"\n")
            elif split_upper=="H":
                new_arr=np.hsplit(self.arr,self.col)
                print("\nSplit Array (Horizontally Stack):")
                print(new_arr,"\n")
            else:
                print("\nInvalided Choice\n")
        except ValueError:
            print("\nInvalided Input!")

    #-------------------- Searching, Sorting & Filter --------------------
    def search(self):
        try:
            search=int(input("Enter element for search: "))
            sea_arr=np.where(self.arr==search)
            print("\nSearchhing element successfully")
            print(sea_arr,"\n")
        except ValueError:
            print(f"\nThis {search} elemente is not match in this array\n")

    def sort(self):
        try:
            print("\nOriginal Array:")
            print(self.arr,"\n")
            sort_arr=np.sort(self.arr)
            print("Sorted Array:")
            print(sort_arr,"\n")
        except ValueError:
            print("\nInvalid Input!")

    def filter(self):
        try:
            elements = input(f"Enter {self.row*self.col} elements (True/False or 1/0): ").split()
            bool_list = [bool(int(i)) for i in elements]
            f_arr=np.array(bool_list).reshape(self.row,self.col)
            print("\nOriginal Array:")
            print(self.arr,"\n")
            print("Filter Array:")
            print(self.arr[f_arr],"\n")
        except ValueError:
            print("\nInvalid Input!")

    #-------------------- Aggregates and Statistics --------------------
    def sum(self):
        try:
            print("\nOriginal Array:")
            print(self.arr,"\n")
            sum=np.sum(self.arr)
            print(f"Sum of Array: {sum}\n")
        except ValueError:
            print("\nInvalid Input!")

    def mean(self):
        try:
            print("\nOriginal Array:")
            print(self.arr,"\n")
            mean=np.mean(self.arr)
            print(f"Mean of Array: {mean}\n")
        except ValueError:
            print("\nInvalid Input!")

    def median(self):
        try:
            print("\nOriginal Array:")
            print(self.arr,"\n")
            median=np.median(self.arr)
            print(f"Median of Array: {median}\n")
        except ValueError:
            print("\nInvalid Input!")

    def standard_deviation(self):
        try:
            print("\nOriginal Array:")
            print(self.arr,"\n")
            standard_deviation=np.std(self.arr)
            print(f"Standard Deviation of Array: {standard_deviation}\n")
        except ValueError:
            print("\nInvalid Input!")

    def variance(self):
        try:
            print("\nOriginal Array:")
            print(self.arr,"\n")
            variance=np.var(self.arr)
            print(f"Variance of Array: {variance}\n")
        except ValueError:
            print("\nInvalid Input!")

    def __del__(self):    
        pass

da=data_analytics()

while True:
    print("choose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Array")
    print("5. Compute Aggregates and Statistics")
    print("6. EXit\n")

    choice=int(input("Enter your choice: "))
    if choice==1:
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        achoice=int(input("Enter your choice: "))
        if achoice==1:
            da.array()
            while True:
                print("Choose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    da.indexing()
                elif choice==2:
                    da.slicing()
                elif choice==3:
                    print("\nReturning to Main Menu.\n")
                    break
                else:
                    print("\nInvalided Choice\n")
        elif achoice==2:
            da.array_2d()
            while True:
                print("Choose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    da.indexing()
                elif choice==2:
                    da.slicing()
                elif choice==3:
                    print("\nReturning to Main Menu.\n")
                    break
                else:
                    print("\nInvalided Choice\n")
        elif achoice==3:
            da.array_3d()
            while True:
                print("Choose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    da.indexing()
                elif choice==2:
                    da.slicing()
                elif choice==3:
                    print("\nReturning to Main Menu.\n")
                    break
                else:
                    print("\nInvalided Choice\n")
        else:
            print("\nInvalided Choice\n")
    elif choice==2:
        while True:
            print("Choose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Go Back\n")
            mchoice=int(input("Enter your choice: "))
            if mchoice==1:
                da.add()
            elif mchoice==2:
                da.sub()
            elif mchoice==3:
                da.mul()
            elif mchoice==4:
                da.div()
            elif mchoice==5:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalid Choice\n")

    elif choice==3:
        while True:
            print("\nChoose an option:")
            print("1. Combine Array")
            print("2. Split Array")
            print("3. Go Back\n")
            choice=int(input("Enter your choice: "))
            if choice==1:
                da.combine()
            elif choice==2:
                da.split()
            elif choice==3:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalid Choice\n")

    elif choice==4:
        while True:
            print("\nChoose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter value")
            print("4. Go Back\n")
            schoice=int(input("Enter your Choice: "))
            if schoice==1:
                da.search()
            elif schoice==2:
                da.sort()
            elif schoice==3:
                da.filter()
            elif schoice==4:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalid Choice\n")

    elif choice==5:
        while True:
            print("Choose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Go Back\n")
            schoice=int(input("Enter your Choice: "))
            if schoice==1:
                da.sum()
            elif schoice==2:
                da.mean()
            elif schoice==3:
                da.median()
            elif schoice==4:
                da.standard_deviation()
            elif schoice==5:
                da.variance()
            elif schoice==6:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalid Choice\n")

    elif choice==6:
        print("\nThank you for using the Numpy Analyzer! Goodbye!\n")
        break
    else:
        print("\nInvalid Choice\n")