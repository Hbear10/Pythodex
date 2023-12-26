from Pokemon import Pokemon
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

pokemons = []

bulbasaur = Pokemon("Bulbasaur", 1, 1, "Grass", "Poison", "Seed Pokémon", 0.7, 6.9,
                    ["Overgrow"], ["Chlorophyll"], 45, 49, 49, 65, 65, 45)
bulbasaur.add_to_list(pokemons)
bulbasaur.legendarify()

shuckle = Pokemon("Shuckle", 213, 2, "Bug", "Rock", "Mold Pokémon", 0.6, 20.5, ["Sturdy", "Gluttony"],
                  ["Contrary"], 20, 10, 230, 10, 230, 5)
shuckle.add_to_list(pokemons)
shuckle.myth()

whiscash = Pokemon("Whiscash", 340, 3, "Water", "Ground", "Whiskers Pokémon", 0.9, 23.6, ["Oblivious", "Anticipation"],
                   ["Hydration"], 110, 78, 73, 76, 71, 60)
whiscash.add_to_list(pokemons)

togekiss = Pokemon("Togekiss", 468, 4, "Fairy", "Flying", "Jubilee Pokémon", 1.5, 38.0, ["Hustle", "Serene Grace"],
                   ["Super Luck"], 85, 50, 95, 120, 115, 80)
togekiss.add_to_list(pokemons)

hydreigon = Pokemon("Hydreigon", 635, 5, "Dark", "Dragon", "Brutal Pokémon", 1.8, 180.0, ["Levitate"], [],
                    92, 105, 90, 125, 90, 98)
hydreigon.add_to_list(pokemons)

talonflame = Pokemon("Talonflame", 663, 6, "Fire", "Flying", "Jubilee Pokémon", 1.2, 24.5, ["Flame Body"],
                     ["Gale Wings"], 78, 81, 71, 74, 69, 126)
talonflame.add_to_list(pokemons)

crabominable = Pokemon("Crabominable", 740, 7, "Fighting", "Ice", "Woolly Crab Pokémon", 1.7, 180.0,
                       ["Hyper Cutter", "Iron Fist"], ["Anger Point"], 97, 132, 77, 62, 67, 43)
crabominable.add_to_list(pokemons)

wyrdeer = Pokemon("Wyrdeer", 899, 8, "Normal", "Psychic", "Big Horn Pokémon", 1.8, 95.1,
                  ["Intimidate", "Frisk"], ["Sad Sipper"], 103, 105, 72, 105, 75, 65)
wyrdeer.add_to_list(pokemons)

pawmot = Pokemon("Pawmot", 923, 9, "Electric", "Fighting", "Hands-On Pokémon", 0.9, 41.0,
                 ["Volt Absorb", "Natural Cure"], ["Iron Fist"], 70, 115, 70, 70, 60, 105)
pawmot.add_to_list(pokemons)

gholdengo = Pokemon("Gholdengo", 1000, 9, "Steel", "Ghost", "Coin Entity Pokémon", 1.2, 30.0, ["Good as gold"], [], 87,
                    60, 95, 133, 91, 84)
gholdengo.add_to_list(pokemons)

print(pokemons)

font = "Joystix Monospace"

count = 0


def destroy_main_pokemon_menu():
    name.destroy()
    type1.destroy()
    number.destroy()
    type2.destroy()
    species.destroy()
    generation.destroy()
    # hp.destroy()
    # height.destroy()
    # weight.destroy()
    # attack.destroy()
    # defence.destroy()
    # speed.destroy()
    # specialAttack.destroy()
    # specialDefence.destroy()
    pokemon_image_label.destroy()
    icon.destroy()


def addonecount():
    global count

    if count == len(pokemons) - 1:
        count = 0
    else:
        count += 1

    main_pokemon()


def minusonecount():
    global count

    if count == 0:
        count = len(pokemons) - 1
    else:
        count -= 1

    main_pokemon()


root = tk.Tk()


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


def start_screen_destroy():
    start_screen.destroy()
    start_button.destroy()


def start_screen():
    global start_screen, start_screen_img, start_button

    start_screen_img = ImageTk.PhotoImage(Image.open("./assets/start_screen.png"))
    start_screen = ttk.Label(root, image=start_screen_img, borderwidth=0)
    start_screen.place(relx=0, rely=0)

    start_button = tk.Button(root, text="Start", font=(font, 15), bg="light blue",
                             command=lambda: [start_screen_destroy(), main_pokemon()])
    start_button.place(relx=0.4, rely=0.85)


