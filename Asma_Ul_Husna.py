# -*- coding: utf-8 -*-
# 99 Names of Allah - GUI Version with Serial Numbers
# Works in Spyder / Anaconda (Python 3.x)

import tkinter as tk
import random

# List of 99 Names (Arabic + Meaning)
asma_ul_husna = [
    ("Allah", "The Greatest Name, God"),
    ("Ar-Rahman", "The Beneficent"),
    ("Ar-Raheem", "The Merciful"),
    ("Al-Malik", "The King, The Owner of Dominion"),
    ("Al-Quddus", "The Absolutely Pure"),
    ("As-Salam", "The Source of Peace"),
    ("Al-Mu'min", "The Giver of Faith, The One Who Gives Security"),
    ("Al-Muhaymin", "The Guardian, The Witness, The Overseer"),
    ("Al-Aziz", "The Almighty, The Powerful"),
    ("Al-Jabbar", "The Compeller, The Restorer"),
    ("Al-Mutakabbir", "The Supreme, The Majestic"),
    ("Al-Khaliq", "The Creator"),
    ("Al-Bari", "The Evolver"),
    ("Al-Musawwir", "The Fashioner"),
    ("Al-Ghaffar", "The All- and Oft-Forgiving"),
    ("Al-Qahhar", "The Subduer, The Ever-Dominating"),
    ("Al-Wahhab", "The Bestower"),
    ("Ar-Razzaq", "The Provider"),
    ("Al-Fattah", "The Opener, The Judge"),
    ("Al-Alim", "The All-Knowing, The Omniscient"),
    ("Al-Qabid", "The Withholder"),
    ("Al-Basit", "The Extender"),
    ("Al-Khafid", "The Abaser"),
    ("Ar-Rafi", "The Exalter"),
    ("Al-Mu’izz", "The Honourer, The Bestower"),
    ("Al-Mudhill", "The Dishonourer"),
    ("As-Sami", "The All-Hearing"),
    ("Al-Basir", "The All-Seeing"),
    ("Al-Hakam", "The Judge, The Giver of Justice"),
    ("Al-Adl", "The Utterly Just"),
    ("Al-Latif", "The Subtle One, The Most Gentle"),
    ("Al-Khabir", "The All-Aware"),
    ("Al-Haleem", "The Forbearing, The Indulgent"),
    ("Al-Azeem", "The Magnificent, The Supreme"),
    ("Al-Ghafoor", "The Forgiving, The Exceedingly Forgiving"),
    ("Ash-Shakur", "The Most Appreciative"),
    ("Al-Ali", "The Most High, The Exalted"),
    ("Al-Kabir", "The Most Great"),
    ("Al-Hafiz", "The Preserver, The All-Heedful"),
    ("Al-Muqit", "The Nourisher"),
    ("Al-Hasib", "The Reckoner"),
    ("Al-Jalil", "The Majestic"),
    ("Al-Karim", "The Generous, The Bountiful"),
    ("Ar-Raqib", "The Watchful"),
    ("Al-Mujib", "The Responsive"),
    ("Al-Wasi", "The All-Encompassing, The Boundless"),
    ("Al-Hakim", "The All-Wise"),
    ("Al-Wadud", "The Most Loving"),
    ("Al-Majid", "The Glorious, The Most Honorable"),
    ("Al-Ba'is", "The Infuser of New Life"),
    ("Ash-Shahid", "The Witness"),
    ("Al-Haqq", "The Ultimate Truth"),
    ("Al-Wakil", "The Trustee, The Disposer of Affairs"),
    ("Al-Qawiyy", "The All-Strong"),
    ("Al-Mateen", "The Firm, The Steadfast"),
    ("Al-Waliyy", "The Protecting Friend, Patron, and Helper"),
    ("Al-Hamid", "The All Praiseworthy"),
    ("Al-Muhsi", "The Accounter, The Numberer of All"),
    ("Al-Mubdi", "The Originator, The Initiator"),
    ("Al-Mu'id", "The Restorer, The Reinstater"),
    ("Al-Muhyi", "The Giver of Life"),
    ("Al-Mumit", "The Creator of Death"),
    ("Al-Hayy", "The Ever-Living"),
    ("Al-Qayyum", "The Sustainer, The Self-Subsisting"),
    ("Al-Wajid", "The Finder, The Perceiver"),
    ("Al-Majid", "The Illustrious, The Magnificent"),
    ("Al-Wahid", "The One, The Unique"),
    ("Al-Ahad", "The only and one, The indivisible"),
    ("As-Samad", "The Eternal, The Absolute"),
    ("Al-Qadir", "The Omnipotent"),
    ("Al-Muqtadir", "The Determiner, The Dominant"),
    ("Al-Muqaddim", "The Expediter, The Promoter"),
    ("Al-Mu’akhkhir", "The Delayer, The Retarder"),
    ("Al-Awwal", "The First"),
    ("Al-Akhir", "The Last"),
    ("Az-Zahir", "The Manifest"),
    ("Al-Batin", "The Hidden"),
    ("Al-Wali", "The Protecting Friend, The Patron"),
    ("Al-Muta'ali", "The Most Exalted"),
    ("Al-Barr", "The Source of All Goodness"),
    ("At-Tawwab", "The Ever-Accepting of Repentance"),
    ("Al-Muntaqim", "The Avenger"),
    ("Al-Afuww", "The Pardoner"),
    ("Ar-Ra’uf", "The Compassionate"),
    ("Malik-ul-Mulk", "The Owner of Sovereignty"),
    ("Al-Muqsit", "The Just One"),
    ("Al-Jami", "The Gatherer, The Uniter"),
    ("Al-Ghani", "The Self-Sufficient, The Wealthy"),
    ("Al-Mughni", "The Enricher"),
    ("Al-Mani", "The Withholder, The Preventer"),
    ("Ad-Darr", "The Distresser"),
    ("An-Nafi", "The Benefactor"),
    ("An-Nur", "The Light"),
    ("Al-Hadi", "The Guide"),
    ("Al-Badi", "The Incomparable Originator"),
    ("Al-Baqi", "The Everlasting"),
    ("Al-Warith", "The Inheritor, The Heir"),
    ("Ar-Rashid", "The Guide to the Right Path"),
    ("As-Sabur", "The Patient"),
    ("Dhul-Jalali wal-Ikram", "Lord of Glory and Honour")
]

