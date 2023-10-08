while True:
 print("convert metre into feet")
 metre=float(input("enter the metre :"))
 inches=metre*40
 feet=int(inches/12)
 remain=int(inches%12)
 print(feet,"feet",end=' ')
 print(remain,"inches")
 print("if you want again conversion press 1 :")
 d=float(input())
 if d==1:
   continue
 else:
   break
 
