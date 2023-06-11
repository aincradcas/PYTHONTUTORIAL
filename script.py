#import time

#Learning python with baqir


#print("Text Here")     #This prints this text in to the console

#variables are things that store a value for example x = 2
#this means that x = 2 so if you would print(X) then it would com up as 2

#first_name = "Baqir"     #This is a variable of my name
#last_name = "Khan"
#full_name = first_name +" "+ last_name   #the 2 strings in the middle make a space
#print(type(name))   #This check the data type so it check if it a string
#print("Hello "+full_name)         #This prints my name and hello

#int data type is basically a whole number not a decieml number that we can do math with

#divide = /
#multiplication = *
#plus = +                     #pretty basic
#minus = -

#age = 14
#age = age + 1  #1st way of increasing
#print(age + 1)   #2nd way of increasing
#age += 1      #thirdway
#print(type(age))    #cheching data type
#print("Your age is "+str(age))   #this is making the int value into a string value
#so we could use in the sendtance

#The Float Data type
#Float data type is basically decimels so int you couldnt storedecimels but in floats you can

#height = 255.5
#print("Your height is" +" " +str(height)) #makes height into a string data type so you could use it
#print(type(height))  #CLASS FLOAT

#boolean is basically true or false

#human = False  #bolean
#print("Are you a human "+str(human)) #changing it from a bool to string
#print(type(human))   #checkiing the data type

#BASICS OF VARIABLES DONE

#---------------------------------------------------------------------------------------------------#

#multiple assignment is to assign multiple variables at the same time in 1 line of code

#name = "Baqir"
#age = 14
#Strong = True

#name, age, Strong = "Baqir", 14, True
 #print(name, age, Strong)     #this is multiple assignment

#print(name)
#print(age)      #prints these all at once  THIS ISNT MULTIPLE ASSIGNMENT
#print(Strong)

#name = "Baqir"   #time stamps 20 51

#print(len(name))   #  this shows how long our name is so baqir has 5 letters
#print(name.find("B"))     #shows us where the letter is so it is the first so it is 0
#print(name.capitalize())      #Capatilize only the first letter of the word
#print(name.upper())    #makes string all upper case
#print(name.lower()) #prints as all lower
#print(name.isdigit()) #checks if it is a digit number
#print(name.isalpha()) #checks if it is in the alphabet
#print(name.count("a"))  #checks how much of theat letter their is
#print(name.replace("a", "o")) #replaces letters with other letters
#print(name*3)   #multiply the string

#type casting converts 1 data type to another

#x = 2

#print(str(x))             #converts x into string data type
#print(type(str(x)))

#name = input("What is your name: ")    #input gives user input to type something in
#print("Your name is " +name)
#age = input("What is your age: ")
#print("WOW your "+ age)                                 #Everything is asking the user something
#Rizz = input("How much rizz do you have ")
#print("Oh so you have: " +Rizz+ " rizzz")

#import math

#pi = 3.14
#x = 10
#y = 6

#print(round(3.14))    #this rounds the number
#print(pi.__ceil__()) #this rounds number up
#print(pi.__floor__())   #this rounds number down
#print(abs(pi)) #show us the absolute value of the number or variable
#print(pow(pi, 2))   #rounds number to something
#print(math.sqrt(pi))          #square root number ONLY IN THE MATH MODULE (import)
#print(max(pi, x, y))   #checks which is the largest number
#print(min(pi,x,y))    #prints the smallest number

#string slicing basicall slices strings or in other words extracts elements from another string to another

# indexing []  or   slicing ()   [start:stop:step]

#name = "aincradcas"
#first_name = name[0:7]     #this only prints out aincrad instead of all of it
#last_name = name[7:10]
#funky_name = name[0:10:2]    #steps basically only say the letters that are 2 after in or case
#reversed_name = name[::-1]    #this reverses our name
#print(last_name)
#print(first_name)
#print(funky_name)
#print(reversed_name)

#website = "http//google.com"
#website1 = "http//bing.com"
#slice1 = slice(6,-4)
#print(website1[slice1])

#slice = slice(6,-4)

#print(website[slice])     #this is how to use it

#if statements are block of code that checks if it is true if it is another code starts running

#age = int(input("How Old Are You: "))

#if age >= 20:                  #check if age is greater then 20 if it is it prints message
    #print("Your are getting old ")

