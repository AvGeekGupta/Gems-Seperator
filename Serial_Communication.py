# File Name - Serial_Communication.py
# Created by Vanshaj Goel
#####################################


import serial as serialcommunication


class SerialCommunication:
    def __init__(self):
        communication_port = "/dev/ttyACM0"
        baud_rate = 9600
        self.serial_communication = serialcommunication.Serial(communication_port, baud_rate)

    def print_colour(self, colour):
        self.serial_communication.write(str.encode(str(colour)))
