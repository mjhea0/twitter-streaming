# dependencies
import sys
import tweepy

# authentication settings 
consumer_key	= "ADD YOUR KEY"
consumer_secret	= "ADD YOUR KEY"
access_token 	= "ADD YOUR KEY"
access_secret 	= "ADD YOUR KEY" 
 
# authenticate 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth) 
 
# listen handler
class StreamListener(tweepy.StreamListener):
	
	# print raw data
	def on_data(self, data):
		print data

    # print out tweet
    def on_status(self, status):
        print status.text
 
 	# print error
    def on_error(self, status_code):
        print >> sys.stderr, 'Error status code: ', status_code
        return True # continue listening

    # print timeout
    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # continue listening

# instantiate 
twitterStream = tweepy.streaming.Stream(auth, StreamListener())
TwitterStream.filter(track=['TrickOrTreat'])