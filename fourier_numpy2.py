import cv2
import numpy as np
import pylab as plt


def test_fourier_numpy2(test_image):
    im1 = test_image[:,:,::-1].copy()
    im_RGB = cv2.split(im1)
    
    plt.subplot(1,4,1),plt.imshow(im1)
    
    j = 2
    title = ('Red','Green','Blue')
    for i in im_RGB:
        F= np.fft.fft2(i)
        F_= np.log(5 + np.fft.fftshift(np.abs(F)))
        plt.subplot(1,4,j),plt.imshow(F_)
        plt.title(title[j-2])
        j =j + 1
        
    plt.show()

#img = cv2.imread('Lenna.jpg')
#test_fourier_numpy2(img)