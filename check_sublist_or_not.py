L1=list(input("enter L1 element :"))
print(L1)
L2=list(input("enter L2 element :"))
print(L2)

for i in L2:
    if i in L1:
        print("yes L2 is sublist of L1")
        break
    else:
        print("no")
        break
