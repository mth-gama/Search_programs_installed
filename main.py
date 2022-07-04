from distutils.command.install_data import install_data
from enum import auto
from sqlite3 import Row
from tkinter import *
from tkinter import font
from tkinter.ttk import Style
from numpy import column_stack, pad
from Functions import *
import winapps
import pyautogui as pg
import os

# Author: Matheus Gama
# E-mail: matheusgama821@gmail.com
# LinkedIn: https://www.linkedin.com/in/matheus-gama-032516181
# GitHub: https://github.com/mth-gama
# Mostra todos os itens instalados


def show_all_apps():
    row_line = 0
    indice_num = 1
    root_2 = Tk()
    root_2.geometry(center(root_2, 432, 270))
    root_2.configure(bg='#FFDEAD')
    root_2.title('SHOW ALL APPS')
    root_2.resizable(False, False)
    corpo_canvas = Canvas(
        root_2,
        bg='#FFDEAD',
        width=400
    )
    my_scroll = Scrollbar(
        root_2,
        orient=VERTICAL,
        command=corpo_canvas.yview,
    )
    corpo_canvas.configure(yscrollcommand=my_scroll.set)
    corpo_canvas.bind('<Configure>', lambda e: corpo_canvas.configure(
        scrollregion=corpo_canvas.bbox('all')))
    corpo_2 = Frame(
        corpo_canvas,
        bg='#FFDEAD',
    )
    corpo_canvas.create_window((0, 0), window=corpo_2, anchor=W)
    corpo_canvas.pack(side=LEFT, anchor=N)
    my_scroll.pack(side=RIGHT, fill=Y)
    for item in winapps.list_installed():
        indice = Label(
            corpo_2,
            text=f"{indice_num}->",
            font="Verdana 10 bold",
            bg='#FFDEAD',
            fg='#8B4513'
        ).grid(row=row_line, column=0, sticky=NW)

        apps = Label(
            corpo_2,
            text=item.name,
            font="Verdana 10 bold",
            bg='#FFDEAD',
            fg='#8B4513',
            wraplength=400,
            justify=LEFT
        ).grid(row=row_line, column=1, sticky=NW)
        row_line = row_line + 1
        indice_num = indice_num + 1

    root_2.mainloop()


def app():
    if app_name.get() == '':
        pg.alert('Please enter with app valid')
    elif app_name.get() == 'Game Master':
        pg.alert('YOU ACTIVED O EASTEREGG\nCONGRATULATION!!!')
        os.startfile(r'EasterEgg.exe')
    else:
        name.set(f'non-existent app "{app_name.get()}"')
        version.set(f'non-existent app "{app_name.get()}"')
        Install_date.set(f'non-existent app "{app_name.get()}"')
        publisher.set(f'non-existent app "{app_name.get()}"')
        uninstall_string.set(f'non-existent app "{app_name.get()}"')
        for item in winapps.search_installed(app_name.get()):
            name.set(item.name)
            version.set(item.version)
            Install_date.set(item.install_date)
            publisher.set(item.publisher)
            uninstall_string.set(item.uninstall_string)


# Window configurations
root = Tk()
root.geometry(center(root, 432, 140))
root.configure(bg='#FFDEAD')
root.resizable(False, True)
root.title('SEARCH PROGRAMS')
# Variables
name = StringVar()
version = StringVar()
Install_date = StringVar()
publisher = StringVar()
uninstall_string = StringVar()

container_top = Frame(
    root,
    bg='#FFDEAD'
)
container_top.grid(row=0, columnspan=2)
Label(
    container_top,
    text='Enter app name: ',
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513'
).grid(row=1, column=0, sticky=W)

Frame(
    container_top,
    width=159,
    height=0,
    bg='#8B4513',
).grid(row=2, column=1, sticky=NW)

Label(
    root,
    text='Name:',
    font='Verdana 10',
    bg='#FFDEAD',
    fg='#8B4513'
).grid(row=3, sticky=NW)

Label(
    root,
    text='Version:',
    font='Verdana 10',
    bg='#FFDEAD',
    fg='#8B4513'
).grid(row=4, sticky=NW)

Label(
    root,
    text='Install date:',
    font='Verdana 10',
    bg='#FFDEAD',
    fg='#8B4513'
).grid(row=5, sticky=NW)

Label(
    root,
    text='Publisher:',
    font='Verdana 10',
    bg='#FFDEAD',
    fg='#8B4513'
).grid(row=6, sticky=NW)

Label(
    root,
    text='Unistall string:',
    font='Verdana 10',
    bg='#FFDEAD',
    fg='#8B4513',
).grid(row=7, sticky=NW)

# Text variables
Label(
    root,
    text="",
    textvariable=name,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=300
).grid(row=3, column=1, sticky=W)

Label(
    root,
    text="",
    textvariable=version,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=300
).grid(row=4, column=1, sticky=W)

Label(
    root,
    text="",
    textvariable=Install_date,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=300
).grid(row=5, column=1, sticky=W)

Label(
    root,
    text="",
    textvariable=publisher,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=300
).grid(row=6, column=1, sticky=W)

Label(
    root,
    text="",
    textvariable=uninstall_string,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=300
).grid(row=7, column=1, sticky=NW)

app_name = Entry(
    container_top,
    font='Verdana 10',
    bg='#FFDEAD',
    fg='#8B4513',
    border=0
)
app_name.grid(row=1, column=1, sticky=W)

btn_search = Button(
    container_top,
    text='Search',
    font='Verdana 9 bold',
    border=0,
    width=6,
    height=1,
    bg='#B8860B',
    fg='#8B4513',
    command=app
).grid(row=1, column=2, sticky=NW, padx=4, pady=1)

btn_show_all = Button(
    container_top,
    text='Show All',
    font='Verdana 9 bold',
    border=0,
    width=8,
    height=1,
    bg='#B8860B',
    fg='#8B4513',
    command=show_all_apps
).grid(row=1, column=3, sticky=NW, padx=4, pady=1)
root.mainloop()
