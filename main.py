from Pokemon import Pokemon
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

screens = ["start"]
pokemons = []

font = "Joystix Monospace"

count = 0


# file handling
def info_get_file():
    global pokemons

    with open("Pokemon.txt", "r", encoding='utf-8') as file:
        lines = (file.readlines())
        print(lines)
        file_length = len(lines)

        legendaries = lines[0].split(",")
        legendaries[-1] = (legendaries[-1]).replace("\n", "")

        if len(legendaries) == 0:
            pass
        else:
            for i in legendaries:
                try:
                    eval(i).legendarify()
                except NameError:
                    pass

        mythicals = lines[1].split(",")
        mythicals[-1] = (mythicals[-1]).replace("\n", "")

        if len(mythicals) == 0:
            pass
        else:
            for i in mythicals:
                try:
                    eval(i).myth()
                except NameError:
                    pass

        if file_length < 3:
            print("No data")
        else:
            listofpoke = {}
            for i in range(2, file_length):
                line = (lines[i]).split(",")
                pokename = line[0].replace("-","").replace("'","").replace(" ","").replace(".","")
                listofpoke[pokename.lower()] = Pokemon(line[0], line[1], line[2], line[3], line[4],
                                                       line[5], line[6], line[7], line[8].split("~"), line[9].split("~"), line[10], line[11],
                                                       line[12],
                                                       line[13], line[14], line[15].replace("\n", ""))

            for pokename, obj in listofpoke.items():
                globals()[pokename] = obj
                eval(pokename).add_to_list(pokemons)



# start screen
def start_screen_destroy():
    start_screen.destroy()
    start_button.destroy()


def start_screen_menu():
    global start_screen, start_screen_img, start_button

    start_screen_img = ImageTk.PhotoImage(Image.open("./assets/start_screen.png"))
    start_screen = ttk.Label(root, image=start_screen_img, borderwidth=0)
    start_screen.place(relx=0, rely=0)

    start_button = tk.Button(root, text="Start", font=(font, 15), bg="yellow",
                             command=lambda: [start_screen_destroy(), option_menu(), screens.append("option menu")])
    start_button.place(relx=0.4, rely=0.85)


# option select
def option_menu():
    global main_pokemon_choose_label, main_pokemon_choose_button, title

    title = ttk.Label(root, text="    Options", font=(font, 25),background="red",foreground="white",underline=4)
    title.place(relx=0.025, rely=0.075)

    main_pokemon_choose_label = ttk.Label(root, text="Pokemon", font=(font, 20),background="red",foreground="white")
    main_pokemon_choose_label.place(relx=0.1, rely=0.175)

    main_pokemon_choose_button = tk.Button(root, text="Enter", font=(font, 15),background="yellow",foreground="black",
                                           command=lambda: [destroy_option_menu(), main_pokemon(),
                                                            screens.append("main pokemon menu")])
    main_pokemon_choose_button.place(relx=0.625, rely=0.175)


def destroy_option_menu():
    main_pokemon_choose_label.destroy()
    main_pokemon_choose_button.destroy()
    title.destroy()


def back_button_func():
    global screens

    if len(screens) == 1:
        root.destroy()
    else:
        if screens[-1] == "option menu":
            destroy_option_menu()
        elif screens[-1] == "main pokemon menu":
            destroy_main_pokemon_menu()
        elif screens[-1] == "second pokemon menu":
            destroy_secondary_pokemon_menu()

        screens.pop()
        if screens[-1] == "start":
            start_screen_menu()
        elif screens[-1] == "option menu":

            option_menu()
        elif screens[-1] == "main pokemon menu":
            main_pokemon()
        back_button_button.destroy()
        back_button()

def back_button():
    global back_button_button

    back_button_button = tk.Button(root, text="<", command=back_button_func, font=(font, 10), background="yellow")
    back_button_button.place(relx=0, rely=0)


