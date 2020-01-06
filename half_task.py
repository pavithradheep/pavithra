import sys
import re
import random
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' 

def staff_login():
    username=input("Enter the username:")
    password=input("Enter the password:")
    if(username=="pavithra" and password=="P@ssw0rd"):
        enter_stud_mark()
    else:
        print("Invalid username or password")
def student_login():
    print("marks")
def student_registration():
    print("deltails")
    def name_check(name):
        if(name.isalpha()):
            return 1
        else:
            print("The name you enter is not valid")
            name_check(input("Enter the name:"))
    def check_number(mobile):
        def isValid(s):
            Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
            return Pattern.match(mobile)
        if (isValid(mobile)):
            return 1
        else:
            print ("The number you enter is not valid ")
            check_number(input("Enter the mobile number:"))        
    def check_email(email):
        if(re.search(regex,email)):
            return 1     
        else:
            print("The email ID you enter is not valid")
            check_email(input("Enter the mail ID:"))
    def password_check(passwd):
        SpecialSym =['$', '@', '#', '%'] 
        val = True
      
        if len(passwd) < 6:
            print('length should be at least 6') 
            val = False
          
        if len(passwd) > 20: 
            print('length should be not be greater than 8') 
            val = False
          
        if not any(char.isdigit() for char in passwd): 
            print('Password should have at least one numeral') 
            val = False
          
        if not any(char.isupper() for char in passwd): 
            print('Password should have at least one uppercase letter') 
            val = False
          
        if not any(char.islower() for char in passwd): 
            print('Password should have at least one lowercase letter') 
            val = False
          
        if not any(char in SpecialSym for char in passwd): 
            print('Password should have at least one of the symbols $@#') 
            val = False
        if val: 
            return val 
    def main(password):
        if (password_check(password)):
            return 1 
        else:
            print("Invalid Password !!") 
            main(input("Enter the password:"))
    print("********STUDENT REGISTRATION********")        
    name=input("Enter the name: ")
    name_check(name)
    mobile=input("Enter the mobile number:")
    check_number(mobile)
    email=input("Enter the mail ID :")
    check_email(email)
    password=input("Enter the password:")
    main(password) 
    student_ID =(random.randrange(1, 50, 2)) 
    print("student_ID:",student_ID)
    print("***Your form is submitted successfully***")
    
print("******Login Page********")
choice=int(input(("1. Student Login \n2. Staff Login \n3. Student Registration \n4. Logout \nEnter your choice:")))
if choice == 1:
    student_login()
elif choice == 2:
    staff_login()
elif choice == 3:
    student_registration()
elif choice== 4:
    sys.exit
else:
    print("You must only select either 1,2,3, or 4")
    print("Please try again")
