"""Implements several datasets for use in regression and classification
"""
import numpy as np;
import datetime as dt;

class Dataset:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx, idy=None):
        if(idy == None):
            return self.data[idx]
        else:
            return self.data[idx][idy];
        

class GaussianDistribution(Dataset):
    """A Gaussian distribution is a probability distribution that is characterized by a mean and a variance."""
    def __init__(self, mean:tuple[list] = ([0.,0.], [1., 1.]), variance:float=1.):
        """Constructs a Gaussian distribution.

        Args:
            mean (tuple[list], optional): The mean of the distribution. Defaults to ([0.,0.], [1., 1.]).
            variance (float, optional): The variance of the distribution. Defaults to 1.

        Returns:
            None
        """
        self.mean = mean;
        self.variance = variance;
    
    def __call__(self, num_examples:int = 100):
        self.RANDOM_SEED = np.random.seed(np.random.SeedSequence(dt.datetime.now().microsecond));
        normal = np.random.multivariate_normal;
        
        #   Squared width of the distribution
        width = self.variance**2;
        
        #   Generate examples
        sgx_0 = normal(self.mean[0], [[width, 0.0], [0.0, width]], num_examples);
        sgx_1 = normal(self.mean[1], [[width, 0.0], [0.0, width]], num_examples);
    