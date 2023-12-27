
### Supporting code for Computer Vision Assignment 1
### See "Assignment 1.ipynb" for instructions

import math
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

def load(img_path):
    """Loads an image from a file path.

    HINT: Look up `skimage.io.imread()` function.
    HINT: Converting all pixel values to a range between 0.0 and 1.0
    (i.e. divide by 255) will make your life easier later on!

    Inputs:
        image_path: file path to the image.

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    
    # plt.imread('images/whipbird.jpg')
    image = io.imread(img_path)
    return image

def print_stats(image):
    """ Prints the height, width and number of channels in an image.
        
    Inputs:
        image: numpy array of shape(image_height, image_width, n_channels).
        
    Returns: none
                
    """
    print(f'image height: {image.shape[0]}')
    print(f'image width: {image.shape[1]}')
    if len(image.shape) > 2:
        print(f'number of image channels: {image.shape[2]}')
    
    return None

def crop(image, start_row, start_col, num_rows, num_cols):
    """Crop an image based on the specified bounds. Use array slicing.
    Inputs:
        image: numpy array of shape(image_height, image_width, 3).
        start_row (int): The starting row index 
        start_col (int): The starting column index 
        num_rows (int): Number of rows in our cropped image.
        num_cols (int): Number of columns in our cropped image.

    Returns:
        out: numpy array of shape(num_rows, num_cols, 3).
    """
    print('shape of image1', image.shape)
    r, c, _ = image.shape
    if start_row + num_rows > r or start_col + num_cols > c: 
        print('crop dimensions invalid')
        return image
    ### YOUR CODE HERE
    out = image[start_row : start_row + num_rows, start_col:start_col + num_cols,:]
    return out

def binary(image, threshold):
    outputImage = np.zeros(image.shape)
    thresholdVal = 255 * threshold 
    outputImage[image >= thresholdVal] = 255
    return outputImage

def change_contrast(image, factor):
    """Change the value of every pixel by following

                        x_n = factor * (x_p - 0.5) + 0.5

    where x_n is the new value and x_p is the original value.
    Assumes pixel values between 0.0 and 1.0 
    If you are using values 0-255, change 0.5 to 128.

    Inputs:
        image: numpy array of shape(image_height, image_width, 3).
        factor (float): contrast adjustment

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    # as we are using jpgs which have 256 values we use 0.5
    max=np.max(image)
    # otherwise known as the midpoint
    midpoint = 128 if max != 1 else 0.5
    # using array broadcasting 
    # return  np.clip(factor * (image - midpoint) + midpoint, 0, 255)
    new_image = np.zeros(image.shape, image.dtype)
    # looping through all iamge channels
    r,c,d = image.shape
    for i in range(r):
        for j in range(c):
            for k in range(d):
                new_image[i,j,k] = np.clip(factor*(image[i,j,k]-midpoint) + midpoint, 0, 255)

    return new_image


def resize(input_image, output_rows, output_cols):
    """Resize an image using the nearest neighbor method.
    i.e. for each output pixel, use the value of the nearest input pixel after scaling

    Inputs:
        input_image: RGB image stored as an array, with shape
            `(input_rows, input_cols, 3)`.
        output_rows (int): proportion of desired rows to maintain
        output_cols (int): proportion of desired columns maintain

    Returns:
        np.ndarray: Resized image, with shape `(output_rows, output_cols, 3)`.
    """
    # check if invalid range
    if output_rows <= 0 or output_cols <= 0: return input_image
    r, c, d = input_image.shape
    # output rows is as a scaled factor so the number of pixels int the output array dimension is the original dimension * scaling factor
    output_rows = int(r * output_rows)
    output_cols = int(r * output_cols)
    rowScaleFactor = r / output_rows 
    colScaleFactor = c / output_cols 
    print(r, c, output_rows, output_cols)
    # scaledImage = np.zeros((output_rows, output_cols, d), dtype=np.uint8)
    scaledImage = np.zeros((output_rows, output_cols, 3), dtype=np.uint8)
    for i in range(output_rows):
        for j in range(output_cols):
            scaled_row = int(rowScaleFactor * i)
            scaled_col = int(colScaleFactor * j)
            scaledImage[i,j,:] = input_image[scaled_row, scaled_col,:]
    return scaledImage

