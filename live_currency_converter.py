import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Replace with your free API key from https://www.exchangerate-api.com/
API_KEY = '6a98bb7a5f8b3ab44cdee0a3'
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Function to perform currency conversion


def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_cb.get()
        to_currency = to_currency_cb.get()

        if from_currency == "" or to_currency == "":
            messagebox.showwarning("Warning", "Select both currencies")
            return

        response = requests.get(API_URL + from_currency)
        data = response.json()

        if data["result"] == "success":
            rate = data["conversion_rates"][to_currency]
            result = round(amount * rate, 2)
            result_label.config(
                text=f"{amount} {from_currency} = {result} {to_currency}")
        else:
            messagebox.showerror("Error", "Failed to fetch exchange rates.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")


# Create GUI window
app = tk.Tk()
app.title("Currency Exchange App")
app.geometry("700x500")
app.resizable(True, True)

# Title
title_label = tk.Label(app, text="Currency Converter", font=("Helvetica", 16))
title_label.pack(pady=10)

# Amount Entry
amount_entry = tk.Entry(app, font=("Helvetica", 12), justify='center')
amount_entry.pack(pady=5)
amount_entry.insert(0, "1")

# Currency Dropdowns
currency_list = ["USD", "EUR", "GBP", "GHS",
                 "NGN", "INR", "JPY", "CNY", "CAD", "AUD"]
from_currency_cb = ttk.Combobox(
    app, values=currency_list, font=("Helvetica", 10))
to_currency_cb = ttk.Combobox(
    app, values=currency_list, font=("Helvetica", 10))
from_currency_cb.pack(pady=5)
to_currency_cb.pack(pady=5)
from_currency_cb.set("USD")
to_currency_cb.set("GHS")

# Convert Button
convert_btn = tk.Button(app, text="Convert", command=convert_currency, font=(
    "Helvetica", 12), bg="#4CAF50", fg="white")
convert_btn.pack(pady=10)

# Result Display
result_label = tk.Label(app, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the app
app.mainloop()
