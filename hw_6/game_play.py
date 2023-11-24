import random

print("Поехали!!!")
words = ["яблоко", "ананас", "груша", "банан", "апельсин", "персик"]
word = random.choice(words)


def start():
    word_letters = []
    attempts = 3

    print("У вас 3 попытки")
    print("Удачи!")

    while attempts > 0:
        Invisible_letters = ""
        for letter in word:
            if letter in word_letters:
                Invisible_letters += letter
            else:
                Invisible_letters += "_"

        print(f"Наше слово {Invisible_letters}")
        print(f"у вас {attempts} попыток")
        user = input("Ввeдите букву: ").lower()

        if user in word_letters:
            print(f"Вы отгадали букву {user}")
            continue
        word_letters.append(user)
        
        if user not in word:
            attempts -= 1
            print("Нет такой буквы!")

        if "_" not in Invisible_letters:
            print("Победа!")
            break
        if attempts == 0:
            print("Проигрыш")
            break
start()