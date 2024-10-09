""" Regression and Classification with Linear Models
"""

import numpy as np;

class UnivariateLinearRegression:
    """A univariate linear regression is a technique that aims to discover the best straight line that fits the data points.
    Given an array of values, the univariate linear function we aim to find is a function of the form
    
        h_w(x) = w_1*x + w_0
    
    where w_0, w_1 are the weights (coefficients of the polynomial). To find the weights, it is necessary to minimize a loss function
    Since Gauss, the square loss function (L_2) is used as the loss function.
    """
    
    def __init__(self, points:list[tuple[float, float]]):
        self.data:list[float]               = points;
        self.weights:tuple[float, float]    = (0, 0);
        self.loss:float;
    
    def evaluateWeights(self) -> tuple[float, float]:
        num_points:int = len(self.data);
        x_values = [x[0] for x in self.data];
        y_values = [y[1] for y in self.data];
        xy_prod = [];
        
        for i in range(len(self.data)):
            xy_prod.append(x_values[i]*y_values[i]);
        
        xy_sum      = sum(xy_prod);
        x_square_sum = sum([x**2 for x in x_values]);
        x_sum       = sum(x_values);
        y_sum       = sum(y_values);
        
        w_1 = (num_points*xy_sum - x_sum*y_sum) / (num_points*x_square_sum - x_sum**2);
        
        w_0 = (y_sum - w_1*x_sum) / num_points;
        
        return (w_0, w_1);
        
        
if __name__ == '__main__':
    LinReg = UnivariateLinearRegression([(0,0), (1,1), (2,4), (3,9), (4, 16)]);
    
    print(LinReg.data);
    print(len(LinReg.data));
    print(LinReg.evaluateWeights());