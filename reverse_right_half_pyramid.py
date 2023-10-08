def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(n-i):
            print("*",end=" ")
        print()
n=int(input("Enter the Number of Rows :"))
pattern(n)
