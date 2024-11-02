"""`Neuron.py` module
Implements several models for neurons appliable to artificial neural networks and convoluted neural networks

@author: nrosenthal
@version: 1.0
@since: 2024-11-01
"""

import numpy as np;

class INeuron:
    """`INeuron` interface
    Defines a common interface for all neurons
    
    
    @author: nrosenthal
    @version: 1.0
    @since: 2024-11-01
    """
    def __init__(self, weights: np.array, bias: float):
        """
        Initializes the neuron with the given weights and bias
        
        Parameters:
            weights (np.array): The weights of the neuron
            bias (float): The bias of the neuron
        """
        self.weights = weights;
        self.bias = bias;
    
    def __call__(self, features: np.array):
        """
        Computes the output of the neuron given the list of features as input
        
        Parameters:
            features (np.array): The list of feature values to compute the output of the neuron
        
        Returns:
            float: The output of the neuron
        """
        return np.dot(self.weights, features) + self.bias;
    

class IdentifiableNeuron(INeuron):
    """`IdentifiableNeuron` class
    Implements a neuron that can be identified by an unique index.
    
    @author: nrosenthal
    @version: 1.0
    @since: 2024-11-01
    """
    def __init__(self, weights: np.array, bias: float, identifier: int):
        """
        Initializes the neuron with the given weights and bias
        
        Parameters:
            weights (np.array): The weights of the neuron
            bias (float): The bias of the neuron
        """
        super().__init__(weights, bias);
        self.identifier = identifier; 