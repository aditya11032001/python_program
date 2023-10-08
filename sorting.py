#sorting of list

n=int(input("enter the number want in list:"))
lst=[]
i=0
while(i<n):
    m=int(input("enter value:"))
    lst.append(m)
    i+=1
print("original list is:",lst)

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]<=lst[j]):
            break
        else:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("sorting list is:",lst)
        