def secondary_pokemon_menu():
    global name, next, last, count, weight, height, hp, attack, defence, specialAttack, specialDefence, speed, total, \
        ability, hiddenAbility, back_page

    name = ttk.Label(root, text=pokemons[count].name, font=(font, 25), background="red",foreground="white")
    height = (ttk.Label(root, text=f"Height:{pokemons[count].height}m", font=(font, 15), background="red",foreground="white"))
    weight = (ttk.Label(root, text=f"Weight:{pokemons[count].weight}kg", font=(font, 15), background="red",foreground="white"))

    if len(pokemons[count].abilities) == 1:
        textability = f"Ability:{pokemons[count].abilities[0]}"
    elif len(pokemons[count].abilities) == 2:
        textability = f"Abilities:{pokemons[count].abilities[0]},\n          {pokemons[count].abilities[1]}"
    else:
        textability = "Abilities:None"
    ability = (ttk.Label(root, text=textability, font=(font, 15), background="red",foreground="white"))
    if pokemons[count].habilities[0] == "":
        textability = "Hidden Ability:None"
    elif len(pokemons[count].habilities) == 1:
        textability = f"hidden Ability:{pokemons[count].habilities[0]}"
    elif len(pokemons[count].habilities) == 2:
        textability = f"hiddenAbilities:{pokemons[count].habilities[0]},{pokemons[count].habilities[1]}"

    hiddenAbility = (ttk.Label(root, text=f"{textability}", font=(font, 15), background="red",foreground="white"))

    hp = (ttk.Label(root, text=f"HP:{pokemons[count].hp}", font=(font, 15), background="red",foreground="white"))
    attack = (ttk.Label(root, text=f"Attack:{pokemons[count].attack}", font=(font, 15), background="red",foreground="white"))
    defence = (ttk.Label(root, text=f"Defence:{pokemons[count].defence}", font=(font, 15), background="red",foreground="white"))
    specialAttack = (
        ttk.Label(root, text=f"Special Attack:{pokemons[count].spattack}", font=(font, 15), background="red",foreground="white"))
    specialDefence = (
        ttk.Label(root, text=f"Special Defence:{pokemons[count].spdefence}", font=(font, 15), background="red",foreground="white"))
    speed = (ttk.Label(root, text=f"Speed:{pokemons[count].speed}", font=(font, 15), background="red",foreground="white"))
    total = (ttk.Label(root, text=f"Total:{pokemons[count].total}", font=(font, 15), background="red",foreground="white"))

    next = tk.Button(root, font=(font, 12), bg="yellow", fg="black", text=">",
                     command=lambda: [destroy_secondary_pokemon_menu(), addonecount(), secondary_pokemon_menu()])
    last = tk.Button(root, font=(font, 12), bg="yellow", fg="black", text="<",
                     command=lambda: [destroy_secondary_pokemon_menu(), minusonecount(), secondary_pokemon_menu()])
    back_page = tk.Button(root, font=(font, 12), bg="yellow", text="Less...",
                          command=lambda: [destroy_secondary_pokemon_menu(), main_pokemon(), screens.pop(),
                                           screens.append("main pokemon menu")])

    name.place(relx=0.025, rely=0.075)
    height.place(relx=0.025, rely=0.15)
    weight.place(relx=0.025, rely=0.2)
    ability.place(relx=0.025, rely=0.275)
    hiddenAbility.place(relx=0.025, rely=0.375)

    hp.place(relx=0.025, rely=0.475)
    attack.place(relx=0.025, rely=0.525)
    defence.place(relx=0.025, rely=0.575)
    specialAttack.place(relx=0.025, rely=0.625)
    specialDefence.place(relx=0.025, rely=0.675)
    speed.place(relx=0.025, rely=0.725)
    total.place(relx=0.025, rely=0.775)

    next.place(relx=0.9, rely=0.9)
    last.place(relx=0.8, rely=0.9)
    back_page.place(relx=0.35, rely=0.9)


def destroy_secondary_pokemon_menu():
    name.destroy()
    hp.destroy()
    height.destroy()
    weight.destroy()
    attack.destroy()
    total.destroy()
    defence.destroy()
    speed.destroy()
    specialAttack.destroy()
    specialDefence.destroy()
    ability.destroy()
    hiddenAbility.destroy()
    next.destroy()
    last.destroy()
    back_page.destroy()


