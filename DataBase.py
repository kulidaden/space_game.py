from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
import pygame.mixer
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
from space_game import run
import pyglet
import re
import smtplib

conn = sqlite3.connect('D:/Python/w/DataBase/Diplom.db')
sql=conn.cursor()


root1=Tk()
path = 'D:\Python\w\img\88.jpg'
image = Image.open(path)
width = 600
height = 300
image = image.resize((width, height), Image.LANCZOS)
image = ImageTk.PhotoImage(image)
canvas = tk.Canvas( width=width, height=height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=image)
lab1 = canvas.create_text(160,20,text='Вітаємо в грі SpaceDefenders',font='Verdana 15', fill="#00bfff")
entry1 = Entry(root1, width=30)
canvas.create_window((208, 100), anchor='nw', height=25, window=entry1)
entry2 = Entry(root1, width=30, show='*')
canvas.create_window((208, 130), anchor='nw', height=25, window=entry2)
entry3 = Entry(root1, width=30)
canvas.create_window((208, 160), anchor='nw', height=25, window=entry3)
lab3 = canvas.create_text(175, 110, text='Емейл:', font='Verdana 13', fill="#00bfff")
lab4 = canvas.create_text(170, 140, text='Пароль:', font='Verdana 13', fill="#00bfff")
lab5 = canvas.create_text(168, 168, text='Нікнейм:', font='Verdana 13', fill="#00bfff")
lab6 = canvas.create_text(300, 250, text='Для авторизації заповніть поля: "Емайл", "Пароль".\n'
                                         'Для реєстрації заповніть усі поля!', font='Verdana 12', fill="yellow")

