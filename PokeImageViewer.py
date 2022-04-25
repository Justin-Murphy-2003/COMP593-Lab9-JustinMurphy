from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_list, get_pokemon_image_url
from library import download_image_from_url, set_image_as_background
import os
import sys
import ctypes

def main():
    script_dir = sys.path[0]
    img_dir = os.path.join(script_dir, "images")
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)

    root = Tk()
    root.title("Pokemon Image Viewer")

    #set taskbar image
    app_id = 'pokemon.image.viewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join(script_dir, 'Poke-Ball.ico'))
    #configurations for resizing image
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500,600)

    frm = ttk.Frame(root)
    frm.grid(sticky=(N,E,W,S))
    frm.rowconfigure(0, weight=10)
    frm.rowconfigure(1, weight=1)
    frm.rowconfigure(2, weight=1)
    frm.columnconfigure(0, weight=1)

    #set default image
    img_poke = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    lbl_img = ttk.Label(frm, image=img_poke)
    lbl_img.grid(row=0, column=0, padx=10, pady=10)

    pokemon_list = get_pokemon_list()
    pokemon_list.sort()
    pokemon_list =  [p.capitalize() for p in pokemon_list]
    #combobox
    cbo_pokemon = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    cbo_pokemon.set('Select a Pokemon')
    cbo_pokemon.grid(row=1, column=0, padx=10, pady=10)

    def handle_poke_select(event):
        pokemon_name = cbo_pokemon.get()
        image_url = get_pokemon_image_url(pokemon_name)
        image_path = os.path.join(img_dir, pokemon_name + '.png')
        download_image_from_url(image_url, image_path)
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])
    
    cbo_pokemon.bind("<<ComboboxSelected>>", handle_poke_select)

    def set_desktop():
        pokemon_name = cbo_pokemon.get()
        image_path = os.path.join(img_dir, pokemon_name + '.png')
        set_image_as_background(image_path)

    btn_set_desktop = ttk.Button(frm, text="Set as desktop background", command=set_desktop)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)

    root.mainloop()

main()