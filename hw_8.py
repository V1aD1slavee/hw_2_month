import sqlite3
import random

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS clients(
id INTEGER PRIMARY KEY,
name VARCHAR (50) NOT NULL,
surname VARCHAR (80) NOT NULL,
age INTEGER NOT NULL,
email TEXT DEFAULT NULL,
balance DOUBLE (8,2),
props VARCHAR (20) NOT NULL,
is_active BOOLEAN DEFAULT FALSE
);
"""
)


class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.email = None
        self.balance = 0
        self.props = None
        self.is_active = False

    def new_props(self):
        self.props = str(random.randint(1000000, 99999999))

    def register(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.new_props()
        cursor.execute(
            f"""INSERT INTO clients (name, surname, age, email, balance, props, is_active)
                       VALUES ('{name}', '{surname}', '{age}', '{email}', 0, '{self.props}', True);"""
        )
        connection.commit()

    def refill(self, amount):
        if amount > 1000000:
            print("Ограничение по пополению счёта не свыше 1000000 сом")
        elif amount <= 1000000:
            print("Счёт пополнен!")
            self.is_active = True
            commission = 5
            total_amount = amount - commission
            cursor.execute(
                f"""UPDATE clients SET balance = balance + {total_amount} WHERE email = '{self.email}'"""
            )
            self.balance += total_amount
            connection.commit()

    def withdrawal(self, amount):
        if amount < 20:
            print("Минимальная сумма списания 20 сом")
        elif amount > self.balance:
            print("Недостаточно средств ")
        else:
            cursor.execute(
                f"""UPDATE clients SET balance = balance - {amount} WHERE email = '{self.email}'"""
            )
            connection.commit()
            self.balance -= amount
            print(f"Ваш баланс: {self.balance} сом.")

    def main(self):
        while True:
            print("Выберите действие:")
            choise = int(
                input(
                    "1-Регистрация, 2-Пополнить счёт, 3-Вывести деньги, 4 - Сумма на счёте 0-Выйти \n: "
                )
            )
            if choise == 0:
                print("Всего доброго!")
                break
            elif choise == 1:
                name = input("Введите ваше имя: ")
                surname = input("Введите вашу фамилию: ")
                age = input("Введите ваш возраст: ")
                email = input("Введите ваш email: ")
                self.register(name, surname, age, email)
            elif choise == 2:
                amount = int(input("Введите сумму для пополнения: "))

                self.refill(amount)

            elif choise == 3:
                amount = int(input("Введите сумму для снятия: "))
                self.withdrawal(amount)
            elif choise == 4:
                print(f"ваш баланс {self.balance}")
            else:
                print("Ошибка, попробуйте еще раз")


mbank = Bank()
mbank.main()
mbank.new_props()