def menu():
    root1.destroy()
    root3 = Tk()
    path = 'D:\Python\w\img\menu.jpg'
    image = Image.open(path)
    width = 800
    height = 500
    image = image.resize((width, height), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(root3, width=width, height=height)
    canvas.pack(side="top", fill="both")
    canvas.create_image(0, 0, anchor="nw", image=image)


    def bTnp1():
        root3.destroy()
        run()

    btnp1 = Button(root3, text='ПОЧАТИ ГРУ', command=bTnp1, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 100), anchor="nw", window=btnp1)

    def bTnp2():
        # таблиця лідерів
        def q4():
            root4.destroy()
            root4.quit()
            root3.destroy()
            root3.quit()

        root4 = Toplevel(root3)
        root4.geometry('900x650+350+80')
        root4.resizable(True, True)
        root4.overrideredirect(True)
        path = 'D:\Python\w\img\menu.jpg'
        image = Image.open(path)
        width = 1000
        height = 650
        image = image.resize((width, height), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(root4, width=width, height=height)
        canvas.pack(side="left", fill="both")
        canvas.create_image(0, 0, anchor="nw", image=image)
        btnq = Button(canvas, text='Вихід', font='Verdana 10', command=q4, width=10, bg='#00bfff')
        canvas.create_window((1, 621), anchor="nw", window=btnq)

        def naz():
            root4.withdraw()
            root3.deiconify()

        btnp1 = Button(canvas, text='Назад', command=naz, font='Verdana 10', width=10, bg='#00bfff')
        canvas.create_window((816, 621), anchor="nw", window=btnp1)

        conn = sqlite3.connect('D:/Python/w/DataBase/Diplom.db')
        cursor = conn.execute("SELECT  nickname,marks FROM users ORDER BY marks DESC LIMIT 10;")
        canvas.create_text(200, 70, text="Нікнейм", font='Verdana 20 bold', fill='#EFFF00')
        canvas.create_text(420, 70, text="Бали", font='Verdana 20 bold', fill='#EFFF00')
        i = 50
        for row in cursor:
            canvas.create_text(200, 70 + i, text=row[0], font='Verdana 20 bold', fill='#00bfff')
            canvas.create_text(420, 70 + i, text=row[1], font='Verdantyra 20 bold', fill='#00bfff')
            i += 50

        with open('player.txt', 'r') as p:
            login = p.readline().strip()
            cursor2 = conn.execute(
                f"SELECT COUNT(*)+1 as rank FROM users WHERE marks > (SELECT marks FROM users WHERE login = '{login}');")
        canvas.create_text(700, 70, text="Місце в рейтингу", font='Verdana 20 bold', fill='#EFFF00')
        canvas.create_text(460, 20, text="Топ-10", font='Verdana 23 bold', fill='#EFFF00')
        for row in cursor2:
            canvas.create_rectangle(665, 110, 737, 150, fill='#00bfff', outline='#00bfff')
            canvas.create_text(700, 130, text=row[0], font='Verdana 25 bold', fill='#EFFF00')
        conn.close()
        root4.mainloop()

    def bTnp3():
        # інструкція
        def q4():
            root5.destroy()
            root5.quit()
            root3.destroy()
            root3.quit()

        root5 = Toplevel(root3)
        root5.geometry('900x600+350+100')
        root5.resizable(True, True)
        root5.overrideredirect(True)
        path = '''D:\Python\w\img\w.jpg'''
        image = Image.open(path)
        width = 1000
        height = 600
        image = image.resize((width, height), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(root5, width=width, height=height)
        canvas.pack(side="left", fill="both")
        canvas.create_image(0, 0, anchor="nw", image=image)
        btnq = Button(canvas, text='Вихід', font='Verdana 10', command=q4, width=10, bg='#00bfff')
        canvas.create_window((1, 571), anchor="nw", window=btnq)

        def naz():
            root5.withdraw()
            root3.deiconify()

        txt = '\t\t\t- ЯК РОЗПОЧАТИ ГРУ?\nПІСЛЯ НАТИСКАННЯ НА КНОПКУ "ПОЧАТИ ГРУ" ВІДБУВАЄТЬСЯ ЇЇ ЗАПУСК. КОЛИ ГРА ' \
              'ЗАПУСТИЛАСЬ ВИ ПОЧИНАЄТЕ ВІДРАЗУ КЕРУВАТИ ЛІТАКОМ І НАВАЛА ПРИБУЛЬЦІВ РУХАЄТЬСЯ НА ВАС.\n' \
              '\t\t\t- ЯК ГРАТИ?\nЗА ДОПОМОГОЮ КНОПКИ "D" ВАШ КОРАБЕЛЬ БУДЕ РУХАТИСЬ ПРАВОРУЧ, А НАТИСНУВАШИ КНОПКУ' \
              '"A" - ЛІВОРУЧ. ДЛЯ ТОГО, ЩОБ СТРІЛЯТИ ПО ПРИБУЛЬЦЯМ, ПОТРІБНО НАТИСНУТИ НА ПРОБІЛ. \n' \
              '\t\t\t- ДОДАТКОВІ КОРАБЛІ\nУ ВАС Є ТРИ ДОДАТКОВИХ КОРАБЛІ, ЯКІ ВИ МОЖЕТЕ ВИКОРИСТАТИ У ТОМУ РАЗІ, ' \
              'ЯКЩО ПРИБУЛЬЦІ ДІЙДУТЬ ДО ВАШОГО КОРАБЛЯ.\n \t\t\t- РАХУНОК\nПРАВОРУЧ ЗВЕРХУ Є ПОТОЧНИЙ ' \
              'РАХУНОК ЗА ЦЮ ГРУ. ПОСЕРЕДИНІ ЗВЕРХУ ВКАЗАНИЙ ВАШ ЗАГАЛЬНИЙ РЕКОРД.\n' \
              '\t\t\t-ЗАВЕРШЕННЯ ГРИ\nГРУ БУДЕ ЗАВЕРШЕНО, ЯКЩО ВИ ЗАКРИЄТЕ ЇЇ АБО У ВАС НЕ ЗАЛИШИТЬСЯ КОРАБЛІВ.'

        btnp1 = Button(canvas, text='Назад', command=naz, font='Verdana 10', width=10, bg='#00bfff')
        canvas.create_window((817, 571), anchor="nw", window=btnp1)
        canvas.create_text(450, 250, text=txt, font='Verdana 16', width=800, fill='#00bfff')
        root5.mainloop()

    def bTnp4():
        # про гру
        def q4():
            root6.destroy()
            root6.quit()
            root3.destroy()
            root3.quit()

        root6 = Toplevel(root3)
        root6.geometry('900x600+350+100')
        root6.resizable(True, True)
        root6.overrideredirect(True)
        path = 'D:\Python\w\img\qq.jpg'
        image = Image.open(path)
        width = 1000
        height = 600
        image = image.resize((width, height), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(root6, width=width, height=height)
        canvas.pack(side="left", fill="both")
        canvas.create_image(0, 0, anchor="nw", image=image)
        btnq = Button(canvas, text='Вихід', font='Verdana 10', command=q4, width=10, bg='#00bfff')
        canvas.create_window((1, 571), anchor="nw", window=btnq)
        txt = 'ЦЯ ГРА БУЛА РОЗРОБЛЕНА У 2023 РОЦІ. АВТОР ГРИ КУЛІДА ДЕНИС. ВОНА Є АНАЛОГОМ ' \
              'РІЗНОМАНІТНИХ КОСМІЧНИХ ІГОР.'
        canvas.create_text(450, 250, text=txt, font='Verdana 16', width=400, fill='#EFFF00')

        def naz():
            root6.withdraw()
            root3.deiconify()

        btnp1 = Button(canvas, text='Назад', command=naz, font='Verdana 10', width=10, bg='#00bfff')
        canvas.create_window((817, 571), anchor="nw", window=btnp1)
        root6.mainloop()
    def q3():
        root3.destroy()
        root3.quit()
    btnp2 = Button(root3, text='ТАБЛИЦЯ ЛІДЕРІВ', command=bTnp2, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 170), anchor="nw", window=btnp2)
    btnp3 = Button(root3, text='ІНСТРУКЦІЯ', command=bTnp3, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 240), anchor="nw", window=btnp3)
    btnp4 = Button(root3, text='ПРО ГРУ', command=bTnp4, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 310), anchor="nw", window=btnp4)
    btnp5 = Button(root3, text='ВИХІД', command=q3, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 380), anchor="nw", window=btnp5)
    root3.geometry('800x500+400+150')
    root3.resizable(False, False)
    root3.overrideredirect(True)
    root3.mainloop()

