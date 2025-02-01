def ask_password():
    for i in range(3):
        a = input("Введите пароль: ")
        if a == password:
            print('Правильный пароль')
            return
        else:
            print('Неверно')
            if i == 2:
                print("Повторите попытку позже")


password = "123456789"
ask_password()
