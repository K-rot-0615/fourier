import cv2
import numpy as np
from matplotlib import pyplot as plt


def test_fourier_numpy3(test_image):
    f = np.fft.fft2(test_image)
    print(f)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    
    plt.subplot(121),plt.imshow(test_image, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

#img = cv2.imread('Lenna.jpg',0)
#test_fourier_numpy3(img)