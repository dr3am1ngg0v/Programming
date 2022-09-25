# Работа выполнена студентом УрФУ Фт-210007 Митрофановым Иваном.
# Данный код представляет собой шифратор сообщений методом шифра Цезаря.


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
    
    step = 3                                                            # Шаг смещения
    result = ''
    
    language = input("Укажите язык сообщения (RU или EN): ")              # Выбор языка сообщения

    if language == 'RU' or language == 'ru':
        
        for i in message:                                               # Алгоритм шифрования на русском языке
            
            placement = alphabet_RU.find(i)
            if alphabet_RU.find(i) == len(alphabet_RU) - 3 or alphabet_RU.find(i) == len(alphabet_RU) - 2 or alphabet_RU.find(i) == len(alphabet_RU) - 1: 
                                                                                                    # Проверка, присутствуют ли три последних знака (7, 8, 9) алфавита в сообщении
                                                                                                    # Если да, то 7 станет 1, 8 станет 2, а 9 станет 3, то есть цифры будут идти в повтор (не знаю честно, как это объяснить :D)
                                                                                                    # Проверка идет по количеству символов в алфавите
                placement = alphabet_RU.find(i) - 9 
                new_placement = placement + step
            else:
                placement = alphabet_RU.find(i)
                new_placement = placement + step
                
            if i in alphabet_RU:
                result += alphabet_RU[new_placement]
            else:
                result += i
        
        os.system('cls')
        print(len(alphabet_RU), alphabet_RU.find(i))
        print("Шифрованное сообщение: ", result.lower().capitalize())
        choice_def()
                
    
    else:
                
        if language == 'EN' or language == 'en':
            
            for i in message:                                               # Алгоритм шифрования на английском языке
                
                placement = alphabet_EN.find(i)
                
                if alphabet_EN.find(i) == len(alphabet_EN) - 3 or alphabet_EN.find(i) == len(alphabet_EN) - 2 or alphabet_EN.find(i) == len(alphabet_EN) - 1: # Проверка, присутствуют ли три последних знака (7, 8, 9) алфавита в сообщении
                                                                                                    
                    placement = alphabet_EN.find(i) - 9
                    new_placement = placement + step
                else:
                    placement = alphabet_EN.find(i)
                    new_placement = placement + step
                
                if i in alphabet_EN:
                    result += alphabet_EN[new_placement]
                else:
                    result += i
            
            os.system('cls')
            print("Шифрованное сообщение: ", result.lower().capitalize())
            choice_def()
            
        else:
            print('Возникла ошибка при выборе языка!')
            main()
            
main()

