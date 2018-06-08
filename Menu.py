class Menu():
    """ Menu controleur """

    MSG_KEY_ERROR = "Vous avez fait un choix non valide:"
    def __init__(self, menu_choices_table, menu_name):
        self.name = menu_name
        self.choices = menu_choices_table
    
    def __str__(self):
        ret_str = self.name + "\n"
        for choice_key, choice_value in self.choices.items():
            ret_str += "{button}: {name}\n".format(button=choice_key, name=choice_value[2])
        return (ret_str)
    
    @classmethod
    def quit(cls):
        return 1

    def run(self):
        is_end = 0
        while not is_end:
            print(self)
            button = input()
            try:
                func, arg, name = self.choices[button]
                #protejer l'input: équivalent des injections?
                #simplifier les 2 lignes du dessous ?
                if arg:
                    is_end = func(arg)
                else:
                    is_end = func()
            except KeyError:
                print(self.MSG_KEY_ERROR)

class Game(Menu):
    def __init__(self, menu_choices_table, menu_name, map_game):
        self.name = menu_name
        self.choices = menu_choices_table
        self.map_game = map_game
    
    def run(self):
        is_end = 0
        while not is_end:
            print(self)
            print(self.map_game)
            button = input()
            try:
                list_button = list(button)
                button = list_button.pop(0)
                complement = "".join(list_button)
                func, arg, name = self.choices[button]
                if arg:
                    if (complement and complement.isdigit()):
                        arg = [x * int(complement) for x in arg]
                    elif complement and not complement.isdigit():
                        print(self.MSG_KEY_ERROR)
                        continue 
                    is_end = func(arg, self.map_game)
                else:
                    is_end = func()
            except KeyError:
                print(self.MSG_KEY_ERROR)
            
