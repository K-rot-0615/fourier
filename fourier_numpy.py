# -* - coding : utf -8 -* -
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def test_fourier_numpy(test_image):

    fimage = np.fft.fft2(test_image)
    fimage = np.log(np.abs(fimage) + 1)
    fimage = fimage / np.amax(fimage) * 255

    print(fimage)
    print(fimage.shape)

    ft = np.fft.fft2(test_image) #2次元FFT
    ft = np.fft.fftshift(ft) #DC成分が中央にくるようにデータを入れ替え

    #画像で保存    
    Pow = np.abs(ft)**2 #パワースペクトルを計算
    Pow = np.log10(Pow) #対数表示 
    Pmax = np.max(Pow)
    Pow = Pow / Pmax *255
    pow_img = Image.fromarray(np.uint8(Pow))

    #pow_img.save('line_fft.jpg')
    pow_img.show()

    '''
    img = np.array(test_image)

    ft = np.fft.fft2(img) #2次元FFT
    ft = np.fft.fftshift(ft) #DC成分が中央にくるようにデータを入れ替え

    #グラフ化
    magnitude_spectrum = 20*np.log(np.abs(ft))
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    '''

#img = Image.open("lenna.png")
#test_fourier_numpy(img)