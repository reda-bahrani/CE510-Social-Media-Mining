from codes import consumer_key, consumer_secret, access_token, access_token_secret
from tweepy import OAuthHandler
from tweepy import Stream
import socket
import json

class TweetListener(Stream):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, *args, csocket):
        super().__init__(*args)
        self.client_socket = csocket

    def on_data(self, data):
        msg = str(json.loads(data))
        print(msg)
        with open("tweets.json", "a") as f:
            f.write(msg)
        return True


    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    c_socket = socket.socket()
    listener = TweetListener(
        consumer_key, consumer_secret,
        access_token, access_token_secret, 
        csocket=c_socket)

    listener.filter(track=['covid-19', 'the great resignation'])