# main pokemon menu
def main_pokemon():
    global name, number, type1, type2, generation, species, pokemon_image_label, next, \
        typebg, typefg, pokemon_image, count, icon_image, icon, last, to_page_two_button

    name = ttk.Label(root, text=pokemons[count].name, font=(font, 25), foreground="white", background="red")

    number = (ttk.Label(root, text=f"#{pokemons[count].number}", font=(font, 17), foreground="white", background="red"))

    typebg = "white"
    typefg = "black"

    type_colour_check(pokemons[count].type1)
    type1 = (ttk.Label(root, text=pokemons[count].type1, font=(font, 17), background=typebg, foreground=typefg))
    type_colour_check(pokemons[count].type2)
    type2 = (ttk.Label(root, text=pokemons[count].type2, font=(font, 17), background=typebg, foreground=typefg))
    generation = (ttk.Label(root, text=f"Gen: {pokemons[count].generation}", font=(font, 12), foreground="white",
                            background="red"))
    species = (ttk.Label(root, text=pokemons[count].species, font=(font, 17), foreground="white", background="red"))

    pokemon_image = ImageTk.PhotoImage(Image.open(f"./assets/{pokemons[count].name.lower()}.png"))
    pokemon_image_label = ttk.Label(root, image=pokemon_image, background="red", borderwidth=0)

    next = tk.Button(root, font=(font, 12), bg="yellow", fg="black", text=">",
                     command=lambda: [destroy_main_pokemon_menu(), addonecount(), main_pokemon()])
    last = tk.Button(root, font=(font, 12), bg="yellow", fg="black", text="<",
                     command=lambda: [destroy_main_pokemon_menu(), minusonecount(), main_pokemon()])

    to_page_two_button = tk.Button(root, font=(font, 12), bg="yellow", text="More...",
                                   command=lambda: [destroy_main_pokemon_menu(), secondary_pokemon_menu(),
                                                    screens.pop(), screens.append("second pokemon menu")])

    if pokemons[count].legendary:
        icon_image = ImageTk.PhotoImage(Image.open(f"./assets/legendary_Preview.png"))
    else:
        icon_image = ImageTk.PhotoImage(Image.open(f"./assets/myth.png"))
    icon = ttk.Label(root, image=icon_image, background="red", borderwidth=0)

    if pokemons[count].legendary or pokemons[count].mythical:
        icon.place(relx=0.7, rely=0.05)
    else:
        icon.place(relx=1, rely=1)

    name.place(relx=0.025, rely=0.075)
    number.place(relx=0.025, rely=0.2)
    type1.place(relx=0.025, rely=0.265)
    type2.place(relx=0.4, rely=0.265)
    generation.place(relx=0.025, rely=0.9)
    species.place(relx=0.025, rely=0.15)

    next.place(relx=0.9, rely=0.9)
    last.place(relx=0.8, rely=0.9)
    to_page_two_button.place(relx=0.35, rely=0.9)

    pokemon_image_label.place(relx=0.25, rely=0.4)


def destroy_main_pokemon_menu():
    name.destroy()
    type1.destroy()
    number.destroy()
    type2.destroy()
    species.destroy()
    generation.destroy()
    next.destroy()
    last.destroy()
    pokemon_image_label.destroy()
    icon.destroy()
    to_page_two_button.destroy()


def addonecount():
    global count

    if count == len(pokemons) - 1:
        count = 0
    else:
        count += 1


def minusonecount():
    global count

    if count == 0:
        count = len(pokemons) - 1
    else:
        count -= 1


def type_colour_check(type):
    global typefg
    global typebg

    if type == "Grass":
        typebg = "green"
        typefg = "white"
    elif type == "Poison":
        typebg = "purple"
        typefg = "white"
    elif type == "Fighting":
        typebg = "orange"
        typefg = "white"
    elif type == "Ice":
        typebg = "light blue"
        typefg = "black"
    elif type == "Electric":
        typebg = "yellow"
        typefg = "black"
    elif type == "Bug":
        typebg = "#996600"
        typefg = "white"
    elif type == "Rock":
        typebg = "#333300"
        typefg = "#ffffff"
    elif type == "Steel":
        typebg = "light grey"
        typefg = "white"
    elif type == "Ghost":
        typebg = "#660066"
        typefg = "white"
    elif type == "Water":
        typebg = "blue"
        typefg = "white"
    elif type == "Ground":
        typebg = "brown"
        typefg = "white"
    elif type == "Flying":
        typebg = "#9999ff"
        typefg = "white"
    elif type == "Fairy":
        typebg = "pink"
        typefg = "white"
    elif type == "Dark":
        typebg = "black"
        typefg = "white"
    elif type == "Dragon":
        typebg = "#333399"
        typefg = "white"
    elif type == "Fire":
        typebg = "#ff6600"
        typefg = "white"
    elif type == "Normal":
        typebg = "grey"
        typefg = "white"
    elif type == "Psychic":
        typebg = "#cc0099"
        typefg = "white"

    else:
        typebg = "black"
        typefg = "white"


root = tk.Tk()

info_get_file()

start_screen_menu()
back_button()

root.config(bg="red")
root.title("Pythodex")
root.geometry("550x600+50+50")
root.iconbitmap("./assets/PythodexLogo.ico")

root.mainloop()
