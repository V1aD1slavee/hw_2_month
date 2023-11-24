class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(
            f"Полное Имя: {self.fullname}\nВозраст: {self.age}\nСемейное положение: {self.is_married}"
        )


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience,):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 15000

    def pay(self):
        for i in range(self.experience):
            self.salary += 3000
            print(f"Имя: {self.fullname}\n Ваша зарплата состовляет:  {self.salary}")


people = Teacher("Галина Ивановна", 74, "Замужем",14)
people.introduce_myself()
people.pay()
