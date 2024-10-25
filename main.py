from regression_and_classification.LinearRegression import UnivariateLinearRegression

if __name__ == '__main__':
    LinReg = UnivariateLinearRegression([
        (0,0), (1,1), (2, 4), (3,9), (4,16), (5,25)
    ]);
    
    LinReg();