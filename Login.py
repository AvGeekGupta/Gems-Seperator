# File Name - Login.py
# Created by Tanya Malhotra
###########################


import sys
import Main

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Login_support

import tkinter.messagebox

from Database import Database as Database


w = None
MySQL = Database()


def vp_start_gui():
    """Starting point when module is the main routine."""
    global w, root
    root = tk.Tk()
    top = Login_Page(root)
    Login_support.init(root, top)
    root.mainloop()


def create_Login_Page(root):
    """Starting point when module is imported by another program."""
    global w, rt
    rt = root
    w = tk.Toplevel(root)
    top = Login_Page(w)
    Login_support.init(w, top)
    return w, top


class Login_Page:
    def __init__(self, top=None):
        """This class configures and populates the top level window.
           top is the top level containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1920x1001+-9+-9")
        top.resizable(1, 1)
        top.title("Gems Seperator - Login")
        top.configure(borderwidth="5")
        top.configure(relief="raised")
        top.configure(background="#bce8f5")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top, font=font9, bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Heading_Label = ttk.Label(top)
        self.Heading_Label.place(relx=0.365, rely=0.06, height=89, width=505)
        self.Heading_Label.configure(background="#bce8f5")
        self.Heading_Label.configure(foreground="#000000")
        self.Heading_Label.configure(font="-family {Microsoft Tai Le} -size 40 -weight bold -underline 1")
        self.Heading_Label.configure(relief="flat")
        self.Heading_Label.configure(text='''Gems Seperator''')

        self.User_Login_Label = ttk.Label(top)
        self.User_Login_Label.place(relx=0.432, rely=0.28, height=69, width=255)
        self.User_Login_Label.configure(background="#bce8f5")
        self.User_Login_Label.configure(foreground="#000000")
        self.User_Login_Label.configure(font="-family {Microsoft Tai Le} -size 30 -weight bold -underline 1")
        self.User_Login_Label.configure(relief="flat")
        self.User_Login_Label.configure(text='''User Login''')

        self.Username_Label = ttk.Label(top)
        self.Username_Label.place(relx=0.342, rely=0.519, height=46, width=166)
        self.Username_Label.configure(background="#bce8f5")
        self.Username_Label.configure(foreground="#000000")
        self.Username_Label.configure(font="-family {Microsoft Tai Le} -size 20")
        self.Username_Label.configure(relief="flat")
        self.Username_Label.configure(text='''Username :''')

        self.Password_Label = ttk.Label(top)
        self.Password_Label.place(relx=0.347, rely=0.619, height=46, width=156)
        self.Password_Label.configure(background="#bce8f5")
        self.Password_Label.configure(foreground="#000000")
        self.Password_Label.configure(font="-family {Microsoft Tai Le} -size 20")
        self.Password_Label.configure(relief="flat")
        self.Password_Label.configure(text='''Password :''')

        self.Login_Button = ttk.Button(top)
        self.Login_Button.place(relx=0.438, rely=0.759, height=50, width=238)
        self.Login_Button.configure(takefocus="")
        self.Login_Button.configure(text='''Login''')
        self.Login_Button.configure(command=self.login_button_click)

        self.Username_Textbox = tk.Entry(top)
        self.Username_Textbox.place(relx=0.49, rely=0.519, relheight=0.044, relwidth=0.21)
        self.Username_Textbox.configure(background="white")
        self.Username_Textbox.configure(font="-family {Microsoft Tai Le} -size 20")
        self.Username_Textbox.configure(foreground="black")
        self.Username_Textbox.configure(highlightbackground="#d9d9d9")
        self.Username_Textbox.configure(highlightcolor="black")
        self.Username_Textbox.configure(insertbackground="black")
        self.Username_Textbox.configure(selectbackground="#c4c4c4")
        self.Username_Textbox.configure(selectforeground="black")

        self.Password_Textbox = tk.Entry(top)
        self.Password_Textbox.place(relx=0.49, rely=0.619, relheight=0.044, relwidth=0.21)
        self.Password_Textbox.configure(background="white")
        self.Password_Textbox.configure(font="-family {Microsoft Tai Le} -size 20")
        self.Password_Textbox.configure(foreground="black")
        self.Password_Textbox.configure(highlightbackground="#d9d9d9")
        self.Password_Textbox.configure(highlightcolor="black")
        self.Password_Textbox.configure(insertbackground="black")
        self.Password_Textbox.configure(selectbackground="#c4c4c4")
        self.Password_Textbox.configure(selectforeground="black")
        self.Password_Textbox.configure(show="*")



    def login_button_click(self):
        login = MySQL.user_login_verification(str(self.Username_Textbox.get()), str(self.Password_Textbox.get()))
        if login == 1:
            root.destroy()
            Main.vp_start_gui()
        else:
            tkinter.messagebox.showerror(title="ERROR", message="Incorrect username and password. Please Retry.")