#elif age == 100:
    #print("you a very old ")

#else:
  #  print("You Are Young Enjoy Your Life! ")    #if not true this prints out


#logical oeprators (and.or.not) check if 2 or more stameents are true

#temp = int(input("What Is The Temperature Outside?: "))

#if not(temp >= 0 and temp <= 30):
   # print("Is Is Good Weather Outside! ")

#if temp >= 31 and temp <= 60:
    #print("It is very hot")

#if temp <= -1 and temp >= -10:
   # print("Shiverrrrrrr")

#elif temp > 0 or temp < 0:
    #print("its o")

#while loop is omething that will run its code if the condition is true

#name = ""
#while len(name) == 0:
    #name = input("Enter Your name: ")
   # print("ENTER YOUR NAME PLEASE ")
#print("Hello " +name)

#1 7 31

#for loops are things that will execute block of code limited amount of time

#for i in range(10):
   # print(i+1)

#for i in range (100,200,2):   #start,end,step
   # print(i)

#for i in "baqir":
#print(i)

#for c in "doctor":
  #  print(c)



#for seconds in range(10,0,-1):
   # print(seconds)
    #time.sleep(1)
#time.sleep(3)
#print("Happy New Year! ")

#nested loops one loop inside another loop

#rows = int(input("HOW MANY ROWS DO YOU WANT: "))
#columns = int(input("HOW MANY COLUMNS DO YOU WANT: "))
#symbol = input("Enter the symbol: ")

#for i in range(rows):
    #for j in range(columns):
     #   print(symbol, end="")
   # print()

#loop control statements change the origanal execution

#while True:
    #name = input("Enter Your Name ")
    #if name != "":
       # break

#trap_number = 123-242-242
#for i in trap_number:
   # for i == "-":
       # continue
        #print(i)

#for i in range(10,15):
  #  if i == "13":
      #  pass
  #  else:
        #print(i)



#list are used to store  multiple items in 1 Variable

#list = ["Pizza","Burger","ButterChicken"]      #[] in a variable make it a lst

#list.append("Ice cream")
#list.append("your mom ")
#list.remove("Burger")
#list.pop()
#list.insert(1,"your dad ")
#list.sort()
#list.clear()


#for i in list:
    #print(i)

#2d lists are list in lists

#drinks = ["coke","pepsi","drpepepr"]
#dinner = ["butter chicken","salan","pakora"]
#dessert = ["Ice cream","chocolate","sweet bread"]

#food = [drinks,dinner,dessert]

#print(drinks[0])

#tuple

#student = ("bro",14,"male")

#print(student.count("bro"))
#print(student.index("male"))


#set

#utensils = {"fork","knife","spoon"}
#dishes = {"plate","bowl","cup"}

#utensils.add("napkin")
#utensils.remove("knife")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)


#for x in dinner_table:
    #print(x)

#capitals = {"UK":"London",
        #    "Japan":"Tokyo",
          #  "Russia":"moscow",}

#print(capitals["Japan"])
#print(capitals.get("UK"))
#print(capitals.keys())
#print(capitals.values(),capitals.keys())
#print(capitals.items())

#for key, value in capitals.items():
      #    print(key, value)

    #index operators []

#name = "baqir ali"

#if(name[0].islower()):
   # name = name.capitalize()

#first_name = name[0:5].upper()
#last_name = name[6:9]

#print(name)
#print(first_name)
#print(last_name)

#function is a block of code that you can run when called

#def hello(name):
   # print("hello kid " +name)
   # print("Have a nice day")

#hello(input("WHAT IS YOU NAME: " ))

#return staements are used in fuction to return the value back to the caller

#def multiply(number1,number2):
    #return number1 * number2

#x = multiply(2,3)

#print(multiply(2,3))

#def hello(first,middle,last):
   # print("Hello "  +first+" "+middle+" "+last)

#hello(middle = "ali",last = "khan",first = "baqir")

#print(round((abs((float(input("Type a pos number: " )))))))

#scope is the region that the variable is rcognized

#def name():
    #name = "Bro"    #in the function the variable is  local but outside it is global
   # print(name)

#args

#def add(*args):
  #  sum = 0
   # for i in args:
    #    sum += i
   # return sum
#print(add(1,2,3))

