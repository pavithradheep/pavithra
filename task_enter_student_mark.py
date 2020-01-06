import csv
import sys
def enter_stud_mark():
        print("Enter id:")
        id=input()
        print("Enter first name:")
        firstname=input()
        print("Enter mark1:")
        mark1=int(input())
        print("Enter mark2:")
        mark2=input()
        print("Enter mark3:")
        mark3=int(input())
        print("Enter mark4:")
        mark4=input()
        print("Enter mark5:")
        mark5=int(input())
        print("Enter mark6:")
        mark6=input()
        with open('studentfile.txt','a') as studentfile:
            studentfileWriter=csv.writer(studentfile)
            studentfileWriter.writerow([id,firstname,mark1,mark2,mark3,mark4,mark5,mark6])
            print("Record has been written to file")
            studentfile.close()
        con=input("Do you want to continue y/n:")
        if con=='y':
            login()
        elif con=='n':
            sys.exit
enter_stud_mark()
