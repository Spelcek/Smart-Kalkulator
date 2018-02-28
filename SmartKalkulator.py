#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "SmartKalkulator"

def zmnozi(x,y):
    z=x*y
    return z

def sestej(x,y):
    z=x+y
    return z

def odstej(x,y):
    z=x-y
    return z

def deli(x,y):
    z=x/y
    return z

if __name__ == "__main__": #kadar pozenemo to datoteko kot glavno, se izvede ta

    x=int(raw_input("Vnesi Številko za x"))
    print x

    y=int(raw_input("Vnesi Številko za y"))
    print y

while True:
    operation=raw_input("Izberi operacijo (+, -, *, /):")
    print "izbrali ste:" + str(operation)

    if operation=="+":
        print sestej(x,y)

    elif operation=="-":
        print odstej(x,y)

    elif operation=="*":
        print zmnozi(x,y)

    elif operation=="/":
        print deli(x,y)


    else:
        print"Nisi izbral nobene ponujene moznosti."
        break



