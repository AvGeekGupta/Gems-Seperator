# File Name - Neural_Network.py
# Created by Utkarsh Gupta
###############################


from Neuron import Neuron as Neuron
from Database import Database as Database


MySQL = Database()


class NeuralNetwork:
    def __init__(self):
        self.mysql = Database()
        self.blue_neuron = Neuron()
        self.brown_neuron = Neuron()
        self.green_neuron = Neuron()
        self.pink_neuron = Neuron()
        self.red_neuron = Neuron()
        self.yellow_neuron = Neuron()

    def get_synaptic_weights(self):
        synaptic_weights = self.mysql.get_synaptic_weights("blue")
        self.blue_neuron = Neuron(synaptic_weights[0], synaptic_weights[1], synaptic_weights[2])
        synaptic_weights = self.mysql.get_synaptic_weights("brown")
        self.brown_neuron = Neuron(synaptic_weights[0], synaptic_weights[1], synaptic_weights[2])
        synaptic_weights = self.mysql.get_synaptic_weights("green")
        self.green_neuron = Neuron(synaptic_weights[0], synaptic_weights[1], synaptic_weights[2])
        synaptic_weights = self.mysql.get_synaptic_weights("pink")
        self.pink_neuron = Neuron(synaptic_weights[0], synaptic_weights[1], synaptic_weights[2])
        synaptic_weights = self.mysql.get_synaptic_weights("red")
        self.red_neuron = Neuron(synaptic_weights[0], synaptic_weights[1], synaptic_weights[2])
        synaptic_weights = self.mysql.get_synaptic_weights("yellow")
        self.yellow_neuron = Neuron(synaptic_weights[0], synaptic_weights[1], synaptic_weights[2])

    def train(self, rgb_components, colour):
        blue = 0
        brown = 0
        green = 0
        pink = 0
        red = 0
        yellow = 0
        if colour == 1:
            blue = 1
        elif colour == 2:
            brown = 1
        elif colour == 3:
            green = 1
        elif colour == 4:
            pink = 1
        elif colour == 5:
            red = 1
        else:
            yellow = 1
        self.blue_neuron.train(rgb_components, blue)
        self.brown_neuron.train(rgb_components, brown)
        self.green_neuron.train(rgb_components, green)
        self.pink_neuron.train(rgb_components, pink)
        self.red_neuron.train(rgb_components, red)
        self.yellow_neuron.train(rgb_components, yellow)

    def think(self, rgb_components):
        blue = self.blue_neuron.think(rgb_components)
        brown = self.brown_neuron.think(rgb_components)
        green = self.green_neuron.think(rgb_components)
        pink = self.pink_neuron.think(rgb_components)
        red = self.red_neuron.think(rgb_components)
        yellow = self.yellow_neuron.think(rgb_components)
        colour = max(blue, brown, green, pink, red, yellow)
        if colour == blue:
            color = 1
        elif colour == brown:
            color = 2
        elif colour == green:
            color = 3
        elif colour == pink:
            color = 4
        elif colour == red:
            color = 5
        else:
            color = 6
        return color

    def percenterror(self):
        return ((self.blue_neuron.percent_error() + self.brown_neuron.percent_error() +
                 self.green_neuron.percent_error() + self.pink_neuron.percent_error() + self.red_neuron.percent_error()
                 + self.yellow_neuron.percent_error()) / 6)

    def write_synaptic_weights(self):
        MySQL.write_synaptic_weights(self.blue_neuron.get_synaptic_weights(), "blue")
        MySQL.write_synaptic_weights(self.brown_neuron.get_synaptic_weights(), "brown")
        MySQL.write_synaptic_weights(self.green_neuron.get_synaptic_weights(), "green")
        MySQL.write_synaptic_weights(self.pink_neuron.get_synaptic_weights(), "pink")
        MySQL.write_synaptic_weights(self.red_neuron.get_synaptic_weights(), "red")
        MySQL.write_synaptic_weights(self.yellow_neuron.get_synaptic_weights(), "yellow")
