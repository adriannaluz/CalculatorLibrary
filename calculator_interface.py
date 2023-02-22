# calculator visual interface

import PySimpleGUI as sg

# Layout / Create GUI
layout = [
    [sg.Txt("" * 10)],
    [sg.Text("", size=(15, 1), font=("Helvetica", 18),
             text_color="red", key="input")],
    [sg.Txt("" * 10)],
    [
        sg.ReadFormButton("("),
        sg.ReadFormButton(")"),
        sg.ReadFormButton("c"),
        sg.ReadFormButton("«"),
    ],
    [
        sg.ReadFormButton("7"),
        sg.ReadFormButton("8"),
        sg.ReadFormButton("9"),
        sg.ReadFormButton("÷"),
    ],
    [
        sg.ReadFormButton("4"),
        sg.ReadFormButton("5"),
        sg.ReadFormButton("6"),
        sg.ReadFormButton("x"),
    ],
    [
        sg.ReadFormButton("1"),
        sg.ReadFormButton("2"),
        sg.ReadFormButton("3"),
        sg.ReadFormButton("-"),
    ],
    [
        sg.ReadFormButton("."),
        sg.ReadFormButton("0"),
        sg.ReadFormButton("="),
        sg.ReadFormButton("+"),
    ],
]

# Set PySimpleGUI
form = sg.Window(
    "CALCULATOR",
    default_button_element_size=(5, 2),
    auto_size_buttons=False,
    grab_anywhere=False,
)
form.Layout(layout)

# Set Process
Equal = ""
List_Op_Error = ["+", "-", "*", "/", "("]

# Loop
while True:
    button, value = form.Read()  # call GUI

    # close the window
    if button == "Quit" or button is None:
        break
