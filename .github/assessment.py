#survey 
import time
number=int
age=int
print("welcome to my questionare.")
time.sleep(1)
Name=input ("whats your name? ")
time.sleep(1)
age=int(input ("Whats your age? "))
#try fix < and > (fixed)
time.sleep(1)
if age < 8:
    print("youre too young try our questionare for younger ones")
if age > 13: 
    print ("just a tad too old. why dont you try out our questionare for older kids")
elif age:
    print ("shall we get started")
