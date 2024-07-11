# class Person:
#     pass  # Порожній блок для тіла класу

# p = Person() # об'єкт-екземпляр класу

#========================================
class User:
    name = 'Anonymous'
    age = 15

user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = "John"
user2.age = 90

print(user2.name)
print(user2.age)


#++++++++++++++++++++++++++++++++

class User:
    name = None # властивості, атрибути
    age = None
    phone = None

    def greeting(self ):   # метод клaсу
        return f"I'm {self.name}"

user_1 = User() # обʼєкт класу User
user_1.name = "Mariia"
user_1.age = 34
user_1.phone = '089898' # викликаємо атрибути
print(user_1) # <__main__.User object at 0x104458d10>
print(user_1.name) # Mariia
print(user_1.greeting())# викликаємо метод класу I'm Mariia

#++++++++++++++++++++++++++++++++   Наслідування
class Person:
    name = None

    def greeting(self):
        print(f"I'm {self.name}")
    
class Developer(Person):
    def do_job(self):
        print(f"I'm {self.name} writting code at that moment")
    
    # створимо обʼєкт класу Джуніор

# junior = Developer()
# junior.name = "Mariia"
# junior.greeting()
# junior.do_job()


class Manager(Person):
    def manage(self):
        print("Deadline is coming")

class TeamLead(Developer, Manager):
    def manage(self):
        print("I'm TeamLead")
        return super().manage()

teamLead = TeamLead()
teamLead.name = 'Lev'
teamLead.greeting()
teamLead.do_job()
teamLead.manage()

