from tkinter import*
import random
import string

protex_li = string.ascii_lowercase

get = []


for rec in range(0, random.randint(7, 10)):
    get.append(str(random.choice(protex_li)))

mylist = ''.join(get)

protex_li_1 = [
    'mail.ru',
    'gmail.com',
    'yandex.ru',
    'coolmail.ru',
    'coolshit.com',
]
protex_end = []
for i in range(0, 3):
    protex_end.append(mylist + str('@') + random.choice(protex_li_1))


class GenAddr:
    def __init__(self):
        self.fra = Frame(roGen)
        self.fra.pack(side=LEFT)

        self.fra2 = Frame(roGen)
        self.fra2.pack(side=RIGHT)

        self.tex = Text(self.fra, width = 30, height = 3, wrap=WORD)
        self.tex.pack()

        self.butGen = Button(self.fra2, text = 'Start', bg = 'gray', fg = 'white', width = 5)
        self.butGen.bind('<Button-1>', self.startGen)
        self.butGen.pack(padx = 10, pady = 6)

        self.but = Button(self.fra2, text = 'Exit', bg = 'gray', fg = 'white',width = 5, command = quit)
        self.but.bind('<Button-2>', self.outgo)
        self.but.pack(padx = 10, pady = 6)

    def startGen(self, event):
        self.tex.delete(1.0, END)
        self.tex.insert(END, protex_end)

    def outgo(self, event):
        roGen.destroy()

if __name__ == '__main__':

    roGen = Tk()
    roGen.geometry('300x90')
    obj = GenAddr()
    roGen.mainloop()