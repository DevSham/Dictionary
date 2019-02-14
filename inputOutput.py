#prompting user to enter their year of birth.
dob = input("please enter your yeaar of birth:")
#change input immediately to integer since its captured as string.
year = int(dob)
age = 2019 - year
if age<18 :
    print("user is a minor.")
elif age >=18 and age<=36:
    print("user is a youth.")
else:
    print("user is an elder.")