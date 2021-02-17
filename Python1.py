#Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
#What is Python? flexible programming language and designed to be human-readable.
#Why use Python? Great starter languange, Great advanced language, and Woderfull community.
#What can I build with Python? Machine learning models, Artificial intelligence, Web applications, Automation utilities, and Many more!
#What do I need to get started with python? Somewhere to run Python(Go to python.org and download the current version of Python), Somewhere to code Python(Go to Code.Visual Studio.com then download Visual Studio Code).
#Learn more at python.org, and download Python Extension for VS Code at the Marketplace.

first_name = input("What's your First Name : ")
last_name = input("What's your Last Name : ")
full_name = first_name + last_name
print('Hello' + {full_name})
#Functions to modify strings
sentence = 'I am {full_name}'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# first_name
# last_name

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
#print(first_name + last_name)
print('Hello, '+ first_name + ' ' + last_name)

# Custom string formatting
output = 'Hello, ' + first_name + ' ' + last_name
output = 'Hello, {} {}' .format(first_name, last_name)
output = 'Hello, {0} {1}' .format(first_name, last_name)
#Only available in Python 3
output = f'Hello, {first_name} {last_name}'

#Formatting Strings
first_name = 'Cynk'
last_name = 'Carillo'

output = 'Hello, ' + first_name + ' ' + last_name
output = 'Hello, '{} {}' .format(first_name, last_name)
output = 'Hello, '{0} {1}' .format(first_name, last_name)
output = f'Hello, {first_name} {second_name} '
print(output)

#Numeric Data Types
pi = 3.14159
print(pi)

#Math;
# + for addition
# - for subraction
# * for multiplication
# / for division
# ** exponent

first_sum = 6
second_sum = 2
print(first_num + second_num)
print(first_num ** second_num)

# String that contains numbers; Converting Numbers int Strings
days_in_feb = 28
print(str(days_in_feb)+ 'days in February')

#Numbers stored as Strings
first_num = '5'
second_num = '6'
print(first_num + second_num)

#Output is 56 not 30

#Input always return strings
first_num = input('Enter first number ')
second_num = input('Enter second number ')
print(first_num + second_num)

#Output is 56 not 30

#Converting Numbers stored as String must be converted to numeric vales to do Math
first_num = input('Enter first number ')
second_num = input('Enter second number ')
print(int(first_num) + int(second_num))
print(int(float(first_num) + float(second_num))

#Example output; First Number is 5 then the Second Number is 6 then the answer is 11 or 11.0
#int is to print an Integer while float is to print a decimal version

#Data Lists and Arrays
price_with_tax = price + price * federal_tax

module(current module)
#Module;
Index | Module Name
0       Data Science Concepts
1       Preparing you Data
2       Selecting features
3       Splitting your data
4       Selecting an algorithm
5       Traning your model

#Numbers
pi = 3.14159
print(pi)

first_num = 5
second_num = 6
print(first_num + second_num)
#Operation
# + for addition
# - for subraction
# * for multiplication
# / for division
# ** exponent

#Date data types
#To get current date and time
#We need to use the datetimr library
from datetime import datetime

current_date = datetime.now()
#The now function returns a datetime object
print('Today is: + str(current_date))

#Function you can use with datetime objects to manipulate dates
from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))

#Timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

#Use date function to control date formatting
from datetime import datetime
current_date = datetime.now()

print('Date: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

#Convert date as string then convert to datetime object
from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print ('Birthday: 'str(birthday_date))

#Date
#To get current date and time we need to use the datetime library
from datetime import datetime

current_date = datetime.now()
#The now function returns current date and time as a datetime object

#You must convert the datetime object to a string
#before you can concatenate it to another string
print('Today is: ' + str(current_date))


#Date function
#To get current date and time we need to use the datetime library
from datetime import datetime, timedelta
#The now function returns current date and time as a datetime object
one_day = timedelta(days=1)
yesterday = today - one_day
print('Today is: ' + str(yesterday))

one_week = timedelta(week=1)
last_week = today - one_week
print('Last week was: ' + str(last_week)

#To get current date and time we need to use the datetime library
from datetime import datetime

#The now functipon returns current and time
today = datetime.now()

#use day, month, year, hour, minute, second function
#to display only part of the date
#All these function returns integers
#Convert then to strings before concatenating them to another string
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Ssecond: ' + str(today.second))

from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print ('Birthday: 'str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Days before birthday: ' + str(birthday_eve))

#Condition logic
if price >= 1.00:
tax = 0.7
print(tax)