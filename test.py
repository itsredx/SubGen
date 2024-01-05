import tkinter as tk
from tkinter import *



def create_toggle_button(root, image1, image2, value):
    """Creates a toggle button with image switching and state tracking."""
    photo1 = tk.PhotoImage(file=image1)
    photo2 = tk.PhotoImage(file=image2)
    button = tk.Button(
        root,
        image=photo1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: toggle_button(button, photo1, photo2, value)
    )
    button.image_on = photo1
    button.image_off = photo2
    button.value = value
    return button

def toggle_button(button, image_on, image_off, value):
    """Toggles the button's image and updates other buttons accordingly."""
    if button.config('image')[-1] == image_on:
        button.config(image=image_off)
        global active_button_value
        active_button_value = None
    else:
        button.config(image=image_on)
        active_button_value = value

        # Set other buttons to "off" state
        for other_button in toggle_buttons:
            if other_button != button:
                other_button.config(image=other_button.image_off)

root = tk.Tk()

toggle_buttons = []
active_button_value = None

# Create and place the toggle buttons
button1 = create_toggle_button(root, "img02.png", "img01.png", 1)
button1.place(x=100, y=50)
toggle_buttons.append(button1)

button2 = create_toggle_button(root, "img04.png", "img03.png", 2)
button2.place(x=250, y=50)
toggle_buttons.append(button2)

button3 = create_toggle_button(root, "img05.png", "img06.png", 3)
button3.place(x=400, y=50)
toggle_buttons.append(button3)

# Set the initial state of the first button to "on"
print(toggle_buttons)
toggle_buttons[0].config(image=toggle_buttons[0].image_on)
toggle_buttons[1].config(image=toggle_buttons[1].image_off)
toggle_buttons[2].config(image=toggle_buttons[2].image_off)
active_button_value = toggle_buttons[0].value


root.mainloop()

"""
    img01 = PhotoImage(file = f"img01.png")
    b3 = Button(
        image = img01,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b3.place(
        x = 767, y = 143,
        width = 73,
        height = 28)

    img03 = PhotoImage(file = f"img03.png")
    b4 = Button(
        image = img03,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 684, y = 143,
        width = 73,
        height = 28)


    img06 = PhotoImage(file = f"img06.png")
    b5 = Button(
        image = img06,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b5.place(
        x = 601, y = 143,
        width = 73,
        height = 28)

"""
