import sqlite3

while True:
    print("\n=========== SELECT SEMISTER ============\n")
    print("1. first semister")
    print("2. second semister")  
    print("3. third semister")
    print("4. forth semister")
    print("5. fifth semister")
    print("6. sixth semister")  
    choice = int(input("Enter the semister 1-6:- "))
    break
if choice == 1:
    print("\n=======First Semister Marks=======\n")
    name = input("Enter student first name :- ")
    name = input("Enter student roll no.:- ")
    name = input("Enter student obtained marks:- ")
    name = input("Enter student total marks :- ")
elif choice == 2:
    print("\n=======Second Semister Marks=======\n")
    name = input("Enter student first name :- ")
    roll_no = input("Enter student roll no. :- ")
    while True:
        sub_1 = int(input("Programming by usin C :- "))
        if sub_1 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_1/40
            sub_1 = marks*100
            print(f"Programming by usin C  = {sub_1}%")
            break
    while True:
        sub_2 = int(input("Programming by usin C  Lab :- "))
        if sub_2 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_2/60
            sub_2 = marks*100
            print(f"Programming by usin C  Lab = {sub_2}%")
            break
    while True:
        sub_3 = int(input("Basics Of Electronoic And Electrical Engineering :- "))
        if sub_3 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_3/40
            sub_3 = marks*100
            print(f"Basics Of Electronoic And Electrical Engineering = {sub_3}%")
            break
    while True:
        sub_4 = int(input("Basics Of Electronoic And Electrical Engineering lab :- "))
        if sub_4 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_4/60
            sub_4 = marks*100
            print(f"Basics Of Electronoic And Electrical Engineering lab = {sub_4}%")
            break
    while True:
        sub_5 = int(input("Applide Mathamatics :- "))
        if sub_5 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_5/40
            sub_5 = marks*100
            print(f"Applide Mathamatics  = {sub_5}%")
            break
    while True:
        sub_6 = int(input("Skill Development And Communication :- "))
        if sub_6 >60:
            print("Enter a marks below 40")
        else:
            marks = sub_6/60
            sub_6 = marks*100
            print(f"Skill Development And Communication = {sub_6}%")
            break
    while True:
        sub_7 = int(input("Basics of Information And Technology (BIT) :- "))
        if sub_7 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_7/60
            sub_s7 = marks*100
            print(f"Basics of Information And Technology (BIT) = {sub_7}%")
            break
elif choice == 3:
    print("\n=======Third Semister Marks=======\n")
    name = input("Enter student first name :- ")
    roll_no = input("Enter student roll no. :- ")
    while True:
        sub_1 = int(input("Data structure :- "))
        if sub_1 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_1/40
            dsa = marks*100
            print(f"Data structure = {dsa}%")
            break
    while True:
        sub_2 = int(input("Data structure Lab :- "))
        if sub_2 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_2/60
            dsa_lab = marks*100
            print(f"Data structure Lab = {dsa_lab}%")
            break
    while True:
        sub_3 = int(input("Digital Electronics :- "))
        if sub_3 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_3/40
            de = marks*100
            print(f"Digital Electronics = {de}%")
            break
    while True:
        sub_4 = int(input("Digital Electronic lab :- "))
        if sub_4 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_4/60
            de_lab= marks*100
            print(f"Digital Electronic lab = {de_lab}%")
            break
    while True:
        sub_5 = int(input("Operating System :- "))
        if sub_5 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_5/40
            os = marks*100
            print(f"Operating System  = {os}%")
            break
    while True:
        sub_6 = int(input("Computer Network :- "))
        if sub_6 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_6/40
            cn = marks*100
            print(f"Computer Network = {cn}%")
            break
    while True:
        sub_7 = int(input("Computer Netwok Lab :- "))
        if sub_7 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_7/60
            cn_lab = marks*100
            print(f"Computer Netwok Lab = {cn_lab}%")
            break
    while True:
        sub_8 = int(input("Stress Management :- "))  
        if sub_8 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_8/60
            Stress_Management = marks*100
            print(f"Stress Management = {Stress_Management}%")
            break
    while True:
        sub_9 = int(input("Multimedia :- "))
        if sub_9 >60:
            print("Enter a marks below 60")
        else:
            marks = sub_9/60
            multimedia = marks*100
            print(f"Multimedia = {multimedia}%") 
            total = 60*5+40*4
            overall = sub_1+sub_2+sub_3+sub_4+sub_5+sub_6+sub_7+sub_8+sub_9
            over = overall/total
            overall = over*100
            print(f"The all subject percentage is {overall}%")
            break
