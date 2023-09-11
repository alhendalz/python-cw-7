class person :
    name = "zahraa"
    age = 18

FIRST_PERSON = person
print(FIRST_PERSON.name)
print(FIRST_PERSON.age)


class person :
    def person(is_adult):
        if is_adult > 18:
         print("you have too much responsibilties")
        if is_adult < 18: 
            print("you lucky")

class person:
    def __init__(self , name , age):
        self.name = "zahraa"
        self.age = 18
FIRST_PERSON = person("zahraa" , 18)
print(FIRST_PERSON.name)
print(FIRST_PERSON.age)
second_person = person
print("My name is Jhon and I am 22 years old")