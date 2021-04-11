# Import libraries
import feedparser           # Used for parsing though RSS feeds via url
import sys                  # Used to obtain arguments from the cli

# To Dos:
#           Expand RSS feed library (Maybe find a library online to import feed urls from?)
#           Create local feed database? (Users can utlize a local database containing a list of feed urls, allowing them to customize feeds)
#               Create empty 'feeds' dictionary and append it by iterating through a local file containing a custom list of feed URLs
#                   .opml File?
#                   .txt File?
#           Create advanced menu for feed topics (finance, world news, security news, etc.) 

# Banner and welcome message
print('''
..................................................................................................................................................
..#####...##..##..######..##..##...####...##..##..........######..######..######..#####...........#####...######...####...#####...######..#####...
..##..##...####.....##....##..##..##..##..###.##..........##......##......##......##..##..........##..##..##......##..##..##..##..##......##..##..
..#####.....##......##....######..##..##..##.###..........####....####....####....##..##..........#####...####....######..##..##..####....#####...
..##........##......##....##..##..##..##..##..##..........##......##......##......##..##..........##..##..##......##..##..##..##..##......##..##..
..##........##......##....##..##...####...##..##..........##......######..######..#####...........##..##..######..##..##..#####...######..##..##..
..................................................................................................................................................

This project was created during a Scripting Languages course taught at my uni. 
It's purpose (for now) is to print the top 5 stories from a given RSS feed. 
I plan on expanding this project a bit more to include some additional functionality and ease-of-use. 
Stay tuned! 
-V
''')

# Dictionary to contain built-in RSS feed URLs
# Key:Value format: 'Feed ID':'Feed URL'
feeds = [
    "http://feeds.bbci.co.uk/news/rss.xml?edition=us",                # BBC News
    "http://rss.cnn.com/rss/cnn_topstories.rss",                      # CNN
    "https://www.espn.com/espn/rss/news",                             # ESPN
    "http://feeds.foxnews.com/foxnews/latest/?feed=rss",              # Fox News
    "https://lifehacker.com/rss",                                     # Lifehacker
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",         # New York Times - World News
    "https://feeds.npr.org/1001/rss.xml",                             # NPR News
    "https://www.reddit.com/r/news/.rss",                             # Reddit r/News
    "https://ir.thomsonreuters.com/rss/news-releases.xml?items=15",   # Reuters Financial News
    "https://feeds.a.dj.com/rss/RSSWorldNews.xml",                    # Wall Street Journal - World News
    "https://threatpost.com/feed/",                                   # Threatpost
    "https://www.bleepingcomputer.com/feed/",                         # Bleeping Computer
    "https://www.reddit.com/r/netsec/.rss"                            # Reddit r/NetSec
]

# Function to parse and print feed articles
def parseFeed(feedList, numPosts):
    # Print the feed title
    if 'title' in feedList.feed:
        print('\nTitle: ' + feedList.feed.title)
    else:
        print('\n[No Title]')

    # Print the feed URL
    if 'link' in feedList.feed:
        print('Link: ' + feedList.feed.link)
    else:
        print('[No Link]')

    # Print the feed Description
    if 'description' in feedList.feed:
        print('Description: ' + feedList.feed.description + '\n')
    else:
        print('[No Description]\n')

    # Loop to display 'numPosts' number of articles
    for i in range(numPosts):
        # Print entry title
        if 'title' in feedList.entries[i]:
            print(str(i + 1) + ': ' + feedList.entries[i].title)
        else:
            print('[No Title]')

        # Print entry publish date
        if 'published' in feedList.entries[i]:
            print('Date: ' + feedList.entries[i].published)
        else:
            print('[No Publish Date]')

        # Print entry category
        if 'category' in feedList.entries[i]:
            print('Category: ' + feedList.entries[i].category)
        else:
            print('[No Category]')

        # Print entry summary
        if 'summary' in feedList.entries[i]:
            print('Summary: ' + feedList.entries[i].summary)
        else:
            print('[No Summary]')

        # Print entry URL
        if 'link' in feedList.entries[i]:
            print('Read More: ' + feedList.entries[i].link + '\n')
        else:
            print('[No Link]\n')

# Prints the menu of built-in feeds
def menu():
    print('''
    Built-in Feed Menu

    0.  Custom URL (In progress)
    1.  BBC News
    2.  CNN Top Stories
    3.  ESPN
    4.  Fox News - Latest
    5.  LifeHacker
    6.  New York Times
    7.  NPR Top Stories
    8.  Reddit r/news
    9.  Reuters Financial News
    10. Wall Street Journal - World News
    11. Threatpost
    12. Bleeping Computer - Latest
    13. Reddit r/NetSec
    ''')

def topics_menu():
    print('''
    Welcome! Please select a news topic:

    1. Top News Stories
    2. World 
    3. Finance
    4. Sports
    5. Tech
    6. Health
    7. Education
    8. Travel
    ''')

