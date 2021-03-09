from tkinter import *
import random as r

a = ["lion", "tiger", "cow"]
b = ["maruthi", "martin", "suzuki"]
c = ["biriyani", "kebab", "curry"]
m = {"animal": a, "cars": b, "food": c}

x = 'cars'
j = r.choice(m[x])
j2 = j
print(j)
j = list(j)
h = list("_" * len(j))
ch = 6
hang = 0
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def reset():
    global ch, hang, h, j, j2
    a = ["lion", "tiger", "cow"]
    b = ["maruthi", "martin", "suzuki"]
    c = ["biriyani", "kebab", "curry"]
    m = {"animal": a, "cars": b, "food": c}
    x = 'cars'
    j = r.choice(m[x])
    j2 = j
    print(j)
    j = list(j)
    h = list("_" * len(j))
    ch = 6
    hang = 0
    man.configure(text=hangman[hang])
    word.configure(text=h)


def playagain():
    play = Tk()
    play.configure(bg='#34495E')
    play.geometry('400x300')
    playmsg = Label(play, text="PLAY AGAIN?", font=('Times', 35, 'bold'), relief=RAISED, bd=5, bg='#1C2833', fg='red',
                    padx=10, pady=20)
    playmsg.place(x=25, y=0)
    btno = Button(play, text='NO', font=('Georgia', 17, 'bold'), bd=5, bg='red', padx=50, pady=50,
                  command=lambda: [hng.destroy(), play.destroy()])
    btno.place(x=20, y=120)
    btyes = Button(play, text='YES', font=('Georgia', 17, 'bold'), bd=5, bg='red', padx=50, pady=50,
                   command=lambda: [reset(), play.destroy()])
    btyes.place(x=210, y=120)
    play.mainloop()


def checkwin():
    if h == list(j2):
        word.configure(text='YOU WIN', fg='#7D3C98')
        playagain()


def checklose():
    if ch == 0:
        word.configure(text='YOU LOSE')
        playagain()


def replace()  :
    y = guess.get()
    if (y in j):
        print("success")
        l = j.index(y)
        j[l] = "guessed"
        h[l] = y
        word.configure(text=h)


def check_guess():
    global ch, hang
    k = guess.get()
    print(k)
    if (str(k) in j):
        replace()
    else:
        ch -= 1
        hang += 1
        man.configure(text=hangman[hang])
        # chances.configure(text=ch)
    guess.delete(0, END)
    checkwin()
    checklose()


hng = Tk()
hng.geometry('900x500')
hng.configure(bg='#34495E')
title = Label(hng, text='HANGMAN', font=('Georgia', 35, 'bold'), relief=RAISED, bd=5, bg='#1C2833', fg='red')
title.grid(row=0, column=5)

guess = Entry(hng, font=('Georgia', 25, 'bold'), relief=RIDGE, bd=5, bg='cyan', justify='center', fg='white')
guess.grid(row=4, column=5)

word = Label(hng, text=h, font=('Georgia', 55, 'bold'), bg='#34495E')
word.grid(row=3, column=5)

'''chances=Label(hng,text=ch,font=('Georgia',55,'bold'),bg='#34495E')
chances.grid(row=2,column=0)'''

man = Label(hng, text=hangman[0], font=('Georgia', 40, 'bold'), bg='#34495E', fg='white')
man.grid(row=0, column=15, rowspan=10, columnspan=2)

bt1 = Button(hng, text='SUBMIT', font=('Georgia', 15, 'bold'), width=15, bd=5, bg='red', command=check_guess)
bt1.grid(row=6, column=5)

hng.mainloop()
