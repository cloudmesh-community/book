from selenium import webdriver
import chromedriver_autoinstaller
import json
from cloudmesh.common.Shell import Shell
from cloudmesh.common.Shell import Console
from cloudmesh.common.systeminfo import os_is_windows, os_is_linux, os_is_mac
import pathlib
import os
import sys
import time

if os_is_linux():
    try:
        r = Shell.run('google-chrome --help')
        print(r)
        if 'not found' in str(r):
            raise Exception
    except Exception as e:
        Console.error('Chrome not installed. Installing now')
        os.system('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ')
        os.system("""sudo sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'""")
        os.system('sudo apt-get update')
        os.system('sudo apt-get -y install google-chrome-stable')

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.minimize_window()

options = webdriver.ChromeOptions()
options.headless = False

options.add_argument("--kiosk")

current_dir = Shell.map_filename('.').path
current_dir = pathlib.Path(current_dir).as_posix()

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
        # This is the folder where i want to place my PDF (in the same directory as this
        'default_directory': current_dir
        # file)
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
    "isLandscapeEnabled": True,
    "scalingType": 3,
    "scaling": "160"
}

prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    "savefile.default_directory": current_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "download.safebrowsing.enabled": True
}
options.add_experimental_option('prefs', prefs)
options.add_argument('--kiosk-printing')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-software-rasterizer')

driver = webdriver.Chrome(options=options)

driver.set_script_timeout(60)

driver.get("https://cybertraining-dsc.github.io/report/printview/")
driver.minimize_window()

driver.execute_script("print();return false;")

driver.quit()

Shell.run('mv "Reports _ Cybertraining.pdf" "Reports_Cybertraining.pdf"')
#Shell.open('./Reports_Cybertraining.pdf')

dest_dir = Shell.map_filename('./dest').path

i_can_run_docker = True
r = None
try:
    r = Shell.run('docker version')
except Exception as e:
    i_can_run_docker = False
    print(e.output)
    if 'must be run with elevated privileges' in str(e.output):
        Console.error('Terminal must be admin. Assuming dest dir exists...')
if 'not found' not in str(r) and i_can_run_docker:
    Shell.run('make -f Makefile.docker epub')

Shell.copy('./dest/book/cover.png', '.')
#Shell.run('wget -O reu2021.pdf
# https://cybertraining-dsc.github.io/docs/pub/reu2021.pdf')

Shell.run('img2pdf cover.png -o cover.pdf')
# pdfs = ['cover.pdf', 'Reports_Cybertraining.pdf']

try:
    r = Shell.run('gs -h')
except Exception as e:
    Console.error('gs not installed. Attempting install now')
    if os_is_linux():
        Shell.run('wget -O ghostscript-9.56.1-linux-x86_64.tgz '\
                  'https://github.com/ArtifexSoftware/ghostpdl'\
                  '-downloads/releases/download/gs9561/ghostscript-9.56.1-linux-x86_64.tgz')
        Shell.run('tar -xvzf ghostscript-9.56.1-linux-x86_64.tgz')
        os.chdir('ghostscript-9.56.1-linux-x86_64')
        Shell.run('./configure')
        Shell.run('make')
        Shell.run('sudo make install')
        os.chdir('..')
        Shell.rmdir('ghostscript-9.56.1-linux-x86_64')
        Shell.rm('ghostscript-9.56.1-linux-x86_64.tgz')
    if os_is_windows():
        try:
            Shell.run('choco --version')
        except Exception as e:
            print(e.output)
            Console.error('choco not installed, so this script cannot install '\
                          'ghostscript for you. Either install ghostscript or '
                          'chocolatey.')
            sys.exit()
        Shell.run('choco install ghostscript -y')
    if os_is_mac():
        try:
            Shell.run('brew')
        except Exception as e:
            print(e.output)
            Console.error('brew not installed, so this script cannot install '\
                          'ghostscript for you. Either install ghostscript or '\
                          'brew.')
            sys.exit()
        Shell.run('brew update')
        Shell.run('brew upgrade')
        Shell.run('brew install ghostscript')
        Shell.run('brew cleanup')
# pypdftk.concat(pdfs, out_file='REU2021.pdf')
command_params = '-dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite ' \
                 '-dPDFSETTINGS=/prepress ' \
                 '-sOutputFile=REU2021.pdf cover.pdf Reports_Cybertraining.pdf'

if os_is_windows():
    Shell.run(fr'"C:\Program Files\gs\gs9.56.1\bin\gswin64.exe" '
              fr'{command_params}')
else:
    Shell.run(f'gs {command_params}')
Shell.open('REU2021.pdf')
