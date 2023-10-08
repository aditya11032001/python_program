lst=[]
list_num=int(input("Enter the number of list:"))
for i in range(list_num):
    list_item=int(input("Enter item:"))
    lst.append(list_item)
print("Original list:",lst)
lst.sort()
lst1=list(set(lst))
lst1.sort()
print("****************************************************")
print("Smallest element in list:",min(lst))
print("Second Smallest element in list:",lst1[1])
print("Largest element in list:",max(lst))
print("Second largest element in list:",lst1[-2])
