'''
Напишіть клас Bank для опису простих операції з вашим банківським рахунком: 
покласти на рахунок, 
зняти з рахунку, 
переглянути рахунок.

 При створенні екземпляру класу, екземпляр отримує атрибут __balance з певним значенням. Клас повинен містити методи для додавання коштів на рахунок і знімання з рахунку, за умови, що на рахунку достатньо коштів.


'''

class Bank:


    def __init__(self, initial_balance = 0 ) -> None:
        self.__balance = initial_balance
    
    def put_money(self, amount):
        if amount > 0:
             self.__balance += amount
             print(f"Ви успішно поклали {amount:.2f} грн на рахунок. Ваш новий баланс: {self.__balance:.2f} грн.")
        else:
             print("Неможливо покласти негативну суму.")

    def get_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Ви зняли {amount:.2f} грн з рахунку. Ваш новий баланс: {self.__balance:.2f} грн.")
        elif amount <= 0:
            print("Неможливо зняти негативну суму.")
        else:
            print(f"Недостатньо коштів на рахунку. Максимальна сума зняття: {self.__balance:.2f} грн.")
        
    def check_money(self):
        print(f"Ваш баланс: {self.__balance:.2f} грн.")

bank_account = Bank(1000)

bank_account.put_money(500)

bank_account.get_money(200)

bank_account.check_money()

bank_account.get_money(1500)

bank_account.put_money(-100)