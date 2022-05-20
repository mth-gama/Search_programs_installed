from distutils.command.install_data import install_data
from sqlite3 import Row
from tkinter import *
from tkinter import font
from tkinter.ttk import Style
from numpy import pad
from Functions import *
import winapps

# Author: Matheus Gama
# E-mail: matheusgama821@gmail.com
# LinkedIn: https://www.linkedin.com/in/matheus-gama-032516181
# GitHub: https://github.com/mth-gama


def app():
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
root.geometry(center(root, 353,140))
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
    text = 'Enter app name: ',
    font = 'Verdana 10 bold',
    bg = '#FFDEAD',
    fg='#8B4513'
).grid(row = 1, column=0,sticky=W)

Frame (
    container_top,
    width=159,
    height=0,
    bg='#8B4513',
).grid(row=2,column=1, sticky=NW)

Label(
    root,
    text = 'Name:',
    font = 'Verdana 10',
    bg = '#FFDEAD',
    fg='#8B4513'
).grid(row = 3, sticky=NW)

Label(
    root,
    text = 'Version:',
    font = 'Verdana 10',
    bg = '#FFDEAD',
    fg='#8B4513'
).grid(row = 4, sticky=NW)

Label(
    root,
    text = 'Install date:',
    font = 'Verdana 10',
    bg = '#FFDEAD',
    fg='#8B4513'
).grid(row = 5, sticky=NW)

Label(
    root,
    text = 'Publisher:',
    font = 'Verdana 10',
    bg = '#FFDEAD',
    fg='#8B4513'
).grid(row = 6, sticky=NW)

Label(
    root,
    text = 'Unistall string:',
    font = 'Verdana 10',
    bg = '#FFDEAD',
    fg='#8B4513',
).grid(row = 7, sticky=NW)

# Text variables
Label (
    root,
    text="",
    textvariable= name,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=210
).grid(row=3 , column=1, sticky=W)

Label (
    root,
    text="",
    textvariable= version,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=210
).grid(row=4 , column=1, sticky=W)

Label (
    root,
    text="",
    textvariable= Install_date,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=210
).grid(row=5 , column=1, sticky=W)

Label (
    root,
    text="",
    textvariable= publisher,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=210
).grid(row=6 , column=1, sticky=W)

Label (
    root,
    text="",
    textvariable= uninstall_string,
    font='Verdana 10 bold',
    bg='#FFDEAD',
    fg='#8B4513',
    justify=LEFT,
    wraplength=210
).grid(row=7 , column=1, sticky=NW)

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
root.mainloop()


    
# Mostra o item indicado se esta ou não instalado
