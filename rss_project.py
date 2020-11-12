# Import libraries
import feedparser           # Used for parsing though RSS feeds via url
import sys                  # Used to obtain arguments from the cli

# RSS Feed Links
# 1. BBC Link
url_BBC = "http://feeds.bbci.co.uk/news/rss.xml?edition=us"
bbc_feed = feedparser.parse(url_BBC)

# 2. CNN Link
url_CNN = "http://rss.cnn.com/rss/cnn_topstories.rss"
cnn_feed = feedparser.parse(url_CNN)

# 3. ESPN Link
url_ESPN = "https://www.espn.com/espn/rss/news"
espn_feed = feedparser.parse(url_ESPN)

# 4. Fox News
url_Fox = "http://feeds.foxnews.com/foxnews/latest/?feed=rss"
fox_feed = feedparser.parse(url_Fox)

# 5. LifeHacker
url_LifeHacker = "https://lifehacker.com/rss"
lifehacker_feed = feedparser.parse(url_LifeHacker)

# 6. New York Times
url_NYT = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
nyt_feed = feedparser.parse(url_NYT)

# 7. NPR
url_NPR = "https://feeds.npr.org/1001/rss.xml"
npr_feed = feedparser.parse(url_NPR)

# 8. Reddit ( r/news )
url_Reddit = "https://www.reddit.com/r/news/.rss"
reddit_feed = feedparser.parse(url_Reddit)

# 9. Reuters
url_Reuters = "https://ir.thomsonreuters.com/rss/news-releases.xml?items=15"
reuters_feed = feedparser.parse(url_Reuters)

# 10. Wall Street Journal
url_WallStreet = "https://feeds.a.dj.com/rss/RSSWorldNews.xml"
wallstreet_feed = feedparser.parse(url_WallStreet)

# Check for arguments in the cli
# Usage: python3 rss_project.py [url_of_rss_feed]
if len(sys.argv) > 1:
    # Convert argument to string
    url_argument = str(sys.argv[1])
    # Use feedparser to parse the argument
    argument_feed = feedparser.parse(url_argument)

    # Print the feed title and link
    print ("\nTitle: " + argument_feed['feed']['title'])
    print ("Link: " + argument_feed['feed']['link'] + "\n")

    # Print the top 5 entries in the feed
    print ("1: " + argument_feed['entries'][0]['title'])
    print ("Link: " + argument_feed['entries'][0]['link'])
    print ("2: " + argument_feed['entries'][1]['title'])
    print ("Link: " + argument_feed['entries'][1]['link'])
    print ("3: " + argument_feed['entries'][2]['title'])
    print ("Link: " + argument_feed['entries'][2]['link'])
    print ("4: " + argument_feed['entries'][3]['title'])
    print ("Link: " + argument_feed['entries'][3]['link'])
    print ("5: " + argument_feed['entries'][4]['link'])
    print ("Link: " + argument_feed['entries'][4]['link'] + "\n")