#animal = "cow"
#item = "moon"

#import random

#x = random.randint(1,6)


#roll = input("Do you want to roll a die?: ")
#print("Your die has landed on: " +str(x))

#myList = ["rock","paper","scisors"]
#z = random.choice(myList)
#ques = input("Do you want to play rock paper scisors?: " )
#boom = input("ROCK PAPER SCISSORS(put your answer here) " )

#print(z)

#cards = [1,2,3,4,5,6,7,8,9]
#random.shuffle(cards)
#print(cards)
#try:
    #num = int(input("Type the number you want to divide: "))
    #den = int(input("Type the denominater "))
   # result = num / den
   # print(result)
#except ValueError:
   # print("You cant divide with letters")
#except ZeroDivisionError:
 #   print("You cant do division with zeros :(")
#except Exception:
# print("SomeThing Went Wrong :(")

#file detection

#import os

#path = "C:\\priv stuff"

#if os.path.exists(path):
   # print("Path Exist :)")
   # if os.path.isfile(path):
   #     print("This is a file ")
  #  elif os.path.isdir(path):
   #     print("This is a directory ")
#else:
  #  print("It does not excist :(")
#import os

#with open("test13.txt"): as file:
#print(file.read())


#object oreindted


#class GundamBox:


   # def __init__(self,picture,image,inside,componyBrand):
      #  self.picture = picture
      #  self.image = image
       # self.inside = inside
       # self.componyBrand = componyBrand


       # def Open(self):
       #  print("The box is opening ")

       # def Close(self):
         #print("Box is closing ")

# inheritance

#class Animal:

   # alive = True
   # move = True
   # eatsMeat = True
   # eatsVeg = True

   # def eat(self):
     #   print("The animal is eating ")

   # def sleep(self):
     #   print("The animal is sleeping ")

#class Lion(Animal):
   # pass

#class Cheetah(Animal):
   # pass

##class Cow(Animal):
  #  pass

#lion = Lion()
#cheetah =Cheetah()
#cow = Cow()

#print(lion.alive)
#cheetah.eatsMeat
#cow.sleep()

#super func

#class Toy:
   # type = None

#def changeColour(toy,type):

   # toy.type = Anime

#toy1 = Toy()
#toy2 = Toy()
#toy3 = Toy()

#changeColour(toy1,"AnimeGoku")

#print(toy1.type)

#functions to variable 

#filter

#gui windows

#from tkinter import *

#window = Tk()     makes a variable for the window
#window.geometry("420x420")     changes the size of the window
#window.title("My first GUI")      titile of the window

#Icon = PhotoImage(file="img.png")   photo of the window
#window.iconphoto(True,Icon)       icon on the top left
#window.config(background="lightblue")     back round clolour

#window.mainloop()   the actual window 


#label

#from tkinter import *

#window = Tk()

#window.config(height=500,width=500)
#photo1 = PhotoImage(file="img.png")
#label = Label(window,text="This Is A Test :)"
           #   ,font=("Arial",50,"bold")
           #   ,fg = "light blue",bg="black",relief="sunken",bd=10,
           #   image=photo1,height=1080,width=1920,
            #  compound="center")
#label.pack()

#window.mainloop()

#from tkinter import*

#count = 0

#def click():
#    global count
  #  count+=1
  #  print(count)

#window = Tk()
#photo = PhotoImage(file="img.png")

#button = Button(window,
          #      text="CLICKME",
           #     command=click,
           #     font=("Arial",50),
            #    fg="red",
             #   activeforeground="white",
              #  activebackground="black",
            #    image=photo,
              #  compound="center")
#button.pack()


#window.mainloop()

#entry box 

#from tkinter import *
#window = Tk()

#def submit():
   ## username = entry.get()
   # print("Hello " +username)


#entry = Entry(window,
    #          font=("Arial",100),
  #            fg="pink")
#entry.pack(side="left")
#window.title("TEST")
#submitButton = Button(window,text="submit",command="submit")
#submitButton.pack(side="right")

#window.mainloop()

#checkbox

#def display():
   # print("chek")
#from tkinter import *
#window = Tk()
#x = IntVar()
#checkbutton1 = Checkbutton(window,
      #                     text="DO YOU AGREE?",
       #                    variable=x,
       #                    command=display)
#checkbutton1.pack()

