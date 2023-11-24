class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Имя: {self.name},Электронная почта: {self.email} ,Номер телефона: {self.phone}"


class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, grup_were_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_were_study = grup_were_study

    def study(self):
        print(f"Имя студента: {self.name} Ученическая группа: {self.group_were_study}")


class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, grup_were_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_were_teach = grup_were_teach

    def teach(self):
        print(f"Имя учителя: {self.name} \nУченическая группа: {self.group_were_teach}")


class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = admin_id

    def create_group(self):
        name_group = input("Введите название новой группы: ")
        print(f"Группа с названием '{name_group}' успешно создна!")


class Mentor(Student, Teacher):
    def __init__(self,name,email,phone,student_id,grup_were_study,teacher_id,grup_were_teach,):
        Student.__init__(self,name, email, phone, student_id, grup_were_study)
        Teacher.__init__(self, name, email, phone, teacher_id, grup_were_teach)


stud_1 = Student("Андрей", "andrey228@gmail.com", "0555555555", 1, "13-1B")
teach_1 = Teacher("Сыймык", "syimyk2005@gmail.com", "0232313243", 1, "13-1B")
admin_1 = Admin("Владислав", "vladboulderchannel@gmail.com", "0226606163", 1)
mentor_1 = Mentor("Мирослав", "miroslav228@gmail.com", "0555554422", 1, "13-1B", 1, "13-1B")

print(stud_1)
stud_1.study()


print(teach_1)
teach_1.teach()


print(admin_1)
admin_1.create_group()

print(mentor_1)
mentor_1.study()
mentor_1.teach()
