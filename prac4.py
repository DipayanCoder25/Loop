'''num=int(input("Enter a numerator: "))
num2=int(input("Enter a demonerator: "))
if num % num2 ==0:
    print(f"{num} is divisible by {num2}")
else:
    print(f"{num} is not divisible by {num2}")
    
import random
name=input("Enter a name: ")
salami=["1000BDT","120BDT","100BDT","12"]
letter=input("Enter a single character: ")
if len(letter)==1 and letter.isalpha():
    salami_selected=random.choice(salami)
    if len():
    print(f"{name} has gotten {salami_selected}")
else:
    print("Enter a valid chracter")      
    
mean1=23
total_num=30
intial_num=12
wrong_num=14
correct_num=6
sum=mean1*total_num
num2=(sum-(wrong_num)-(correct_num))
print("new num is :",num2)
ans=num2/total_num
print(ans)
  
  
num1=input("Enter a number: ")
num2=input("Enter another number: ")
print("Before swapping num1=",num1,"Num2=",num2) 
temp=num1
num1=num2 
num2=temp
print("After swapping num1=",num1,"Num2=",num2) 

num=int(input("Enter your number: "))
if num>0:
    if num%2==0:
        print("Possitive and even number")
    else:
        print("Possitive and odd number")
        
else:
    if num%2==0:
        print("Negative and even number")
    else:
        print("Negative and odd number")
               
        
               
        
medical_cuz=input("Enter do you have any medical causes: Y or N: ").lower()
attendence=int(input("Enter your ateendence:"))
if medical_cuz=='y':
    print("Your're allowed")
else:
    if attendence>=75:
        print("You're allowed")
    else:
        print("Your're not allowed") 
       
electticity_unit=int(input("Enter electricity amount: "))
if electticity_unit >50:
    amount= electticity_unit*2.50
    service_charge=30
    total_amount=amount+service_charge
    print(f'The total amount is {total_amount}')
elif electticity_unit >90:
    amount= electticity_unit*5.50
    service_charge=70
    total_amount=amount+service_charge
    print(f'The total amount is {total_amount}')
elif electticity_unit >120:
    amount= electticity_unit*12.50
    service_charge=130
    total_amount=amount+service_charge
    print(f'The total amount is {total_amount}')
elif electticity_unit >200:
    amount= electticity_unit*17.50
    service_charge=190
    total_amount=amount+service_charge
    print(f'The total amount is {total_amount}')
elif electticity_unit >300:
    amount= electticity_unit*20.50
    service_charge=200
    total_amount=amount+service_charge
    print(f'The total amount is {total_amount}')
 
print("What you want to ride? 1.Car or 2.Plane ")    
option=input("Enter what you want to ride")
if option==1:
    print("What type of Car you want to chose")
    print("1.Racing")
    print("2.Expensive")
    print("3.Normal")
    choice=input("Enter car type")
    if choice==1:
        print("You got a Racing car")
    elif choice==2:
        print("You got a expensive car")
    else:
        print("You got a normal car")     
elif option==2:
      print("What type of plane you want to buy?")
      print("1.Normal") 
      print("2.Private jet")
      print("3.Expensive")
      choice=input("Enter what type of plane you want to buy:")
      if choice==1:
          
          print("You bought a normal plane")
      elif choice==2:
          
          print("You bought a private jet.")
      else:
          print("You bought a expensive plane.Weldone")
else:
    print("Invalid option.Press 1 or 2")
   
name = input("Enter your name here: ")
gmail = input("Enter your gmail here: ")
password = input("Enter your password here: ")

# Check if any fields are empty and print them
if name == "" or gmail == "" or password == "":
    print("The following segment(s) are empty:")
    if name == "":
        print("- Name")
    if gmail == "":
        print("- Gmail")
    if password == "":


    
    correct_password = "!QAZ@WSX"
    if password == correct_password:
        print("Registration Completed")
    else:
        print("Passoword doesn't match")
else:
    print("Something went wrong")
    print("404")


string1=input("Enter a string: ")
string2=""
for i in string1:
    string2 = i+ string2
print("The reversed string",string2)   
print("The normal string",string1) 
  '''
for i in range(10,1,-1):
    print(i)  