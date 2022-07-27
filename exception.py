'''
num1=input("enter a number")
print(num1)
'''
num1=int(input("enter first number : "))
num2=int(input("Enter second number : "))
list1 =[1,2,3]

try:
    print(list1[9])
    print(num1/num2)
except ZeroDivisionError:
    print("Cannot divide by zero!")
exception IndexError:

    print("List is out of bounds")
finally:
    print("Ended try catch block")

    print("Progrsm ended")
