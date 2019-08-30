def reversed(str):
     str2 = str[::-1]
     li=[]
     li = str.split(" ")
     li_rev = li[::-1]

     for i in li_rev:
         print(i,end=" ")
     print("\n")
     print(str2)

str = input("Enter the string\n")
reversed(str)
