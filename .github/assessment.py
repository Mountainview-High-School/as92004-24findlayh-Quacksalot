#survey 
import time
print("welcome to my questionare.")
time.sleep(1)
Name=input ("whats your name? ")
time.sleep(1)
age=input ("Whats your age? ")
if age < 8:
    print("youre too young try our questionare for younger ones")
else:
    print ("shall we get started")
if age > 13: 
    print ("just a tad too old. why dont you try out our questionare for older kids")
else:
    print ("shall we get started")