def main_pokemon():
    global name, number, type1, type2, generation, species, pokemon_image_label, next, \
        typebg, typefg, pokemon_image, count, icon_image, icon
    # weight, height,hp, attack, defence, specialAttack, specialDefence, speed, total

    name = ttk.Label(root, text=pokemons[count].name, font=(font, 25), foreground="#0f0f0a")

    numberlen = len(str(pokemons[count].number))
    if numberlen < 1:
        number = (ttk.Label(root, text="#0000", font=(font, 17), foreground="#6b6b47"))
    elif numberlen == 1:
        number = (ttk.Label(root, text=f"#000{pokemons[count].number}", font=(font, 17), foreground="#6b6b47"))
    elif numberlen == 2:
        number = (ttk.Label(root, text=f"#00{pokemons[count].number}", font=(font, 17), foreground="#6b6b47"))
    elif numberlen == 3:
        number = (ttk.Label(root, text=f"#0{pokemons[count].number}", font=(font, 17), foreground="#6b6b47"))
    elif numberlen == 4:
        number = (ttk.Label(root, text=f"#{pokemons[count].number}", font=(font, 17), foreground="#6b6b47"))
    else:
        number = (ttk.Label(root, text="#Error", font=(font, 17)))

    typebg = "white"
    typefg = "black"

    type_colour_check(pokemons[count].type1)
    type1 = (ttk.Label(root, text=pokemons[count].type1, font=(font, 17), background=typebg, foreground=typefg))
    type_colour_check(pokemons[count].type2)
    type2 = (ttk.Label(root, text=pokemons[count].type2, font=(font, 17), background=typebg, foreground=typefg))
    generation = (ttk.Label(root, text=f"Gen: {pokemons[count].generation}", font=(font, 12), foreground="#6b6b47"))
    species = (ttk.Label(root, text=pokemons[count].species, font=(font, 17), foreground="#6b6b47"))
    # height = (ttk.Label(root, text=f"Height: {pokemons[count].height}m", font=(font, 12),foreground="#6b6b47"))
    # weight = (ttk.Label(root, text=f"Weight: {pokemons[count].weight}kg", font=(font, 12),foreground="#6b6b47"))
    # ability = (ttk.Label(root, text=pokemons[count].abilities, font=(font, 12),foreground="#6b6b47"))
    # hiddenAbility = (ttk.Label(root, text=pokemons[count].habilities, font=(font, 12),foreground="#6b6b47"))
    # hp = (ttk.Label(root, text=f"HP: {pokemons[count].hp}", font=(font, 12),foreground="#6b6b47"))
    # attack = (ttk.Label(root, text=f"Attack: {pokemons[count].attack}", font=(font, 12),foreground="#6b6b47"))
    # defence = (ttk.Label(root, text=f"Defence: {pokemons[count].defence}", font=(font, 12),foreground="#6b6b47"))
    # specialAttack = (ttk.Label(root, text=f"Special Attack: {pokemons[count].spattack}", font=(font, 12),foreground="#6b6b47"))
    # specialDefence = (ttk.Label(root, text=f"Special Defence: {pokemons[count].spdefence}", font=(font, 12),foreground="#6b6b47"))
    # speed = (ttk.Label(root, text=f"Speed: {pokemons[count].speed}", font=(font, 12),foreground="#6b6b47"))
    # total = (ttk.Label(root, text=f"Total: {pokemons[count].total}", font=(font, 12),foreground="#6b6b47"))

    pokemon_image = ImageTk.PhotoImage(Image.open(f"./assets/{pokemons[count].name.lower()}.png"))
    pokemon_image_label = ttk.Label(root, image=pokemon_image, background="red", borderwidth=0)

    next = tk.Button(root, font=(font, 12), bg="yellow", fg="black", text=">",
                     command=lambda: [destroy_main_pokemon_menu(), addonecount()])
    last = tk.Button(root, font=(font, 12), bg="yellow", fg="black", text="<",
                     command=lambda: [destroy_main_pokemon_menu(), minusonecount()])

    if pokemons[count].legendary:
        icon_image = ImageTk.PhotoImage(Image.open(f"./assets/legendary_Preview.png"))
    else:
        icon_image = ImageTk.PhotoImage(Image.open(f"./assets/myth.png"))
    icon = ttk.Label(root, image=icon_image, background="red", borderwidth=0)

    if pokemons[count].legendary or pokemons[count].mythical:
        icon.place(relx=0.7, rely=0.05)
    else:
        icon.place(relx=1, rely=1)

    name.place(relx=0.025, rely=0.05)
    number.place(relx=0.025, rely=0.3)
    type1.place(relx=0.025, rely=0.225)
    type2.place(relx=0.4, rely=0.225)
    generation.place(relx=0.1, rely=0.9)
    species.place(relx=0.025, rely=0.15)

    next.place(relx=0.9, rely=0.9)
    last.place(relx=0.8, rely=0.9)

    pokemon_image_label.place(relx=0.25, rely=0.4)

    # height.place(relx=0.025, rely=0.4)
    # weight.place(relx=0.5, rely=0.4)

    # hp.place(relx=0.025, rely=0.475)
    # attack.place(relx=0.025, rely=0.53)
    # defence.place(relx=0.025, rely=0.595)
    # specialAttack.place(relx=0.025, rely=0.66)
    # specialDefence.place(relx=0.025, rely=0.725)
    # speed.place(relx=0.025, rely=0.785)
    # total.place(relx=0.025, rely=0.845)


start_screen()

root.config(bg="red")
root.title("Pythodex")
root.geometry("550x600+50+50")
root.iconbitmap("./assets/PythodexLogo.ico")

root.mainloop()