def greyscale(input_image):
    """Convert a RGB image to greyscale. 
    A simple method is to take the average of R, G, B at each pixel.
    Or you can look up more sophisticated methods online.
    
    Inputs:
    input_image: RGB image stored as an array, with shape
            `(input_rows, input_cols, 3)`.

    Returns:
        np.ndarray: Greyscale image, with shape `(output_rows, output_cols)`.
    """
    # out = input_image[:,:,0]
    out = np.mean(input_image, axis=2)
    return out

def conv2D(image, kernel):
    """ Convolution of a 2D image with a 2D kernel. 
    Convolution is applied to each pixel in the image.
    Assume values outside image bounds are 0.
    
    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape    
    feature_map_height = Hi - Hk + 1
    feature_map_width = Wi - Wk + 1
    # check if dimension is invalid
    if feature_map_height <= 0 or feature_map_width <= 0:
        return image
    # add padding to image before convoluting so output array is of shape Hi, Wi as specified rather than feature map height, feature map width
    # padding = original image height - feature map height = Hi -(Hi - Hk + 1) = Hk - 1
    # padding_height = Hk - 1
    # padding_width = Wk - 1
    padding_height = Hk // 2
    padding_width = Wk // 2
    # modify image by padding
    # ((before_1, after_1), (before_2, after_2), constant adds zeros
    image = np.pad(image, ((padding_height, padding_height), (padding_width, padding_width)), mode='constant')
    output = np.zeros((Hi, Wi))
    for m in range(Hi):
        for n in range(Wi):
            output[m, n] = np.sum(image[m:m+Hk, n:n+Wk] * kernel)
    return output


def rotate_180_ccw(matrix):
    # reverse rows than cols
    res = np.flip(np.flip(matrix, axis=0), axis=1)
    return res

def test_conv2D():
    """ A simple test for your 2D convolution function.
        You can modify it as you like to debug your function.
    
    Returns:
        None
    """
    # Test code 
    # Simple convolution kernel.
    kernel = np.array(
    [
        [1,0,1],
        [0,0,0],
        [1,0,0]
    ])

    # Create a test image: a white square in the middle
    test_img = np.zeros((9, 9))
    test_img[3:6, 3:6] = 1

    # Run your conv_nested function on the test image
    test_output = conv2D(test_img, kernel)

    # Build the expected output
    expected_output = np.zeros((9, 9))
    expected_output[2:7, 2:7] = 1
    expected_output[5:, 5:] = 0
    expected_output[4, 2:5] = 2
    expected_output[2:5, 4] = 2
    expected_output[4, 4] = 3
    expected_output = rotate_180_ccw(expected_output)
    # rotate expected output counter clockwise 90 degrees as because orientation if fliped
    print(f'test_output \n {test_output}')
    print(f'expected_output \n {expected_output}')
    # Test if the output matches expected output, assert raises error if False
    assert np.max(test_output - expected_output) < 1e-10, "Your solution is not correct."   
    print('solution is correct')


def conv(image, kernel):
    """Convolution of a RGB or grayscale image with a 2D kernel
    
    Args:
        image: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
    """
    numChannels = image.shape[2]
    output = np.zeros_like(image) # np.zeros(image.shape)
    # apply convolution by applying filter to each channel independently
    for i in range(numChannels):
        output[:,:,i] = conv2D(image[:,:,i], kernel)
    return output
    
    
def gauss2D(size, sigma):

    """Function to mimic the 'fspecial' gaussian MATLAB function.
       You should not need to edit it.
       
    Args:
        size: filter height and width
        sigma: std deviation of Gaussian
        
    Returns:
        numpy array of shape (size, size) representing Gaussian filter
    """

    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()


def corr(image, kernel):
    """Cross correlation of a RGB image with a 2D kernel
    
    Args:
        image: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk). Dimensions will be odd.

    Returns:
        out: numpy array of shape (Hi, Wi, 3) or (Hi, Wi)
    """
    out = None
    ### YOUR CODE HERE

    return out

