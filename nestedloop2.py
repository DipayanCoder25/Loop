'''for i in range(1,10,1):
    for j in range(1,5,1):
        print(j)
        print(' ')
    print("\n")    

num=int(input("Enter rows number: "))
for i in range(num):
    for j in range(i+1):
        print('*',end="")
    print(" ")      

num=int(input("Enter rows number: "))
number=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
        number+=1
    print("")    
 
num=int(input("Enter rows number: "))

for i in range(num):
    for j in range(num-i):
        print('*',end="")
    print(" ")  
     
rows=5
for i in range(rows,0,-1):
    print(' ' *(rows-i)+'*'*(2*i-1))
          '''   
          #diamond shape
rows=5
for i in range(1,rows+1):
    for space in range(rows-i):
        print(' ',end='')
    for star in range(2*i-1):
        print('*',end='')
    print("\n")  
for i in range(rows-1,0,-1):
    for space in range(rows-i):
        print(' ',end='')
    for star in range(2*i-1):
        print('*',end='')
    print("\n")                                      