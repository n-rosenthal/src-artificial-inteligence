""" `Layers.py` module
The `Layers.py` module is an interface for the `Neuron.py` and `ActivationFunctions.py` modules.
It is responsible for creating and manipulating layers of neurons and activation functions.

@author: nrosenthal
@version: 1.0
@since: 2024-11-01
"""

from Neuron import *;
from ActivationFunctions import *;
import numpy as np;
from abc import ABC, abstractmethod;

class ILayer(ABC):
    """ILayer interface is an abstract base class for creating and manipulating layers of neurons and activation functions.
    """
    
    def __init__(self):
        """
        Initializes the layer with an empty list of neurons.
        """
        self.neurons: list[INeuron] = [];

    @abstractmethod
    def __call__(self, features: list[list[float]] | np.ndarray) -> list[float] | np.ndarray:
        """
        Returns the output of the layer for the given input features.

        Parameters:
            features (list[list[float]]): The input features for the layer.

        Returns:
            list[float]: The output of the layer for the given input features.
        """
        pass;
    
    @abstractmethod
    def __repr__(self):
        """
        Returns a string representation of the layer.

        Returns:
            str: The string representation of the layer.
        """
        pass;
    
    @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the layer.

        Returns:
            str: The string representation of the layer.
        """
        pass;
    
    @abstractmethod
    def set(self, neurons: list[INeuron]):
        """
        Sets the layer's neurons to the given list of neurons.

        Parameters:
            neurons (list[INeuron]): The list of neurons to set the layer to.
        """
        self.neurons = neurons;
        
    
    @abstractmethod
    def get(self) -> list[INeuron]:
        """
        Returns the list of neurons in the layer.

        Returns:
            list[INeuron]: The list of neurons in the layer.
        """
        return self.neurons;
    
    
class NeuralNetworkLayer(ILayer):
    """A layer of neurons in a neural network.
    """
    
    def __init__(self, neurons: list[INeuron]):
        self.neurons = neurons;
        
    def __call__(self, features: list[list[float]] | np.ndarray) -> list[float] | np.ndarray:
        return [neuron(features) for neuron in self.neurons];
    
    def __repr__(self):
        return str(self());
    
    def __str__(self):
        return str(self());
    
    def set(self, neurons: list[INeuron]):
        self.neurons = neurons;
    
    def get(self) -> list[INeuron]:
        return self.neurons;

class InputLayer:
    """The input layer of a neural network.
    """
    def __call__(self, features: list[list[float]] | np.ndarray) -> list[float] | np.ndarray:
        return features[0];
    
    def __repr__(self):
        return str(self);
    
    def __str__(self):
        return str(self);

def layer(neurons: list[INeuron]) -> NeuralNetworkLayer:
    """
    Returns a NeuralNetworkLayer from a list of neurons.

    Parameters:
        neurons (list[INeuron]): The list of neurons to create the layer from.

    Returns:
        NeuralNetworkLayer: The layer created from the list of neurons.
    """
    return NeuralNetworkLayer(neurons);



if __name__ == "__main__":
    import ActivationFunctions as af;
    
    def softmax(x: float) -> float:
        return np.exp(x) / np.sum(np.exp(x));
    
    
    network : NeuralNetworkLayer = layer([
        layer([IdentifiableNeuron([1, 2], 0.5, 0), IdentifiableNeuron([3, 4], 0.4, 1)]), # (2, 3),
        softmax
    ]);
    
    def train(network: NeuralNetworkLayer, features: list[list[float]] | np.ndarray, labels: list[float] | np.ndarray):
        predictions = network(features);
        loss = (predictions - labels).sum();
        print(loss);
        network.set([IdentifiableNeuron([1, 2], 0.5, 0), IdentifiableNeuron([3, 4], 0.4, 1)]);

    train(network, [[0, 0], [0, 1], [1, 0], [1, 1]], [0, 1, 1, 0]);
    
    