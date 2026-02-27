import datetime


print("welcome to personal journal Manager !")
print("please select an option:")

class journal:
    def __init__(self,filename="jornnal.txt"):
        self.filename=filename
        
    def add_entry(self,entry):
        self.entry=entry
        new=datetime.datetime.now()
        timetamp=new.strftime ("%Y-%m-%d %H:%M:%S")
        
        try:
            with open(self.filename,"a")as file:
                file.write(f"[{timetamp}]\n{entry}\n")
                file.write("\n")
                
                print("\nEntry add successfully\n")
        except PermissionError:
            print("\nERROR:permissionerror denied while writing to file\n")
            
    def view_entry(self):
        try:
            with open(self.filename,"r")as file:
                b = file.read()
                if b:
                    print("\nyour journal entris:")
                    print("-"*20)
                    print(b)
                else :
                    print("\nNo journal entries found. start by adding a new entry!\n")
                
        except FileNotFoundError:
            print("ERROR: The journal file does not exist. Please add a new entry first")
            
    def search_entry(self,search):
        self.search=search
        try:
            with open(self.filename,"r")as file:
                c = file.read()
                entry=c.strip().split("\n\n")
                found = False
                for entrys in entry:
                    if self.search in entrys:
                        print("mathcing:")
                        print("-"*20)
                        print(entrys)
                        found = True
                        
                if not found:
                        print("\n No entries were found for keyworld:\n",self.search)
        except FileNotFoundError:
            print("\n File not found")
            
    def delet_entry(self,delet):
        self.delet=delet
        try:
            if self.delet=="yes":
                 with open(self.filename,"w")as file:
                    pass 
                    print("\nall journmal entry have been delet.\n")
            else:
                print("\n No journal entries to delet.\n")
                
        except FileNotFoundError:
            print("\nError : file not found\n")
                
                    
                        
                
jobj=journal()
        
                
while True:
    
    print("1. Add a new entry")
    print("2. View All Entries")
    print("3. Search For an Entry")
    print("4. Delete All entries")
    print("5. exit")
    
    choice = int(input("User Input:"))
    
    if choice==1:
        a=input("\nEnter your journal entry: \n")
        jobj.add_entry(a)
        
    elif choice==2:
        jobj.view_entry()
        
    elif choice==3:
        c=input("\nEnter a keyw world or date to search: \n")
        jobj.search_entry(c)
        
    elif choice==4:
        d=input("Are you sure you want to delet all entries? (yes/no) :")
        jobj.delet_entry(d)
    elif choice==5:
        print("\n Thank you for using personal jorunal manager. Good bye!\n")
        break
    else:
        print("Invalid choice")