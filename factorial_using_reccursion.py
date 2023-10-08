def fact(n):
    facto=1
    while n>1:
        facto=facto*n
        n-=1
    return facto
n=int(input("enter the number :"))
p=fact(n)
print("factorial of",n,"is :",p)
