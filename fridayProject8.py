import sqlite3
import tkinter as tk
from tkinter import messagebox

# --- Step 1: Create/connect to the database ---
conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birthday TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    contact_method TEXT
)
''')

conn.commit()

# --- Step 2: Create the GUI using Tkinter ---
root = tk.Tk()
root.title("Customer Info Form")
# --- Labels and Entry fields ---
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Birthday").grid(row=1, column=0)
birthday_entry = tk.Entry(root)
birthday_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Phone").grid(row=3, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1)

tk.Label(root, text="Address").grid(row=4, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1)