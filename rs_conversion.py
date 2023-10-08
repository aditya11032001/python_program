def function(n):
    facto=1
    while n>500:
        facto=int(n/500)
        fact=int(n%500)
        n=fact
    return facto
n=int(input("enter the amount :"))
m=function(n)
print("notes of 500 :",m)
    
        
