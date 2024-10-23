"""Defines several types of neurons to be used in artificial neural networks
@author: nrosenthal
@version: 1.0
@since: 2024-10-23
"""

from abc import ABC, abstractmethod;
from ActivationFunctions import *;
import random;
import math;
import numpy as np;

class Neuron:
    """
    An (m+1)-input neuron. The first input is the bias, set to 1. Each input is a feature to which a weight is associated.
    """
    def __init__(self, weights: list[float], activation_function: ActivationFunction):
        self.weights = weights;
        self.activation_function = activation_function;
        
        #   Assume the bias is always 1
        self.weights.append(1);
        
    @abstractmethod
    def __call__(self, features: list[float]) -> float:
        return self.activation_function(sum([features[i] * self.weights[i] for i in range(len(features))]));
    
    @abstractmethod
    def __str__(self) -> str:
        return str(self.weights);
    
    @abstractmethod
    def __repr__(self) -> str:
        return str(self.weights);
    
    def set(self, weights: list[float]):
        self.weights = weights;
        

class SingleNeuron(Neuron):
    """
    A single neuron. The first input is the bias, set to 1. Each input is a feature to which a weight is associated.
    """
    def __init__(self, weights: list[float], bias: float):
        super().__init__(weights, SigmoidFunction());
        self.bias = bias;
        
    def __call__(self, features: list[float]) -> float:
        """
        Computes the output of the neuron given the list of features as input. The output is the value of the sigmoid function applied to the sum of the products of the feature values and their corresponding weights plus the bias.
        Args:
            features (list[float]): The list of feature values to compute the output of the neuron.
        Returns:
            float: The output of the neuron.
        """
        return self.activation_function(self.bias + sum([features[i] * self.weights[i] for i in range(len(features))]));
        
    def __str__(self) -> str:
        return str(self.weights);
    
    def __repr__(self) -> str:
        return str(self.weights);
    
    def set(self, weights: list[float]):
        super().set(weights);
        

def neuron(features: list[float]) -> float:
    """
    A function that is used to create a neuron with a 1-input and 1-output layer. The function takes a list of features as input and returns the output of the neuron.
    Args:
        features (list[float]): The list of feature values to compute the output of the neuron. 
    Returns:
        float: The output of the neuron.
    """
    return SingleNeuron([np.random.normal() for _ in range(len(features) + 1)], np.random.normal()).__call__(features);


def neurons(features: list[list[float]]) -> list[float]:
    """
    A function that is used to create a list of neurons with a 1-input and 1-output layer. The function takes a list of lists of features as input and returns a list of outputs of the neurons.
    Args:
        features (list[list[float]]): The list of lists of feature values to compute the outputs of the neurons. 
    Returns:
        list[float]: The list of outputs of the neurons.
    """
    return [neuron(feature) for feature in features];
    
def main():
    features = [[0, 0], [0, 1], [1, 0], [1, 1]];
    print(neuron(neurons(features)));
    
    
    
    
if __name__ == '__main__':
    main();