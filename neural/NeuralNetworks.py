from Neurons import SingleNeuron, neuron as make_neuron, neurons as make_neurons;
import numpy as np
from deep-ml exercises.SingleNeuron import mse;

class NeuralNetworkLayer:
    """A layer of neurons in a neural network."""
    def __init__(self, neurons: list[SingleNeuron]):
        self.neurons = neurons;

    def __call__(self, features: list[list[float]]) -> list[float]:
        return [neuron(features) for neuron in self.neurons];

    def __repr__(self) -> str:
        return str(self.neurons);

    def __str__(self) -> str:
        return str(self.neurons);
    
    def set(self, neurons: list[SingleNeuron]):
        self.neurons = neurons;
        

def layer(neurons: list[SingleNeuron]) -> NeuralNetworkLayer:
    return NeuralNetworkLayer(neurons);


def layers(neurons: list[list[SingleNeuron]]) -> list[NeuralNetworkLayer]:
    return [layer(neuron) for neuron in neurons];

class NeuralNetwork:
    def __init__(self, layers: list[NeuralNetworkLayer], learning_rate: float, epochs: int):
        self.layers = layers;
        self.learning_rate = learning_rate;
        self.epochs = epochs;
        
        