def ent():
    login = conn.execute(f"SELECT login FROM users where login='{entry1.get()}'")
    result1 = login.fetchall()

    if result1 != list():
        highscore1 = conn.execute(f"SELECT marks FROM users where login='{entry1.get()}'")
        highscore2 = highscore1.fetchall()
        with open('highscore.txt', 'w') as f:
            print(highscore2[0][0], file=f)
        with open('player.txt', 'w') as p:
            print(result1[0][0], file=p)
        password = conn.execute(f"SELECT password FROM users where password='{entry2.get()}'")
        result2 = password.fetchall()
        if result2 != list():
            menu()
        else:
            messagebox.showinfo("Помилка", "Введені данні не коректні!")
    else:
        messagebox.showinfo("Помилка", "Введені данні не коректні!")

def reg():
    email=entry1.get()
            # Перевірка формату електронної пошти за допомогою регулярного виразу
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Помилка","Такої електронної пошти не існує")
    else:
        login1 = conn.execute(f"SELECT login FROM users where login='{entry1.get()}'")
        result1 = login1.fetchall()
        login2 = conn.execute(f"SELECT nickname FROM users where nickname='{entry3.get()}'")
        result2 = login2.fetchall()
        if result1 != list() or result2 != list():
            messagebox.showerror("Помилка", "Такий логін або нікнейм вже зареєстрований!")
        else:
            messagebox.showinfo("Форма", "Користувач успішно зареєстрований!")
            conn.cursor()
            conn.execute(f"INSERT INTO users(login,password,nickname, marks) VALUES('{entry1.get()}','{entry2.get()}','{entry3.get()}', 0);")
            conn.commit()
            menu()

# ФУНКЦІЇ ВІКНА
def q():
    root1.quit()
btn1=Button(root1,text='Вихід',command=q,bg='#00bfff').place(x=2,y=272)



btn2=Button(root1,text='Вхід',command=ent,bd=1,bg='#00bfff',width=5).place(x=200,y=200)

btn3=Button(root1,text='Реєстрація',command=reg,bd=1,bg='#00bfff').place(x=350,y=200)


# ХАРАКТЕРИСТИКИ ВІКНКА
root1.geometry('600x300+500+200')
root1.resizable(False,False)
root1.overrideredirect(True)
root1.mainloop()

