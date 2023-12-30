# Picascii -Turning pictures in to asciiart

## Installation

### Requirements

* Python 3.12.1
* Python Packages
  * For the creation of pip installable packages
    * packaging (23.2)
    * setuptools (69.0.3)
    * pip_review (1.3.0)
  * Dependencies to actually run picascii
    * Pillow (10.1.0)
  * An operating system that can install and run python.
    * Windows
    * MacOS
    * Linux
    * Anything that is BSD
    * Probably anything else. If I can build and run the specified version of Python it can run this.

## Procedure

Windows, MacOS, and Linux (Ubuntu) being popular OS's are listed here.

### Windows

1. Create a folder for output for this script and place it there (for instance, for a user named **Liv**, if your name is different then use THAT name in place of **Liv**, a good spot would be : `C:\Users\Liv\Documents\picascii`)
2. Go to Microsoft Store (Login if you haven't)
3. Search for Python
4. Install Python 3.12
5. Open Python 3.12 via start menu (You will be greeted with a Python REPL (Read Eval Print Loop) Prompt). Don't fret if your python experience level is less than basic. Help is on the way!
6. Type following into the prompt one line at a time:

```Python
import venv
venv.create(env_dir='C:\\Users\\Liv\\Documents\\picascii\\.venv', clear=True, with_pip=True, upgrade_deps=True) 
```

If we are using the example folder (The user name would be your own instead of 'Liv' though. If it is the same, then lucky hit, good for you, and hello.!)

This will take a pretty minute so please be patient and wait for the >>> to appear.
7. Now close the python prompt by typing and hitting enter.

```Python
exit()
```

8. Open Windows Powershell (Win+R followed by 'cmd.exe' and then Enter)
It should open up in your user folder
Type out the following to get to the proper folder (Denoted by a '&#126;>' Prefix, Don't type the prefix.)

```powershell
cd Documents\picascii
. .venv\Scripts\activate.ps1
```

Notice that your prompt should change its look to denoted virtual directory
It might look like this:

```Text
(.venv) C:\Users\Liv\Documents\picascii>
```

9 . To verify that the right python is selected do the following (line by line):

Powershell:

```Powershell
python
```

Python Prompt:

```Python
import sys
sys.executable
```

if `C:\\Users\\Liv\\Documents\\picascii\\.venv\\Scripts\\python.exe` (Knowing that the **Liv** is replaced with whatever your username is, of course.) shows up here then everything is correct so far.

10. Just exit the python prompt by typing

```Python
exit()
```

11. Now make sure everything is truly updated the venv creator should have already done that but it is always good to be sure.

Do the following and be patient on each of the steps (Line by Line, Do not attempt to enter as one chunk, you could potentially have undesirable results.):

Powershell:

```Powershell
python -m pip install --upgrade pip
python -m pip install pip_review
python -m pip_review -a
python -m pip install Pillow 
```

12. Now install this package to the virtual environment.

13. Let's just say you have checked out the project into the default code folder for this project. (`C:\Users\Liv\source\repos\picascii`) [Replacing the user name if necessary.] You will need to open another powershell window (You will need keep that one and do the following)

Powershell:

```Powershell
cd C:\Users\Liv\Documents\picascii
. .venv\Scripts\activate.ps1
cd C:\Users\Liv\source\repos\picascii
pip install .
```

Wait while python install all the dependencies and this package.

14. You can now close the "pip install" powershell window. You do not need it anymore.

15. Go to the other Powershell Window and be ready to have some fun!
    a. Select a picture (Let's say it is called 'livs_favorite_drawing.jpg' for the example, and you want to create a file called 'livs_favorite_text_drawing.txt', if a different picture with a different file name was selected then use that picture's filename) of your choosing and copy into the `C:\Users\Liv\Documents\picascii` folder. 
    b. Type the following to generate a text drawing picture whose largest dimension is 256:

Powershell:

```Powershell
python -m picascii --with-colors --input-file livs_favorite_drawing.jpg  --output-file livs_favorite_text_drawing.txt --max-side-size 256
```

It should generate the text file livs_favorite_text_drawing.txt (If it doesn't, please tell me, either I did something wrong or I in my excitement didn't explain things in this file properly. Nonetheless, I would need your input on this matter if something goes wrong. I would gladly receive your input if you have any suggestions or concerns. )
16. Open livs_favorite_text_drawing.txt in a consistent Text editor that uses a proper monospaced font such as Microsoft Visual Studio Code (The zooming out instructions are written for Microsoft Visual Studio Code).  You might not see desired results if you are using plain old Notepad or Word.
Zoom out of the text by typing Ctrl+- until the screen does not respond to you zooming out any more.
You should your image take shape on your screen.  You might have to scroll a little to see the entire work. But, you should see the gist of it. Neat. Right?  
Hit Ctrl+(NumPad 0) to get back to normal zoom and actually be able to read things again.

### MacOS

1. Install Python 3.12 to your mac first navigating to https://www.python.org
2. Hover on the Downloads Tab and click on Mac OS
3. Select the Latest release (3.12.1 at the time of this writing)
4. Scroll down to the bottom of the page where it says "Files"
5. Click on the file link that has macOS listed as the operating system. (Probably something like 'macOS 64-bit universal2 installer')
6. Your browser will download the installer. Please be patient.
7. For these next steps I hope you have administrator access for macOS will not let you run the installer properly without it.
  a. Execute the downloaded package (.pkg) file.
  b. MacOS will guide you the process of installing it. Usually default settings are appropriate.
8. Once installed open the Terminal application (Can't find it? Spotlight is your friend! Just do a ⌘+Space and type in 'Terminal')
9. Type out the following to create the project folder. This time I don't have to mention **Liv** as much since Mac OS (just so you know, Linux does as well) has the **&#126;** to denote the user home folder (That is, For **Liv**, it would expand to `/Users/Liv`). (Oh you are going to love this! It is actually a  little bit less legwork on a Mac (or Linux, explained later))

Bash:

```bash
mkdir -p ~/Documents/picascii
```

10. Create and then activiate the virtual environment. ( No skipping rope with the Python REPL like in windows. YES! You may dance and/or get out your choice musical instrument (if any) to celebrate if you like. 😉) If these commands do not execute you might want to make sure that python3.12 is in your $PATH.

Bash:

```bash
python3.12 -m venv --copies --clear --upgrade_deps ~/Documents/picascii/.venv
cd ~/Documents/picascii 
. .venv/bin/activate
```

The shell prompt should reflect that you are in the virtual environment by displaying a `(.venv)` in beginning of the text.

11. Verify that right python is being used. Make sure you use python and not python3.12 from here on out.

Bash:

```bash
python <( echo "import sys" ; echo "print(sys.executable)" )
```

You should see `/Users/Liv/Documents/picascii/.venv/bin/python`. If you do, then all is well. Phew! If not, then check your steps!
12. Now make sure everything is truly updated. The venv creation step should have already done that but it is always good to be sure.
Do the following and be patient on each of the steps:

Bash:

```bash
python -m pip install --upgrade pip
python -m pip install pip_review
python -m pip_review -a
python -m pip install Pillow 
```

13. Now install my package. Let's say you checked it out using the GitHub Client, or unzipped it from a code zip into the folder `~/proj/picascii`

Bash:

```bash
pushd ~/proj/picascii
pip install .
popd
```

14. Now Lets have fun!
    a. For best results select a picture (Let's say it is called 'livs_favorite_drawing.jpg' for the example, if a different picture was select then use that picture filename) of your choosing and copy into the &#126;/Documents/picascii folder. (Remember **&#126;** == `/Users/Liv` if you are **Liv**. If not replace it with your user name.) 
15. Type the following to generate a text drawing picture whose largest dimension is 256

Bash:

```bash
python -m picascii --with-colors --input-file livs_favorite_drawing.jpg  --output-file livs_favorite_text_drawing.txt --max-side-size 256
```

It should generate the text file livs_favorite_text_drawing.txt (If it doesn't, please tell me, either I did something wrong or I in my excitement didn't explain things in this file properly. Nonetheless, I would need your input on this matter if something goes wrong. I would gladly receive your input if you have any suggestions or concerns. )
16. Open livs_favorite_text_drawing.txt in a consistent Text editor that uses a proper monospaced font such as Microsoft Visual Studio Code (Yes they do have that for Mac too!) (The zooming out instructions are written for Microsoft Visual Studio Code).  You might not see desired results if you are using plain old Notepad or Word.
Zoom out of the text by typing ⌘+- until the screen does not respond to you zooming out any more.
You should your image take shape on your screen.  You might have to scroll a little to see the entire work. But, you should see the gist of it. Neat. Right?  
Hit ⌘+(NumPad 0) to get back to normal zoom and actually be able to read things again. If you do not have a NumPad because you have one of those common "skimpy" Apple Keyboards the simply Navigate the VS Code Menubar to (View > Appearance > Reset Zoom) and click.

### Linux (Ubuntu)

0. Open your terminal emulator
1. Install Python 3.12 (I have followed these instructions before. I vouch for them.)

Bash:

```bash
apt update && apt upgrade -y
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa
```

If You are prompted just hit enter.

Bash:

```bash
apt update
apt install python3.12
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
```

2. Type out the following to create the project folder. This time I don't have to mention **Liv** as much since Linux (just so you know, Mac OS does as well) has the **&#126;** to denote the user home folder (That is, For **Liv**, it would expand to `/home/Liv`). (Oh you are going to love this! It is actually a  little bit less legwork on Linux (or a Mac, as explained earlier))

Bash:

```bash
mkdir -p ~/Documents/picascii
```

3. Create and then activate the virtual environment. ( No skipping rope with the Python REPL like in windows. YES! You may dance and/or get out your choice musical instrument (if any) to celebrate if you like. 😉) If these commands do not execute you might want to make sure that python3.12 is in your $PATH.

Bash:

```bash
python3.12 -m venv --copies --clear --upgrade_deps ~/Documents/picascii/.venv
cd ~/Documents/picascii 
. .venv/bin/activate
```

The shell prompt should reflect that you are in the virtual environment by displaying a `(.venv)` in beginning of the text.

4. Verify that right python is being used. Make sure you use python and not python3.12 from here on out.

Bash:

```bash
python <( echo "import sys" ; echo "print(sys.executable)" )
```

You should see `/home/Liv/Documents/picascii/.venv/bin/python`. If you do, then all is well. Phew! If not, then check your steps!
5. Now make sure everything is truly updated. The venv creation step should have already done that but it is always good to be sure.
Do the following and be patient on each of the steps:

Bash:

```bash
python -m pip install --upgrade pip
python -m pip install pip_review
python -m pip_review -a
python -m pip install Pillow 
```

6. Now install my package. Let's say you checked it out using the GitHub Client, or unzipped it from a code zip into the folder `~/proj/picascii`

Bash:

```bash
pushd ~/proj/picascii
pip install .
popd
```

7. Now Lets have fun!
    a. For best results select a picture (Let's say it is called 'livs_favorite_drawing.jpg' for the example, if a different picture was select then use that picture filename) of your choosing and copy into the &#126;/Documents/picascii folder. (Remember **&#126;** == `/home/Liv` if you are **Liv**. If not replace it with your user name.) 
8. Type the following to generate a text drawing picture whose largest dimension is 256

Bash:

```bash
python -m picascii --with-colors --input-file livs_favorite_drawing.jpg  --output-file livs_favorite_text_drawing.txt --max-side-size 256
```

It should generate the text file livs_favorite_text_drawing.txt (If it doesn't, please tell me, either I did something wrong or I in my excitement didn't explain things in this file properly. Nonetheless, I would need your input on this matter if something goes wrong. I would gladly receive your input if you have any suggestions or concerns. )
9. Open livs_favorite_text_drawing.txt in a consistent Text editor that uses a proper monospaced font such as Microsoft Visual Studio Code (Yes they do have that for Mac too!) (The zooming out instructions are written for Microsoft Visual Studio Code).  You might not see desired results if you are using plain old Notepad or Word.
Zoom out of the text by typing Ctrl+- until the screen does not respond to you zooming out any more.
You should your image take shape on your screen.  You might have to scroll a little to see the entire work. But, you should see the gist of it. Neat. Right?  
Hit Ctrl+(NumPad 0) to get back to normal zoom and actually be able to read things again. If you do not have a NumPad because you have one of those common "skimpy" Apple Keyboards the simply Navigate the VS Code Menubar to (View > Appearance > Reset Zoom) and click.

## And Finally

If you feel inclined with to display gratitude, or congratulatory gestures, then just send me a pat on the back. (Just Send a message containing 'Picascii is so awesome! ✋️🫷🙎‍♂️' to one of the listed channels below.)

✝️ And you feel you want to praise the ONE who should be praised (the author of the author, the author of everything) then all you got to do is say a simple prayer of gratitude. He is the one who put this idea in my head by making me in such a way that I would come up with something such as this. And if you want help for things outside of this project (such as the things of life) then you can ask Him for that too. He is patiently waiting. What do have to lose? ✝️

If you have any concerns or suggestions then send them to the place as well.




## Contact

Charles Timothy Montgomery 2023

Use it? Sure! Have Fun. But do please be kind and respectful to others!

Want Make something out this as in extend it or put? Well ping me and tell me about it. I would like to be part of the action!

Email: <chazzofalf@gmail.com>, OR <charles.montgomery@charter.net>

discord: @chazz_the_intrepid

X: @chazz_the_intre

Facebook: @charles.montgomery3

Github: @chazzofalf

If you want some other way of contacting me, please just DM me using one of above listed contact methods. 
If you do. Please be prepared to fully identify yourself and explain your desired business with me.