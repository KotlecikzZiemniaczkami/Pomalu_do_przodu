import menu

# base is just a list made of words and their definitions from database
me = menu.Menu('postgres', 'admin', 1)
me.window()

