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
        
if __name__ == '__main__':
    def f(x) -> float:
        return x**2;
    
    PlotableFunction(f, {})();