import glob
import skimage.io
import skimage.color
import cv2 as cv
import numpy as np
import tensorflow as tf


class MRIdataGenerator(tf.keras.utils.Sequence):
    def __init__(self, file_path, batch_size, mask_type="radial", shuffle=True):
        self.file_path = file_path
        self.batch_size = batch_size
        self.mask_type = mask_type
        self.shuffle = shuffle

        self.files = glob.glob(file_path + "*.png")[:4500]
        self.len = len(self.files)

        self.on_epoch_end()
    def on_epoch_end(self):
        np.random.shuffle(self.files)
    
    def __getitem__(self, index):
        images_indexes = self.files[index*self.batch_size:(index+1)*self.batch_size]

        fully_sampled = []
        under_sampled = []
        for i in images_indexes:
            fully_sampled_img = skimage.io.imread(i)
            fully_sampled_img = skimage.color.rgb2gray(skimage.color.rgba2rgb(fully_sampled_img))

            under_sampled_img = self.undersample_image(fully_sampled_img, sample_type=self.mask_type)
            fully_sampled_img = fully_sampled_img * 2.0 - 1.0 
            under_sampled_img = under_sampled_img * 2.0 - 1.0

            fully_sampled_img = np.expand_dims(fully_sampled_img, -1)
            under_sampled_img = np.expand_dims(under_sampled_img, -1)

            fully_sampled.append(fully_sampled_img)
            under_sampled.append(under_sampled_img)

        fully_sampled = np.array(fully_sampled)
        under_sampled = np.array(under_sampled)

        return under_sampled, fully_sampled
    def __len__(self):
        return self.len // self.batch_size
    
    def undersample_image(self, image, sample_type = "radial"):
        img_dom = image.copy()
        under_kspace = np.fft.fft2(img_dom)
        under_kspace = np.fft.fftshift(under_kspace)
        if sample_type == "radial":
            mask = cv.imread("./dataset/radial_masks/radial_20.tif")
            mask = mask / 255
            under_kspace = under_kspace * mask[:,:,0]
        elif sample_type == "cartesian_col":
            # mask = uniform_pattern((256, 256),0.20,center=True,dim="1D",radius_nlines=12,direction="row")
            mask = np.load("./dataset/cartesain_mask.npy")
            under_kspace[mask] = 0
        elif sample_type == "cartesian_row":
            # mask = uniform_pattern((256, 256),0.20,center=True,dim="1D",radius_nlines=12,direction="column")
            mask = np.load("./dataset/cartesain_mask.npy")
            mask = np.array(mask, dtype="int")
#             under_kspace[mask] = 0
            under_kspace = under_kspace * mask
        elif sample_type == "gaussian":
            mask = np.load("./dataset/gaussian2d_mask.npy")
            mask = np.array(mask, dtype="int")
#             under_kspace[mask] = 0
            under_kspace = under_kspace * mask
        
        img_und = np.fft.ifftshift(under_kspace.real + 1j*under_kspace.imag)
        img_und = np.fft.ifft2(img_und.real + 1j*img_und.imag)
        img_und = np.abs(img_und.real + 1j*img_und.imag)

        return img_und