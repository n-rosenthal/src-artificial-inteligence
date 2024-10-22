"""Implementation of several activation functions for artificial neural networks"""

from abc import ABC, abstractmethod
from typing import Callable
import math


class ActivationFunction(ABC):
    @abstractmethod
    def __call__(self, x: float) -> float:
        pass
    
    def __str__(self) -> str:
        return self.__class__.__name__;
    

class SigmoidFunction(ActivationFunction):
    """Implementation of the logistic function as a sigmoid function.
    """
    
    def __call__(self, x: float) -> float:
        """
        Calls the sigmoid function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the sigmoid function.

        Returns:
            float: The output value after applying the sigmoid function to the input.
        """
        return 1 / (1 + math.exp(-x));
    

class HyperbolicTangent(ActivationFunction):
    """Implementation of the hyperbolic tangent function as a sigmoid, activation function."""
    
    def __call__(self, x: float) -> float:
        """
        Calls the hyperbolic tangent function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the hyperbolic tangent function.

        Returns:
            float: The output value after applying the hyperbolic tangent function to the input.
        """
        return math.tanh(x);
    

#   Rectifiers (rectified linear units) activation functions
class ParametricRectifier:
    """Implementation of the Parametric Rectifier function as an activation function. The unit is active when the input is greater than a threshold value."""
    def __init__(self, threshold: float):
        self.threshold = threshold;
    
    def __call__(self, x: float) -> float:
        """
        Calls the Parametric Rectifier function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the Parametric Rectifier function.

        Returns:
            float: The output value after applying the Parametric Rectifier function to the input.
        """
        if x > self.threshold:
            return x;
        else:
            return 0
        
class ReLU(ParametricRectifier):
    """Implementation of the Rectified Linear Unit function as an activation function. The unit is active when the input is greater than 0."""
    def __init__(self):
        super(ReLU, self).__init__(0);


if __name__ == '__main__':
    activation = ReLU();
    
    print(activation(0));
    print(activation(1));
    print(activation(-1));