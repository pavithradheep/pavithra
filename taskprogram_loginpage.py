import sys
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
