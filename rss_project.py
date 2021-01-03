# Import libraries
import feedparser           # Used for parsing though RSS feeds via url
import sys                  # Used to obtain arguments from the cli

# To Dos:
#           Add option for custom URL in menu 
#           Expand RSS feed library (Maybe find a library online to import feed urls from?)
#           Create a welcome message



# RSS Feed Links
bbc_feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml?edition=us")                      #1

cnn_feed = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")                            #2

espn_feed = feedparser.parse("https://www.espn.com/espn/rss/news")                                  #3

fox_feed = feedparser.parse("http://feeds.foxnews.com/foxnews/latest/?feed=rss")                    #4

lifehacker_feed = feedparser.parse("https://lifehacker.com/rss")                                    #5

nyt_feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")               #6

npr_feed = feedparser.parse("https://feeds.npr.org/1001/rss.xml")                                   #7

reddit_feed = feedparser.parse("https://www.reddit.com/r/news/.rss")                                #8

reuters_feed = feedparser.parse("https://ir.thomsonreuters.com/rss/news-releases.xml?items=15")     #9

wallstreet_feed = feedparser.parse("https://feeds.a.dj.com/rss/RSSWorldNews.xml")                   #10

# Check for arguments in the cli
# Usage: python3 rss_project.py [url_of_rss_feed]
if len(sys.argv) > 1:
    # Convert argument to string and use feedparser to parse the argument
    argument_feed = feedparser.parse(str(sys.argv[1]))

    # Test loop
    # Prompt user for custom feed_number variable
    number_of_feeds = int(input("Number of feeds to view: "))
    # Variable for while loop
    feed_number = 0

    # Print the feed title and feed URL
    print ("\nTitle: " + argument_feed['feed']['title'])
    print ("Link: " + argument_feed['feed']['link'] + "\n")

    # Use loop to display 'feed_number' amount of feeds   
    while feed_number < number_of_feeds:
        print (str(feed_number + 1) + ": " + argument_feed['entries'][feed_number]['title'])
        print ("Link: " + argument_feed['entries'][feed_number]['link'])
        feed_number += 1
else:
    # Create a menu for user input
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

    Enter the number of the RSS feed you want to view ('exit' or CTRL+C to exit): """)

    # Create a loop for continuous program use
    while menu_choice != "exit":
    # Conditional statements to handle user input
        if menu_choice == "0":
            print("Coming soon...")
        elif menu_choice == "1":
            # Print the feed title and feed URL
            print ("\nTitle: " + bbc_feed['feed']['title'])
            print ("Link: " + bbc_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + bbc_feed['entries'][feed_number]['title'])
                print ("Link: " + bbc_feed['entries'][feed_number]['link'])
                feed_number += 1    
        elif menu_choice == "2":
            # Print the feed title and feed URL
            print ("\nTitle: " + cnn_feed['feed']['title'])
            print ("Link: " + cnn_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + cnn_feed['entries'][feed_number]['title'])
                print ("Link: " + cnn_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "3":
            # Print the feed title and feed URL
            print ("\nTitle: " + espn_feed['feed']['title'])
            print ("Link: " + espn_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + espn_feed['entries'][feed_number]['title'])
                print ("Link: " + espn_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "4":
            # Print the feed title and feed URL
            print ("\nTitle: " + fox_feed['feed']['title'])
            print ("Link: " + fox_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + fox_feed['entries'][feed_number]['title'])
                print ("Link: " + fox_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "5":
            # Print the feed title and feed URL
            print ("\nTitle: " + lifehacker_feed['feed']['title'])
            print ("Link: " + lifehacker_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + lifehacker_feed['entries'][feed_number]['title'])
                print ("Link: " + lifehacker_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "6":
            # Print the feed title and feed URL
            print ("\nTitle: " + nyt_feed['feed']['title'])
            print ("Link: " + nyt_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + nyt_feed['entries'][feed_number]['title'])
                print ("Link: " + nyt_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "7":
            # Print the feed title and feed URL
            print ("\nTitle: " + npr_feed['feed']['title'])
            print ("Link: " + npr_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + npr_feed['entries'][feed_number]['title'])
                print ("Link: " + npr_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "8":
            # Print the feed title and feed URL
            print ("\nTitle: " + reddit_feed['feed']['title'])
            print ("Link: " + reddit_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + reddit_feed['entries'][feed_number]['title'])
                print ("Link: " + reddit_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "9":
            # Print the feed title and feed URL
            print ("\nTitle: " + reuters_feed['feed']['title'])
            print ("Link: " + reuters_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + reuters_feed['entries'][feed_number]['title'])
                print ("Link: " + reuters_feed['entries'][feed_number]['link'])
                feed_number += 1 
        elif menu_choice == "10":
            # Print the feed title and feed URL
            print ("\nTitle: " + wallstreet_feed['feed']['title'])
            print ("Link: " + wallstreet_feed['feed']['link'] + "\n")

            feed_number = 0

            # Use loop to display 'feed_number' amount of feeds   
            while feed_number < 5:
                print (str(feed_number + 1) + ": " + wallstreet_feed['entries'][feed_number]['title'])
                print ("Link: " + wallstreet_feed['entries'][feed_number]['link'])
                feed_number += 1 
        else:
            # Error handling: Request new entry
            print("\nERROR! Invalid input! Please enter a number (0-10) or type 'exit' to exit")
            print("\nRedisplaying menu...")
            
        
    # Display the menu to re-run the program
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

    Enter the number of the RSS feed you want to view ('exit' or CTRL+C to exit): """)

# Thanks for stopping by! <3