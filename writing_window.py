import tkinter

# it is a class which will be mother of 2 windows: delete word and correct word

class WritingWindow:
    def __init__(self, label: str, title: str, writing: str):
        self.__writing1 = label
        self.__writing2 = writing
        self.__title = title
        self.__ww = 0
        self.__en = 0
        self.__id = 0

    # is reading an id which was written by user
    def giveId(self):
        self.__id = int(self.en.get())

    # GUI
    def window(self):
        # making a root
        self.__ww = tkinter.Tk()
        # putting a gui title
        self.__ww.title(self.__title)
        # everything what will be on the screen
        label = tkinter.Label(self.__ww, width=45, bg='red', fg='black', text=self.__writing1)
        en = tkinter.Entry(self.__ww, width=50, bg='black', fg='red', borderwidth=10)
        self.en.insert(0, "Id: ")
        button = tkinter.Button(self.__ww, width=20, bg='red', fg='black', text=self.__writing2, borderwidth=7, command = self.giveId)

        label.grid(row=0)
        en.grid(row=1)
        button.grid(row=2)

    # is returning id
    def getId(self):
        return self.__id