elif choice == 4:
    print("\n=======forth semister marks=======\n")
    name = input("Enter student first name :- ")
    name = input("Enter student roll no.:- ")
    name = input("Enter student obtained marks:- ")
    name = input("Enter student total marks :- ") 
      
elif choice == 5:
    while True:
        sub_1 = int(input("Python Programming :- "))
        if sub_1 >40:
            print("Enter a marks below 40")
        else:
            marks = sub_1/40
            python = marks*100
            print(f"Python Programming = {python}%")
        break
while True:
    sub_2 = int(input("Python Programming Lab :- "))
    if sub_2 >60:
        print("Enter a marks below 60")
    else:
        marks = sub_2/60
        python_lab = marks*100
        print(f"Python Programming Lab = {python_lab}%")
        break
while True:
    sub_3 = int(input("Linux Programming :- "))
    if sub_3 >40:
        print("Enter a marks below 40")
    else:
        marks = sub_3/40
        linux= marks*100
        print(f"Linux Programming = {linux}%")
        break
while True:
    sub_4 = int(input("Linux Programming lab :- "))
    if sub_4 >60:
        print("Enter a marks below 60")
    else:
        marks = sub_4/60
        linux_lab= marks*100
        print(f"Linux Programming lab = {linux_lab}%")
        break
while True:
    sub_5 = int(input("Cloud Computing :- "))
    if sub_5 >40:
        print("Enter a marks below 40")
    else:
        marks = sub_5/40
        cloud = marks*100
        print(f"Cloud Computing  = {cloud}%")
        break
while True:
    sub_6 = int(input("Cloud Computing Lab :- "))
    if sub_6 >60:
        print("Enter a marks below 40")
    else:
        marks = sub_6/60
        cloud_lab = marks*100
        print(f"Cloud Computing Lab = {cloud_lab}%")
        break
while True:
    sub_7 = int(input("Computer Peripheral :- "))
    if sub_7 >60:
        print("Enter a marks below 60")
    else:
        marks = sub_7/40
        peripheral = marks*100
        print(f"Computer Peripheral = {peripheral}%")
        break
while True:
    sub_8 = int(input("Computer Peripheral Lab :- "))  
    if sub_8 >60:
        print("Enter a marks below 60")
    else:
        marks = sub_8/60
        Peripheral_Lab = marks*100
        print(f"Computer Peripheral Lab = {Peripheral_Lab}%")
        break
while True:
    sub_9 = int(input("Industrial Traning :- "))
    if sub_9 >60:
        print("Enter a marks below 60")
    else:
        marks = sub_9/60
        Traning = marks*100
        print(f"Industrial Traning = {Traning}%") 
        break
while True:
    sub_10 = int(input("Seminar :- "))
    if sub_10 >60:
        print("Enter a marks below 60")
    else:
        marks = sub_10/60
        seminar = marks*100
        print(f"Industrial Traning = {seminar}%")
        break
while True:
    sub_11 = int(input("Minor Project :- "))
    if sub_11 >60:
        print("Enter a marks below 60")
    else:
        marks = sub_11/60
        Project = marks*100
        print(f"Minor Project = {Project}%")
        total = 60*7+40*4
        overall = sub_1+sub_2+sub_3+sub_4+sub_5+sub_6+sub_7+sub_8+sub_9+sub_10+sub_11
        over = overall/total
        overall = over*100
        print(f"The all subject percentage is {overall}%")
        break
