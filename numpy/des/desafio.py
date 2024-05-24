import numpy as np
url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'

data = np.loadtxt(url,skiprows=1,delimiter=',',usecols=np.arange(1,6,1))
print(data)
print('-'*50)
print(data.shape)
print('-'*50)
print(data.ndim)
print('-'*50)
print(data.T)