# HelloW.py - 1. Program
# - Indbygget funktion - print
# - Hjemmelavet funktion og betingelse

print ("hej med jer")


def pn(t):
    print("Hej med dig: ")
    print(t)
    print("Godt at se dig")
          

def lms(n):
    if n<10:
        print("tal under 10")
    elif n == 10:
        print("tal er 10")
    else:
        print("tal over 10")
    

pn("Jens")
pn("Lotte")

lms(5)
lms(24)
lms(10)

