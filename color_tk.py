from tkinter import *
import random

score = 0
displayed_color = None

def enter_but():
    global score
    user_input = color.get().strip().lower()
    if user_input == displayed_color['fg']:
        score += 1
    score_label.config(text=f"Score: {score}")
    display_text()

def display_text():
    colors = ["blue", "orange", "yellow", "green", "pink", "black", "red"]
    random_color = random.choice(colors)
    
    text_options = [c for c in colors if c != random_color]
    random_text = random.choice(text_options)
    
    displayed_color.config(text=random_text, fg=random_color)

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="white")
    gui.title("Color Game")

    gui.geometry("300x300")
    
    score_label = Label(gui, text="Score: 0", font=('Arial', 12), bg="white")
    score_label.grid(row=0, column=0, columnspan=2)
    
    displayed_color = Label(gui, font=('Arial', 24))
    displayed_color.grid(row=1, column=0, columnspan=2)
    
    color = StringVar()
    color_field = Entry(gui, textvariable=color,bd=2,relief="solid")
    color_field.grid(row=2, column=0, columnspan=2)
    
    enter_button = Button(gui, text="Enter", command=enter_but)
    enter_button.grid(row=3, column=0, columnspan=2)
    
    display_text()
    
    gui.mainloop()
