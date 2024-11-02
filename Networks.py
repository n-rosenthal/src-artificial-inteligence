""" `Networks.py` module
The `Networks.py` module is an interface for the `Layers.py` and `Neuron.py` modules.
It is responsible for creating and manipulating neural networks and layers of neurons.

@author: nrosenthal
@version: 1.0
@since: 2024-11-01
"""

from abc import ABC, abstractmethod;
from Layers import *;
from Neuron import *;

class INetwork(ABC):
    @abstractmethod
    def __call__(self, features: list[list[float]] | np.ndarray) -> list[float] | np.ndarray:
        """
        Returns the output of the network for the given input features.

        Parameters:
            features (list[list[float]]): The input features for the network.

        Returns:
            list[float]: The output of the network for the given input features.
        """
        pass;

    @abstractmethod
    def get(self) -> list[INeuron]:
        """
        Returns the list of neurons in the network.

        Returns:
            list[INeuron]: The list of neurons in the network.
        """
        pass;
    
    @abstractmethod
    def get_layers(self) -> list[ILayer]:
        """
        Returns the list of layers in the network.

        Returns:
            list[INeuralNetworkLayer]: The list of layers in the network.
        """
        pass;
    
    @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the network.

        Returns:
            str: The string representation of the network.
        """
        pass;
    
    @abstractmethod
    def __repr__(self):
        """
        Returns a string representation of the network.

        Returns:
            str: The string representation of the network.
        """
        pass;
    
    @abstractmethod
    def __len__(self):
        """
        Returns the number of layers in the network.

        Returns:
            int: The number of layers in the network.
        """
        pass;
    

class NeuralNetwork:
    """
    The NeuralNetwork class is an abstract base class for creating and manipulating neural networks.
    It is responsible for creating and manipulating layers of neurons and activation functions.

    Attributes:
        layers (list[INeuralNetworkLayer]): The list of layers in the network.
        learning_rate (float): The learning rate of the network.
        epochs (int): The number of epochs to train the network.
        data (dict): data dictionary for the neural network, training process, accuracy etc.

    Args:
        layers (list[INeuralNetworkLayer]): The list of layers in the network.
        learning_rate (float): The learning rate of the network.
        epochs (int): The number of epochs to train the network.
    """
    def __init__(self, layers: list[NeuralNetworkLayer], learning_rate: float, epochs: int):
        """
        Initializes the NeuralNetwork.
        
        Parameters:
            layers (list[NeuralNetworkLayer]): The list of layers in the network.
            learning_rate (float): The learning rate of the network.
            epochs (int): The number of epochs to train the network.
        """
        self.layers = layers;
        self.learning_rate = learning_rate;
        self.epochs = epochs;
        self.data = {};
        
    
    def mse(self, probabilities: list[float] | np.ndarray, labels: list[int]) -> float:
        """
        Computes the mean squared error (MSE) between predicted probabilities and true binary labels.

        Parameters:
            probabilities (list[float]): The predicted probabilities.
            labels (list[int]): The true binary labels.
            
        Returns:
            float: The mean squared error.
        """
        mse = 0;
        for i in range(len(labels)):
            currentProbability = probabilities[i];
            currentLabel = labels[i];
            
            mse += (currentProbability - currentLabel) ** 2;
        return mse / len(labels);
    
    def step(self, features: list[list[float]] | np.ndarray) -> list[float] | np.ndarray:
        """
        Computes the output of the network for the given input features.

        Parameters:
            features (list[list[float]]): The input features for the network.

        Returns:
            list[float]: The output of the network for the given input features.
        """
        for layer in self.layers:
            features = layer(features);
        return features;
    
    def __call__(self, features: list[list[float]] | np.ndarray) -> list[float] | np.ndarray:
        """
        Returns the output of the network for the given input features.

        Parameters:
            features (list[list[float]]): The input features for the network.

        Returns:
            list[float]: The output of the network for the given input features.
        """
        return self.step(features);
    
    def get(self) -> list[INeuron]:
        """
        Returns the list of neurons in the network.

        Returns:
            list[INeuron]: The list of neurons in the network.
        """
        neurons = [];
        for layer in self.layers:
            neurons.extend(layer.get());
        return neurons;
            
        
def backpropagate(network: NeuralNetwork, features: list[list[float]] | np.ndarray, labels: list[int]) -> NeuralNetwork:
    """
    Trains a neural network using backpropagation.

    Parameters:
        network (NeuralNetwork): The neural network to train.
        features (list[list[float]]): The input features for the network.
        labels (list[int]): The true binary labels.

    Returns:
        NeuralNetwork: The trained neural network.
    """
    for epoch in range(network.epochs):
        for i in range(len(features)):
            probabilities = network.step(features[i]);
            error = network.mse(probabilities, labels[i]);
            network.data[epoch] = error;
    return network;



if __name__ == "__main__":
    network: NeuralNetwork = NeuralNetwork([
        NeuralNetworkLayer([0.1, 0.2, 0.3]),
        NeuralNetworkLayer([0.4, 0.5, 0.6]),
        NeuralNetworkLayer([0.8, 0.9, 1.0])
    ], 0.01, 1000);
    
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]];
    labels = [0, 1, 1, 0];
    
    network = backpropagate(network, inputs, labels);
    
    print(network([0, 0]), network([0, 1]), network([1, 0]), network([1, 1]));