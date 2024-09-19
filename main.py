from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
#*-------------------------------------------------*
try:
    data=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
words =data.to_dict(orient="records")
current_word = {}

#*-------------------------------------------------*

def next_card():
    global current_word, flip_timer
    screen.after_cancel(flip_timer)
    current_word = random.choice(words)
    canvas.itemconfigure(language_name,text="French")
    canvas.itemconfigure(word, text=current_word["French"])
    canvas.itemconfigure(canvas_picture, image=front_image)

    screen.after(3000, english_side)
#****************************************************

def english_side():
    canvas.itemconfigure(language_name, text="English")
    canvas.itemconfigure(word, text=current_word["English"])
    canvas.itemconfigure(canvas_picture, image=back_image)
#****************************************************

def remove_learned_card():
    global current_word
    words.remove(current_word)

    words_to_learn = pandas.DataFrame(words)
    words_to_learn.to_csv('./data/words_to_learn.csv')
    next_card()


#*-------------------------------------------------*
screen = Tk()
screen.config(padx=60, pady=60, bg=BACKGROUND_COLOR)
screen.title("Flashy")

#*-------------------------------------------------*
canvas = Canvas()
canvas.config(width=800,height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
#canvas image
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_picture = canvas.create_image(400, 262, image=front_image)
#canvas text
language_name = canvas.create_text(400, 150, text="", fill="#000000" ,font=("Courier", 40, "normal"))
word = canvas.create_text(400, 263, text="",fill="#000000", font=("Courier", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

flip_timer = screen.after(3000,english_side)
#*-------------------------------------------------*
cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image)
cross_button.config(borderwidth=0, highlightcolor=BACKGROUND_COLOR, command=next_card)
cross_button.grid(row=1, column=0)

#****************************************************
check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image)
check_button.config(borderwidth=0, highlightcolor=BACKGROUND_COLOR, command=remove_learned_card)
check_button.grid(row=1, column=1)

#*-------------------------------------------------*
next_card()

screen.mainloop()