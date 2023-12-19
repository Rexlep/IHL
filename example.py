import customtkinter as ctk
import tkinter as tk
from ihover.option import Hover

root = ctk.CTk()
root.geometry('300x400')
root.title("ihover")

tk_btn = tk.Button(root, text="Hover Me", font=("Arial", 20))
tk_btn.pack(pady=40)

ctk_btn = ctk.CTkButton(root, text="Hover Me", font=("Arial", 20))
ctk_btn.pack()

Hover(tk_btn, "I am hover", duration=1, font=("Elephant", 12))
Hover(ctk_btn, "I am hover", duration=1)

root.mainloop()