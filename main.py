from tkinter import *
import requests
from tkinter import ttk
import tkinter as tk
window = tk.Tk()


root = Label(window, text="Abbasi currency converter",font = "arial 18 bold",width=60,bg="grey", bd =10,fg="black", relief=RAISED)
root.pack(padx=10, pady=10,fill=X)





window.title("Currency Converter")
window.config(bg="#202630")
window.geometry("400x450")

# set the window size and background imagei


#background_image = tk.PhotoImage(file="background.png")
#background_label = tk.Label(window, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create the custom styles for the widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), foreground="#333")
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12), foreground="#333")
style.configure("TButton", font=("Helvetica", 12), foreground="#fff", background="#333")
style.map("TButton", foreground=[("active", "#fff"), ("disabled", "#ccc")], background=[("active", "#333"), ("disabled", "#ccc")])

# get the currency exchange rates from the internet
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
rates = response.json()['rates']

# create the available currencies list
available_currencies = list(rates.keys())

# create the input widgets
amount_label = ttk.Label(window, text="Please Enter amount:")
amount_label.pack(pady=20)
amount_entry = ttk.Entry(window)
amount_entry.pack()

currency_from_label = ttk.Label(window, text="From:")
currency_from_label.pack(pady=10)
currency_from_menu = ttk.Combobox(window, values=available_currencies, state="readonly")
currency_from_menu.pack()

currency_to_label = ttk.Label(window, text="To:")
currency_to_label.pack(pady=10)
currency_to_menu = ttk.Combobox(window, values=available_currencies, state="readonly")
currency_to_menu.pack()

result_label = ttk.Label(window, text="", style="TLabel")
result_label.pack(pady=20)

# create the conversion function
def convert_currency():
    try:
        # get the input values
        amount = float(amount_entry.get())
        currency_from = currency_from_menu.get()
        currency_to = currency_to_menu.get()

        # convert the currency
        result = amount * rates[currency_to] / rates[currency_from]

        # update the result label
        result_label.configure(text=f"{amount:.2f} {currency_from} is equal to {result:.2f} {currency_to}")
    except ValueError:
        result_label.configure(text="Invalid input")

def exp():
    exit()

button = tk.Button(window, text="PRESS TO CONVERT", command=convert_currency,fg="dark red",bg='white',bd=10)
button.pack(pady=20)
but2 = tk.Button(window,text="EXIT",command=exp,fg="dark red",bg='white',bd=10)
but2.pack(pady=0)

window.mainloop()


root.mainloop()
