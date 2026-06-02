#survey
import time
number=int
age=int
tries = 0
score = 0
print("welcome to my questionare for online safety.")
time.sleep(1)
Name=input ("whats your name? ")
time.sleep(1)
age=int(input ("Whats your age? "))
#try fix < and > (fixed)
time.sleep(1)
if age < 8:
    print("youre too young try our questionare for younger ones")
    exit()
if age > 13: 
    print ("just a tad too old. why dont you try out our questionare for older kids")
    exit()
else:
    print ("shall we get started")



time.sleep(1)
print("Question 1:")
time.sleep(1)
print("You want to join an online gaming site. Which of the following information is okay for you to post online?")#Answer = A
time.sleep(0.75)
print("A, a nickname?")
time.sleep(0.75)
print("B, your name?")
time.sleep(0.75)
print("C, your email address?")
time.sleep(0.75)
#figure out how to make it break after three tries DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
while not input == ("A"):
    answer = input ("Is it A, B, Or C? ").upper() 
    if answer == "A":
        print("Correct! A nickname is a great way to protect your identity online.")
    elif answer == "B" or "C": 
        time.sleep(0.75)
        print("Incorrect, Try again.")
        tries+=1
    if tries == 3:    
        break 
print (tries)



time.sleep(1)
print("Question 2:")
time.sleep(1)
print("Someone sends you a text thats is hurtful and makes you feel bad about yourself. what should you do?")#Answer = B
time.sleep(0.75)
print("A, Delete the message and try to forget about it?")
time.sleep(0.75)
print("B, Keep the text and show an adult you trust?")
time.sleep(0.75)
print("C, Text the person back saying something mean to them?")
time.sleep(0.75)
while not (input == "B" ):
    answer = input ("Is it A, B, Or C? ").upper()
    if answer == "B":
        print("Correct! Always show a trusted adult.") 
    elif answer == "A" or "C":
        time.sleep(0.75)
        print("Incorrect, Try again.")
        tries+=1
    if tries == 3:
        break
print (tries)


time.sleep(1)
print("Question 3:")
time.sleep(1)
print("Someone in your class is a real bully. Some of the other people in your class say: 'Let's get them back, and spam them with random texts.' What do you reply?")#Answer = A
time.sleep(0.75)
print("A, 'we shouldn't be mean to them just because they're mean to us.'?")
time.sleep(0.75)
print("B, 'Yeah, totally they're evil and deserve it!'?")
time.sleep(0.75)
print("C, 'Yes, i think that is agreat idea. Maybe they will understand what it feels like, and stop bulling us!'?")
time.sleep(0.75)
while not (input == "A" ):
    answer = input ("Is it A, B, Or C? ").upper()
    if answer == "A":
        print("Correct! You should never bully somone just because they bully you.")
    elif answer == "B" or "C":
        time.sleep(0.75)
        print("Incorrect, Try again.")
        tries+=1
    if tries == 3: 
        break
print (tries)






