# RSS Project
This project was created during a Scripting Languages course taught at my uni. It's purpose (for now) is to print the top 5 stories from a given RSS feed. I plan on expanding this project a bit more to include some additional functionality and ease-of-use. Stay tuned! -V

# Prereqs
This project uses python3 and the "feedparser" module to analyze and format feed data (.xml) for human eyes.

## Python
Python3 is used in this project and is (normally) already installed on linux machines.
To view your current python version in Linux:
```markdown
python3 -v
```
or
```markdown
python3 --version
```
### Install the latest version using apt
To download the latest version with apt:
```markdown
sudo apt-get upgrade python3
```
### Install required modules (feedparser)
You can install feedparser with pip by running the following command:
```markdown
pip3 install feedparser
```

# Usage
To use the program with a custom URL:
```markdown
python3 PythonFeedReader.py [URL]
```
To use the program with pre-built URLs: 
```markdown
python3 PythonFeedReader.py
```

## Current (01/2020) menu of pre-built options:

1. BBC News
2. CNN Top Stories
3. ESPN
4. Fox News - Latest
5. LifeHacker
6. New York Times
7. NPR Top Stories
8. Reddit r/news
9. Reuters Financial News
10. Wall Street Journal - World News
11. Threatpost

# Disclaimer
This project was inspired by the Mr. Robot television series. Feel free to use it as you see fit! <3
