# Import libraries
import feedparser           # Used for parsing though RSS feeds via url
import sys                  # Used to obtain arguments from the cli

# To Dos:
#           Expand RSS feed library (Maybe find a library online to import feed urls from?)
#           Create local feed database? (Users can utlize a local database containing a list of feed urls, allowing them to customize feeds)
#               Create empty 'feeds' dictionary and append it by iterating through a local file containing a custom list of feed URLs
#           Create handler for option 0 (custom URL)
#           Create advanced menu for feed topics (finance, world news, security news, etc.)

# Banner and welcome message
print("""
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
""")

# Dictionary to contain default RSS feed URLs
feeds = {
    1:"http://feeds.bbci.co.uk/news/rss.xml?edition=us", 
    2:"http://rss.cnn.com/rss/cnn_topstories.rss", 
    3:"https://www.espn.com/espn/rss/news", 
    4:"http://feeds.foxnews.com/foxnews/latest/?feed=rss", 
    5:"https://lifehacker.com/rss", 
    6:"https://rss.nytimes.com/services/xml/rss/nyt/World.xml", 
    7:"https://feeds.npr.org/1001/rss.xml", 
    8:"https://www.reddit.com/r/news/.rss", 
    9:"https://ir.thomsonreuters.com/rss/news-releases.xml?items=15", 
    10:"https://feeds.a.dj.com/rss/RSSWorldNews.xml",
    11:"https://threatpost.com/feed/",
    12:"https://www.bleepingcomputer.com/feed/"
}

# Function to parse and print feed articles
def parseFeed(feedList, numPosts):
    # Print the feed title
    if 'title' in feedList.feed:
        print ("\nTitle: " + feedList.feed.title)
    else:
        print ("\n[No Title]")

    # Print the feed URL
    if 'link' in feedList.feed:
        print ("Link: " + feedList.feed.link)
    else:
        print ("[No Link]")

    # Print the feed Description
    if 'description' in feedList.feed:
        print ("Description: " + feedList.feed.description + "\n")
    else:
        print ("[No Description]\n")

    # Loop to display 'numPosts' number of articles
    for i in range(numPosts):
        # Print entry title
        if 'title' in feedList.entries[i]:
            print (str(i + 1) + ": " + feedList.entries[i].title)
        else:
            print ("[No Title]")

        # Print entry publish date
        if 'published' in feedList.entries[i]:
            print ("Date: " + feedList.entries[i].published)
        else:
            print ("[No Publish Date]")

        # Print entry category
        if 'category' in feedList.entries[i]:
            print ("Category: " + feedList.entries[i].category)
        else:
            print ("[No Category]")

        # Print entry summary
        if 'summary' in feedList.entries[i]:
            print ("Summary: " + feedList.entries[i].summary)
        else:
            print ("[No Summary]")

        # Print entry URL
        if 'link' in feedList.entries[i]:
            print ("Link: " + feedList.entries[i].link + "\n")
        else:
            print ("[No Link]\n")

# Function to display menu and obtain user selection
def getInput():
    menu_choice = input("""
    Menu
    0. Custom URL
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
    12. Bleeping Computer - Latest
    Enter the number of the RSS feed you want to view ('exit' or CTRL+C to exit): """)

    return menu_choice

# Check for arguments in the cli
# Usage: python3 PythonFeedReader.py [url_of_rss_feed]
# Example: python3 PythonFeedReader.py https://threatpost.com/feed/
if len(sys.argv) > 1:
    # Convert argument to string and use feedparser to parse the argument
    argument_feed = feedparser.parse(str(sys.argv[1]))

    # Prompt user for custom feed_number variable
    number_of_articles = int(input("Number of feeds to view: "))
    
    # Print the feed title, URL, and 'number_of_articles' amount of articles
    parseFeed(argument_feed, number_of_articles)
else:
    # Display menu and prompt for user selection
    choice = getInput()

    # Create a loop for continuous program use
    while choice != "exit":
        try:
            if int(choice) in range(len(feeds) + 1):
                # parseFeed params = feed, numFeeds
                parseFeed(feedparser.parse(feeds[int(choice)]), 5)
                choice = getInput()
            else:
                # Error handling: Request new entry
                print ("\nERROR! Invalid input! Please enter an integer or type 'exit' to exit")
                print ("\nRedisplaying menu...")
                # Redisplay menu
                choice = getInput()
        except:
             # Error handling: Request new entry
                print ("Exception triggered...")
                #print ("\nERROR! Invalid input! Please enter an integer or type 'exit' to exit")
                #print ("\nRedisplaying menu...")
                # Redisplay menu
                choice = getInput()
            
# Thanks for stopping by! <3