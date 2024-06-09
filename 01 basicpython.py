print("Hellow world")

#veriable
#number
number01=10#int
number02=20.24#float
number03=1j#complex
print(number01+number02+number03)


#typecast
int_number1=int(2024)
float_number=float(20.24)
Complex_number=1j
str_num_to_text=str(int_number1)
print(int_number1+float_number+Complex_number)
print(type(str_num_to_text))

#complex
x = 1+1j
print(type(x))


a=250
print(x)
a=str(a)
print(type(a))



#Python String
text="programmer"
print(len(text))

#slicing string
text = "Hello, World!"
print(text[2:10])
print(text[:8])

#modify  string
text02="greate programmer"
tu=text02.upper()
tl=text02.lower()
print(tu,tl)

t="  programmer  "
print(t)
#after sript
print(t.strip())

#sub string separate
t1="hello programmer"
print(t1.split())

# Concatenation string

st1="good"
st2="boy"
print(st1+" "+st2)

#format String
number=15
txt=f"{number} is a odd number"
print(txt)


#operator in python
#assaign operator =

n1=10
n2=20
sum=n1+n2
subtruction=n1-n2
divition=n1/n2
multiplication=n1*n2
divisor=n2/n1
print(f"sum={sum},subtruction={subtruction},multiplication={multiplication},divition={divition}")


print("lolgical operator ")

if(n1>n2 and n1==10 or n2==20 ):
    print("conditioon work")
else:
    print("This condition not true")   

print(not 5 ==5 )

#user  input 
name=input("Enter name:")
age=int(input('Enter age :'))
section=input("enter section:")

print(name +age +section)

#Try case
try:
    print(de)
except:
    print('not valid')    

