lou-tools-bot
=============
LoU Bot is a chatbot that is part of the set of tools (LoU Tools) designed for the EA/Phenomic game, Lord of Ultima.

The bot is designed to be similar in function to an IRC bot (but without all the useful functions). It is also designed to be flexible in the commands that can be added. The bot fully complies with the rules for 3rd party tools.

For more info / usage instructions / updates etc., visit the forum topic.

*Unfortunately the original forum topic with info and usage was deleted by a recent forum move. Setup instructions are below.*

Setup Instructions
------------------
1. Edit the config.py files. Most the variables are self explanatory - you can probably leave SPEED and TIMEOUT alone, but make sure to set the rest to the correct values. DB needs to be an absolute path to the location where you want to store the database.
2. Run setup.py. If you install python (and if it's in your PATH), you should just be able to run 'python setup.py' on the command line. This command creates the database file.
3. After that, it's up to you! If you're familiar with Python, you can edit the filters.py file to add some advanced filters, otherwise you can use run.py (with various command line arguments) to add/remove basic responses. If you execute run.py without any arguments, it should print out the usage information. Executing run.py with '-r' will start the bot.

License
-------
The project is licensed under the [GNU General Public License Version 3](http://www.gnu.org/licenses/gpl-3.0.txt).

Thanks
------
Thanks to [JetBrains](http://www.jetbrains.com/) for giving the LoU Tools project a free license to use [PyCharm](http://www.jetbrains.com/pycharm/), it was very useful in the creation of LoU Bot, as well as upcoming upgrades to the main LoU Tools website.
