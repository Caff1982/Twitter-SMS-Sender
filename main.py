from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from send_sms import send_sms
import config


class TwitterClient:
    """
    Class for interacting with twitter API

    args:
        user_id (str): The twitter user-id of the account to monitor
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.auth = self.authenticate()
        self.api = API(self.auth)

    def authenticate(self):
        auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
        return auth

    def start_stream(self):
        listener = TwitterListener(self.user_id)
        stream = Stream(self.api.auth, listener)
        while True:
            try:
                print('Connecting to Twitter stream...')
                stream.filter(follow=[self.user_id])
            except Exception as e:
                print('An error occured: ', e)
                print('Reconnecting...')
            except KeyboardInterrupt:
                print('Disconnecting...')
                stream.disconnect()
                break


class TwitterListener(StreamListener):
    """
    Listens to twitter stream and sends SMS if applicable
    
    args:
        user_id (str): The twitter id of the user
        keywords (list): List of words, if any are in tweet SMS is sent
    """

    def __init__(self, user_id):
        self.user_id = user_id
        # Keywords to search for in tweets
        self.keywords = ['doge', 'dogecoin', 'btc', 'bitcoin',
                         'eth', 'ethereum']

    def on_status(self, tweet):
        if tweet.user.id_str == self.user_id:
            if any(word in tweet.text for word in self.keywords):
                send_sms(tweet.text)

    def on_error(self, status_code):
        print('An error occured: ', status_code)
        return True

    def on_timeout(self):
        print('Listener timeout. Will try to reconnect')
        return True


if __name__ == '__main__':
    client = TwitterClient(config.USER_ID)
    client.start_stream()
    