import menu

# base is just a list made of words and their definitions from database
me = menu.Menu('postgres', 'admin', 1)
me.window()

# trzeba dodac ekran logowania, dodatkowa tabele w bazie danych z danymi uzytkownika, polaczyc tabele relacja,
# wprowadzic zabezpieczenia zeby kazdy uzytkownik mogl pracowac tylko na swoich kartach,
# poprawic kod sql w words zeby pobieral tylko fiszki aktualnego uzytkownika
# oraz dokonczyc wszystkie gui
