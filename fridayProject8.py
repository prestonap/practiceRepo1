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