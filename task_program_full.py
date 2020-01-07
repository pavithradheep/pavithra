import sys
import csv
import re
import random
student_fields = ['roll', 'name', 'mark1', 'mark2', 'mark3']
student_database = 'students.csv'
 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def main():
    login()
def enter_stud_mark():
    global student_fields
    global student_database
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
    print("Data saved successfully")
    con=input("Do you want to continue y/n:")
    if con=='y':
        login()
    elif con=='n':
        sys.exit
def search_student():
    global student_fields
    global student_database
 
    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("mark1: ", row[2])
                    print("mark2: ", row[3])
                    print("mark3: ", row[4])
                    break
        else:
            print("Roll No. not found in our database")
        con=input("Do you want to continue y/n:")
        if con=='y':
            login()
        elif con=='n':
            sys.exit
            
def view_mark():
    global student_fields
    global student_database
    print("--- Student Records ---")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    con=input("Do you want to continue y/n:")
    if con=='y':
        login()
    elif con=='n':
        sys.exit
def staff_login():
    username=input("Enter the username:")
    password=input("Enter the password:")
    if(username=="pavithra" and password=="P@ssw0rd"):
        enter_stud_mark()
    else:
        print("Invalid username or password")
def student_login():
    option=input("Do you want to display all the marks:y/n")
    if option=='y':
        view_mark()
    else:
        search_student()
        
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
    con=input("Do you want to continue y/n:")
    if con=='y':
        login()
    elif con=='n':
        sys.exit
def login():
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
main()        
