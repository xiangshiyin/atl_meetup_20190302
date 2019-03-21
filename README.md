# ATL_meetup_20190302
Materials for meetup demo

* The notebook containing the demo scripts: [demo_v1.ipynb](./notebook/demo_v1.ipynb)
* The data is located at the [data](./data/) folder
* Jupyter notebook needs to be installed in order to run the notebook script. You can directly install [Anaconda](https://www.anaconda.com/distribution/), and it contains jupyter notebook and other commonly used python libraries. Please choose the version based on your computer's operation system. The graphical installer might be easier for general users.
* There are many tutorials available online about Jupyter notebook, here is [one example](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).
* After the installation, simply navigate to any directory containing the notebook you want to run or any directory above the directory containing the notebook, and run ``jupyter notebook`` from command line, and a browser page will automatically open where you can click the notebook and get access to the notebook view.
    * You might get issues like `'jupyter' is not recognized as an internal or external command`. The reason is that the installation path of Jupyter notebook is not added the environment variable `PATH`, so that the computer can't recognize it. There are many solutions available online based your operation system, here is [one example](https://stackoverflow.com/questions/52287117/jupyter-is-not-recognized-as-an-internal-or-external-command).
* As mentioned in the presentation, once you have [Anaconda](https://www.anaconda.com/distribution/) installed, you'll have both conda and pip available as package manager. If you want to use pip, you can do `pip install [package name]` to install any package you want. If you are not sure, just check the documentation of corresponding packages, you'll figure out how, it should be very straightforward (a lot of them have github page containing source code and documentations showing you everything). Here is an example, where you can find out how to install the package [tqdm](https://github.com/tqdm/tqdm).
    * [pip_commands.sh](./pip_commands.sh) contains commonly used pip commands.
    * [conda_commands.sh](./conda_commands.sh) contains commonly used conda commands.
    * Official documentation is always the best resource to check.

* In order to test the mysql query, you have to install mysql on your computer, and run the sql script to create the table and load the data. 
    * [Windows](https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html) documentation
    * [Mac OS](https://dev.mysql.com/doc/refman/8.0/en/osx-installation.html) documentation
        * You can also install mysql via [Homebrew](https://gist.github.com/nrollr/3f57fc15ded7dddddcc4e82fe137b58e)

* All the packages needed for the notebook script has been listed in [requirements.txt](./requirements.txt)
* [virtualenv_commands.sh](./virtualenv_commands.sh) contains commonly used virutalenv commands to create and use virtual environment. There are many resources available online, here is [one example](https://docs.python-guide.org/dev/virtualenvs/).
* Good tutorial on pandas dataframe size optimization: [[link](https://www.dataquest.io/blog/pandas-big-data)]