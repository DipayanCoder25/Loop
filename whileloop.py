'''num=int(input("Enter a number:"))
ans=0
for i in range(num,100):
    ans+=i
    i+=2
print(ans)    

num=int(input("Enter a number: "))
sum=0
i=0
while i<num:
    sum+=num
    i+=1
print(sum)   

num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if sum==num:
    print("It's an arnstrong number")
else:
    print("It's not an arnstrong number")        

i=0
while i<=0:
    print("I will run forever")
  
num1=float(input("Enter a number: "))
num2=float(input("Enter anothr number"))
while num1!=0:
    temp=num1
    num1=num2%num1
    num2=temp
hcf=num2           
print("The HCF is: ",hcf)   
'''
num=int(input("Enter a number: "))
rev=0
temp=num
while temp>0:
    rem=temp%10
    rev=rem+(rev*10)
    temp=num//10 
if rev==num:
    print("It's a palindrom ")
else:
    print("It's not a palindrom ")
            