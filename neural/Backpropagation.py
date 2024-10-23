from Neurons import SingleNeuron, neuron as make_neuron, neurons as make_neurons;
from ActivationFunctions import SigmoidFunction;
from NeuralNetworks import NeuralNetwork, layer as make_layer, layers as make_layers;
import numpy as np

def backpropagate(network: list[NeuralNetworkLayer], features: list[list[float]], labels: list[float], learning_rate: float) -> None: