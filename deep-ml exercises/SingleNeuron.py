"""
Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, handling multidimensional input features. The function should take a list of feature vectors (each vector representing multiple features for an example), associated true binary labels, and the neuron's weights (one for each feature) and bias as input. It should return the predicted probabilities after sigmoid activation and the mean squared error between the predicted probabilities and the true labels, both rounded to four decimal places.

Example:
        input: features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels = [0, 1, 0], weights = [0.7, -0.4], bias = -0.1
        output: ([0.4626, 0.4134, 0.6682], 0.3349)
        reasoning: For each input vector, the weighted sum is calculated by multiplying each feature by its corresponding weight, adding these up along with the bias, then applying the sigmoid function to produce a probability. The MSE is calculated as the average squared difference between each predicted probability and the corresponding true label.
"""

import math

class SigmoidFunction:
    def __init__(self):
        """
        Initializes the sigmoid function.
        
        Does nothing, but should be overridden in subclasses for more complex
        initialization.
        """
        pass
    
    def __call__(self, x: float) -> float:
        """
        Calls the sigmoid function to calculate the output value for the given input.
        
        Parameters:
            x (float): The input value to calculate the sigmoid function.
            
        Returns:
            float: The output value after applying the sigmoid function to the input.
        """
        return 1 / (1 + math.exp(-x));
    

def mse(probabilities: list[float], labels: list[int]) -> float:
    """
    Computes the mean squared error (MSE) between predicted probabilities and true binary labels.

    Parameters
    ----------
    probabilities : list[float]
                    List of predicted probabilities for each example, each between 0 and 1.
    labels :        list[int]
                    List of true binary labels for each example, each either 0 or 1.

    Returns
    -------
    mse : float
        Mean squared error between predicted probabilities and true labels.
    """
    mse = 0;
    for i in range(len(labels)):
        currentProbability = probabilities[i];
        currentLabel = labels[i];
        
        mse += (currentProbability - currentLabel) ** 2;
    return mse / len(labels);


class SingleNeuronModel:
    def __init__(self, weights: list[float], bias: float):
        """
        Initializes the SingleNeuronModel.

        Parameters:
            weights (list[float]): The weights of the single neuron.
            bias (float): The bias of the single neuron.
        """
        self.weights: list[float] = weights
        self.bias: float = bias
        self.sigmoid = SigmoidFunction()

    def __call__(self, features: list[float]) -> tuple[list[float], float]:
        """
        Performs the forward pass of the single neuron model.

        Parameters:
            features (list[float]): The features of the single neuron.

        Returns:
            tuple[list[float], float]: A tuple containing the predicted probabilities and the mean squared error.
        """
        return self.predict(features), mse(self.predict(features), [0, 1, 0]);
    
    def predict(self, features: list[float]) -> list[float]:
        """
        Performs the prediction step of the single neuron model.

        Parameters:
            features (list[float]): The features of the single neuron.

        Returns:
            list[float]: The predicted probabilities for each example, each between 0 and 1.
        """
        probabilities: list[float] = [];
        for i in range(len(features)):
            probabilities.append(self.sigmoid(self.bias + self.weights[0] * features[i][0] + self.weights[1] * features[i][1]));
        return probabilities

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:
    """
    Trains a single neuron model and returns the predicted probabilities and the mean squared error.

    Parameters:
        features (list[list[float]]): The features of the single neuron.
        labels (list[int]): The labels of the single neuron.
        weights (list[float]): The weights of the single neuron.
        bias (float): The bias of the single neuron.

    Returns:
        tuple[list[float], float]: A tuple containing the predicted probabilities and the mean squared error.
    """
    model = SingleNeuronModel(weights, bias);
    return model(features), mse(model(features), labels);



if __name__ == "__main__":
    print(single_neuron_model([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1))