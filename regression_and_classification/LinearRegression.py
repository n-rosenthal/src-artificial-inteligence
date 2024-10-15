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
        
    def __len__(self) -> int:
        """Returns the length of the `self.data` list

        Returns:
            int: number of points in the data
        """
        return len(self.data);
    
    def _evaluate_w_1(self) -> tuple[float, float, float]:
        """Evaluates the value for the w_1 weight.

        Returns:
            tuple[float, float, float] = (coefficient w_1, sum of x values, sum of y values)
        """
        num_points:int              = len(self);
        x_values:list[float]        = [coord[0] for coord in self.data];
        y_values:list[float]        = [coord[1] for coord in self.data];
        xy_prod:list[float]         = [coord[0]*coord[1] for coord in self.data];
        x_sum:float                 = sum(x_values);
        y_sum:float                 = sum(y_values);
        x_sq_sum:float              = sum([x**2 for x in x_values]);
        
        return ((num_points*sum(xy_prod) - x_sum*y_sum) / (num_points*x_sq_sum - x_sum**2), x_sum, y_sum);        
    
    def _evaluate_w_0(self, w_1: float, x_sum: float, y_sum: float) -> float:
        return (y_sum - w_1*x_sum) / len(self);
        
    
    def evaluateWeights(self) -> tuple[float, float]:
        w_1, x_sum, y_sum = self._evaluate_w_1();
        return (self._evaluate_w_0(w_1, x_sum, y_sum), w_1);
    
    def __call__(self):
        self.weights = self.evaluateWeights();
        fun = lambda x : self.weights[1]*x + self.weights[0];
        
        from primitives.ffun import PlotableDataPoints, PlotableFunction
        x_values:list[float]        = [coord[0] for coord in self.data];
        y_values:list[float]        = [coord[1] for coord in self.data];
        points = [];
        fun_values = [];
        for i in range(len(x_values)):
            points.append((x_values[i], y_values[i]));
            fun_values.append((x_values[i], fun(x_values[i])));
            
        datapoints_plotable = PlotableDataPoints(points, {});
        datapoints_plotable();
        
        function_plotable = PlotableFunction(fun, x_values, {});
        function_plotable();
        
if __name__ == '__main__':
    LinReg = UnivariateLinearRegression([(0,0), (1,1), (2,4), (3,9), (4, 16)]);
    LinReg();