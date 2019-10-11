def board(n):
    for i in range(1,n+1):
        if(i%2==0):
            for j in range(int(n/2)+1):
                print('|',end=" ")
            print()
        else:
            for j in range(n):
                print('-',end="")
            print()
n=int(input())
board(n)
