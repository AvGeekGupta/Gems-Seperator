# File Name - Main.py
# Created by Tanya Malhotra
###########################


import time
import Login
import threading
import Graph_Plot
import numpy as np
from ColourInput import ColourInput as ColourInput
from File_Handling import FileHandling as FileHandling
from Image_Capture import ImageCapture as ImageCapture
from Neural_Network import NeuralNetwork as NeuralNetwork
from Serial_Communication import SerialCommunication as SerialCommunication
from tkinter import messagebox

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

import Main_support
from tkinter import *
from PIL import ImageTk, Image


ColourCount = [0, 0, 0, 0, 0, 0, 0]


def vp_start_gui():
    """6Starting point when module is the main routine."""
    global w, root
    root = tk.Tk()
    top = Main(Login.MySQL.get_name(), root)
    Main_support.init(root, top)
    root.mainloop()


w = None
total_gems = 0
ExcelSheet = FileHandling()
ClickPicture = ImageCapture()
ColourDetection = NeuralNetwork()
Arduino = SerialCommunication()

def create_Main(root):
    """Starting point when module is imported by another program."""
    global w, rt
    rt = root
    w = tk.Toplevel(root)
    top = Main(Login.MySQL.get_name(), w)
    Main_support.init(w, top)
    return w, top


def destroy_Main():
    global w
    w.destroy()
    w = None


class StartEngineProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.iteration = True

    def run(self):
        global total_gems
        while self.iteration:
            colour_code = ClickPicture.click_image()
            colour = ColourDetection.think(colour_code)
            Login.MySQL.writecolor(colour_code, colour)
            Arduino.print_colour(colour)
            ColourCount[colour] += 1
            ColourCount[6] += 1
            time.sleep(4)
            root.update()

    def stop(self):
        self.iteration = False


