# My first Python GUI for keeping track of exchange rates
# Author: Mustafa Osman Dilmaç

import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

currency_codes = ["TRY","USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "KRW", "SGD", "NOK", "MXN"]

def get_exchange(from_currency_var, to_currency_var, amount_entry, result_label):

    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())
  
    c = CurrencyRates()

    result = c.convert(from_currency, to_currency, amount)

    result_label.config(text=f"Converted Amount: {result:.2f} {to_currency}")


def main():
    root = tk.Tk()
    root.geometry("330x300")
    root.title("Currency Converter by MOD")
    root.resizable(False,False)
    
    frame = tk.Frame(root)
    frame.pack(padx=20,pady=20)

    from_currency_label = tk.Label(frame, text="Convert From:")
    from_currency_label.grid(row=0,column=0)

    from_currency_var = tk.StringVar()
    from_currency_menu = ttk.Combobox(frame, textvariable=from_currency_var, values=currency_codes)
    from_currency_menu.grid(row=0, column=1)
    from_currency_menu.set("TRY")

    to_currency_label = tk.Label(frame, text="To Currency:")
    to_currency_label.grid(row=1, column=0)

    to_currency_var = tk.StringVar()
    to_currency_menu = ttk.Combobox(frame, textvariable=to_currency_var, values=currency_codes)
    to_currency_menu.grid(row=1, column=1)
    to_currency_menu.set("USD")

    amount_label = tk.Label(frame, text="Amount:")
    amount_label.grid(row=2, column=0)

    amount_entry = tk.Entry(frame)
    amount_entry.grid(row=2, column=1)

    convert_button = tk.Button(frame, text="Convert", command=lambda: get_exchange(from_currency_var, to_currency_var, amount_entry, result_label))
    convert_button.grid(row=3, column=0, columnspan=2)

    result_label = tk.Label(frame, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()