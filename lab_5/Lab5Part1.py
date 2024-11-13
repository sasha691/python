from utils.LabLib import ModelLab5
from keras import models, layers
import cv2
import matplotlib.image as mpimg
from tensorflow.keras.datasets import mnist # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from keras.utils import to_categorical # type: ignore

class Model1(ModelLab5):
    def __init__(self, neuron_in: int = 32, neuron_out = 10, epochs = 5, data_augmentation = False, show_info = False):
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
        train_images.shape, test_images.shape, len(train_labels), len(test_labels)
        # print("Train images shape:", train_images.shape)
        # print("Test images shape:", test_images.shape)
        # print("Number of train labels:", len(train_labels))
        # print("Number of test labels:", len(test_labels))
        # digit = train_images[0]
        # plt.imshow(digit, cmap=plt.cm.binary)
        # plt.show()

        self.network = models.Sequential()
        self.network.add(layers.Flatten(input_shape=(28 * 28,))) 
        self.network.add(layers.Dense(neuron_in, activation='relu'))
        self.network.add(layers.Dense(neuron_out, activation='softmax'))

        self.network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

        self.train_images = train_images.reshape((60000, 28 * 28)).astype('float32') / 255
        self.test_images = test_images.reshape((10000, 28 * 28)).astype('float32') / 255

        self.train_labels = to_categorical(train_labels)
        self.test_labels = to_categorical(test_labels)
        
        self.history = self.network.fit(self.train_images, self.train_labels, epochs=epochs, batch_size=neuron_in,\
                                   validation_data=(self.test_images, self.test_labels))
        if show_info:
            self.show_info()

        self.network.summary()

class Model2(ModelLab5):
    def __init__(self, neuron_in: int = 32, neuron_out = 10, epochs = 5, validation_split = 0.1, data_augmentation = False, show_info = False):
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
        self.train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
        self.test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

        self.train_labels = to_categorical(train_labels)
        self.test_labels = to_categorical(test_labels)

        self.network = models.Sequential()

        self.network.add(layers.Conv2D(neuron_in, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(neuron_in * 2, (3, 3), activation='relu'))
        self.network.add(layers.MaxPooling2D((2, 2)))
        self.network.add(layers.Conv2D(neuron_in * 2, (3, 3), activation='relu'))
        self.network.add(layers.Flatten())
        self.network.add(layers.Dense(neuron_in * 2, activation='relu'))
        self.network.add(layers.Dense(neuron_out, activation='softmax'))

        self.network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        if data_augmentation:
            train_datagen = ImageDataGenerator(
                rotation_range=10,
                width_shift_range=0.1,
                height_shift_range=0.1,
                zoom_range=0.1,
                shear_range=0.1,
                brightness_range=[0.8, 1.2]
            )
            validation_datagen = ImageDataGenerator()

            # Використання генераторів для тренувального і валідаційного наборів
            train_generator = train_datagen.flow(self.train_images, self.train_labels, batch_size=neuron_in)
            validation_generator = validation_datagen.flow(self.test_images, self.test_labels, batch_size=neuron_in)

            # Тренування моделі з генераторами
            self.history = self.network.fit(
                train_generator,
                epochs=epochs,
                validation_data=validation_generator
            )
        else:
            self.history = self.network.fit(self.train_images, 
                                            self.train_labels, 
                                            epochs=epochs, 
                                            batch_size=neuron_in, 
                                            validation_split=validation_split
                                            )

        if show_info:
            self.show_info()

        self.network.summary()
       
    def user_image(self, path_to_image: str = None):
        if path_to_image is None:
            return self.train_images
        img = mpimg.imread(path_to_image)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_img = cv2.resize(gray_img, (28, 28))
        resized_img = resized_img.astype('uint8')
        black_white_img = cv2.adaptiveThreshold(resized_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 11, 2)
        processed_image = black_white_img.reshape((1, 28, 28, 1)).astype('float32') / 255
        return processed_image
                