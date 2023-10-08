p=int(input("enter the first value :"))
q=int(input("enter the second value :"))
r=max(p,q)
while True:
    if r%p==0 and r%q==0:
        print(r)
        break
    r=r+1
