from DataPreprocessing import Data as data
from CNN import CNN as CNN

# Instantiating data preprocessor class
data_preprocessor = data('CIFAR-100')

# Instantiating convolutional neural network
network = CNN(data_preprocessor)

# Training the network
network.train(10, 10)

# Test the network
network.test()



