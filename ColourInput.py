import tkinter as tk
import tkinter.ttk as ttk
from Image_Capture import ImageCapture as ImageCapture
from Database import Database as Database
from Serial_Communication import SerialCommunication as SerialCommunication


ClickPicture = ImageCapture()
Arduino = SerialCommunication()
MySQL = Database()


class ColourInput:
    def __init__(self):
        self.root = tk.Tk()
        """This class configures and populates the toplevel window.
                   top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font16 = "-family {Microsoft Tai Le} -size 15 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        self.root.geometry("590x160+805+450")
        self.root.resizable(0, 0)
        self.root.title("What Colour is this?")
        self.root.configure(borderwidth="5")
        self.root.configure(relief="raised")
        self.root.configure(background="#bce8f5")

        self.Question_Label = ttk.Label(self.root)
        self.Question_Label.configure(background="#bce8f5")
        self.Question_Label.configure(foreground="#000000")
        self.Question_Label.configure(font=font16)
        self.Question_Label.configure(relief="flat")
        self.Question_Label.configure(text='''What is the colour of the gem?''')
        self.Question_Label.grid(row=1)

        self.Info_Label1 = ttk.Label(self.root)
        self.Info_Label1.configure(background="#bce8f5")
        self.Info_Label1.configure(foreground="#000000")
        self.Info_Label1.configure(font=font16)
        self.Info_Label1.configure(relief="flat")
        self.Info_Label1.configure(text='''Blue: 1 | Brown: 2 | Green: 3 | Pink: 4 | Red: 5 | Yellow: 6''')
        self.Info_Label1.grid(row=2)

        self.blanklabel = ttk.Label(self.root)
        self.blanklabel.configure(background="#bce8f5")
        self.blanklabel.configure(foreground="#000000")
        self.blanklabel.configure(font=font16)
        self.blanklabel.configure(relief="flat")
        self.blanklabel.configure(text='''''')
        self.blanklabel.grid(row=3)

        self.Colourcode = tk.Entry(self.root)
        self.Colourcode.configure(background="white")
        self.Colourcode.configure(font="-family {Microsoft Tai Le} -size 20")
        self.Colourcode.configure(foreground="black")
        self.Colourcode.configure(highlightbackground="#d9d9d9")
        self.Colourcode.configure(highlightcolor="black")
        self.Colourcode.configure(insertbackground="black")
        self.Colourcode.configure(selectbackground="#c4c4c4")
        self.Colourcode.configure(selectforeground="black")
        self.Colourcode.configure(width=4)
        self.Colourcode.grid(row=4)

        self.Submit_Button = ttk.Button(self.root)
        self.Submit_Button.configure(text='''Submit''')
        self.Submit_Button.configure(command=self.submit_button_click)
        self.Submit_Button.grid(row=5)

    def submit_button_click(self):
        colourcode = ClickPicture.click_image()
        MySQL.writecolor(colourcode, int(self.Colourcode.get()))
        Arduino.print_colour(int(self.Colourcode.get()))
        self.root.destroy()
