# Tensorflwow on Ubuntu 20.04

We describe how to install tensorflow on Ubuntu 20.04. As of August 7th there is no officially released 
version of tensorflow for Ubuntu 20.04. We describe how you can achieve it with little effort.

If you have improvements to this install, please create a pull request.

First, make sure you have an up to date Ubuntu 20.04.

Next, make sure you have created a propper python 3 virtual env as to not interfere with your system python.

```
python3 -m venv ~/ENV3
source ~/ENV38/bin/activate
```


Now go to the Nvidia Web page and download CudNN 7.6.5 tgz file. You will need to create a an Account to log in.
Than you can download the file from:

```
mkdir tmp
cd tmp
wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/7.6.5.32/Production/10.1_20191031/cudnn-10.1-linux-x64-v7.6.5.32.tgz>
```

After this install the current default nvidia-cuda-toolkit with 

```bash
sudo apt install nvidia-cuda-toolkit
```

Now let us install the downloaded files

```bash
tar xvf ./cudnn-10.1-linux-x64-v7.6.5.32.tgz 
sudo cp cuda/include/cudnn.h  /usr/lib/cuda/include/
sudo cp cuda/lib64/libcudnn*  /usr/lib/cuda/lib64/
sudo chmod a+r /usr/lib/cuda/include/cudnn.h /usr/lib/cuda/lib64/libcudnn*
```

To update your .bashrc file you can use the following commands:

```bash
echo 'export LD_LIBRARY_PATH=/usr/lib/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/lib/cuda/include:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

Now we can install tensorflow with

```bash
pip install tensorflow
```

To test it use 

```python
python
>>> import tensorflow as tf
>>> tf.config.list_physical_devices("GPU")
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```
