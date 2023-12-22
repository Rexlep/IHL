# IHL
This is a package for tkinter or customtkinter widgets

![Screenshot 2023-12-22 123309](https://github.com/Akascape/CTkListbox/assets/141561659/d25babec-82d0-4a90-a61c-6f7f66e186da)

## Installation
```
pip install IHL
```

## Usage
```python
import customtkinter as ctk
import tkinter as tk
from IHL.hover.option import Hover

root = ctk.CTk()
root.geometry('300x400')
root.title("IHL")

tk_btn = tk.Button(root, text="Hover Me", font=("Arial", 20))
tk_btn.pack(pady=40)

ctk_btn = ctk.CTkButton(root, text="Hover Me", font=("Arial", 20))
ctk_btn.pack()

Hover(tk_btn, "I am hover", duration=1, font=("Elephant", 12))
Hover(ctk_btn, "I am hover", duration=1)

root.mainloop()
```

## Arguments
| Parameter | Description |
|-----------| ------------|
| fg | text color of hover window |
| bg | color of background |
| border_color | border color of the hover window |
| border_width | width of the border frame |
| font | set font and size for text |
| move_with_mouse | movement of mouse |

Tanks for visiting i hope it was helpful to increase your development skill
