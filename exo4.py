
print('exercices from kimi ai')
print('first exercice \n')
name = input('what is your name ? \n')
age = int(input('how old are you ? \n'))
print(f'hello {name.title}! In 10 years you will be {age+10} years old\n')

print('secend exercice \n')
degree = float(input('type a degree : '))

if degree>=90:
    print('Excellent')
elif degree>=75:
    print('Very Good')
elif degree>=60:
    print('Good')
elif degree>=50:
    print('Pass')
else:
    print('Fail \n')

print('exercice 3 :\n')


year = int(input('enter the year : '))
if year>0:
    if year%400==0:
        print(f'this year {year} is a leap year')
    elif year%100==0:
        print('it not leap year')
    elif year%4==0:
        print(f'this year {year} is a leap year')
    else:
        print(f'this year {year} is not leap year')
else:
    print("there is no negative number")

