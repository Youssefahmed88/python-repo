'''
a="Hello, World"
print(a[0:])                                          ## print string
print(a[-1], len(a))
print(a[0::2]) #last parameter sign to steps
#///////////////////////////////////////////////     
print('i', end=' ')
print('Love', end='*')
print("Python")
print('i')                                            ##spaces, end lines
print('Love')
print("Python")
print('I', 'Love', 'python', sep=' ')
#///////////////////////////////////////////////
print('\"\"')

print(5/2)      #2.5
print(5//2)     #2
print(2**3)     #pow(2,3) = 8
x=5
print(x)
x=float(x)      #casting
print(x)
///////////////////////////////////////////////
s='hello'
print(s.lstrip())           #erase white spaces in the begining
print(s.strip())            #erase all white spaces 
print(s.lstrip('h'))        #erase first element

x=eval(input('enter your grade\n'))
if (x >= 90 and x <= 100):
    print('A')
elif x <90 and x >=80:
    print('B')
elif not x>=80:
    print('x is smaler than 80')
'''

##///////////////////////  ##For loop
'''
for i in range(5):              
    print('Hello',i)
print()
for i in 'hello':
    print(i, end=' ')      
print()
for i in range(1,7):
    print(i, end=' ')
print()
for i in range(10,0,-1):
    print(i,end=' ')
print('\n')
x=5 
while x > 0:                  ##while loop 
    print(x, end=' ')
    x -=1
print('\nDone')

x=eval(input('enter number\n'))    ## input integer, casting it to string and print len()
print(len(str(x)))

fact=1                        ##Factorial
for i in range(1,x+1):
    fact *=i
print(fact)
'''

'''
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))
x = str(num1) + str(num2) + str(num3)
x=int(x)+2
print(x)
'''

    ##program ask to print all factors of the number 
'''
num=int(input('enter num\n'))
for i in range(1, num+1):          
    if num % i==0:
        print(i, end=' ')
'''

'''
x=int(input('enter x\n'))
n1=0
n2=1
if x==1:
    print(n1)
else:
    print(n1, n2, end=' ')

for i in range(2, x+1):
    n3=n1+n2
    print(n3, end=' ')
    n1=n2
    n2=n3

'''

'''
def fun(num):
    print('the factors of', num,'are:')
    for i in range(1, num+1):
        if num % i==0:
            print(i)

x=eval(input('enter the number\n'))
fun(x)
##print(fun)
'''

#/////////////////////////////////////////////////////////////////////  list
'''
list=[1,2.3,3,'Computer Science']  ##list take ant data type

if 4.7 in list:
    print('true')
else if 4.7 not in list:
    print('false')

for i in range(len(list)):
    print(list[i], end=' ')

list *=2                     ##this line mean the list1 will be repeated twice
print('\n',list)

print(list[0:2])
'''
#////////////////////////////////////////////    #Tuple
'''
my_tuple=('Youssef', 'Developer')     ##Tuple is immutable,however there is one way to add items to tuple:
y=('pentester',)
my_tuple +=y        
print(my_tuple)

list1=list(my_tuple)                 ##to convert from tuple to list by command list()
print(list1)
'''
#///////////////////////// ##Dictionary
'''
phonebook={'Mazen':'225511229', 'Youssef':'22511229', 1:15}     ##dictionary has two parts: key,value key isn't repeatable 
if 'Mazen' in phonebook:                        ##in, not in are key words
    del phonebook['Mazen']
elif 'zein' not in phonebook:
    print('not found')
print(phonebook)               ##print phonebook with brackets
print(*phonebook, *phonebook.values())    ##print all keys and all values
for key,value in phonebook.items():       
    print(key,value,sep=':')          ##print key to value 

'''
##///////////////////////////////          #sets
'''
set1=set([5,3,7,2,1])
set2=set([5,3,9,8])
set1.add(10)
set1.update([2,13,15,19])
set1.remove(19)
set1.discard(15)
set3=set1|set2          ##union
set3=set1.union(set2)   
set4=set1.intersection(set2)    ##intersection

print(*set1)     ##to print it without brackets
print(set1)      ##to print it with brackets
print(set3,set4)
'''
#program calculates sum and average of list
'''
n=int(input('enter array size\n'))   ##take size of the list
list1=[]       ##initialize empty list
for i in range(n):
    item=int(input('enter the items of array\n'))   
    list1.append(item)              #add the item to the list
sum=0
for i in range(len(list1)):
    sum +=list1[i]
print('Sum:',sum,'Average:', sum/len(list1))
'''
#///////////////////////////////////////////////////###Function
'''
def area(a,b):
    print('Triangle\'s Area',.5*a*b)
x=eval(input('Enter the dimensions of Triangle\n'))
y=eval(input())
area(x,y)
'''
###reusing function by import*
##from file import*
'''
def count(numbers):
    even=0
    odd=0
    for i in numbers:
        if i%2==0:
            even +=1
        else:
            odd +=1
    return even,odd

numbers=[1,2,3,4,5,6,7,8,9]
even_count,odd_count=count(numbers)
print('Number of even digits:',even_count)
print('Number of odd digits:',odd_count)
'''
'''
def validate_password(paswd):
    digit = False
    lower = False
    upper = False
    for i in paswd:
        if i.isdigit():
            digit = True
        elif i.islower():
            lower = True
        elif i.isupper():
            upper = True
    if len(paswd) >= 8 and digit and lower and upper:
        return True
    else:
        return False
    
password = input('Enter your password:\n')
if validate_password(password):
    print('Valid password')
else:
    print('Invalid password')
'''

