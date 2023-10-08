while True:
 print("convert seconds into hours and minutes")
 sec=int(input("Enter the values of seconds :"))
 hour=int(sec/3600)
 min=int((sec%3600)/60)
 sec=(sec%3600)%60
 print("hours is :",hour)
 print("min is :",min)
 print("sec is :",sec)
 print("if want another conversion press : 1")
 c=int(input())
 if c==1:
     continue
 else:
     break
