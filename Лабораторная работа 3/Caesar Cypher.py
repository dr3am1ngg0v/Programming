# Работа выполнена студентом УрФУ Фт-210007 Митрофановым Иваном.
# Данный код представляет собой шифратор сообщений методом шифра Цезаря.
# В данном коде существует один недочёт, который описан в README.md на GitHub. Прошу с ним ознакомиться.


import os
os.system('cls')

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'                   # Алфавит русского языка с цифрами
alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'                          # Алфавит английского языка с цифрами

def choice_def():
    choice = input('Зашифровать еще сообщение? (Да - 1 или Нет - 2): ')
        
    if choice == '1':
        os.system('cls')
        main()
    else:
        if choice == '2':
            os.system('cls')
            print('Удачного дня!')
        else:
            os.system('cls')
            print("Произошла ошибка! Повторите ввод!")
            choice_def()

def main():
    
    message = input("Введите сообщение для шифровки: ").upper()          # Команда для ввода сообщения и его последующего преобразования в верхний регистр
    
    step = int(input("Укажите шаг смещения: "))                                                            # Шаг смещения
    result = ''
    
    language = input("Укажите язык сообщения (RU или EN): ")              # Выбор языка сообщения

    if language == 'RU' or language == 'ru':
                                     # Алгоритм шифрования на русском языке
        for i in message:
                      
            placement = alphabet_RU.find(i)
            new_placement = placement + step
                
            if i in alphabet_RU:
                result += alphabet_RU[new_placement]
            else:
                result += i
        
        os.system('cls')
        print("Шифрованное сообщение: ", result.capitalize())
        choice_def()
                
    
    else:
                
        if language == 'EN' or language == 'en':
            
            for i in message:                                               # Алгоритм шифрования на английском языке
            
                placement = alphabet_EN.find(i)
                new_placement = placement + step
                
                if i in alphabet_EN:
                    result += alphabet_EN[new_placement]
                else:
                    result += i
            
            os.system('cls')
            print("Шифрованное сообщение: ", result.capitalize())
            choice_def()
            
        else:
            os.system('cls')
            print('Возникла ошибка при выборе языка!')
            main()
            
main()

