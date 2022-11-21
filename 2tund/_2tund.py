from math import * 
#Задача  3 Выяснить у пользователя желание расшифровать порядковый номер дня недели в название. Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами), спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.
quest=str(input("Хотите расшифровать порядкойвый номер дня недели? Да/Нет")
if a=="Да":
    b=int(input("Порядковый номер дня недели: "))
    if b>=1 and b<=7:
        if b==1:
            day="Monday"
        elif b==2:
            day="Tuesday"
        elif b==3:
            day="Wednesday"
        elif b==4:
            day=="Thursday"
        elif b=5:
            day="Fiday"

#Задача  2 Спросить у пользователя 3 числа, если они окажуться положительными, то проверить могут ли они быть углами одного треугольника(сумма углов 180) и уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний).
a=int(input("enter the 1 arv "))
b=int(input("enter the 2 arv "))
c=int(input("enter the 3 arv "))
if a>0 and b>0 and c>0:
    if a+b+c==180:
        if a==90 or b==90 or c==90:
            print("прямоугольн")
        elif a<90 and b<90 and c<90:
            print ("остроугольный")
        else:
            print("тупоугольный")
    else: 
        print("это не треугольник")
else: 
    print("фигня какая то ")

#Задача  1 Пользователь вводит число, программа определяет знак числа(положительное оно или отрицательное), если число положительное, то проверяет его на  четность и нечетность.
arv=int(input("enter the arv "))
if arv.isalpha():
    print(" see on tekst")
elif arv.isdigit():
    arv=int(arv) 
    if arv<0: 
        if arv%2==0:
            print(f"{arv} paaris")
        else:
            print(f"{arv} paaritu")
    else:
        print(f"{arv}-ei sobi ")
else:
    print(f"{arv} - segatud tekst ja number")
    



hinne=int(input("Mis hinne sa said?"))
if hinne>=1 and hinne <=5:
    if hinne==1 or hinne==2:
        vastus="Kurb"
    elif hinne==3:
        vastus="Rhuldav"
    elif hinne==4:
        vastus="Hea"
    else:
        vastus="Vaga hea"
else:
    vastus="viga andmetes"
print(vastus)

a=float(input("korgus: "))
b=float(input("laius: "))
if a>0 and b>0: #or,not,==,!=, 
    S=a*b 
else:
    S="ei saa leida"
print("Pindala:",S)


