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

class LeakyReLU(ParametricRectifier):
    """Implmementation of the Rectified Linear Unit (ReLU) function in its `Leaky` variant. The unit is active when the input is greater than 0.
    If the input is equal to 0, the output is multiplied by a negative coefficient."""
    def __init__(self, negative_slope: float):
        super(LeakyReLU, self).__init__(0);
        self.negative_slope = negative_slope;
        
    def __call__(self, x: float) -> float:
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
            return x * self.negative_slope;


class SoftPlus(ActivationFunction):
    """Implementation of the SoftPlus function as an activation function. The unit is active when the input is greater than 0."""
    def __call__(self, x: float) -> float:
        """
        Calls the SoftPlus function to calculate the output value for the given input.

        Parameters:
            x (float): The input value to calculate the SoftPlus function.

        Returns:
            float: The output value after applying the SoftPlus function to the input.
        """
        return math.log(1 + math.exp(x));


if __name__ == '__main__':
    for i in range(-10, 10):
        print(f"{i} -> SigmoidFunction({i}) = {SigmoidFunction()(i)}");
        print(f"{i} -> HyperbolicTangent({i}) = {HyperbolicTangent()(i)}");
        print(f"{i} -> ReLU({i}) = {ReLU()(i)}");
        print(f"{i} -> LeakyReLU({i}) = {LeakyReLU(0.1)(i)}");
        print(f"{i} -> SoftPlus({i}) = {SoftPlus()(i)}");
        print()
        
    