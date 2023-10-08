a=eval(input("enter the value of A :"))
b=eval(input("enter the value of B :"))

try:
    c=a/b
    print("Division of A and B :",c)
except ZeroDivisionError:
    print("this error is a zero division error")


'''
a:5
b:0
'''
