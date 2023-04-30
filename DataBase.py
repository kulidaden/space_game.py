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

conn = sqlite3.connect('D:/Python/Proj/DataBase/Diplom.db')
sql=conn.cursor()


root1=Tk()
path = 'D:\Python\Proj\img\88.jpg'
image = Image.open(path)
width = 600
height = 300
image = image.resize((width, height), Image.LANCZOS)
image = ImageTk.PhotoImage(image)
canvas = tk.Canvas( width=width, height=height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=image)
lab1 = canvas.create_text(160,20,text='Вітаємо в грі SpaceDefenders',font='Verdana 15', fill="#00bfff")
lab2 = canvas.create_text(503,20,text='або',font='Verdana 10', fill="#00bfff")


# ФУНКЦІЇ ВІКНА
def q():
    root1.quit()
btn1=Button(root1,text='Вихід',command=q,bg='#00bfff').place(x=2,y=272)


def enter():
    root1.destroy()
    root2 = Tk()
    path = 'D:\Python\Proj\img\88.jpg'
    image = Image.open(path)
    width = 600
    height = 300
    image = image.resize((width, height), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(root2, width=width, height=height)
    canvas.pack(side="top", fill="both")
    canvas.create_image(0, 0, anchor="nw", image=image)
    btnq = Button(root2, text='Вихід', command=quit, width=10, bg='#00bfff')
    canvas.create_window((2,272 ), anchor="nw", window=btnq)
    def ent():
        login = conn.execute(f"SELECT login FROM users where login='{entry1.get()}'")
        result1=login.fetchall()
        # print(result1)
        if result1 != list():
            highscore1 = conn.execute(f"SELECT marks FROM users where login='{entry1.get()}'")
            highscore2=highscore1.fetchall()
            print(highscore2)
            with open('highscore.txt', 'w') as f:
                print(highscore2[0][0], file=f)
            with open('player.txt','w') as p:
                print(result1[0][0],file=p)
            password=conn.execute(f"SELECT password FROM users where password='{entry2.get()}'")
            result2=password.fetchall()
            if result2!=list():
                root2.destroy()
                root3 = Tk()
                path = 'D:\Python\Proj\img\menu.jpg'
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
                btnp1 = Button(root3, text='ГРАТИ', command=bTnp1, width=25, height=2, bg='#00bfff')
                canvas.create_window((320, 100), anchor="nw", window=btnp1)
                def bTnp2():
                    root4=Toplevel(root3)
                    root4.geometry('900x600+350+100')
                    root4.resizable(True,True)
                    root4.overrideredirect(True)
                    path = 'D:\Python\Proj\img\menu.jpg'
                    image = Image.open(path)
                    width = 1000
                    height = 600
                    image = image.resize((width, height), Image.LANCZOS)
                    image = ImageTk.PhotoImage(image)
                    canvas = tk.Canvas(root4, width=width, height=height)
                    canvas.pack(side="left", fill="both")
                    canvas.create_image(0, 0, anchor="nw", image=image)
                    btnq = Button(canvas, text='Вихід',font='Verdana 10', command=quit, width=10, bg='#00bfff')
                    canvas.create_window((1,571), anchor="nw", window=btnq)

                    def naz():
                        root4.withdraw()
                        root3.deiconify()
                    btnp1 = Button(canvas, text='Назад', command=naz,font='Verdana 10', width=10, bg='#00bfff')
                    canvas.create_window((817, 571), anchor="nw", window=btnp1)

                    conn = sqlite3.connect('D:/Python/Proj/DataBase/Diplom.db')
                    cursor = conn.execute("SELECT  nickname,marks FROM users ORDER BY marks DESC LIMIT 10;")
                    canvas.create_text(200,20, text="Ваше ім'я", font='Verdana 20 bold',fill='#EFFF00')
                    canvas.create_text(400, 20, text="Бали", font='Verdana 20 bold',fill='#EFFF00')
                    i = 50
                    for row in cursor:
                        canvas.create_text(200,20+i, text=row[0], font='Verdana 20 bold',fill='#00bfff')
                        canvas.create_text(400,20+i, text=row[1], font='Verdana 20 bold',fill='#00bfff')
                        i += 50

                    with open('player.txt', 'r') as p:
                        login = p.readline().strip()
                        cursor2=conn.execute(f"SELECT COUNT(*)+1 as rank FROM users WHERE marks > (SELECT marks FROM users WHERE login = '{login}');")
                    canvas.create_text(750,20, text="Місце в рейтингу", font='Verdana 20 bold',fill='#EFFF00')
                    for row in cursor2:
                        # print(row[0])
                        canvas.create_rectangle(720,50,785,90,fill='#00bfff',outline='#00bfff')
                        canvas.create_text(750,70, text=row[0], font='Verdana 25 bold',fill='#EFFF00')
                    conn.close()
                    root4.mainloop()
                btnp2 = Button(root3, text='ТАБЛИЦЯ ЛІДЕРІВ', command=bTnp2, width=25, height=2, bg='#00bfff')
                canvas.create_window((320, 170), anchor="nw", window=btnp2)
                btnp3 = Button(root3, text='Вихід', command=exit, width=25, height=2, bg='#00bfff')
                canvas.create_window((320, 240), anchor="nw", window=btnp3)
                root3.geometry('800x500+400+200')
                root3.resizable(False, False)
                root3.overrideredirect(True)
                root3.mainloop()
            else:
                messagebox.showinfo("Помилка","Введені данні не коректні")
        else:
            messagebox.showinfo("Помилка", "Введені данні не коректні")

    # pygame.mixer.init()
    # pygame.mixer.music.load('D:\Python\Proj\music\kos_1.mp3')
    # pygame.mixer.music.play()
    btnq1 = Button(root2, text='Увійти', command=ent, width=10, bg='#00bfff')
    canvas.create_window((260, 160), anchor="nw", window=btnq1)
    root2.geometry('600x300+500+200')
    lab1 = canvas.create_text(160, 20, text='Вітаємо в грі SpaceDefenders', font='Verdana 15', fill="#00bfff")
    lab2 = canvas.create_text(300, 80, text='Увійдіть в аккаунт', font='Verdana 13', fill="#00bfff")
    lab3 = canvas.create_text(175, 110, text='Емейл:', font='Verdana 13', fill="#00bfff")
    lab4 = canvas.create_text(170, 140, text='Пароль:', font='Verdana 13', fill="#00bfff")
    entry1=Entry(root2,width=30)
    canvas.create_window((208,100),anchor='nw',height=25,window=entry1)
    entry2=Entry(root2,width=30,show='*')
    canvas.create_window((208,130),anchor='nw',height=25,window=entry2)
    root2.resizable(False, False)
    root2.overrideredirect(True)
    root2.mainloop()
btn2=Button(root1,text='Вхід',command=enter,bd=1,bg='#00bfff').place(x=450,y=5)


def regist():
    root1.withdraw()
    root2 = Toplevel(root1)
    path = 'D:\Python\Proj\img\88.jpg'
    image = Image.open(path)
    width = 600
    height = 300
    image = image.resize((width, height), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(root2, width=width, height=height)
    canvas.pack(side="top", fill="both")
    canvas.create_image(0, 0, anchor="nw", image=image)
    btnq = Button(root2, text='Вихід', command=quit, width=10, bg='#00bfff')
    canvas.create_window((2,272 ), anchor="nw", window=btnq)


    root2.geometry('600x300+500+200')
    lab1 = canvas.create_text(160, 20, text='Вітаємо в грі SpaceDefenders', font='Verdana 15', fill="#00bfff")
    lab2 = canvas.create_text(300, 80, text='Зареєструйтесь', font='Verdana 13', fill="#00bfff")
    lab3 = canvas.create_text(175, 110, text='Емейл:', font='Verdana 13', fill="#00bfff")
    lab4 = canvas.create_text(170, 140, text='Пароль:', font='Verdana 13', fill="#00bfff")
    lab5 = canvas.create_text(168, 168, text='Нікнейм:', font='Verdana 13', fill="#00bfff")
    entry3=Entry(root2,width=30)
    canvas.create_window((208,100),anchor='nw',window=entry3)
    entry4=Entry(root2,show='*',width=30)
    canvas.create_window((208,130),anchor='nw',window=entry4)




    def reg():
        login1 = conn.execute(f"SELECT login FROM users where login='{entry3.get()}'")
        result1 = login1.fetchall()
        login2 = conn.execute(f"SELECT nickname FROM users where nickname='{entry5.get()}'")
        result2 = login2.fetchall()
        if result1 != list() or result2 != list():
            messagebox.showerror("Помилка", "Такий логін або нікнейм вже зареєстрований!")
        else:
            messagebox.showinfo("Форма", "Корстувач успішно зареєстрований!")
            conn.cursor()
            conn.execute(f"INSERT INTO users(login,password,nickname, marks) VALUES('{entry3.get()}','{entry4.get()}','{entry5.get()}', 0);")
            conn.commit()
            root2.withdraw()
            root1.deiconify()





    btnq1 = Button(root2, text='Зареєструватися',command=reg, width=15, bg='#00bfff')
    canvas.create_window((240,190), anchor="nw", window=btnq1)

    entry5=Entry(root2,width=30)
    canvas.create_window((208,160),anchor='nw',window=entry5)
    root2.resizable(False, False)
    root2.overrideredirect(True)
    root2.mainloop()
btn3=Button(root1,text='Реєстрація',command=regist,bd=1,bg='#00bfff').place(x=525,y=5)


# ХАРАКТЕРИСТИКИ ВІКНКА
root1.wm_attributes("-transparentcolor",'white')
root1.wm_attributes('-topmost',1)
root1.geometry('600x300+500+200')
root1.resizable(False,False)
root1.overrideredirect(True)
root1.mainloop()

