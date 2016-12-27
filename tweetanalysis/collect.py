from tweepy import *
from tweepy.streaming import StreamListener

CREDENTIALS_PATH = 'C:\\Users\\naveen\\Desktop\\g.txt'
with open(CREDENTIALS_PATH) as f:
    for line in f:
        line = line.rstrip('\n').split(":")
        if line[0] == "CONSUMER_KEY":
            CONSUMER_KEY = line[1]
        elif line[0] == "CONSUMER_SECRET":
            CONSUMER_SECRET = line[1]
        elif line[0] == "ACCESS_TOKEN":
            ACCESS_TOKEN = line[1]
        elif line[0] == "ACCESS_TOKEN_SECRET":
            ACCESS_TOKEN_SECRET = line[1]
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)
api = API(auth)


class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('D:\\education\\python\\twiiter.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status_code):
        print(status_code)
        # return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#CycloneVardah'], async=True)
