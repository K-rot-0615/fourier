import numpy as np
import cv2
from filter import lowpass
from matplotlib import pyplot as plt

def test_fourier_cv(test_image):
    dft = cv2.dft(np.float32(test_image),flags = cv2.DFT_COMPLEX_OUTPUT)
    print(dft)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    
    plt.subplot(121),plt.imshow(test_image, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

#img = cv2.imread('lenna.jpg',0)
#test_fourier_cv(img)