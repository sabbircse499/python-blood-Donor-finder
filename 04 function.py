#general function non return and parameter function

def student():
    print("hello sabbir")

student()

#return and parameterized function
def sum(a,b):
    s=a+b
    return s

number1=int(input("Enter number one :"))
number2=int(input("Enter number two :")) 
addition=sum(number1,number2)
print(f" addition is {addition}")
