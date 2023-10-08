amount=int(input("enter amount :"))
notes=[500,200,100,50,20,10,5,1]
notesCount={}

for i in notes:
    if amount>=i:
        notesCount[i]=amount//i
        amount=amount%i

print("notes count :")
for key,val in notesCount.items():
    print(f"{key}:{val}")
