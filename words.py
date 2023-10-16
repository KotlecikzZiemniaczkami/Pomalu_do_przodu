import tkinter

# class which main task is represent word and definition of this word
class Words:
    def __init__(self, word_id: int, word: str, definition: str, kill: int):
        self.__word_id = word_id
        self.__word = word
        self.__definition = definition
        self.fc = 0
        self.en = 0
        self.__kill = kill

    # just setter
    def set_word(self, word, definition):
        self.__word = word
        self.__definition = definition

    # just getter (gets word)
    def get_word(self):
        return self.__word

    # just getter (gets definition)
    def get_definition(self):
        return self.__definition

    # it is for a check button from flashcard method. It checks if word given by user is correct
    def read(self):
        is_correct = "Your answer is incorrect. Next time try: " + self.__word
        answer = self.en.get()
        if answer == self.__word:
            is_correct = "Great!"

        label = tkinter.Label(self.fc, width=45, bg='red', fg='black', text=is_correct)
        label.grid(row=4, column=0, columnspan=2)

    #it is killing a GUI
    def stop(self):
        self.__kill = 1
        self.fc.destroy()

    # GUI of a flashcard
    def flashcard(self):
        # checks if GUI can exist longer
        if self.__kill:
            return self.__kill
        # making a root
        self.fc = tkinter.Tk()
        # putting a gui title
        self.fc.title('fight the word!')

        # creating everything
        label = tkinter.Label(self.fc, width=45, bg='red', fg='black', text="definition: " + self.__definition)
        self.en = tkinter.Entry(self.fc, width=50, bg='black', fg='red', borderwidth=10)
        self.en.insert(0, "word:")
        button = tkinter.Button(self.fc, width=20, bg='red', fg='black', text='check', borderwidth=7, command=self.read)
        button2 = tkinter.Button(self.fc, width=20, bg='red', fg='black', text='stop', borderwidth=7, command=self.stop)
        label2 = tkinter.Label(self.fc, width=45, bg='red', fg='black',
                               text="this card's id is: " + str(self.__word_id))

        # putting everything on the screen
        label.grid(row=0, column=0, columnspan=2)
        self.en.grid(row=1, column=0, columnspan=2)
        button.grid(row=2, column=0)
        button2.grid(row=2, column=1)
        label2.grid(row=3, column=0, columnspan=2)
        self.fc.mainloop()
        return self.__kill