else:
    # Create a menu for user input
    menu_choice = input("""
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

    Enter the number of the RSS feed you want to view (0 to exit): """)

    # Create a loop for continuous program use
    while menu_choice != "0":
    # Conditional statements to handle user input
        if menu_choice == "1":
            # Print the feed title and link
            print ("\nTitle: " + bbc_feed['feed']['title'])
            print ("Link: " + bbc_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + bbc_feed['entries'][0]['title'])
            print ("Link: " + bbc_feed['entries'][0]['link'])
            print ("2: " + bbc_feed['entries'][1]['title'])
            print ("Link: " + bbc_feed['entries'][1]['link'])
            print ("3: " + bbc_feed['entries'][2]['title'])
            print ("Link: " + bbc_feed['entries'][2]['link'])
            print ("4: " + bbc_feed['entries'][3]['title'])
            print ("Link: " + bbc_feed['entries'][3]['link'])
            print ("5: " + bbc_feed['entries'][4]['link'])
            print ("Link: " + bbc_feed['entries'][4]['link'])
        elif menu_choice == "2":
            # Print the feed title and link
            print ("\nTitle: " + cnn_feed['feed']['title'])
            print ("Link: " + cnn_feed['feed']['link'] + "\n")
            
            # Print the top 5 entries in the feed
            print ("1: " + cnn_feed['entries'][0]['title'])
            print ("Link: " + cnn_feed['entries'][0]['link'])
            print ("2: " + cnn_feed['entries'][1]['title'])
            print ("Link: " + cnn_feed['entries'][1]['link'])
            print ("3: " + cnn_feed['entries'][2]['title'])
            print ("Link: " + cnn_feed['entries'][2]['link'])
            print ("4: " + cnn_feed['entries'][3]['title'])
            print ("Link: " + cnn_feed['entries'][3]['link'])
            print ("5: " + cnn_feed['entries'][4]['link'])
            print ("Link: " + cnn_feed['entries'][4]['link'])
        elif menu_choice == "3":
            # Print the feed title and link
            print ("\nTitle: " + espn_feed['feed']['title'])
            print ("Link: " + espn_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + espn_feed['entries'][0]['title'])
            print ("Link: " + espn_feed['entries'][0]['link'])
            print ("2: " + espn_feed['entries'][1]['title'])
            print ("Link: " + espn_feed['entries'][1]['link'])
            print ("3: " + espn_feed['entries'][2]['title'])
            print ("Link: " + espn_feed['entries'][2]['link'])
            print ("4: " + espn_feed['entries'][3]['title'])
            print ("Link: " + espn_feed['entries'][3]['link'])
            print ("5: " + espn_feed['entries'][4]['link'])
            print ("Link: " + espn_feed['entries'][4]['link'])
        elif menu_choice == "4":
            # Print the feed title and link
            print ("\nTitle: " + fox_feed['feed']['title'])
            print ("Link: " + fox_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + fox_feed['entries'][0]['title'])
            print ("Link: " + fox_feed['entries'][0]['link'])
            print ("2: " + fox_feed['entries'][1]['title'])
            print ("Link: " + fox_feed['entries'][1]['link'])
            print ("3: " + fox_feed['entries'][2]['title'])
            print ("Link: " + fox_feed['entries'][2]['link'])
            print ("4: " + fox_feed['entries'][3]['title'])
            print ("Link: " + fox_feed['entries'][3]['link'])
            print ("5: " + fox_feed['entries'][4]['link'])
            print ("Link: " + fox_feed['entries'][4]['link'])
        elif menu_choice == "5":
            # Print the feed title and link
            print ("\nTitle: " + lifehacker_feed['feed']['title'])
            print ("Link: " + lifehacker_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + lifehacker_feed['entries'][0]['title'])
            print ("Link: " + lifehacker_feed['entries'][0]['link'])
            print ("2: " + lifehacker_feed['entries'][1]['title'])
            print ("Link: " + lifehacker_feed['entries'][1]['link'])
            print ("3: " + lifehacker_feed['entries'][2]['title'])
            print ("Link: " + lifehacker_feed['entries'][2]['link'])
            print ("4: " + lifehacker_feed['entries'][3]['title'])
            print ("Link: " + lifehacker_feed['entries'][3]['link'])
            print ("5: " + lifehacker_feed['entries'][4]['link'])
            print ("Link: " + lifehacker_feed['entries'][4]['link'])
        elif menu_choice == "6":
            # Print the feed title and link
            print ("\nTitle: " + nyt_feed['feed']['title'])
            print ("Link: " + nyt_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + nyt_feed['entries'][0]['title'])
            print ("Link: " + nyt_feed['entries'][0]['link'])
            print ("2: " + nyt_feed['entries'][1]['title'])
            print ("Link: " + nyt_feed['entries'][1]['link'])
            print ("3: " + nyt_feed['entries'][2]['title'])
            print ("Link: " + nyt_feed['entries'][2]['link'])
            print ("4: " + nyt_feed['entries'][3]['title'])
            print ("Link: " + nyt_feed['entries'][3]['link'])
            print ("5: " + nyt_feed['entries'][4]['link'])
            print ("Link: " + nyt_feed['entries'][4]['link'])
        elif menu_choice == "7":
            # Print the feed title and link
            print ("\nTitle: " + npr_feed['feed']['title'])
            print ("Link: " + npr_feed['feed']['link'] + "\n")
            
            # Print the top 5 entries in the feed
            print ("1: " + npr_feed['entries'][0]['title'])
            print ("Link: " + npr_feed['entries'][0]['link'])
            print ("2: " + npr_feed['entries'][1]['title'])
            print ("Link: " + npr_feed['entries'][1]['link'])
            print ("3: " + npr_feed['entries'][2]['title'])
            print ("Link: " + npr_feed['entries'][2]['link'])
            print ("4: " + npr_feed['entries'][3]['title'])
            print ("Link: " + npr_feed['entries'][3]['link'])
            print ("5: " + npr_feed['entries'][4]['link'])
            print ("Link: " + npr_feed['entries'][4]['link'])
        elif menu_choice == "8":
            # Print the feed title and link
            print ("\nTitle: " + reddit_feed['feed']['title'])
            print ("Link: " + reddit_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + reddit_feed['entries'][0]['title'])
            print ("Link: " + reddit_feed['entries'][0]['link'])
            print ("2: " + reddit_feed['entries'][1]['title'])
            print ("Link: " + reddit_feed['entries'][1]['link'])
            print ("3: " + reddit_feed['entries'][2]['title'])
            print ("Link: " + reddit_feed['entries'][2]['link'])
            print ("4: " + reddit_feed['entries'][3]['title'])
            print ("Link: " + reddit_feed['entries'][3]['link'])
            print ("5: " + reddit_feed['entries'][4]['link'])
            print ("Link: " + reddit_feed['entries'][4]['link'])
        elif menu_choice == "9":
            # Print the feed title and link
            print ("\nTitle: " + reuters_feed['feed']['title'])
            print ("Link: " + reuters_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + reuters_feed['entries'][0]['title'])
            print ("Link: " + reuters_feed['entries'][0]['link'])
            print ("2: " + reuters_feed['entries'][1]['title'])
            print ("Link: " + reuters_feed['entries'][1]['link'])
            print ("3: " + reuters_feed['entries'][2]['title'])
            print ("Link: " + reuters_feed['entries'][2]['link'])
            print ("4: " + reuters_feed['entries'][3]['title'])
            print ("Link: " + reuters_feed['entries'][3]['link'])
            print ("5: " + reuters_feed['entries'][4]['link'])
            print ("Link: " + reuters_feed['entries'][4]['link'])
        elif menu_choice == "10":
            # Print the feed title and link
            print ("\nTitle: " + wallstreet_feed['feed']['title'])
            print ("Link: " + wallstreet_feed['feed']['link'] + "\n")

            # Print the top 5 entries in the feed
            print ("1: " + wallstreet_feed['entries'][0]['title'])
            print ("Link: " + wallstreet_feed['entries'][0]['link'])
            print ("2: " + wallstreet_feed['entries'][1]['title'])
            print ("Link: " + wallstreet_feed['entries'][1]['link'])
            print ("3: " + wallstreet_feed['entries'][2]['title'])
            print ("Link: " + wallstreet_feed['entries'][2]['link'])
            print ("4: " + wallstreet_feed['entries'][3]['title'])
            print ("Link: " + wallstreet_feed['entries'][3]['link'])
            print ("5: " + wallstreet_feed['entries'][4]['link'])
            print ("Link: " + wallstreet_feed['entries'][4]['link'])
        else:
            # Error handling: Request new entry
            print("\nERROR! Invalid input!")
        
    # Display the menu to re-run the program
        menu_choice = input("""
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

    Enter the number of the RSS feed you want to view (0 to exit): """)