a=int(input("enter first number :"))
b=int(input("enter second number :"))
if a<b:
    small=a
else:
    small=b
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        hcf=i
print(i)
