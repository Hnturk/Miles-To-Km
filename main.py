from tkinter import *


def converter():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


screen = Tk()
screen.title("Miles to Kilometer Converter")
screen.config(padx=30, pady=30)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

convert_btn = Button(text="Convert", command=converter)
convert_btn.grid(column=1, row=2)

screen.mainloop()
