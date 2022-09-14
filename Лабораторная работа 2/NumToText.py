import os
os.system('cls')

def secch():
            choice = int(input("Хотите перевести другую сумму? (Да - 1, Нет - 2): "))
            
            if choice == 1:
                os.system('cls')
                main()
                
            if choice == 2:
                os.system('cls')
                print("Хорошего дня!")
                
            else:
                print("Данной команды не существует! Попробуйте еще раз!")
                secch()

def main():
    print("Добро пожаловать!")
    number = int(input("Введите сумму для перевода (от 1 до 999999 рублей): "))

    if number > 999999 or number < 1:
        
        def ch():
            choice = int(input("Произошла ошибка при чтении суммы. Хотите ввести другое число? (Да - 1, Нет - 2): "))
            
            if choice == 1:
                os.system('cls')
                main()
                
            if choice == 2:
                os.system('cls')
                print("Хорошего дня!")
                
            else:
                print("Данной команды не существует! Попробуйте еще раз!")
                ch()
        ch()
    else:        
        
        x = number // 100000
        a = number - x * 100000
        z = a // 10000
        a = a - z * 10000
        c = a // 1000
        a = a - c * 1000
        v = a // 100
        a = a - v * 100
        b = a // 10
        a = a - b * 10
        n = a // 1 

        hun = ['сто ','двести ','триста ', 'четыреста ','пятьсот ','шестьсот ','семьсот ','восемьсот ','девятьсот ']
        doz = ['десять ','одиннадцать ','двенадцать ','тринадцать ','четырнадцать ','пятнадцать ','шестнадцать ','семнадцать ','восемнадцать ','девятнадцать ', 'двадцать ','тридцать ','сорок ','пятьдесят ','шестдесят ','семдесят ','восемдесят ','девяносто ',''] 
        th = ['','тысяча ', 'тысячи ','тысяч ']
        dig = ['один ','два ','три ','четыре ','пять ','шесть ','семь ','восемь ','девять ','одна ']
        roubles = ['рубль','рубля','рублей']

        if x != 0:
            s = hun[x-1]
        else:
            s = th[0]

        if z != 0:
            if z == 1:
                if c == 0:
                    d = doz[0]
                    f = th[0]
                else:
                    d = doz[c]
                    f = th[0]
            else:
                d = doz[z + 8]
                if c != 0:
                    f = dig[c - 1]
                else:
                    f = th[0]
        else:
            d = th[0]
            if c != 0:
                if c == 1:
                    f = dig[9]
                else:
                    f = dig[c - 1]
            else:
                f = th[0]

        if x != 0 or z != 0 or c != 0:
            if z == 1 or (c != 2 and c != 3 and c != 4):
                m = th[3]
            else:
                pass
            if z != 1 and c == 1:
                m = th[1]
            else:
                pass
            if z != 1 and (c==2 or c==3 or c==4):
                m = th[2]
            else:
                pass
            if x != 0 and z == 0 and c == 0:
                m = th[3]
            else:
                pass
            if x != 0 and c == 0:
                m = th[3]
            else:
                pass
        else:
            m = th[0]

        if v != 0:
            g = hun[v - 1]
        else:
            g = th[0]

        if b != 0:
            if b == 1:
                if n == 0:
                    h = doz[0]
                    j = th[0]
                else:
                    h = doz[n]
                    j = th[0]
            else:
                h = doz[b + 8]
                if n != 0:
                    j = dig[n - 1]
                else:
                    j = th[0]
        else:
            h = th[0]
            if n != 0:
                j = dig[n - 1]
            else:
                j = th[0]

        if n == 1:
            if b != 1:
                r = roubles[0]
            else:
                r = roubles[2]
        else:
            pass

        if n == 2 or n == 3 or n == 4:
            if b != 1:
                r = roubles[1]
            else:
                r = roubles[2]
        else:
            pass

        if n > 4 or n == 0:
            r = roubles[2]
        else:
            pass

        print("Ваша сумма для перевода: ", str(s) + str(d) + str(f) + str(m) + str(g) + str(h) + str(j) + str(r))
        
        secch()
        
main()