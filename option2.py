import customtkinter as ctk


class ToolTip(object):
    def __init__(self, widget, duration=1.0, font=("tahoma", 12, "normal"),
                 bg="#2B2B2B", fg="#ffffff", borderwidth=1):
        self.widget = widget
        self.tipwindow = None
        self.x = self.y = 0
        self.duration = duration
        self.delay_id = None
        self.font = font
        self.bg = bg
        self.fg = fg
        self.borderwidth = borderwidth

    def showtip(self, text):
        "Display text in the tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_pointerx() + 10
        y = self.widget.winfo_pointery() + 10
        self.tipwindow = ctk.CTkToplevel(self.widget)
        self.tipwindow.wm_overrideredirect(True)
        self.tipwindow.wm_geometry("+%d+%d" % (x, y))
        label = ctk.CTkLabel(
            self.tipwindow,
            text=self.text,
            justify=ctk.LEFT,
            background=self.bg,
            foreground=self.fg,
            relief=ctk.SOLID,
            borderwidth=self.borderwidth,
            font=self.font
        )
        label.pack(ipadx=1)
        self.tipwindow.bind('<Motion>', self.on_tooltip_motion)  # Bind <Motion> event

    def on_tooltip_motion(self, event):
        "Update tooltip position with mouse movement"
        if self.tipwindow:
            x = event.x_root + 10
            y = event.y_root + 10
            self.tipwindow.wm_geometry("+%d+%d" % (x, y))

    def hidetip(self):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None

    def delayed_showtip(self, text):
        if self.widget.winfo_ismapped() and self.widget.winfo_containing(self.x, self.y) == self.widget:
            self.showtip(text)
        self.delay_id = None

    def schedule_delayed_showtip(self, text):
        if self.delay_id:
            self.widget.after_cancel(self.delay_id)
        self.delay_id = self.widget.after(int(self.duration * 1000), self.delayed_showtip, text)


def Hover(widget, text, duration=1.0, font=("tahoma", "12", "normal"),
          bg="#2B2B2B", fg="#ffffff", borderwidth=1):
    toolTip = ToolTip(widget, duration, font, bg, fg, borderwidth)

    def enter(event):
        toolTip.x = event.x_root
        toolTip.y = event.y_root
        toolTip.schedule_delayed_showtip(text)

    def leave(event):
        toolTip.hidetip()
        if toolTip.delay_id:
            widget.after_cancel(toolTip.delay_id)
            toolTip.delay_id = None

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
    widget.bind('<Motion>', toolTip.on_tooltip_motion)