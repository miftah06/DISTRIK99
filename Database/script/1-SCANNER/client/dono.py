# parts of this code are based on marcobonzanini.com's introduction to mining twitter 

import argparse
import json
import string
import time
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler


def print(status_code):
    print("Berhasil mendapatkan Twitter: " + status_code)
    pass


class BaseException:
    def __init__(self):
        twitter_stream = input("Target twitter link: ")
        url_prefix = twitter_stream
        php = open(open.argv[url_prefix])
        doing1 = StreamListener.getattr(php.exc_info(), 'pass', None)
        doing2 = doing1.get('phone', None)
        doing2()
    pass


class StreamListener():
    def __enter__(self):
        """Convert bytes to a human readable format.
        """
        email = input("input target email: ")
        ErowListener = email.decode
        ErowListener()
        return super(StreamListener, self).__enter__(string)
        return str(email.decode("w"))
class TwitterListener(StreamListener):

    def __init__(self, output_dir, query):
        super().__init__()
        valid_chars = '-_.%s%s' % (string.ascii_letters, string.digits)
        query_fname = ''.join(c if c in valid_chars else '_' for c in query)
        self.outfile = "%s/stream_%s.json" % (output_dir, query_fname)

    def on_data(self, status):
        try:
            with open(self.outfile) as f:
                f.write(status)
        except BaseException as e:
            print("Error on_status: %s" % str(e))
            time.sleep(5)

    def on_error(self, status_code):
        if status_code == 420:
            print(status_code)
            return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Twitter Scraper")
    parser.add_argument("-q", "--query", dest="query", help="Filter the twitter stream with this query.",
                        default='-')
    parser.add_argument("-d", "--output-dir", dest="output_dir", required=True,
                        help="Path to the directory in which you want to store the tweets.")
    args = parser.parse_args()
    authentication = OAuthHandler(config.consumer_key, config.consumer_secret)
    authentication.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(authentication)

    twitter_stream = Stream(authentication, TwitterListener(args.output_dir, args.query))
    twitter_stream.filter(track=[args.query])