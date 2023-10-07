# name = input('Enter you name: ')
# print('Hello ', name)

person_a_name = input("What is your name: ")
person_a_age = input('enter your age: ')

person_b_name = input("What is your name: ")
person_b_age = input('enter your age: ')

person_a_age = int(person_a_age)
person_b_age = int(person_b_age)

if person_a_age > person_b_age:
    print(person_a_name,  " is older then", person_b_name)
    print(person_a_name, "is ", person_a_age, " year old and ", person_b_name, "is ", person_b_age, " is year old")
else:
    print(person_b_name, " is older then", person_a_name)
    print(person_a_name, "is ", person_a_age, " year old and ", person_b_name, "is ", person_b_age, " is year old")
