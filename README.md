# DEPRECATED: see [The Reverse](https://github.com/AlphaCodeCorp/The-Reverse) on AlphaCode. 

# MissyThePromBot-Exia

Missy is a bot allowing to choose the roles of the members of each group randomly among "Leader", "Scrib", "Secretary", "Time Keeper"

> Others features would come during his development.

## Getting Started

First make sure you have the following:
- [git](https://git-scm.com/)
  - Optional: Get a UI such as [GitHub Desktop](https://desktop.github.com/) or [TortoiseGit](https://tortoisegit.org/)
- [Python 3](https://www.python.org/). We recommend the *current* version.



Now you need to pull a copy of the codebase onto your computer. Make a fork of the repo by clicking the **Fork** button at the top of this page. Next, click the green button **Clone or download** and copy your *Clone with HTTPS* URL, and then run the command `git clone <paste link>`. This will take a minute.

When cloning finishes, open a command window to the source and run the command `pip install -r package.txt`. This will take a minute or two the first time. While it's running, copy the `.config.json.example` file in the project root, and name it `.config.json`.Now you need to fill the Token key. To get your key, login to Discord Developer Portal and go to [your applications](https://discordapp.com/developers/applications). Press on **New Application**, enter an **Application Name** (this is required), then go to the Bot tab, press **Add Bot**, copy the **Token key**, then replace `TOKEN` in `.config.json` with this key.

Once all that's done you're ready to fire up the discord bot! Just run the command `python bot.py` in the project root. the first start could take another minute.
