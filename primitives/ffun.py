from types import FunctionType;
import math
from typing import Any;

class PlotableFunction:
    def __init__(self, fun: FunctionType, config:dict={}):
        self.config = {};
        self.function = {};
        
        self.initialize(config);
        self.setFunction(fun);
    
    def initialize(self, config:dict={}) -> None:
        if(config == {}):
            self.config["xpos"] = 100;
            self.config["ypos"] = 100;
            self.config["step"] = 1;
            self.config["grid"] = True,
        else:
            raise NotImplemented;
        
    def setFunction(self, fun) -> None:
        self.function["x_values"] = [x for x in range(-self.config["xpos"], self.config["xpos"] + math.ceil(self.config["step"]))];
        self.function["y_values"] = [fun(x) for x in self.function["x_values"]];
        self.function["function"] = fun;
    
    def __plot(self) -> None:
        import matplotlib.pyplot as plt;
        fig, ax = plt.subplots();
        ax.plot(self.function["x_values"], self.function["y_values"]);
        ax.set(xlabel="x", ylabel="y=f(x)", title=f"{self.function["function"].__name__}");
        if(self.config["grid"] == True):
            ax.grid();
            
        fig.savefig("f_x__plot.png");
        plt.show();
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.__plot();

class Plotable:
    """Interface for plotable classes
    """
    def __init__(self, dataObject: Any, config:dict={}):
        self.configure(config);
        self.setDataObject(dataObject);
    
    def configure(self, config:dict={}) -> None:
        self.config = config;
    
    def setDataObject(self, dataObect:Any) -> None:
        self.data = dataObect;
        
    def plot(self) -> None:
        pass;
    
    def __call__(self):
        return self.plot();
    
class PlotableDataPoints(Plotable):
    """Plots a collection of points in 2-dimensional space.
    The points should be a list of 2-uples [(x_0, y_0), (x_1, y_1), ...]"""
    def __init__(self, dataPoints:list[tuple[float, float]], config:dict={}):
        super().__init__(dataPoints, config);
    
    def plot(self, saveFigure:bool=False) -> None:
        import matplotlib.pyplot as plt;
        fig, ax = plt.subplots();
        ax.scatter([coord[0] for coord in self.data], [coord[1] for coord in self.data], "o");
        ax.set(xlabel="x", ylabel="y", title="data points");
        ax.grid();
        
        if(saveFigure):    
            fig.savefig("data_points__plot.png");
        plt.show();

class PlotableFunction(Plotable):
    """Plots a collection of points in 2-dimension space as the inputs and outputs of a function.
    The class object should receive a function and a list of inputs for the function [x_0, x_1, ...]"""
    def __init__(self, fun: FunctionType, inputs:list[int | float], config:dict={}):
        super().__init__((fun, inputs), config);
    
    
    def setDataObject(self, dataObject: tuple):
        """Sets the function and its inputs"""
        self.function = dataObject[0];
        self.inputs   = dataObject[1];
        
    def plot(self) -> None:
        import matplotlib.pyplot as plt;
        fig, ax = plt.subplots();
        ax.plot([coord for coord in self.inputs], [self.function(x) for x in self.inputs], ".b-");
        ax.set(xlabel="x", ylabel="y", title="y = f(x)");
                
        try:
            if(self.config["saveFigure"]):    
                fig.savefig("function__plot.png");
            if(self.config["grid"]):
                ax.grid();
        except Exception as e:
            print(e);
        plt.show();  

class Solver:
    """Solves numeric functions through Newton's method for root-finding.
    """
    __slots__ = ['fun', 'roots', ];
    
    def __init__(self, fun: FunctionType):
        self.fun = fun;
        self.roots = self.solve();
        
    def solve(self) -> list[float]:
        """Uses a binary approach"""
        from scipy.misc import derivative;
        
        dx:float = 1e-4;
        x_value:float = 1;
        niter:int = 100;
        roots:list[float] = [];
        
        while(niter > 0):
            x_value = x_value - (self.fun(x_value) / derivative(self.fun, x_value, dx));
            print(x_value, niter)
            niter-=1;
            if(abs(self.fun(x_value)) < dx):
                roots.append(x_value);
        
        roots.append(x_value);
        
        return (roots);
    
    def __call__(self) -> str:
        return f"Solver[func={self.fun.__name__}, roots=({self.roots})]";
        
if __name__ == '__main__':
    