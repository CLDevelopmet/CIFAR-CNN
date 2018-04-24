import pickle
import pandas

class Data:
    def __init__(self, working_dir):
        print("Data have been imported")
        print(working_dir)

    def extract_cifar10(self):
        # Extracting images and labels of CIFAR-10 dataset from given directory
        print('Extrating CIFAR-10 dataset')

    def extract_cifar100(self):
        # Extracting images and labels of CIFAR-100 dataset
        print('Extraction CIFAR-100 dataset')

    def train_batch(self, size):
        # Output of a training data batch
        print('Returning trainig batch of size %i')

    def test_data(self):
        # Outputs testing data
        print('Testing data')

    def draw_image(self):
        # Draws an image
        print('Drawing an image')