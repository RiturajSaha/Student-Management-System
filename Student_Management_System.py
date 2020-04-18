# libraries
import os
import shutil
import sys
import datetime


# golbal variables
n=0
acesscode="R2J"
stud={}
top=""


# methods
def ext():
    input("\nPress [enter] to continue...")
    main()
      
def password():
    print("\n**********Student Management System For Higher Education**********\n\n")
    pas=input("\nEnter Access code: ")
    if pas!=acesscode:
             print("\nWrong Access code!")
             n=input("\nWant to Enter Again(1/0)- ")
             if n=='1':
                 os.system("cls")
                 password()
             else:
                
                print("Program Terminating...")
                input("\nPress [enter] to Exit Console...")
                sys.exit()
    else:
           print("Acess Granted!\n")
           print("{Any Abnormal Input During Runtime will Terminate the Program!}")
           ext()

def directory():
    for roll in stud:
          text="\n"+roll
    file=open("data/database/Directory",'a')
    file.write(text)
    file.close() 

def deleteStd():
    os.system("cls")
    roll=input("Enter Roll Number of the Student- ")
    rollno="data/database/"+roll
    if os.path.isfile(rollno)==True:
            os.remove(rollno)
            file=open("data/database/Directory",'r')
            text=file.read()
            file.close()
            lst=text.split()                   
            lst.remove(roll)
            str=''.join(lst)                  
            file2=open("data/database/Directory",'w')
            file2.write(str)
            file2.close()
            print("\nAll Previous Data of ",roll," Deleted!")
    else:
        print(roll," Not Found!")
    ext()    

def updateStd():
    os.system("cls")
    roll=input("Enter Roll Number of the Student- ")
    rollno="data/database/"+roll
    if os.path.isfile(rollno)==True:
            os.remove(rollno)
            print("All Previous Data of ",roll," Deleted!")
            rollno=roll
            print("Enter Updated Data-\n")
            name=input("Enter Name- ")
            name=name.upper()
            branch=input("Enter Branch and Section- ")
            branch=branch.upper()
            sem=input("Enter Semester- ")
            rollno=Student(name,branch,sem,rollno)
            rollno.subject()
            stud[rollno.roll]=rollno    
            print(roll," Updated!")
    else:
        print(roll," Not Found!")
    ext()    

def deleteAll():
    os.system("cls")
    print("\nFormatting Database!")
    print("However the Access code will remain unchanged!")
    o=input("Are you  sure (1/0)?")
    if o=='1':
        pas=input("\nEnter Access code-\n")
        if pas!=acesscode:
             print("\nWrong Access code!")
             print("\nReset Aborted!")
             ext()
        else:
            shutil.rmtree("data/database")
            print("Database Formatted!")
            print("\nProgram Terminating!")
            input("\nPress [enter] to Exit Console...")
            sys.exit() 
    else:
         print("Reset Failed!")
         ext()
           
def createStd():
      
      os.system("cls")
      rollno=input("\nEnter Roll Number- ")
      name=input("Enter Name- ")
      name=name.upper()
      branch=input("Enter Branch and Section- ")
      branch=branch.upper()
      sem=input("Enter Semester[1,8]- ")
        
      if sem.isalpha()==True:
          print("\nInvalid Input!")    
      elif (int(sem)<1)or(int(sem)>8):
          print("\nInvalid Input!")    
      else:
          rollno=Student(name,branch,sem,rollno)
          rollno.subject()
          
      ext()
      
def displayAll():
    os.system("cls")
    if os.path.isfile("data/database/Directory")==False:
        print("\nNothing Found!")
    else:
        
        print("\nAvailable Roll Numbers-")
        file=open("data/database/Directory",'r')
        rnos=file.read()
        file.close()
        print(rnos)
    ext()
    
def displayStd():
    
    os.system("cls")
    rollno=input("\nEnter Roll Number- ")
    roll="data/database/"+rollno
    if os.path.isfile(roll)==True:
        print(rollno," found!")
        file=open(roll,"r")
        text=file.read()
        print(text)
        file.close()

    else:
         print(rollno," not found!")
    ext()
    
def changeAcesscode():
    
    os.system("cls")
    text=input("\nEnter Old Access code- ")
    file=open("data/imp/Acesscode",'r')
    acesscode=file.readline()
    file.close()
    if text==acesscode:
        print("\nPassword should be atmost 8 characters...") 
        newp=input("\nEnter New Access code- ")
        if len(newp)>8:
                 print("Invalid Access code!")
                 o=input("Press 1 to enter again...")
                 if o=='1':
                     changeAcesscode()
                     
                 else:
                     print("Access code Change Failed!") 
                     
                     
        else:
            acesscode=newp
            file=open("data/imp/Acesscode","w")
            file.write(acesscode)
            file.close()
            print("Password changed!")
            
    else:
             print("Wrong Password Entered!")
    ext()         

