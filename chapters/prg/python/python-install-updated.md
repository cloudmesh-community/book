---
date: 2021-06-24
title: Tutorial on Installing Python
linkTitle: Install Python
tags: ["project", "reu", "tutorial"]
description: "Time for Python"
author: Jacques, Fleischer
github_url: https://github.com/cybertraining-dsc/su21-reu-361/edit/main/tutorials/python/index.md
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{% pageinfo %}}

## Abstract

This tutorial teaches how to install Python on Windows 10.

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** python


## Windows

Click the following image to be redirected to a 2-minute YouTube walkthrough.

{{% youtube T6UYyu5XVMc %}}

1. First, open up any web browser. This tutorial utilizes Google Chrome, but any other browser should work as long as it is not a 1990s version of Netscape. (Do not worry— you probably don't have this.) The browser of choice can be Microsoft Edge, Firefox, Opera— as long as it can perform a search on a search engine, access a webpage, and download a file.
\
&nbsp;

2. Open your browser by clicking the search box in the bottom left of your screen, where it says "Type here to search". Then, type "google chrome" (or whatever is the name of the browser you use) and click it once it appears.
   1. The "Type here to search" box could be missing if you have customized your taskbar (the taskbar is the long box typically located on the bottom of your screen which has icons). In this case, just click the Windows logo in the bottom left and type your browser name.
   2. This is just one way to open your browser. You can even click a shortcut to your web browser on your taskbar, on your Desktop, or your Start Menu. In computing, there is typically many ways to accomplish the same end objective.
 \
&nbsp;

3. Once your browser has loaded, search for "python" on Google or any search engine. Click the result that reads "Downloads" from the website "python.org".
 \
&nbsp;

4. As of June 2021, the latest version of Python is `3.9.5`. You may see a different number. As long as you click the button under "Download the latest version for Windows", this will work. Try it now.
 \
&nbsp;

5. Once the download has completed, open the file by clicking on it in your Downloads pane.
   1. If you are utilizing a school-issued computer, you may be prevented from opening this .exe file because you are not the administrator. Please email or otherwise get in contact with your instructor, professor, or head of IT to discuss installing Python.
 \
&nbsp;

6. Be sure to check the box that reads "Add Python x.x to PATH". This will allow you to run commands from the terminal/command prompt.
 \
&nbsp;

7. Click "Install Now". The default options that entail this selection are appropriate for this experiment's intents and purposes; choosing "Customize installation" may create reproducibility issues down the road, so please select "Install Now" instead.
   1. The UAC prompt will pop up. UAC stands for "User Account Control" and exists so that the computer will not have unauthorized changes performed on it. Click "Yes" because Python is safe. School-issued computers may ask for an administrator password, so refer to step 5's sidenote.
 \
&nbsp;

8. Sit back and watch the green progress bar, whose speed will depend on the power of the computer.
 \
&nbsp;

9. If the setup was successful, then it will say so. Click "Close".
 \
&nbsp;

10. Click the "Type here to search" box in the bottom-left of the screen, type "cmd", and press Enter.
    1. An alternative method is to press the Windows key and the "R" key at the same time, type "cmd", and press Enter. This is convenient for those who like to use the keyboard.
 \
&nbsp;

11. Type `python --version` and the output should read "Python x.x.x"; as long as it is the latest version from the website, congratulations. Python is installed on the computer.
 \
&nbsp;

## Mac

Click the following image to be redirected to a 5-minute YouTube walkthrough. (Yes, Mac's video is a little longer, but do not fret!
You can skip to the 1:00 minute mark if you are in a hurry.)

{{% youtube TttmzM-EDmk %}}


1. Open a web browser that is able to search and download a file. This tutorial uses Google Chrome for Mac.
 \
&nbsp;

2. Type in `python` in the address bar and press enter. It should perform a search on your default search engine.
 \
&nbsp;

3. Look for the result that is from `python.org`. Click on the subresult that says `Downloads`.
 \
&nbsp;

4. Underneath `Download the latest version for Mac OS X`, there should be a yellow button that reads `Download Python x.x.x`. Click on it, and the download should commence.
 \
&nbsp;

5. Once the download finishes, open it by clicking on it. The installer will open. Click `Continue`, click `Continue` again, click `Continue` again, oh my goodness!
 \
&nbsp;

6. Click `Agree`. 
   1. If you want to check how much free storage you have on your computer, click the Apple icon in the top left of your computer. Click
    `About This Mac` and then click on `Storage`. As of July 2021, Python takes ~120 MB of space. Remember that 1 GB = 1000 MB.
 \
&nbsp;

7. Click `Install`. Enter your password and press Enter. Watch the blue progress bar crawl like a turtle... or blast off at the speed of sound! This depends on your computer speed.
 \
&nbsp;

8. A Finder window will open. You can close it as it is unnecessary. Click `Close` in the bottom-right of the installer. Click `Move to Trash` because you do not need the installer anymore.
 \
&nbsp;

9. Time to confirm that Python installed correctly. Click the magnifying glass in the top-right of your screen and then type `terminal` into Spotlight Search. Double-click `Terminal`.
   1. The terminal will be used frequently in this experiment. Consider keeping it in the dock for convenience. Click and hold the Terminal in the dock, go to `Options`, and click `Keep in Dock`.
 \
&nbsp;    

10. Type `python3 --version` into the terminal and press Enter. It should output the latest version of Python. Congratulations!
 \
&nbsp;

## Linux

Click the following image to be redirected to a 9-minute YouTube walkthrough. (Linux's tutorial is the longest, but it is worth it.)
This tutorial uses Ubuntu, but it should work on other Linux distros, as well.

{{% youtube TttmzM-EDmk %}}


1. Open a web browser. It can be any browser as long as it can perform a search and navigate to a webpage.
 \
&nbsp;
   
2. Search for `python` by typing it into the address bar and pressing enter. Click on `Downloads` underneath the result from `https://www.python.org`.
 \
&nbsp;
   
3. Look at the latest version. It is on the yellow button: `Download Python x.x.x`. You do not need to click this button. Remember this version number.
 \
&nbsp;
   
4. Open a terminal by pressing the Windows key, or by clicking the grid on the bottom left of your screen. Type `terminal`. Click on the `Terminal` result that appears.
 \
&nbsp;
   
5. Type `sudo apt-get update` and press Enter. Wait for it to finish. It may already be up-to-date. 
 \
&nbsp;
   
6. Type `sudo apt-get install libssl-dev openssl make gcc` and press Enter. This will install the libraries required to connect to an FTP to download Python. Type your password for your Linux user account, if prompted, and press Enter.
 \
&nbsp;
   
7. You are then asked if you are okay with a certain amount of disk space being taken up. Type `y`, which stands for Yes, and then press Enter.
   1. If you want to check how much disk space you have, press the Files icon on the left (on the taskbar) and click `Other Locations`. You may have to scroll down on the sidebar in order to see it. It should say how much GB is available. Remember, 1 GB = 1000 MB and 1 MB = 1000 KB.
 \
&nbsp;
      
8. After this finishes, type `cd /opt` and press Enter. Then, remember which version you read on the Python webpage (the latest version). Type `sudo wget https://www.python.org/ftp/python/x.x.x/Python-x.x.x.tgz` after replacing the `x.x.x` with the latest Python version number. As of July 2021, it is `3.9.6`. Press Enter.
 \
&nbsp;
   
9. Wait for the download to complete. Then, type `sudo tar xzvf Python-x.x.x.tgz` after you replace `x.x.x` with the latest Python version number. Press Enter.
 \
&nbsp;
   
10. Type `cd Python-x.x.x` after replacing `x.x.x` with the latest version number. Type `./configure` and press Enter.
 \
&nbsp;
    
11. Once it finishes, type `make` and press Enter. Once *that* finishes, type `sudo make install` and press Enter.
 \
&nbsp;
    
12. Once the installation finishes, type `sudo ln -fs /opt/Python-x.x.x/Python /usr/bin/pythonx.x`. Notice that `x.x.x` should be replaced with the full version number and `x.x` should have the first two numbers in the version number. Press Enter.
 \
&nbsp;
    
13. Confirm Python's successful installation by typing `pythonx.x --version`; be sure to replace x.x with the first two numbers of the version number. It should output the latest version number. Congratulations!
 \
&nbsp;
    
Credit to bobbyiliev for making the required commands publicly available. The commands are available here, as well: https://www.digitalocean.com/community/questions/how-to-install-a-specific-python-version-on-ubuntu
 \
&nbsp;

## Troubleshooting

### Incorrect Python Version on Command Prompt

If the Windows computer has installed an older version of Python, running `python --version` on Command Prompt may output an older version. Typing `python3 --version` may output the correct, latest version.