class Main:
    def __init__(self, name, top=None):
        global total_gems
        self.name = StringVar()
        self.name.set(name)
        self.blue = StringVar()
        self.blue.set(ColourCount[0])
        self.brown = StringVar()
        self.brown.set(ColourCount[1])
        self.green = StringVar()
        self.green.set(ColourCount[2])
        self.pink = StringVar()
        self.pink.set(ColourCount[3])
        self.red = StringVar()
        self.red.set(ColourCount[4])
        self.yellow = StringVar()
        self.yellow.set(ColourCount[5])
        self.total = StringVar()
        self.total.set(ColourCount[6])

        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font13 = "-family {Microsoft Tai Le} -size 20 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font14 = "-family {Microsoft New Tai Lue} -size 40 -weight "  \
            "bold -slant roman -underline 1 -overstrike 0"
        font16 = "-family {Microsoft Tai Le} -size 15 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font17 = "-family {Microsoft Tai Le} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"
        font18 = "-family {Microsoft Tai Le} -size 20 -weight normal "  \
            "-slant roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1920x1001+-9+-9")
        top.resizable(1, 1)
        top.title("Gems Seperator")
        top.configure(borderwidth="5")
        top.configure(relief="raised")
        top.configure(background="#bce8f5")

        self.Vertical_Seperator_1 = ttk.Separator(top)
        self.Vertical_Seperator_1.place(relx=0.151, rely=0.14, relheight=0.849)
        self.Vertical_Seperator_1.configure(orient="vertical")

        self.Horizontal_Seperator_1 = ttk.Separator(top)
        self.Horizontal_Seperator_1.place(relx=0.005, rely=0.13, relwidth=0.99)

        self.Horizontal_Seperator_2 = ttk.Separator(top)
        self.Horizontal_Seperator_2.place(relx=0.156, rely=0.759, relwidth=0.839)

        self.Heading_Label = ttk.Label(top)
        self.Heading_Label.place(relx=0.37, rely=0.02, height=92, width=505)
        self.Heading_Label.configure(background="#bce8f5")
        self.Heading_Label.configure(foreground="#000000")
        self.Heading_Label.configure(font=font14)
        self.Heading_Label.configure(relief="flat")
        self.Heading_Label.configure(text='''Gems Seperator''')

        self.Welcome_Label = ttk.Label(top)
        self.Welcome_Label.place(relx=0.005, rely=0.08, height=47, width=158)
        self.Welcome_Label.configure(background="#bce8f5")
        self.Welcome_Label.configure(foreground="#000000")
        self.Welcome_Label.configure(font=font13)
        self.Welcome_Label.configure(relief="flat")
        self.Welcome_Label.configure(text='''Welcome''')

        self.Name_Label = ttk.Label(top)
        self.Name_Label.place(relx=0.089, rely=0.08, height=47, width=456)
        self.Name_Label.configure(background="#bce8f5")
        self.Name_Label.configure(foreground="#000000")
        self.Name_Label.configure(font=font13)
        self.Name_Label.configure(relief="flat")
        self.Name_Label.configure(textvariable=self.name)

        self.General_Option_Label = ttk.Label(top)
        self.General_Option_Label.place(relx=0.016, rely=0.15, height=46, width=240)
        self.General_Option_Label.configure(background="#bce8f5")
        self.General_Option_Label.configure(foreground="#000000")
        self.General_Option_Label.configure(font=font18)
        self.General_Option_Label.configure(relief="flat")
        self.General_Option_Label.configure(text='''General Options''')

        self.Log_Out_Button = ttk.Button(top)
        self.Log_Out_Button.place(relx=0.016, rely=0.22, height=60, width=228)
        self.Log_Out_Button.configure(takefocus="")
        self.Log_Out_Button.configure(text='''Log Out''')
        self.Log_Out_Button.configure(command=self.log_out_button_click)

        self.Upload_Data_Button = ttk.Button(top)
        self.Upload_Data_Button.place(relx=0.016, rely=0.47, height=60, width=228)
        self.Upload_Data_Button.configure(takefocus="")
        self.Upload_Data_Button.configure(text='''Upload Data''')
        self.Upload_Data_Button.configure(command=self.upload_data_button_click)

        self.Control_Label = ttk.Label(top)
        self.Control_Label.place(relx=0.016, rely=0.4, height=46, width=233)
        self.Control_Label.configure(background="#bce8f5")
        self.Control_Label.configure(foreground="#000000")
        self.Control_Label.configure(font=font18)
        self.Control_Label.configure(relief="flat")
        self.Control_Label.configure(text='''Engine Controls''')

        self.Train_Button = ttk.Button(top)
        self.Train_Button.place(relx=0.016, rely=0.31, height=60, width=228)
        self.Train_Button.configure(takefocus="")
        self.Train_Button.configure(text='''Train System''')
        self.Train_Button.configure(command=self.train_system_button_click)

        self.Start_Button = ttk.Button(top)
        self.Start_Button.place(relx=0.016, rely=0.559, height=60, width=228)
        self.Start_Button.configure(takefocus="")
        self.Start_Button.configure(text='''Start Engine''')
        self.Start_Button.configure(command=self.start_engine_button_click)

        self.Stop_Button = ttk.Button(top)
        self.Stop_Button.place(relx=0.016, rely=0.649, height=60, width=228)
        self.Stop_Button.configure(takefocus="")
        self.Stop_Button.configure(text='''Stop Engine''')
        self.Stop_Button.configure(command=self.stop_engine_button_click)

        self.Write_Label = ttk.Label(top)
        self.Write_Label.place(relx=0.01, rely=0.759, height=46, width=258)
        self.Write_Label.configure(background="#bce8f5")
        self.Write_Label.configure(foreground="#000000")
        self.Write_Label.configure(font=font18)
        self.Write_Label.configure(relief="flat")
        self.Write_Label.configure(text='''Write Data on file''')

        self.Training_Data_Button = ttk.Button(top)
        self.Training_Data_Button.place(relx=0.016, rely=0.829, height=60, width=228)
        self.Training_Data_Button.configure(takefocus="")
        self.Training_Data_Button.configure(text='''Training Graph''')
        self.Training_Data_Button.configure(command=self.training_data_button_click)

        self.Running_Data_Button = ttk.Button(top)
        self.Running_Data_Button.place(relx=0.016, rely=0.919, height=60, width=228)
        self.Running_Data_Button.configure(takefocus="")
        self.Running_Data_Button.configure(text='''Run Results''')
        self.Running_Data_Button.configure(command=self.run_results_button_click)

        self.Picture_Frame = ttk.Label(top)
        self.Picture_Frame.place(relx=0.281, rely=0.14, relheight=0.614, relwidth=0.586)
        self.Picture_Frame.configure(relief='raised')
        self.Picture_Frame.configure(borderwidth="5")
        self.Picture_Frame.configure(cursor="circle")
        self.photo = ImageTk.PhotoImage(Image.open("./Images/default.jpg"))
        self.Picture_Frame.configure(image=self.photo)
        self.Picture_Frame.configure(anchor=CENTER)

        self.Run_Label = ttk.Label(top)
        self.Run_Label.place(relx=0.5, rely=0.769, height=64, width=294)
        self.Run_Label.configure(background="#bce8f5")
        self.Run_Label.configure(foreground="#000000")
        self.Run_Label.configure(font=font17)
        self.Run_Label.configure(relief="flat")
        self.Run_Label.configure(text='''Current Gems data''')

        self.Blue_Label = ttk.Label(top)
        self.Blue_Label.place(relx=0.161, rely=0.849, height=35, width=133)
        self.Blue_Label.configure(background="#bce8f5")
        self.Blue_Label.configure(foreground="#000000")
        self.Blue_Label.configure(font=font16)
        self.Blue_Label.configure(relief="flat")
        self.Blue_Label.configure(text='''Blue Gems :''')

        self.Brown_Label = ttk.Label(top)
        self.Brown_Label.place(relx=0.161, rely=0.889, height=35, width=156)
        self.Brown_Label.configure(background="#bce8f5")
        self.Brown_Label.configure(foreground="#000000")
        self.Brown_Label.configure(font=font16)
        self.Brown_Label.configure(relief="flat")
        self.Brown_Label.configure(text='''Brown Gems :''')

        self.Green_Label = ttk.Label(top)
        self.Green_Label.place(relx=0.438, rely=0.849, height=35, width=152)
        self.Green_Label.configure(background="#bce8f5")
        self.Green_Label.configure(foreground="#000000")
        self.Green_Label.configure(font=font16)
        self.Green_Label.configure(relief="flat")
        self.Green_Label.configure(text='''Green Gems :''')

        self.Pink_Label = ttk.Label(top)
        self.Pink_Label.place(relx=0.438, rely=0.889, height=35, width=132)
        self.Pink_Label.configure(background="#bce8f5")
        self.Pink_Label.configure(foreground="#000000")
        self.Pink_Label.configure(font=font16)
        self.Pink_Label.configure(relief="flat")
        self.Pink_Label.configure(text='''Pink Gems :''')

        self.Red_Label = ttk.Label(top)
        self.Red_Label.place(relx=0.734, rely=0.849, height=35, width=129)
        self.Red_Label.configure(background="#bce8f5")
        self.Red_Label.configure(foreground="#000000")
        self.Red_Label.configure(font=font16)
        self.Red_Label.configure(relief="flat")
        self.Red_Label.configure(text='''Red Gems :''')

        self.Yellow_Label = ttk.Label(top)
        self.Yellow_Label.place(relx=0.734, rely=0.889, height=35, width=158)
        self.Yellow_Label.configure(background="#bce8f5")
        self.Yellow_Label.configure(foreground="#000000")
        self.Yellow_Label.configure(font=font16)
        self.Yellow_Label.configure(relief="flat")
        self.Yellow_Label.configure(text='''Yellow Gems :''')

        self.Total_Label = ttk.Label(top)
        self.Total_Label.place(relx=0.438, rely=0.949, height=35, width=141)
        self.Total_Label.configure(background="#bce8f5")
        self.Total_Label.configure(foreground="#000000")
        self.Total_Label.configure(font=font16)
        self.Total_Label.configure(relief="flat")
        self.Total_Label.configure(text='''Total Gems :''')

        self.Blue_Count_Label = ttk.Label(top)
        self.Blue_Count_Label.place(relx=0.365, rely=0.849, height=35, width=97)
        self.Blue_Count_Label.configure(background="#ffffff")
        self.Blue_Count_Label.configure(foreground="#000000")
        self.Blue_Count_Label.configure(font=font16)
        self.Blue_Count_Label.configure(relief="sunken")
        self.Blue_Count_Label.configure(textvariable=self.blue)

        self.Brown_Count_Label = ttk.Label(top)
        self.Brown_Count_Label.place(relx=0.365, rely=0.889, height=35, width=97)

        self.Brown_Count_Label.configure(background="#ffffff")
        self.Brown_Count_Label.configure(foreground="#000000")
        self.Brown_Count_Label.configure(font=font16)
        self.Brown_Count_Label.configure(relief="sunken")
        self.Brown_Count_Label.configure(textvariable=self.brown)

        self.Green_Count_Label = ttk.Label(top)
        self.Green_Count_Label.place(relx=0.667, rely=0.849, height=35, width=97)

        self.Green_Count_Label.configure(background="#ffffff")
        self.Green_Count_Label.configure(foreground="#000000")
        self.Green_Count_Label.configure(font=font16)
        self.Green_Count_Label.configure(relief="sunken")
        self.Green_Count_Label.configure(textvariable=self.green)

        self.Pink_Count_Label = ttk.Label(top)
        self.Pink_Count_Label.place(relx=0.667, rely=0.889, height=35, width=97)
        self.Pink_Count_Label.configure(background="#ffffff")
        self.Pink_Count_Label.configure(foreground="#000000")
        self.Pink_Count_Label.configure(font=font16)
        self.Pink_Count_Label.configure(relief="sunken")
        self.Pink_Count_Label.configure(textvariable=self.pink)

        self.Red_Count_Label = ttk.Label(top)
        self.Red_Count_Label.place(relx=0.938, rely=0.849, height=35, width=97)
        self.Red_Count_Label.configure(background="#ffffff")
        self.Red_Count_Label.configure(foreground="#000000")
        self.Red_Count_Label.configure(font=font16)
        self.Red_Count_Label.configure(relief="sunken")
        self.Red_Count_Label.configure(textvariable=self.red)

        self.Yellow_Count_Label = ttk.Label(top)
        self.Yellow_Count_Label.place(relx=0.938, rely=0.889, height=35, width=97)
        self.Yellow_Count_Label.configure(background="#ffffff")
        self.Yellow_Count_Label.configure(foreground="#000000")
        self.Yellow_Count_Label.configure(font=font16)
        self.Yellow_Count_Label.configure(relief="sunken")
        self.Yellow_Count_Label.configure(textvariable=self.yellow)

        self.Total_Count_Label = ttk.Label(top)
        self.Total_Count_Label.place(relx=0.641, rely=0.949, height=35, width=97)

        self.Total_Count_Label.configure(background="#ffffff")
        self.Total_Count_Label.configure(foreground="#000000")
        self.Total_Count_Label.configure(font=font16)
        self.Total_Count_Label.configure(relief="sunken")
        self.Total_Count_Label.configure(textvariable=self.total)

        self.menubar = tk.Menu(top, font=font9, bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.724, rely=0.839, relheight=0.09)
        self.TSeparator1.configure(orient="vertical")
        self.TSeparator1.configure(cursor="fleur")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.422, rely=0.839, relheight=0.09)
        self.TSeparator2.configure(orient="vertical")

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.156, rely=0.939, relwidth=0.839)

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.156, rely=0.829, relwidth=0.839)

        self.start_engine_process = StartEngineProcess()


    def log_out_button_click(self):
        root.destroy()
        Login.vp_start_gui()

    def train_system_button_click(self):
        ColourDetection.get_synaptic_weights()
        blue = np.array(Login.MySQL.getcolor("blue"))
        brown = np.array(Login.MySQL.getcolor("brown"))
        green = np.array(Login.MySQL.getcolor("green"))
        pink = np.array(Login.MySQL.getcolor("pink"))
        red = np.array(Login.MySQL.getcolor("red"))
        yellow = np.array(Login.MySQL.getcolor("yellow"))
        for i in range(0, 10000):
            for j in range(0, blue.shape[0]):
                ColourDetection.train(blue[j], 1)
            for j in range(0, brown.shape[0]):
                ColourDetection.train(brown[j], 2)
            for j in range(0, green.shape[0]):
                ColourDetection.train(green[j], 3)
            for j in range(0, pink.shape[0]):
                ColourDetection.train(pink[j], 4)
            for j in range(0, red.shape[0]):
                ColourDetection.train(red[j], 5)
            for j in range(0, yellow.shape[0]):
                ColourDetection.train(yellow[j], 6)
            Login.MySQL.writeerror(ColourDetection.percenterror())
        ColourDetection.write_synaptic_weights()
        ColourDetection.get_synaptic_weights()
        messagebox.showinfo("Trained", "Neural Network model trained successfully.")

    def upload_data_button_click(self):
        ColourInput()

    def start_engine_button_click(self):
        colour_code = ClickPicture.click_image()
        colour = ColourDetection.think(colour_code)
        Login.MySQL.writecolor(colour_code, colour)
        Arduino.print_colour(colour)
        ColourCount[colour] += 1
        ColourCount[6] += 1

    def stop_engine_button_click(self):
        self.start_engine_process.stop()
        root.destroy()
        vp_start_gui()

    def training_data_button_click(self):
        Graph_Plot.Plot(Login.MySQL.get_error())

    def run_results_button_click(self):
        Login.MySQL.write_run_result(ColourCount)
        messagebox.showinfo("Done", "Details Successfully written in Database.")
