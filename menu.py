import tkinter
import psycopg2
import words
import writing_window

class Menu:
    def __init__(self, login, password, userId):
        self.__login = login
        self.__password = password
        self.__userId = userId

    # function which read data from Postgre database and makes words (but only for logged user)
    # and whole mechanism of flashcards
    def __read_from_database(self):
        #read from database
        polaczenie = psycopg2.connect(host="localhost", database="vocabulary", user=self.__login, password=self.__password, port=5432)
        kursor = polaczenie.cursor()
        sql = "SELECT word_id, word, definition FROM words WHERE owner_id = %s"
        kursor.execute(sql, str(self.__userId))
        rep_words = []
        kill_gui = 0
        for w in kursor:
            say = words.Words(w[0], w[1], w[2], kill_gui)
            help_in_rep_word = [say, 1]
            rep_words.append(help_in_rep_word)
        kursor.close()

        # mechanism
        counter = len(rep_words)
        counter_in_while = 0
        while counter != 0:
            if rep_words[counter_in_while][1] != 0:
                kill_gui = rep_words[counter_in_while][0].flashcard()
                if rep_words[counter_in_while][0].get_correctance():
                    rep_words[counter_in_while][1] -= 1
                else:
                    rep_words[counter_in_while][1] += 1
                if rep_words[counter_in_while][1] == 0:
                    counter -= 1
            counter_in_while = (counter_in_while + 1) % len(rep_words)

    def __add_new_word(self):
        return

    def __correct_word(self):
        return

    def __delete_word(self):
        oDW = writing_window.WritingWindow('Ktore slowo chcesz usunac?', 'DESTROYER', 'ACCEPT', self.__userId, 'DELETE FROM words WHERE word_id = %s AND user_id = %s')
        oDW.window()

    # it is a start point of application
    def __login(self):
        return

    def window(self):
        # making a root
        wind = tkinter.Tk()
        # putting a gui title
        wind.title('Hello ;)')

        # creating everything
        label = tkinter.Label(wind, width=45, bg='black', fg='red', text="MENU")
        button = tkinter.Button(wind, width=43, bg='black', fg='red', text='learn', borderwidth=7, command=self.__read_from_database)
        button2 = tkinter.Button(wind, width=43, bg='black', fg='red', text='add new', borderwidth=7, command=self.__add_new_word)
        button3 = tkinter.Button(wind, width=43, bg='black', fg='red', text='correct', borderwidth=7, command=self.__correct_word)
        button4 = tkinter.Button(wind, width=43, bg='black', fg='red', text='delete', borderwidth=7, command=self.__delete_word)
        button5 = tkinter.Button(wind, width=43, bg='black', fg='red', text='quit', borderwidth=7, command=wind.quit)

        # putting everything on the screen
        label.grid(row=0)
        button.grid(row=1)
        button2.grid(row=2)
        button3.grid(row=3)
        button4.grid(row=4)
        button5.grid(row=5)
        wind.mainloop()
