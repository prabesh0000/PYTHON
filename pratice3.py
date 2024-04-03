try:
    x=int(input("enter the number"))

except ValueError :
    print("Please enter a valid number ")


try:
    a=int(input("enter a number"))
    x=25/a 
    print (f"your answer is {x}")

except ZeroDivisionError:
    print ("Number cannot be divided by zero") 