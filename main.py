import logging

from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from send_sms import send_sms
import config


class TwitterClient:
    """
    Class for interacting with twitter API
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.auth = self.authenticate()
        self.api = API(self.auth)

        # Keywords to search for in tweets
        self.keywords = ['traffic', 'update', 'from',
                         'doge', 'dogecoin', 'btc', 'bitcoin',
                         'eth', 'ethereum']

    def authenticate(self):
        auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
        return auth

    def start_stream(self):
        listener = TwitterListener(self.api, self.user_id)
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
    Listens to twitter stream and sends sms if applicable

    user_id (str): The twitter id of the user
    keywords (list): List of words, if any are in tweet sms is sent
    """

    def __init__(self, api, user_id):
        self.api = api
        self.user_id = user_id

        self.message_text = 'Elon Musk tweeted including a key-word'

    def on_status(self, tweet):
        if tweet.user.id_str == self.user_id:
            send_sms(self.message_text)

    def on_error(self, status_code):
        print('An error occured: ', status_code)
        return True

    def on_timeout(self):
        print('Listener timeout. Will try to reconnect')
        return True



if __name__ == '__main__':
    """
    For testing using the @trafficalertuk twitter page
    their id is: 756147538361618433

    For actual use set to @elonmusk user_id: 44196397
    """
    user_id = '3887467873'
    client = TwitterClient(user_id)
    client.start_stream()
    