def displayToppers():
    os.system("cls")
    if os.path.isfile("data/database/Toppers")==False:
          print("Nothing Found!")
    else:      
         file=open("data/database/Toppers",'r')
         text=file.read()
         print(text)
         file.close()
    ext()
    
def delToppers():
    os.system("cls")
    print("\nDeleting Top Performers Record!")
    print("However the Data of the Top Performers will remain unchanged!")
    o=input("Are you  sure (1/0)?")
    if o=='1':
        pas=input("\nEnter Access code-\n")
        if pas!=acesscode:
             print("\nWrong Access code!")
             print("\nAction Aborted!")
             
        else:
            os.remove("data/database/Toppers")
            print("Top Performers Record Deleted!")
            
    else:
         print("Format Failed!")
    ext()     

def main():
    os.system("cls")
    print("\n\nMAIN MENU:-")
    print("----------")
    print("\n 1) Create A Student Data")
    print(" 2) Display Data Of Particular Student")
    print(" 3) Display Data Of All Students")
    print(" 4) Display Top Performers")
    print(" 5) Delete Data Of A Particular Student")
    print(" 6) Update Data Of A Particular Student")
    print(" 7) Delete Top Performer Records")
    print(" 8) Change Access code")
    print(" 9) Reset Database")
    
    
    print("\nEnter 0 to Exit")
    o=input("\nEnter option- ")
    if o=='1':
       createStd()
    elif o=='2':   
       displayStd()
    elif o=='3':
       displayAll()
    elif o=='4':
        displayToppers()
    elif o=='5':
        deleteStd()
    elif o=='6':
        updateStd()
    elif o=='7':
        delToppers()              
    elif o=='8':
        changeAcesscode()
    elif o=='9':
        deleteAll()

    elif o=='0':
       print("\nProgram Terminating!")
       input("\nPress [enter]to Exit Console...")
       sys.exit() 
    else:
        print("\nWrong Option!")
        input("\nPress [enter] to return...")
        os.system("cls")
        main()

       
# classes
class Student:                 
     __name=None
     __branch=None     
     roll=None
     __sem=None
     __submark=" "
     __grade=None
     __data=""
     flag=None

     def __init__(self,name,branch,sem,roll):
          self.__name=name
          self.__branch=branch
          self.roll=roll
          self.__sem=sem
              
     def subject(self):
         
         n=input("Enter Number of Subjects[1,10]- ")
         if (n.isalpha()==True)or int(n)<1 or int(n)>10:
               print("\nInvalid Input!")
               ext()
               
         else:
            flag=None
            n=int(n)
            sum=0.0
            for i in range(0,n,1):
               line=input("Enter Subject Name- ")
               line=line.upper()
               mark=input("Enter Mark[0,100]- ")
               if (mark.isalpha()==True)or(int(mark)<0)or(int(mark)>100):
                   print("\nInvalid Input!")
                   flag=False
                   break                  
                   
               else:
                   flag=True
                   sum=sum+int(mark)   
                   self.__submark=self.__submark+"\n"+line+": "+mark
                    
            if flag:
                sum=sum/n
                if sum>90:
                        self.__grade='O'
                elif sum>80:
                        self.__grade='E'
                elif sum>70:
                        self.__grade='A'
                elif sum>60:
                        self.__grade='B'
                elif sum>50:
                        self.__grade='C'
                else:
                        self.__grade='F'       

                curr=datetime.datetime.now()
                cur=str(curr)             
                self.__data="\nRoll Number- "+self.roll+"\nName- "+self.__name+"\nBranch- "+self.__branch+"\n\nSemester- "+self.__sem+"\nSubjects and Marks- "+self.__submark+"\nAchieved Grade-"+self.__grade+"\nData Created on "+cur 
                myfile="data/database/"+self.roll

                if self.__grade=='O':
                     file=open("data/database/Toppers",'a')
                     file.write("\n--------------------------------\n"+self.__data)
                     file.close()
                   
                   
                if os.path.isfile(myfile)==True:
                       print(self.roll," Already Exists!")
                       
                       wf=open(myfile,'a')
                       newdata="\n\nSemester- "+self.__sem+"\nSubjects and Marks- "+self.__submark+"\nAchieved Grade-"+self.__grade+"\nData Created on "+cur
                       wf.write(newdata)
                       wf.close()
                       print(self.roll," Updated!")
                   
                else:
                       stud[self.roll]=self.__data
                       directory()       
          
                       wf2=open(myfile,"w+")
                       wf2.write(self.__data)
                       wf2.close()
                print(self.roll," Saved!")
                ext()   
         
               
     def display(self):
         print(self.__grade)
         


# main
os.system("cls")

file=open("data/imp/Acesscode",'r')
acesscode=file.readline()
file.close()

if os.path.isdir("data/database")==False:
       os.mkdir("data/database") 

        
password()
