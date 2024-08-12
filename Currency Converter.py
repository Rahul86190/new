import tkinter as tk
from tkinter import ttk
import requests

API_key = '93ce16f5d26f81761edc5329'
BASE_URL = 'https://v6.exchangerate-api.com/v6'

currencies = [
    "USD","INR","EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY",
    "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY",
    "RUB", "BRL", "ZAR", "PHP", "CZK", "IDR", "MYR",
    "HUF", "ISK", "HRK"
]

def fetch_rate(from_currency, to_currency):
    url = f"{BASE_URL}/{API_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rate']
    else:
        raise Exception("Failed to fetch exchange rate")

def currency_converter():
    try:
        from_currency = from_var.get()
        to_currency = to_var.get()
        amount_to_convert = float(enter_amt.get())

        rate = fetch_rate(from_currency, to_currency)
        amount_converted = amount_to_convert * rate

        result.config(text=f"{amount_to_convert} {from_currency} = {amount_converted:.2f} {to_currency}")
    except ValueError:
        result.config(text="Invalid input")
    except Exception as e:
        result.config(text=f"Error occurred: {str(e)}")


root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.config(bg="#1ABC9C")

title_label = tk.Label(root, text="Currency Converter", fg="white", bg="#1ABC9C", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#1ABC9C")
frame.pack(pady=10)

from_var = tk.StringVar(root)
from_var.set('INR')
from_label = tk.Label(frame, text="From:", fg="white", bg="#1ABC9C", font=("Arial", 12))
from_label.grid(row=0, column=0, padx=10)
from_menu = ttk.Combobox(frame, textvariable=from_var, values=currencies, state="readonly", width=10)
from_menu.grid(row=0, column=1, padx=10)

to_var = tk.StringVar(root)
to_var.set('USD')
to_label = tk.Label(frame, text="To:", fg="white", bg="#1ABC9C", font=("Arial", 12))
to_label.grid(row=1, column=0, padx=10, pady=5)
to_menu = ttk.Combobox(frame, textvariable=to_var, values=currencies, state="readonly", width=10)
to_menu.grid(row=1, column=1, padx=10, pady=5)

amount_label = tk.Label(frame, text="Amount:", fg="white", bg="#1ABC9C", font=("Arial", 12))
amount_label.grid(row=2, column=0, padx=10)
enter_amt = tk.Entry(frame, width=12)
enter_amt.grid(row=2, column=1, padx=10)

convert_button = tk.Button(root, text="Convert", command=currency_converter, bg="pink", fg="blue", font=("Arial", 12, "bold"), relief="raised")
convert_button.pack(pady=15)

result = tk.Label(root, text="", fg="white", bg="#1ABC9C", font=("Arial", 14, "bold"))
result.pack(pady=10)

root.mainloop()
