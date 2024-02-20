from game_code.new_owdle import Owdle_v2
from tkinter import *
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import ImageTk, Image
import os
import random


def intento():

    h = combo.get()

    for i in Owdle_v2.chList:
        if i.name == h:
            hero = i

    gen = hero.gender == rH.gender
    gun = hero.gun == rH.gun
    beha = hero.behaviour == rH.behaviour
    mod = hero.mod == rH.mod
    pl = hero.place == rH.place
    year = hero.year == rH.year

    lbName = Label(root, text=hero.name)
    lbGender = Label(root, text=hero.gender, bg=fallo, width=10, height=5)
    lbGun = Label(root, text=hero.gun, bg=fallo, width=10, height=5)
    lbBeha = Label(root, text=hero.behaviour, bg=fallo, width=10, height=5)
    lbMod = Label(root, text=hero.mod, bg=fallo, width=10, height=5)
    lbPlace = Label(root, text=hero.place, bg=fallo, width=10, height=5)
    lbYear = Label(root, text=hero.year, bg=fallo, width=10, height=5)

    foto(root, h)

    if gen:
        lbGender.config(bg=acierto)
    if gun:
        lbGun.config(bg=acierto)
    if beha:
        lbBeha.config(bg=acierto)
    if mod:
        lbMod.config(bg=acierto)
    if pl:
        lbPlace.config(bg=acierto)
    if year:
        lbYear.config(bg=acierto)

    if hero.year < rH.year:
        lbYear.config(text=str(hero.year) + '\nHigher')
    if hero.year > rH.year:
        lbYear.config(text=str(hero.year) + '\nLesser')

    lbName.place(x=300, y=160, width=80)

    lbGender.place(x=95, y=200)

    lbGun.place(x=185, y=200)

    lbBeha.place(x=275, y=200)

    lbMod.place(x=365, y=200)

    lbPlace.place(x=455, y=200)

    lbYear.place(x=545, y=200)

    combo.set('')

    if h == nameH:
        combo.config(state='disabled')
        btn.config(state='disabled')


def foto(root, name_election):

    direc = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(direc, '..', 'source', 'Icon-' + name_election + '.png')
    image = Image.open(ruta)
    image = image.resize((50, 50))

    photo = ImageTk.PhotoImage(image)
    lbFace = Label(root, image=photo, bg='black', width=50, height=50)
    lbFace.image = photo  # Almacena una referencia para evitar que la imagen sea eliminada por el recolector de basura
    lbFace.place(x=25, y=215)

def on_key_pressed(event):
    current_text = combo.get()
    matching_options = [option for option in Owdle_v2.chNameList if option.startswith(current_text)]
    combo['values'] = matching_options
    combo.event_generate("<Button-1>")
    combo.icursor(END)


root = Tk()

root.title('Owdle')
root.resizable(False, False) # (anchura, altura)
root.geometry('650x450')

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_icono = os.path.join(directorio_actual, '..', 'source', 'logo1.ico')
root.iconbitmap(ruta_icono)

root.config(bg='grey')


lbl = Label(root, text='Owdle', bg='grey', fg='orange')
lbl.place(x=10, y=10, width=100, height=30)

btn = Button(root, text='Accept', command=intento, cursor='')
btn.place(x=390, y=60, height=30)

combo = AutocompleteCombobox(root)
combo.set_completion_list(Owdle_v2.chNameList)
combo.place(x=180, y=60, width=200, height=30)

acierto = 'lime'
fallo = 'red'

rH = random.choice(Owdle_v2.chList)
nameH = rH.name
print(rH.name)

root.mainloop()
