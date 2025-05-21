Module 1: Installing Python the Right Way
---

#### Background
Python is deceivingly simple to download. You can go to [python.org](https://www.python.org/downloads/) and download the latest version (3.13 as of May, 2025) or to [anaconda.com](https://www.anaconda.com/download) and get an out-of-the-box python playground. However, especially for scientists, these download methods are not a great solution for longevity of your installation. When it comes time to update your python or install a package that needs a downgraded version of python, why would you stop your science to back to those websites and figure out what version of python you need, what folder it needs to be put into, how many packages need to be re-installed, etc... An ideal download method for scientists is one that requires the most minimal effort to maintain given the passing of time and the exploration of community-made packages. To achieve this goal, this module will walk through how to download python via a package manager, how to use this package manager to maintain and partition python environments for your different projects and, finally, how to share your python environments with scientists. If there is time, this module will finally go over what an IDE is and how it can incorporate the python environments you just created.

#### Module Tasks
1. Download and Install Conda via the Miniconda distribution
2. Create a new python environment
3. Install some useful packages into this environment
4. Export this environment to .yaml (BONUS: Install someone else's environment)
5. Activate this environment in a shell and in VSCode (or another IDE)

#### For Windows Users
##### Downloading Miniconda
Windows users can simply go online and [download](https://www.anaconda.com/download) the latest miniconda distribution. After downloading the .exe file, launch it and follow the prompts. Pay close attention to where this is installed as we will visit this directory later.

#### For Mac (and Linux) Users
##### Installing Homebrew
MacOS in particular has a very broad and useful package manager called `homebrew`. I reccomend using this to install conda without ever having to open a browser. Simply copy and paste this into a `bash` shell and it should install automatically.
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
##### Installing Conda
From there, you can use homebrew via the `brew` command. Start by checking on the installation of homebrew:
```bash
brew --version
```
If this is succesful, install conda via the following command:
```
brew install --cask conda
```
where the `--cask` flag is simply telling what box of packages to grab conda from.

#### Using 
##### Configuring Conda
Before any python installation, we must do a little bit of configuration. First, check the status of your installation using the following command:
```
conda info
```
While checking the existence of your conda install, this command also provides lots of valuable information such as where the conda configuration file lives and where the base environment is stored. Finally, before creating your first python environment, run the following command:
```
conda init
```
to initialize conda. What this command does is it modifies the few lines of code that exist in the configuration file (.condarc for windows and .bashsrc (for example) for Mac) to ensure that your computer knows where to look for the conda.exe file everytime you enter a conda command, i.e. `conda ...`.

NOTE: Sometimes, on mac, the above command says that it did not make any modifications. In this case, try putting the name of your desired shell into the command. For example:
```
conda init zsh
```

##### Creating your first python environment
Time to create your first python environment! As mentioned earlier, miniconda ships with the latest version of python installed. All we need to do is create an environment for this python installation to live in. We do this by the following command:
```
conda create -n "[my_env_name]"
```
This will create a conda environment with python installed. To check on this environment, enter:
```
conda envs list
```
This will show you all of the available environments. You should see, if this is your first time using conda, a `base` environment and the name of the environment you just created. `base` contains some basic python packages, but to do any real work, you should "activate" your new conda environment using:
```
conda activate [my_env_name]
```
From now on, you should see `(my_env_name)` appear at the beginning of your shell line to indicate which conda environment you are in. From here, you can simply call:
```
python.exe --version
```
To check the python version in this environment. Simply running python.exe will begin a python REPL with the pacakge-specific python executable.
##### Installing your first python packages
There are two ways to install packages into a conda environment. The first is by using packages that are available via conda:
```
conda install [some_package]
```
From there, conda will begin by install this packages dependencies and will move on to make sure this package is compatible with all the other packages already install in [my_env_name]. To see a list of packages currently installed, simply run:
```
conda list
```
and look for [my_env_name] among the many other installed packages.
##### Shipping your python packages
To export an environment so someone else can use it, the command is simply:
```
conda env export > [my_env_name].yaml
```
This will create a human-readable log of all the packages you have installed in this specific environment. To then take this file and create a new local environment out of it, use:
```
conda create -f [my_env_name].yaml
```
This will create an identical environment to [my_env_name] in the current directory.

##### Extra Tips:
1. Do not be afraid to just create a new conda environment. If you have to use a large package with lots of dependencies, for example, do not try to install it in the base environment, in hopes of avoiding dependency conflicts.

#### What's IDE and how do we use it?
Integrated Development Environments (IDEs) are simply user interfaces designed to help make coding easier than a windows notebook. While some people choose to use heavy IDEs like PyCharm for their extensive features and others choose to use lightweight IDEs like Windows Notepad at the extreme end of things. So what IDE should you choose as a scientist??
I personally have found VSCode to be the best IDE because it is both extremely capable while also being lightweight. VSCode also allows coding in different languages including Latex!
##### Activating a python environment in VSCode
You can download VSCode [here](https://code.visualstudio.com/download). You can now activate your environment within VSCode. Look in the bottom right corner and you may see the currently active Python version (3.13). Click on this version number to see all available conda environments. Select one and you are on your way!

