while True:
 print("swapping the value from A to B")
 a=float(input("Enter the value A :"))
 b=float(input("Enter the value B :"))
 swap=a
 a=b
 b=swap
 print("The value of A is : ",a)
 print("The value of B is : ",b)
 print("If want another swapping press : 1")
 d=int(input())
 if d==1:
     continue
 else:
     break
