from PIL import Image, ImageOps

from fourier_cv import test_fourier_cv
from fourier_numpy import test_fourier_numpy
from fourier_numpy2 import test_fourier_numpy2
from fourier_numpy3 import test_fourier_numpy3

test_image = Image.open('Lenna.jpg')
gray_image = ImageOps.grayscale(test_image)

test_fourier_cv(gray_image)
#test_fourier_numpy(gray_image)
#test_fourier_numpy2(test_image)
test_fourier_numpy3(gray_image)