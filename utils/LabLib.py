import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
import numpy as np

class Lab:
    def __init__(self):
        pass

    def __call__(self, **args):
        methods = [getattr(self, method) for method in dir(self) if
                   callable(getattr(self, method)) and not method.startswith('_')]
        for method in methods:
            print(method.__name__)
            method()


    @staticmethod
    def _isValidateNumber(value: str, length:int = None) -> bool:
        if length == None:
            return value.isdigit()
        else:
            return value.isdigit() and len(value) == length


    _units = {0: "", 1: "один", 2: "два", 3: "три", 4: "чотири", 
             5: "п'ять", 6: "шість", 7: "сім", 8: "вісім", 9: "дев'ять"}
    
    _teens = {0: "десять", 1: "одинадцять", 2: "дванадцять", 3: "тринадцять", 
             4: "чотирнадцять", 5: "п'ятнадцять", 6: "шістнадцять", 
             7: "сімнадцять", 8: "вісімнадцять", 9: "дев'ятнадцять"}
    
    _tens = {0: "", 1: "десять", 2: "двадцять", 3: "тридцять", 
            4: "сорок", 5: "п'ятдесят", 6: "шістдесят", 
            7: "сімдесят", 8: "вісімдесят", 9: "дев’яносто"}
    
    _hundreds = {0: "", 1: "сто", 2: "двісті", 3: "триста", 
                4: "чотириста", 5: "п'ятсот", 6: "шістсот", 
                7: "сімсот", 8: "вісімсот", 9: "дев'ятсот"}

class ModelLab5():
    def forecast(self, path_to_image = None):
        try:
            print(path_to_image)
            y_pred = self.network.predict(self.user_image(path_to_image=path_to_image))
        except FileNotFoundError:
            print('File not found, default is used')
            y_pred = self.network.predict(self.train_images)
        pred_result = np.argmax(y_pred[0], axis=0)
        print('result ', pred_result)


    def user_image(self, path_to_image: str):
        if path_to_image is None:
            return self.train_images
        img = mpimg.imread(path_to_image)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_img = cv2.resize(gray_img, (28, 28)).astype('uint8')
        _, binary_img = cv2.threshold(resized_img, 128, 255, cv2.THRESH_BINARY)
        # black_white_img = cv2.adaptiveThreshold(resized_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #                                         cv2.THRESH_BINARY, 11, 2)
        inverted_img = cv2.bitwise_not(binary_img)

        plt.imshow(inverted_img, cmap='gray')
        plt.show()
        
        images = inverted_img.reshape((1, 28 * 28)).astype('float64') / 255
        
        return images

    def show_info(self):
        plt.plot(self.history.history['accuracy'], label='accuracy')
        plt.plot(self.history.history['val_accuracy'], label='val_accuracy')
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(loc='upper left')
        plt.show()

        test_loss, test_acc = self.network.evaluate(self.test_images, self.test_labels)
        print('test_loss:', test_loss, 'test_acc:', test_acc)
    
