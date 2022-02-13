import time
import os

def clear():
    os.system('cls')

name = input("Please enter yout name : ")
group = input("please enter your class : ")
stdid = int(input("Please enter your student ID : "))
attempt = 0
x = 1
time.sleep(0.5)
clear()

print("Starting the quiz, please wait ... ")
time.sleep(1)
clear()

while x == 1:

    mark = 0
#//////////////////////////QUESTION 1//////////////////////////////////
    print("QUESTION 1",end="\n\n")

    q1 = input("what is the capital city of Malaysia : ")
    time.sleep(1)

    if q1 == "Kuala Lumpur" or q1 == "kuala lumpur":
        print ("correct !")
        mark += 1

    else:
        print ("incorrect, the answer is Kuala Lumpur")
    
    time.sleep(2)
    clear()
    

#//////////////////////////QUESTION 2//////////////////////////////////

    print("QUESTION 2", end="\n\n")

    print(" 2x + 1 = 3")
    q2 = int(input(" Find the value of x : "))
    time.sleep(1)

    if q2 == 1:
        print ("correct !")
        mark += 1

    else:
        print ("incorrect, the answer is 1")
    
    time.sleep(2)
    clear()

#//////////////////////////QUESTION 3//////////////////////////////////

    print("QUESTION 3", end="\n\n")

    print(" solve the equation in term of u")
    q3 = (input(" 9x - 7i > 3(3x - 7u) "))
    time.sleep(1)

    if q3 == ("i<3u"):
        print ("correct !")
        mark += 1

    else:
        print ("incorrect, the answer is i<3u")

    time.sleep(2)
    clear()

#//////////////////////////QUESTION 4//////////////////////////////////

    print("QUESTION 4", end="\n\n")


    q4 = float(input(" What is the first 3 digit of pi : "))
    time.sleep(1)

    if q4 == 3.142:
        print ("correct !")
        mark += 1

    else:
        print ("incorrect, the answer is 3.142")

    time.sleep(2)
    clear()

#//////////////////////////QUESTION 5//////////////////////////////////

    print("QUESTION 5", end="\n\n")

    q5 = float(input(" 10 / 4 = "))
    time.sleep(1)

    if q5 == 1:
        print ("correct !")
        mark += 1

    else:
        print ("incorrect, the answer is 2.5")

    time.sleep(2)
    clear()

#//////////////////////////end//////////////////////////////////

    print("The quiz end here", end = "\n\n")

    percentage = (mark / 5) * 100

    time.sleep(2)
    print("name :", name)
    time.sleep(0.5)
    print("class :", group)
    time.sleep(0.5)
    print("student ID :", stdid, "\n")
    time.sleep(0.5)
    print( "Mark = %0.2f" %percentage, end = "\n\n")
    time.sleep(0.5)
    print ("number of retry =", attempt)

    retry = input("would you like to retake the quiz? [y,n] : ")
    if retry == "y":
        x = 1
        attempt += 1
        clear()
    else:
        x = 0



    