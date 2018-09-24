# OpenCV {#s-opencv}

---

**:mortar_board: Learning Objectives**

* Provide some simple calculations so we can test cloud services.
* Show case some elementary OpenCV functions
* Show an environmental image analysis application using Secchi disks

---

OpenCV (Open Source Computer Vision Library) is a library of thousands
of algorithms for various applications in computer vision and machine
learning. It has C++, C, Python, Java and MATLAB interfaces and supports
Windows, Linux, Android and Mac OS. In this section, we will explain
basic features of this library, including the implementation of a simple
example.

Overview
--------

OpenCV has countless functions for image and videos processing. The
pipeline starts with reading the images, low-level operations on pixel
values, preprocessing e.g. denoising, and then multiple steps of
higher-level operations which vary depending on the application. OpenCV
covers the whole pipeline, especially providing a large set of library
functions for high-level operations. A simpler library for image
processing in Python is Scipy's multi-dimensional image processing
package (scipy.ndimage).

Installation
------------

OpenCV for Python can be installed on Linux in multiple ways, namely
PyPI(Python Package Index), Linux package manager (apt-get for Ubuntu),
Conda package manager, and also building from source. You are
recommended to use PyPI. Here's the command that you need to run:

    $ pip install opencv-python

This was tested on Ubuntu 16.04 with a fresh Python 3.6 virtual
environment. In order to test, import the module in Python command line:

    import cv2

If it does not raise an error, it is installed correctly. Otherwise, try
to solve the error.

For installation on Windows, see:

* <https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows>

Note that building from source can take a long time and may not be
feasible for deploying to limited platforms such as Raspberry Pi.

A Simple Example
----------------

In this example, an image is loaded. A simple processing is performed,
and the result is written to a new image.

### Loading an image

    %matplotlib inline
    import cv2

    img = cv2.imread('images/opencv/4.2.01.tiff') 

The image was downloaded from USC standard database:

\URL{http://sipi.usc.edu/database/database.php?volume=misc&image=9}
### Displaying the image

The image is saved in a numpy array. Each pixel is represented with 3
values (R,G,B). This provides you with access to manipulate the image at
the level of single pixels. You can display the image using imshow
function as well as Matplotlib's imshow function.

You can display the image using imshow function:

    cv2.imshow('Original',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

or you can use Matplotlib. If you have not installed Matplotlib before,
install it using:

    $ pip install matplotlib

Now you can use:

    import matplotlib.pyplot as plt
    plt.imshow(img)

which results in

![**Figure:** Image display](images/opencv/output_5_1.png)

### Scaling and Rotation

Scaling (resizing) the image relative to different axis

    res = cv2.resize(img,
                     None,
                     fx=1.2, 
                     fy=0.7, 
                     interpolation=cv2.INTER_CUBIC)
    plt.imshow(res)

which results in

![**Figure:** Scaling and rotation](images/opencv/output_7_1.png)

Rotation of the image for an angle of t

    rows,cols,_ = img.shape
    t = 45
    M = cv2.getRotationMatrix2D((cols/2,rows/2),t,1)
    dst = cv2.warpAffine(img,M,(cols,rows))

    plt.imshow(dst)

which results in

![image](images/opencv/output_9_1.png)

### Gray-scaling

    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(img2, cmap='gray')

which results in

![**Figure:** Gray sacling](images/opencv/output_11_1.png)

### Image Thresholding

    ret,thresh =    cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
    plt.subplot(1,2,1), plt.imshow(img2, cmap='gray')
    plt.subplot(1,2,2), plt.imshow(thresh, cmap='gray')

which results in

![**Figure:** Image Thresholding](images/opencv/output_13_1.png)

### Edge Detection

Edge detection using Canny edge detection algorithm

    edges = cv2.Canny(img2,100,200)

    plt.subplot(121),plt.imshow(img2,cmap = 'gray')
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')

which results in

![**Figure:** Edge detection](images/opencv/output_15_1.png)

Additional Features
-------------------

OpenCV has implementations of many machine learning techniques such as
KMeans and Support Vector Machines, that can be put into use with only a
few lines of code. It also has functions especially for video analysis,
feature detection, object recognition and many more. You can find out
more about them in their website

[OpenCV](<https://docs.opencv.org/3.0-beta/index.html>
was initially developed for C++ and still has a focus on that
language, but it is still one of the most valuable image processing
libraries in Python.
