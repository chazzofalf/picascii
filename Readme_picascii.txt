Notice to the user: the following python package is required for this to work: Pillow
Windows Instructions:

Create a folder for this script and place it there (for instance, for a user named Liv,if your name is different then use THAT name in place of Liv, a good spot would be : C:\Users\Liv\projs\picascii with both picascii.py and picascii2.py being placed there)
Go to Microsoft Store (Login if you haven't)
Search for Python
Install Python 3.12
Open Python 3.12 via start menu (You will be greeted with a Python REPL (Read Eval Print Loop) Prompt) Don't fret help is on the way!
Type following into the prompt line by line (Do not enter the '>>>' part they are there to denote the lines you are going to enter.)
>>> import venv
>>> venv.create(env_dir='C:\\Users\\Liv\\projs\\picascii\\.venv',clear=True,with_pip=True,upgrade_deps=True) # If we are using the example folder (The user name would be your own though)
This will take a pretty minute so please be patient and wait for the >>> to appear.
Now close the python prompt
Open Windows Powershell (Win+R followed by 'cmd.exe' and then Enter)
It should open up in your user folder
Type out the following to get to the proper folder (Denoted by a '~>' Prefix, Don't type the prefix.)
~> cd projs\picascii
~> .venv\Scripts\activate.bat
Notice that your prompt should change its look to denoted virtual directory
To verify that the right python is selected do the following
~> python
>>> import sys
>>> sys.executable
if 'C:\\Users\\Liv\\projs\\picascii\\.venv\\Scripts\\python.exe' shows up here then everything is correct so far.
Just exit the python prompt by typing
>>> exit()
Now make sure everything is truly updated the venv creator should have already done that but it is always good to be sure.
Do the following and be patient on each of the steps:
~> python -m pip install --upgrade pip
~> python -m pip install pip_review
~> python -m pip_review -a
~> python -m pip install Pillow 
Now for the "fun" part:
For best results select a picture (Let's say it is called 'livs_favorite_drawing.jpg' for the example, if a different picture was select then use that picture filename) of your choosing and copy into the C:\Users\Liv\projs\picascii folder 
Type the following to generate a text drawing picture whose largest dimension is 256
~> python picascii2.py livs_favorite_drawing.jpg 256
It will generate the text file livs_favorite_drawing.jpg.txt
Open livs_favorite_drawing.jpg.txt in a consistent Text editor that uses a proper monospaced font such as Visual Studio Code. YMMV if you are using plain notepad.
Zoom out of the text by typing Ctrl+- until the screen does not respond any more.
You should your image take shape on your screen. Neat. Right?
Hit Ctrl+(NumPad 0) to get back to normal zoom and actually be able to read things again.

Mac OS Instructions 
Install Python 3.12 to your mac first navigating to https://www.python.org
Hover on the Downloads Tab and click on Mac OS
Select the Latest release (3.12.1 at the time of this writing)
Scroll down to the bottom of the page where it says "Files"
click on the file link that has macOS listed as the operating system. (Probably something like 'macOS 64-bit universal2 installer')
Your browser will download the installer.
For these next steps I hope you have administrator access for macOS will not let you run the installer properly without it.
Execute the downloaded package (.pkg) file.
MacOS will guide you the process of installing it. Usually default settings are appropriate.
Once installed open the Terminal application (Can't find it? Spotlight is your friend! Just do a Cmd+Space and type in 'Terminal')
Type out the following to create the project folder. This time I don't have to mention Liv as much since Mac OS or (just so you know, Linux as well) has the ~ to denote the user home folder. (Command Line lines are prefixed with a $) [Oh you are going to love this! It is actually a  little bit less legwork on Mac]
$ mkdir -p ~/projs/picascii
Lets assume that you have Downloaded picascii.py and picascii2.py to your Downloads folder (if it is not there then find it!)
Copy it to the project folder and make as sure as day that you have also include the ~/projs/picascii otherwise you will clobber picascii2.py with picascii.py
$ cp ~/Downloads/picascii*.py ~/projs/picascii 
Create the virtual environment # No skipping rope with the Python REPL like in windows. YES! You may dance and get out your instrument (if any) to celebrate if you like. 😉
$ python3.12 -m venv --copies --clear --upgrade_deps ~/projs/picascii/.venv
Navigate to the project folder
$ cd ~/projs/picascii 
Activate the virtual environment
$ . ~/projs/picascii/.venv/bin/activate
Verify that right python is being used
$ python <( echo "import sys" ; echo "print(sys.executable)" )
You should see /Users/Liv/projs/picascii/.venv/bin/python. If you do then all is well. Phew!
Now make sure everything is truly updated the venv creator should have already done that but it is always good to be sure.
Do the following and be patient on each of the steps:
$ python -m pip install --upgrade pip
$ python -m pip install pip_review
$ python -m pip_review -a
$ python -m pip install Pillow 
For best results select a picture (Let's say it is called 'livs_favorite_drawing.jpg' for the example, if a different picture was select then use that picture filename) of your choosing and copy into the C:\Users\Liv\projs\picascii folder 
Type the following to generate a text drawing picture whose largest dimension is 256
$ python picascii2.py livs_favorite_drawing.jpg 256
It will generate the text file livs_favorite_drawing.jpg.txt
Open livs_favorite_drawing.jpg.txt in a consistent Text editor that uses a proper monospaced font such as Visual Studio Code. YMMV if you are using plain notepad.
Zoom out of the text by typing Cmd+- until the screen does not respond any more.
You should your image take shape on your screen. Neat. Right?
Hit Cmd+(NumPad 0) to get back to normal zoom and actually be able to read things again.






Charles "chazz_the_intrepid" Timothy Montgomery 2023 
Use it? Sure! Have Fun. But do please be kind and respectful to others! 
Want Make something out this as in extend it or put? Well ping me and tell me about it. I would like to be part of the action! 
Email: chazzofalf@gmail.com 
discord: chazz_the_intrepid 
X: chazz_the_intre 
FB: charles.montgomery3 
Github: chazzofalf

If you want any other way of contacting me please just DM me using one of above listed contact methods.
If you do. Please be prepared to fully identify yourself and explain your desired business with me.