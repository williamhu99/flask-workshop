from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'TOKEN'
ACCESS_SECRET = 'SECERT'
CONSUMER_KEY = 'KEY'
CONSUMER_SECRET = 'SECRET'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)

print twitter.followers.ids(screen_name="cocoweixu")
