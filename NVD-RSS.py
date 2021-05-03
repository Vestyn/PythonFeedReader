# National Vulnerability Database RSS Feed Reader

# Import Libraries
import feedparser

def feedParse(feed):
    # For every <item> in [feed], print feed title, link, description, and date
    for item in feed.entries:
        print('\n========================================================================================================================================================')
        print('Title: ' + item.title)
        print('Updated: ' + item.updated)
        print('Summary: ' + item.summary)
        print('Link: ' + item.link)
        print('========================================================================================================================================================')

def main():
    feedParse(feedparser.parse("https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml"))

if __name__ == "__main__":
    main()