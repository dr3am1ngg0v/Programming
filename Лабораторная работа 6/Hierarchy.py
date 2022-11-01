import os
import sys
import msvcrt as m

os.system('cls')

def convertToInt(n):                                                                                        # Вспомогательная функция для определения целочисленности
    
    try:
        n = int(n)
    
    except Exception:
        return -1
    
    return n

def inputTable(table, n):                                                                                   # Ввод отношений критериев в матрицу n * n
    
    for i in range(n):                                                                                      # Ввод отношений для верхней половины матрицы, считая от главной диагонали
        
        for j in range(n):
            
            if (i == j):
                table[i][j] = 1                                                                             # Элементы главной диагонали равны единице
            
            if (i < j):
                
                while table[i][j] == 0:                                                                     # Для выхода из цикла ввода элемента ожидается верный ввод
                    
                    temp = input("Введите отношение критерия {0} к критерию {1}:".format(i+1, j+1))
                    temp = convertToInt(temp)
                    
                    if (temp == -1) or (1 <= temp <= 9) == False:                                           # Проверка на соответствие условиям
                        print('Отношение должно быть целым числом от 1 до 9')
                    
                    else:
                        table[i][j] = temp
                        
    for i in range(n):                                                                                      # Отражение матрицы по главной диагонали и возведение её элементов в -1 степень
        
        for j in range(n):
            
            if (i > j):
                table[i][j] = 1/table[j][i]
    
    return table

def outputTablePrecise(table, n):                                                                           # Вывод матрицы попарных сравнений
    
    for i in range(n):
        
        for j in range(n):
            print("{0:.4f}".format(table[i][j]), end=" ")
        
        print()

def tableSum(table, n):                                                                                     # Cуммирование всех элементов матрицы
    
    sum = 0
    
    for i in range(n):
    
        for j in range(n):
            sum += table[i][j]
    
    return sum

def countWQ(table, n, sum):                                                                                 # Расчёт весовых коэффициентов
    
    columnSum = 0
    arrayWQ  = list()
    
    for i in range(n):                                                                                      # Расчёт суммы отношений для каждого критерия
        
        for j in range(n):
        
            columnSum += table[j][i]
        
        arrayWQ.append(columnSum/sum)
    
    return arrayWQ

                                                                                                            # Основная часть программы
n = 0
                                                                                                            # Ввод количества критериев
while n == 0:                                                                                               # Цикл будет запрашивать ввод, пока количество не будет положительным целым числом
    
    n = input("Введите количество критериев: ")
    n = convertToInt(n)
    
    if (n == -1) or (n < 1):
    
        print("Количество критериев должно быть положительным целым числом")
        n = 0

a = [[0] * n for i in range(n)]                                                                             # Создание двумерного массива n * n
a = inputTable(a,n)

print("\nМатрица попарного сравнения: ")
outputTablePrecise(a,n)

a_sum = tableSum(a,n)
print("\nСумма элементов матрицы: {0:.4f}".format(a_sum))

WQ = countWQ(a,n,a_sum)                                                                                     # Создание массива, хранящего весовые коэффициенты
WQ.reverse()

print("Весовые коэффициенты:", end=" ")

for elem in WQ:
    print("{0:.2f}".format(elem), end=" ")                                                                  # Форматирование вывода для соответствия условиям задачи

m.getch()
sys.exit()