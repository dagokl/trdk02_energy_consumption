from resources.utils import prepare_data, load_meters_data
import keras

class Autoencoder(keras.Model):
    """
    Creates a model that encodes and decodes the input data.
    A bottleneck is added to the encoder to reduce the dimensionality of the input.
    This creates a latent space that can be used as a feature space.
    The bottleneck should prioritize the most important features in the latent space.
    Thus creating large errors for outliers.
    """
    def __init__(self, latent_dim, time_steps, X_train, X_test):
        super(Autoencoder, self).__init__()
        self.latent_dim = latent_dim
        self.time_steps = time_steps
        self.X_train = X_train
        self.X_test = X_test

    def train(self, epochs=10):
        return self.fit(
            self.X_train,
            self.X_train,
            epochs=epochs,
            batch_size=128,
            validation_split=0.1,
            validation_data=(self.X_test, self.X_test),
            shuffle=True,
            verbose=1,
            callbacks=[
                keras.callbacks.EarlyStopping(monitor="val_loss", patience=3, mode="min")
            ],
        )

    def create_model(self):
        self.encoder = keras.Sequential([
            keras.layers.Input(shape=(self.X_train.shape[1], self.X_train.shape[2])),
            keras.layers.Conv1D(filters=64, kernel_size=5, padding="same", strides=2, activation="relu", kernel_regularizer=keras.regularizers.l2(0.0001)),
            keras.layers.Conv1D(filters=self.latent_dim, kernel_size=5, padding="same", strides=2, activation="relu", kernel_regularizer=keras.regularizers.l2(0.0001))
        ])
        self.decoder = keras.Sequential([
            keras.layers.Conv1DTranspose(filters=self.latent_dim, kernel_size=5, padding="same", strides=2, activation="relu", kernel_regularizer=keras.regularizers.l2(0.0001)),
            keras.layers.Conv1DTranspose(filters=64, kernel_size=5, padding="same", strides=2, activation="relu", kernel_regularizer=keras.regularizers.l2(0.0001)),
            keras.layers.Conv1DTranspose(filters=self.X_train.shape[2], kernel_size=5, padding="same", activation="relu")
        ])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

if __name__ == "__main__":
    time_steps = 24
    latent_dim = 8

    meters_data = load_meters_data()
    X_train, X_test = prepare_data(meters_data, time_steps=time_steps, split_ratio=0.2)
    
    model = Autoencoder(latent_dim=latent_dim, time_steps=time_steps, X_train=X_train, X_test=X_test)
    model.create_model()
    model.compile(optimizer='adam', loss=keras.losses.MeanSquaredError())
    
    model.train()
    model.save('models/autoencoder'+str(time_steps)+'_'+str(latent_dim))