##recursion
'''
def recursion(num):                  ##  num=4 
    if num==0:                       ##  4*rec(3)
        return 1                     ##  4*3*rec(2)  
    else:                            ##  4*3*2*rec(1)
        return num*recursion(num-1)  ##  4*3*2*1*rec(0)
x=eval(input('enter number\n'))      ##  4*3*2*1*1
print(recursion(x))
'''
'''
def palindrom(word):                    ## word=racecar
    if len(word) < 2:                   ## w[0]=r  w[-1]=r  1       word=racecar
        return True                     ## w[0]=a  w[-1]=a  2       word=aceca
    elif word[0]==word[-1]:             ## w[0]=c  w[-1]=c  3       word=cec
        return palindrom(word[1:-1])    ## w[0]=e  w[-1]=e  4       word=e
    else:                               ## length of word is smaller than 2, then the end function
        return False
name=input('enter the word\n')
print(palindrom(name))
'''
'''
list1=[i for i in range(3)]       ##list comprehintion
print(list1)
list1=[i**2 for i in range(3)]
print(list1)
'''
'''
x=2.66666666666
print(format(x, '.2f'))   ##round
'''
'''
## Object-Orianted Programming  OOP
import random
class Coin:                  ##create class

    sideup='Heads'           ## data attribute
    def __inti__(self):         ##constructor function to initialize the sideup data attribute
        self.sideup='Heads'

    def toss(self):                ##method  function to toss the coin
        if random.randint(0,1)==0:
            self.sideup='Heads'
        else:
            self.sideup='Tails'

    def get_sideup(self):          ##accessor  function to return the value of sideup
        return self.sideup

##call the main function
my_coin=Coin()                                   ##create object
print('this sideup is', my_coin.get_sideup())    ##call method
my_coin.toss()                                 
print('this sideup is', my_coin.get_sideup())
'''

'''
class Vehicle:
    def __init__(self, spead, price, mileage):   ##constructor function || method to initialize the attributes

        self.spead=spead                         ##public attribute
        self.price=price                         ##public attribute

        self.__mileage=mileage                   ##private attribute

    def get_mileage(self):        ##accessor function to access || geter function to get
        return self.__mileage    
       
modelx=Vehicle(200,500,18)    ##create object 

modelx.spead=350              ##change the value of public attribute
modelx.price=25000

modelx.mileage=20             ##error because it's private attribute

print('Spead:', modelx.spead)
print('Price:', modelx.price)
print('Mileage:', modelx.get_mileage())
print(modelx)   ##print the state(address) of the object
'''

'''
class Animal:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def get(self):
        return f'\nName: {self.name}\nAge: {self.age}'

class Dog(Animal):

    def __init__(self, name, age, bread):
        super().__init__(name, age)
        self.__bread=bread

    def get_bread(self):
        return self.__bread

class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color=color

    def get_color(self):
        return self.__color

dog1=Dog('Dog', 6, 'Sephered')
cat1=Cat('cat', 2, 'White')

print(dog1.get(), cat1.get())

print('bread:',dog1.get_bread())
print('color:', cat1.get_color())
'''
'''
import tkinter

class MyGUI:
    def __init__(self):

        ##create the main window widget
        self.main_window=tkinter.Tk()

        ##display title
        self.main_window.title('My First GUI') 

        ##create label main window
        self.label=tkinter.Label(self.main_window, text='Hello, World')

        ##call the window widget pack method
        self.label.pack()

        ##enter the tkinter main loop
        tkinter.mainloop()

def main():
    my_gui=MyGUI()
'''
##opening a file
##file1=open(r'path\'s file','r')     to read file                         file1.readline() file1.close()
##file1=open(r'path\'s file','w')     to delete and rewrite the file       file1.write()    file1.close()
##file1=open(r'path\'s file','a')     to append on the file                file1.write()    file1.close()

##print(0b101)   ##binary
##print(0x1)     ##hexadicimal
##print(0o10)    ##octal
