'''for i in range(1,6,1):
    print(i)

num=1
while num<6:
    
    print(num)
    num+=1
  
i=1
while i<6:
    j=1
    while j<=5:
        print(j,end=" ")
        j+=1
    i+=1
    print()
 
for i in range(1,5):
     for j in range(1,21):
         print(j,end=" ")
     print()                   

string=input("Enter a string: ")
char=input("Enter the character you want to find: ")
i=0
count=0  
while i<(len(string)):
    if string[i]==char:
        count+=1
    i+=1  
print("The total accurance ",count)  
 
lower_bound=int(input("Enter a lower number: "))
upper_bound=int(input("Enter the higher number: "))
for num in range(lower_bound,upper_bound+1):
    for j in range(2,num):
        if num%j==0:
            break
    else:
        print(num)
      '''    
num=int(input("Enter number: "))
rem=0
t=num
numlen=0
while t>0:
    numlen=numlen+1
    t=int(t/10)
if numlen>=4:
    numlen=int(numlen/2)
    chick=0
    while num>0:
        rem=num%10
        if chick==numlen:
            midone=rem    
        elif chick==(numlen-1):
            midtwo=rem 
            
        num=int(num/10)
        chick=chick+1
    prood=midone*midtwo
    print(prood)        
            