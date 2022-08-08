Prerequisite:

You need to install the latest python version using this link : https://www.python.org/downloads/
You need to run the scripts from your computer terminal :

On Windows press touche windows + r and enter cmd

On Mac press cmd + space and enter terminal

On Linux press Ctrl + Alt + T

The software uses several libraries that you can find in the requirement.txt file

You can create a new virtual env and download all the libraries using the following commands:

$ pip install ven

$ pip install -r requirements.txt

Launching:

You need to download and copy all the files from the repo and launch the software from the terminal using the following command:

python main.py

Flake8 report:

The repo holds a flake8 report without any issues. It is possible to generate a new one using the following command : 

$  flake8 --format=html --htmldir=flake_report --filename=.py



