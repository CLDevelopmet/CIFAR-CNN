class CNN:
    def __init__(self, data_source, checkpoint_file, parameters):
        print('Convolutional neural network have been imported')
        # Importing data source, that is a class with all images loaded
        self.data_source = data_source
        self.checkpoint_file = checkpoint_file

        # Checking the type of network to be build
        # 'from_meta' would load pre-build network
        if parameters['type'] == 'from_checkpoint':
            self.load_network()

        #
        if parameters['type'] == 'from_meta':
            self.build_network(parameters['meta'])

    def build_network(self, meta_parameters):
        # Builds the network based on given meta parameters
        print('Building the network')
        print(meta_parameters)
        #TODO build input layer
        #TODO build convolutional layer
        #TODO build pooling layer
        #TODO build output layer
        #TODO set up initializer
        #TODO set up optimizer
        #TODO add extra layers capability

    def save_network(self):
        # Saving the network to checkpoint file
        #TODO save the network state in file
        print("Saving the network")

    def load_network(self):
        # Loading the network state from the checkpoint file
        #TODO load the network state from file
        print("Loading the network")

    def train(self, batch_size, n_of_batches):
        # The training class, that takes
        print('training')
        print(batch_size)
        print(n_of_batches)
        #TODO initialize valiables
        #TODO run training set

    def test(self):
        # Test the network, that have been created
        print('testing')
