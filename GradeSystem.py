# Teacher Name Verification 
teacher_name = ["Tahir","Techno","TAHI"]
t_name = input("ENTER YOUR NAME SIR:")
if(t_name in teacher_name):
    print("WELCOME",t_name)
else:
    print("ACCESS DENIED, SORRY",t_name,"\nEXITING...")
    exit()

# TEACHER VERIFICATION /CODE
teacher_name_password = ["t1","T1","t"] #CHANGE
password = input("ENTER PASSWORD:")
if(password in teacher_name_password):
    print("PERMISSION GRANTED\tWELCOME",t_name)
else:
    print("WRONG PASSWORD\tAccess Denied...\nEXITING...")
    exit()

# Student Verification From Lists
student_name = ["zoeya","madia","paul","netwon","motu"]
enter_student_name = input("ENTER STUDENT NAME:")
if(enter_student_name in student_name):
    print("STUDENT NAME:",enter_student_name)
else:
    print("SORRY, STUDENT IS NOT IN THE LIST\nEXITING...")
    exit()

print("\n[SUBJECTS]")

# Input subjects
s1 = input("Enter First Subject: ")
s2 = input("Enter Second Subject: ")
s3 = input("Enter Third Subject: ")
s4 = input("Enter Fourth Subject: ")
s5 = input("Enter Fifth Subject: ")

# Input marks
s1m = int(input("Enter " + s1 + " Marks: "))
s2m = int(input("Enter " + s2 + " Marks: "))
s3m = int(input("Enter " + s3 + " Marks: "))
s4m = int(input("Enter " + s4 + " Marks: "))
s5m = int(input("Enter " + s5 + " Marks: "))

# Percentage
percentage = ((s1m+s2m+s3m+s4m+s5m)/500)*100

# Fail check
if s1m<38 or s2m<38 or s3m<38 or s4m<38 or s5m<38:
    print("\n[FAILED]")

elif percentage >= 90:
    print("\n[Brilliant Student]")

elif percentage >= 80:
    print("\n[Excellent Student]")

elif percentage >= 70:
    print("\n[GOOD A++ Student]")

elif percentage >= 60:
    print("\n[GOOD A+ Student]")

elif percentage >= 50:
    print("\n[BAD, NEED TO FOCUS]")

elif percentage >= 40:
    print("\n[VERY BAD, NEED MORE FOCUS]")

# Print marks
print("Marks:", s1, s1m)
print("Marks:", s2, s2m)
print("Marks:", s3, s3m)
print("Marks:", s4, s4m)
print("Marks:", s5, s5m)

print("Percentage:", percentage)