a=[]
b=[]
number=int(input("How many numbers do you want in your list"))
for i in range(0,number):
    numbers=int(input("Enter the numbers into the list"))                 
    a.append(numbers)
print(a)    

def split1(a):
  
    for i in a:
        if (i%2==0):
            b.append(i)
           
split1(a)        
print(b)