current_index = 0

# Function to display current name
def show_name(index):
    arabic, meaning = asma_ul_husna[index]
    name_label.config(text=f"{index+1:02d}. {arabic}")
    meaning_label.config(text=meaning)

def next_name():
    global current_index
    current_index = (current_index + 1) % len(asma_ul_husna)
    show_name(current_index)

def prev_name():
    global current_index
    current_index = (current_index - 1) % len(asma_ul_husna)
    show_name(current_index)

def random_name():
    global current_index
    current_index = random.randint(0, len(asma_ul_husna)-1)
    show_name(current_index)

# GUI Setup
root = tk.Tk()
root.title("99 Names of Allah (Asma Ul Husna)")
root.geometry("500x300")
root.configure(bg="#f5f5dc")  # light beige

# Title
title = tk.Label(root, text="Asma Ul Husna", font=("Helvetica", 20, "bold"), bg="#f5f5dc", fg="#2e2e2e")
title.pack(pady=10)

# Name Display
name_label = tk.Label(root, text="", font=("Arial", 24, "bold"), bg="#f5f5dc", fg="#005f5f")
name_label.pack(pady=10)

meaning_label = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5dc", fg="#333333", wraplength=400)
meaning_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#f5f5dc")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="◀ Previous", command=prev_name, width=12, bg="#d9ead3").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="🔀 Random", command=random_name, width=12, bg="#f9cb9c").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Next ▶", command=next_name, width=12, bg="#cfe2f3").grid(row=0, column=2, padx=5)

# Initialize display
show_name(current_index)

root.mainloop()


