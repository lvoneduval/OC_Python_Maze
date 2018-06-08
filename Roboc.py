#! /usr/bin/env python3
# coding: utf-8
from Menu import *
from Map import Map
import os

def move(direction, map_game):
    x,y = direction
    increment = -1 if (x < 0 or y < 0) else 1
    ret = 0
    while not ret and x != 0:
        ret = map_game.move(increment, 0)
        x -= increment
    while not ret and y != 0:
        ret = map_game.move(0, increment)
        y -= increment
    return (ret)


def play_game(Map):
    choices_game_menu = {
        "N": (move, (0, -1), "Bouger au nord"),
        "E": (move, (1, 0), "Bouger a l'est"),
        "S": (move, (0, 1), "Bouger au sud"),
        "O": (move, (-1, 0), "Bouger a l'ouest"),
        "Q": (Menu.quit, None, "Quitter et sauvegarder")
    }
    game_menu = Game(choices_game_menu, "", Map)
    game_menu.run()

def load_game(load_dir):
    choices_load_menu = {}
    i = 0
    for file_name in os.listdir(load_dir):
        if file_name.endswith(".txt"):
            path = os.path.join("cartes", file_name)
            map_name = file_name[:-3].lower()
            with open(path, "r") as fd:
                content = fd.read()
                tmp_map = Map(content, map_name)
                print(tmp_map)
                choices_load_menu[str(i)] = (play_game, tmp_map, map_name)
                i += 1
    choices_load_menu["Q"] = (Menu.quit, None, "retour")
    menu_game = Menu(choices_load_menu, "Choisissez une carte")
    menu_game.run()
        

def main():
    choices_main_menu = {
            "1": (load_game, "cartes", "Nouvelle Partie") ,
            "2": (load_game, "sauvegardes", "Charger une Partie"),
            "Q": (exit, None, "quitter")   
            }
    main_menu = Menu(choices_main_menu,"Menu principal")
    main_menu.run()

if __name__ == "__main__":
    main()
