# Installing Python on Windows

Jacques Fleischer and Gregor von Laszewski

* Prerequisite: We assume you have administrative privileges to install programs

We have provided a convenient 2-minute YouTube video that walks you through the steps. Please note that when a newer version of Python becomes available to update the version numbers accordingly.

{{% youtube T6UYyu5XVMc %}}

The video showcases the following steps:

1. First, open up in any web browser the url <https://www.python.org/>

2. As of June 2021, the latest version of Python is `3.9.6`. You may see a different number. We recommend you use the newest official version which is provided to you by simply clicking the  button under "Download the latest version for Windows".

3. Once the download has completed, open the file by clicking on it in your Downloads pane.

4. Be sure to check the box that reads "Add Python x.x to PATH". This will allow you to run commands from the terminal/command prompt.

5. Click "Install Now". The default options that entail this selection are appropriate. 

   1. The UAC prompt will pop up. UAC stands for "User Account Control" and exists so that the computer will 
      not have unauthorized changes performed on it. Click "Yes" because Python is safe. School-issued computers 
      may ask for an administrator password, so refer to step 5's sidenote.

6. The instalation will take some time.

9. If the setup was successful, then it will say so. Click "Close".

10. Click the "Type here to search" box in the bottom-left of the screen, type "cmd", and press Enter.

    1. An alternative method is to press the Windows key and the "R" key at the same time, type "cmd", and 
       press Enter. This is convenient for those who like to use the keyboard.

11. Type `python --version` and the output should read "Python x.x.x"; as long as it is the latest version 
    from the website, congratulations. Python is installed on the computer.
    
## Mac

Click the following image to be redirected to a 5-minute YouTube walkthrough. (Yes, Mac's video is a little longer, but do not fret!
You can skip to the 1:00 minute mark if you are in a hurry.)

{{% youtube TttmzM-EDmk %}}


1. First, open up in any web browser the url <https://www.python.org/>

2. Underneath `Download the latest version for Mac OS X`, there should be a yellow button that reads `Download Python x.x.x`. Click on it, and the download should commence.

3. Once the download finishes, open it by clicking on it. The installer will open. Click `Continue`, click `Continue` again, click `Continue` again.
   Read the agreements.

4. Click `Agree`. 
   1. If you want to check how much free storage you have on your computer, click the Apple icon in the top left of your computer. Click
    `About This Mac` and then click on `Storage`. As of July 2021, Python takes ~120 MB of space. Remember that 1 GB = 1000 MB.


5. Click `Install`. Enter your password and press Enter. The instalation will take a while

6. A Finder window will open. You can close it as it is unnecessary. Click `Close` in the bottom-right of the installer. Click `Move to Trash` because you do not need the installer anymore.

7. Next confirm that Python installed correctly. Click the magnifying glass in the top-right of your screen and then type `terminal` into Spotlight Search. Double-click `Terminal`.
   1. The terminal will be used frequently. Consider keeping it in the dock for convenience. Click and hold the Terminal in the dock, go to `Options`, and click `Keep in Dock`.
  

10. Type `python3 --version` into the terminal and press Enter. It should output the latest version of Python. Congratulations!

## Linux (Ubuntu from Source)

Click the following image to be redirected to a 9-minute YouTube walkthrough. (Linux's tutorial is the longest, but it is worth it.)
This tutorial uses Ubuntu, but it should work on other Linux distros, as well.

{{% youtube TttmzM-EDmk %}}


1. First, open up in any web browser the url <https://www.python.org/>   
   
3. Look at the latest version. It is on the yellow button: `Download Python x.x.x`. You do not need to click this button. Remember this version number.

   
4. Open a terminal by pressing the Windows key, or by clicking the grid on the bottom left of your screen. Type `terminal`. Click on the `Terminal` result that appears.
   
5. Next prepare your system
 
```bash
$ sudo apt-get update
$ sudo apt-get install libssl-dev openssl make gcc
``` 

and press Enter nad typ in y, when appropriate. You are then asked if you are okay with a certain amount of disk space being taken up. Type `y`, which stands for Yes, and then press Enter.

   1. If you want to check how much disk space you have, press the Files icon on the left (on the taskbar) and click `Other Locations`. You may have to scroll down on the sidebar in order to see it. It should say how much GB is available. Remember, 1 GB = 1000 MB and 1 MB = 1000 KB.

      
8. After this finishes, type `cd /opt` and press Enter. Then, remember which version you read on the Python webpage (the latest version). Type 
  
   ```bash
   $ sudo wget https://www.python.org/ftp/python/x.x.x/Python-x.x.x.tgz
   $ sudo tar xzvf Python-x.x.x.tgz
   $ cd Python-x.x.x
   $ ./configure
   $ make
   $ sudo make install
   ``` 
   
PLEASE NOTE THAT GREGOR BELIEVES THE NEXT STEP SHOUDL BE not what is described in 12, but 

```
sudo make alitinstall
```

THis needs t be verified and researched.

12. Once the installation finishes, type `sudo ln -fs /opt/Python-x.x.x/Python /usr/bin/pythonx.x`. Notice that `x.x.x` should be replaced with the full version number and `x.x` should have the first two numbers in the version number. Press Enter.
 
13. Confirm Python's successful installation by typing `pythonx.x --version`; be sure to replace x.x with the first two numbers of the version number. It should output the latest version number. Congratulations!

    
Credit to bobbyiliev for making the required commands publicly available. The commands are available here, as well: https://www.digitalocean.com/community/questions/how-to-install-a-specific-python-version-on-ubuntu

## Python venv

pefore you install packages you need to create a Python venv in your loacl envioronment. We typically do this with 

```bash
$ python3.9 -m venv ~/ENV3
$ source ~/ENV3/bin/activate
```

or for Windows executed in gitbash

```bash
$ python -m venv ~/ENV3
$ source ~/ENV3/Scripts/activate
```


## Troubleshooting

### Incorrect Python Version on Command Prompt

If the Windows computer has installed an older version of Python, running `python --version` on Command Prompt may output an older version. Typing `python3 --version` may output the correct, latest version.



