#import numpy as np
from mpmath import *
print("Which operation do you want?(Basic/Trigonometric/Exponential/Logarithmic)")
response = input().lower()
while True:
    if response == "basic":
        print("Choose among: +, -, /, *")
        res1 = input()
        print("Numbers:")
        a,b = input().split()
        a = float(a);b = float(b)
        if res1 == "+":
            print(a,"+",b,"=",a+b)
        elif res1 == "-":
            print(a,"-",b,"=",a-b)
        elif res1 == "/":
            print(a,"/",b,"=",float(a/b))
        elif res1 == "*":
            print(a,"*",b,"=",a*b)
        else:
            print("wrong input")
    elif response == "trigonometric":
        print("Choose among: sin, cos, tan, cosec, sec, cot")
        res2 = input()
        print("Degrees or Radians?")
        b = input().lower()
        print("Angle:")
        a = float(input())
        if b == "degrees":
            a = (pi*a)/180
            if res2 == "sin":
                print("sin(",a,") = ",sin(a))
            elif res2 == "cos":
                print("cos(",a,") = ",cos(a))
            elif res2 == "tan":
                if sin(a)==0:
                    print("Error")
                else:
                    print("tan(",a,") = ",sin(a)/cos(a))
            elif res2 == "cosec":
                if sin(a)==0:
                    print("Error")
                else:
                    print("cosec(",a,") = ",1/sin(a))
            elif res2 == "sec":
                if cos(a)==0:
                    print("Error")
                else:
                    print("sec(",a,") = ",1/cos(a))
            elif res2 == "cot":
                if cos(a)==0:
                    print("Error")
                else:
                    print("cot(",a,") = ",cos(a)/sin(a))
        elif b == "radians":
            if res2 == "sin":
                print("sin(",a,") = ",sin(a))
            elif res2 == "cos":
                print("cos(",a,") = ",cos(a))
            elif res2 == "tan":
                if sin(a)==0:
                    print("Error")
                else:
                    print("tan(",a,") = ",sin(a)/cos(a))
            elif res2 == "cosec":
                if sin(a)==0:
                    print("Error")
                else:
                    print("cosec(",a,") = ",1/sin(a))
            elif res2 == "sec":
                if cos(a)==0:
                    print("Error")
                else:
                    print("sec(",a,") = ",1/cos(a))
            elif res2 == "cot":
                if cos(a)==0:
                    print("Error")
                else:
                    print("cot(",a,") = ",cos(a)/sin(a))
        else:
            print("wrong input")
    elif response == "exponential":
        print("Numbers:")
        a,b = input().split()
        a = float(a)
        b = float(b)
        print(a,"^",b,"=",a**b)
    elif response == "logarithmic":
        print("Numbers:")
        a,b = input().split()
        a = float(a)
        b = float(b)
        print("log",a ,"to the base", b, "=",log(a)/log(b))
    else:
        print("This is operation isn't supported in this calculator")
    print("Which operation do you want?(Basic/Trigonometric/Exponential/Logarithmic/Quit)")
    response = input().lower()
    if response == "quit":
        break