def world_submenu():
    # World Governments
    # Environmental Science
    # Space Stuff
    print("In Progress...")

def finance_submenu():
    # Stonks
    # US Fincance
    # Crypto
    print("In Progress...")

def sports_submenu():
    # Basketball
    # Football
    # Soccer
    # Baseball
    # General
    print("In Progress...")

def tech_submenu():
    # Latest
    # Security
    print("In Progress...")

def health_submenu():
    # ???
    print("In Progress...")

def edu_submenu():
    # ???
    print("In Progress...")

def travel_submenu():
    # ???
    print("In Progress...")


# Function to display menu and obtain user selection
def getInput():
    # Display menu
    menu()

    # User input
    menu_choice = input('Enter the number of the RSS feed you want to view ("exit" or CTRL+C to exit): ')
    num_feeds = input('How many articles would you like to view? (Default is 5): ')

    # Values returned are a tuple
    return menu_choice, num_feeds
      
# Check for arguments in the cli
# Usage: python3 PythonFeedReader.py [url_of_rss_feed]
# Example: python3 PythonFeedReader.py https://threatpost.com/feed/
if len(sys.argv) > 1:
    # Convert argument to string and use feedparser to parse the argument
    argument_feed = feedparser.parse(str(sys.argv[1]))

    # Prompt user for custom feed_number variable
    number_of_articles = input('Number of feeds to view: ')
    
    # Exception handling
    try:
        # Check for custom number of articles
        if number_of_articles != '':
            # Print the feed title, URL, and 'number_of_articles' amount of articles
            parseFeed(argument_feed, number_of_articles)
        else:
            # Use default number of articles (5)
            parseFeed(argument_feed, 5)
    except:
        # Error message
        print('''
            Exception triggered. Could be a bad URL or invalid number of articles.
            Check your URL or try changing the number of articles to a smaller number.
            Exiting program.
        ''')
else:
    # Display menu and prompt for user selection
    choice = getInput()

    # Create a loop for continuous program use
    while choice != 'exit':
        try:
            # Checks if the menu_choice number is a valid number between 1 and the length of the feeds dictionary
            if int(choice[0]) in range(len(feeds) + 1):
                # Checks if menu_choice number is indicative of a custom URL with default number of articles (5)
                if choice[0] == '0' and choice[1] == '':

                    # Prompt user for custom feed URL
                    custom_URL = input('Please enter the URL of your custom feed (without quotes): ')

                    # parseFeed params = feed, numFeeds
                    # Use default value of 5 for numFeeds
                    parseFeed(feedparser.parse(custom_URL), 5)

                    # Prompt user to continue or terminate program
                    choice = input('Would you like to select a different feed? ("y" for Yes or "exit" to exit): ')
                    if choice == "y":
                        # Redisplays menu and prompts for user input
                        choice = getInput()

                # Checks if menu_choice number is indicative of a custom URL with custom number of articles        
                elif choice[0] == '0' and choice[1]:

                    # Prompt user for custom feed URL
                    custom_URL = input('Please enter the URL of your custom feed (without quotes): ')

                    # Uses custom value for numFeeds
                    parseFeed(feedparser.parse(custom_URL), int(choice[1]))

                    # Prompt user to continue or terminate program
                    choice = input('Would you like to select a different feed? ("y" for Yes or "exit" to exit): ')
                    if choice == "y":
                        # Redisplays menu and prompts for user input
                        choice = getInput()

                # Checks for default number of articles with built-in menu_choice     
                elif choice[1] == "":

                    # Use default value of 5 for numFeeds
                    parseFeed(feedparser.parse(feeds[int(choice[0]) - 1]), 5)

                    # Prompt user to continue or terminate program
                    choice = input('Would you like to select a different feed? ("y" for Yes or "exit" to exit): ')
                    if choice == "y":
                        # Redisplays menu and prompts for user input
                        choice = getInput()
                
                # Uses built-in menu_choice with custom number of articles
                else:

                    # Use custom value for numFeeds
                    parseFeed(feedparser.parse(feeds[int(choice[0]) - 1  ]), int(choice[1]))

                    # Prompt user to continue or terminate program
                    choice = input('Would you like to select a different feed? ("y" for Yes or "exit" to exit): ')
                    if choice == "y":
                        # Redisplays menu and prompts for user input
                        choice = getInput()
            else:
                # Error handling: Request new entry
                print('\nERROR! Invalid input! Please enter an integer or type "exit" to exit')
                print('\nRedisplaying menu...')
                # Redisplay menu and prompts for user input
                choice = getInput()
        except:
            # Error handling / Troubleshooting
            print('''
                Exception triggered. Could be a bad URL or invalid number of articles.
                Check your URL or try changing the number of articles to a smaller number.
                Exiting program.
            ''')
            exit()
            
# Thanks for stopping by! <3