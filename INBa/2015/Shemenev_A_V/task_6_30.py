# Задача 6. Вариант 30.
# Создайте игру, в которой компьютер загадывает название одного из двенадцати месяцев, а игрок должен его угадать.
# Shemenev A.V
# 11.04.2016
import random
month=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"] #Список месяцев
print("Данная программа предлагает вам угадать загаданную компьютером месяц")
x=random.choice(month)
print ("Какой месяц загадал компьютер?")
y=input("Введите ваш ответ (например 'Январь' без кавычек: ")
if x==y:
	print("Правильно!")
if 	x!=y:
	print("Неправильно!,правильный ответ-"+x)
input ("нажмите Enter для выхода")	
		
