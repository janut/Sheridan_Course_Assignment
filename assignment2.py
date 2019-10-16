# https://chrisalbon.com/python/basics/strings_to_datetime/ --> convert string to date
from datetime import datetime
from datetime import date
#import dateutil.parser

# to convert the string/letter to lower case

def uppercase(gen):
    g = gen.upper()
    return g

# check what the letter is and translate it
def gendercheck(g):
    if g == 'M':
        gen = "Male"
        ref = "He was"
        pro = "his"
    elif g == 'F':
        gen = "Female"
        ref = "She was"
        pro = "her"
    elif g == 'N':
        gen = 'Non-binary'
        ref = "They were"
        pro = "their"
    else:
        gen = "with no gender provided"
        ref = "She/He/They"
        pro="his/her/their"
    return gen , ref , pro


#  check SIN#
def sinCheck (a):
    '''if a.isdigit():
         print("It's a digit!")
    else:
         print("It's not a digit!")

    if (len(a) == 10):
        print("It's exactly 10 digits long") #digits might also mean characters!
    else:
        print("It's not exactly 10 digits long") # digits might also mean characters!
'''
    if a.isdigit():
        if len(a) == 10:
            sinnum = a
        elif len(a) < 10:
            sinnum = "not valid SIN#"
        elif len(a) > 10:
            sinnum = "not valid SIN#"
    else:
        sinnum = "not valid SIN#"

    return sinnum


# calculate age
def calculateAge(birthDate):
    today = date.today()
    #print (birthDate.year)
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

# ask for the name
name = input("Enter your name: ")
name = name.title()

# ask for the gender
g=input("Enter your gender (M/F/N): ")
gender = uppercase(g)
gender, ref, pro = gendercheck(gender)
#print(gender)

#ask for date of birth
dob=input("Enter your date of birth in the format DD/MM/YYYY : ")

try:
    dt_start = datetime.strptime(dob, '%d/%m/%Y')
    #print(dt_start)
except ValueError:
    dt_start = datetime.strptime("02/07/2019", '%d/%m/%Y')
    print("Incorrect format for date of birth")



d = dt_start.date()
age = calculateAge(d)
#print(age)

# ask for the city of birth
city = input("Enter the city of the birth: ")
city = city.title()

# ask for SIN # and check
sin = input("Enter the SIN#: ")
sin =sinCheck(sin)

#print out for the User
print(f"{name} is a {age} years old {gender}. {ref} born in {city} and {pro} SIN# is {sin}")
