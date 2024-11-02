"""`ActivationFunctions.py` module

Implementation of several activation functions for artificial neural networks:
    -   Sigmoid function                ::  f(x) = 1 / (1 + exp(-x)), smooth function that maps any value to a value between 0 and 1
    -   Hyperbolic tangent function     ::  f(x) = tanh(x), smooth function that maps any value to a value between -1 and 1
    -   SoftPlus function               ::  f(x) = log(1 + exp(x)), smooth function that maps any value to a value between 0 and infinity
    -   ReLU function                   ::  f(x) = max(0, x), smooth function that maps any value to a value between 0 and infinity
    -   LeakyReLU function              ::  f(x) = max(0, x) + n * min(0, x), smooth function that maps any value to a value between 0 and infinity
    -   Parametric Rectifier function   ::  f(x) = max(0, x), smooth function that maps any value to a value between 0 and infinity
    
Each activation function is a subclass of the `ActivationFunction` abstract class. The `ActivationFunction` class is an interface that defines the `__call__` method. The `__call__` method takes an input value `x` and returns the output value after applying the activation function to the input.

@author:    nrosenthal
@version:   1.0
@since:     2024-11-01
"""

import math;
import numpy as np;
from abc import ABC, abstractmethod;

class ActivationFunction(ABC):
    """
    Abstract base class for activation functions.
    An `ActivationFunction` is an interface that defines the `__call__` method. The `__call__` method takes an input value `x` and returns the output value after applying the activation function to the input.
    
    An `ActivationFunction` is responsible for computing the output value for a given input value `x` for a specific activation function. This is useful in neural networks, where activation functions are used to compute the output values for each layer of the network.
    
    @author:    nrosenthal
    @version:   1.0
    @since:     2024-11-01
    """
    @abstractmethod
    def __call__(self, x: float) -> float:
        """
        Calls the activation function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the activation function.

        Returns:
            float: The output value after applying the activation function to the input.
        """
        pass;
    

#       Implementation of the activation functions

class SigmoidFunction(ActivationFunction):
    """
    Implementation of the logistic function as a sigmoid function. 
    """
    def __call__(self, x: float) -> float:
        """
        Calls the sigmoid function to calculate the output value for the given input.

        y = 1 / (1 + exp(-x))

        Parameters:
            x (float): The input value to calculate the sigmoid function.

        Returns:
            float: The output value after applying the sigmoid function to the input.
        """
        return 1 / (1 + math.exp(-x));
    

class HyperbolicTangent(ActivationFunction):
    """
    Implementation of the hyperbolic tangent function as a sigmoid, activation function.
    """
    def __call__(self, x: float) -> float:
        """
        Calls the hyperbolic tangent function to calculate the output value for the given input.
        
        y = tanh(x)

        Parameters:
            x (float): The input value to calculate the hyperbolic tangent function.

        Returns:    
            float: The output value after applying the hyperbolic tangent function to the input.
        """
        return math.tanh(x);
    

class SoftPlus(ActivationFunction):
    """
    Implementation of the SoftPlus function as an activation function.
    
    y = log(1 + exp(x))
    """
    def __call__(self, x: float) -> float:
        """
        Calls the SoftPlus function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the SoftPlus function.

        Returns:
            float: The output value after applying the SoftPlus function to the input.
        """
        return math.log(1 + math.exp(x));
    
    
class ReLU(ActivationFunction):
    """
    Implementation of the ReLU function as an activation function.
    
    y = max(0, x)
    """
    def __call__(self, x: float) -> float:
        """
        Calls the ReLU function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the ReLU function.

        Returns:
            float: The output value after applying the ReLU function to the input.
        """
        return max(0, x);
    
    
class LeakyReLU(ActivationFunction):
    """
    Implementation of the Leaky ReLU function as an activation function.
    
    y = max(0, x) + n * min(0, x)
    """
    def __call__(self, x: float, negative_slope: float = 0.01) -> float:
        """
        Calls the Leaky ReLU function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the Leaky ReLU function.

        Returns:
            float: The output value after applying the Leaky ReLU function to the input.
        """
        if x > 0:
            return x;
        else:
            return negative_slope * x;
        

class ParametricRectifier(ActivationFunction):  
    """
    Implementation of the Parametric Rectifier function as an activation function.
    
    y = max(0, x) + n * min(0, x)
    """
    def __call__(self, x: float, negative_slope: float = 0.01, threshold: float = 0) -> float:
        """
        Calls the Parametric Rectifier function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the Parametric Rectifier function.

        Returns:
            float: The output value after applying the Parametric Rectifier function to the input.
        """
        if x > threshold:
            return x;
        else:
            return negative_slope * x;
        

class Identity(ActivationFunction):
    """
    Implementation of the Identity function as an activation function.
    
    y = x
    """
    def __call__(self, x: float) -> float:
        """
        Calls the Identity function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the Identity function.

        Returns:
            float: The output value after applying the Identity function to the input.
        """
        return x;
        