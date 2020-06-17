# File Name - Neuron.py
# Created by Utkarsh Gupta
##########################


import numpy as np


class Neuron:
    def __init__(self, red_component=0.0, green_component=0.0, blue_component=0.0):
        self.synaptic_weight = np.array([[red_component,
                                         green_component,
                                         blue_component]])
        self.error = 0.0

    def activation_function(self, x):
        return 1 / (1 + np.exp(-x))

    def activation_function_derivative(self, x):
        return self.activation_function(x) * (1 - self.activation_function(x))

    def train(self, rgb_components, colour):
        output = self.activation_function(np.dot(np.array([[rgb_components[0], rgb_components[1], rgb_components[2]]]), self.synaptic_weight.T))
        self.error = colour - output
        adjustment = np.dot(np.array([[rgb_components[0], rgb_components[1], rgb_components[2]]]).T, (self.error.T * self.activation_function_derivative(output).T).T)
        self.synaptic_weight += adjustment.T

    def think(self, rgb_components):
        rgb_components = rgb_components.astype(float)
        output = self.activation_function(np.dot(rgb_components.T, self.synaptic_weight.T))
        return output

    def percent_error(self):
        return self.error[0][0] * 100

    def get_synaptic_weights(self):
        return self.synaptic_weight
